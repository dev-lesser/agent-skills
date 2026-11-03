"""Exercise the vendored CLI's fail-closed data and persistence boundaries."""
import json
from pathlib import Path
import shutil
import subprocess
import sys

import pytest

SKILL = Path(__file__).resolve().parents[1] / "plugins/react-ui/skills/ui-ux-pro-max"


@pytest.fixture
def workspace(tmp_path):
    skill = shutil.copytree(SKILL, tmp_path / "skill")
    output = tmp_path / "project"
    output.mkdir()
    return skill, output


def run(workspace, *flags, query="SaaS"):
    skill, output = workspace
    return subprocess.run(
        [sys.executable, "-B", str(skill / "scripts/search.py"), query,
         "--design-system", "--json", "-p", "Example", "--output-dir", str(output), *flags],
        cwd=output, capture_output=True, text=True, timeout=20,
    )


def tree(root):
    return {str(p.relative_to(root)): ("link", str(p.readlink())) if p.is_symlink()
            else ("directory",) if p.is_dir() else ("file", p.read_bytes())
            for p in root.rglob("*")}


@pytest.mark.parametrize("name,flags", [
    ("products.csv", ()), ("styles.csv", ()), ("colors.csv", ()),
    ("typography.csv", ()), ("landing.csv", ()), ("ui-reasoning.csv", ()),
    ("motion.csv", ("--motion", "5")),
    ("ux-guidelines.csv", ("--page", "dashboard")),
])
@pytest.mark.parametrize("damage", ["missing", "invalid-encoding", "directory"])
def test_required_resource_failure_never_recommends_or_writes(workspace, name, flags, damage):
    skill, output = workspace
    resource = skill / "data" / name
    resource.unlink()
    if damage == "invalid-encoding":
        resource.write_bytes(b"\xffinvalid utf8")
    elif damage == "directory":
        resource.mkdir()
    before = tree(output)
    result = run(workspace, "--persist", *flags)
    assert result.returncode != 0, result.stdout
    assert result.stdout == ""
    assert name in result.stderr
    assert "error:" in result.stderr.lower()
    assert "Traceback" not in result.stderr
    assert tree(output) == before


@pytest.mark.parametrize("relative", ["design-system", "design-system/example", "design-system/example/pages",
                                     "design-system/example/MASTER.md", "design-system/example/pages/dashboard.md"])
@pytest.mark.parametrize("force", [False, True])
def test_managed_symlink_rejected_without_any_write(workspace, relative, force):
    _, output = workspace
    outside = output.parent / "outside"
    outside.mkdir()
    link = output / relative
    link.parent.mkdir(parents=True, exist_ok=True)
    target = outside
    if link.suffix == ".md":
        target = outside / "keep.md"
        target.write_text("Unchanged external content")
    link.symlink_to(target, target_is_directory=target.is_dir())
    before = tree(output), tree(outside)
    result = run(workspace, "--persist", "--page", "dashboard", *(["--force"] if force else []))
    assert result.returncode != 0, result.stdout
    assert not result.stdout
    assert "symlink" in result.stderr.lower()
    assert (tree(output), tree(outside)) == before


def test_valid_recommendation_is_readonly_without_optional_motion_data(workspace):
    skill, output = workspace
    (skill / "data/motion.csv").unlink()
    before = tree(skill), tree(output)
    result = run(workspace)
    assert result.returncode == 0, result.stderr
    report = json.loads(result.stdout)
    assert report["design_system"]["reasoning_default"] is False
    assert report["design_system"]["source_identities"]["product"]
    assert report["persistence"] is None
    assert (tree(skill), tree(output)) == before


def test_unmatched_query_reports_fallback_without_writes(workspace):
    skill, output = workspace
    before = tree(skill), tree(output)
    result = run(workspace, query="zzzznotacatalogentryqvx")
    assert result.returncode == 0, result.stderr
    design = json.loads(result.stdout)["design_system"]
    assert design["reasoning_default"] is True
    assert design["source_identities"]["product"] is None
    assert design["source_identities"]["reasoning"] is None
    assert (tree(skill), tree(output)) == before


def test_existing_records_preserved_until_explicit_force(workspace):
    _, output = workspace
    assert run(workspace, "--persist", "--page", "dashboard").returncode == 0
    master = output / "design-system/example/MASTER.md"
    page = master.parent / "pages/dashboard.md"
    master.write_text("Keep master")
    page.write_text("Keep page")
    result = run(workspace, "--persist", "--page", "dashboard")
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout)["persistence"]["status"] == "skipped_exists"
    assert master.read_text() == "Keep master"
    assert page.read_text() == "Keep page"
    result = run(workspace, "--persist", "--page", "dashboard", "--force")
    assert result.returncode == 0, result.stderr
    assert master.read_text() != "Keep master"
    assert page.read_text() != "Keep page"


def test_reviewed_output_root_can_resolve_through_symlink(workspace):
    skill, output = workspace
    selected = output.parent / "reviewed-root"
    selected.symlink_to(output, target_is_directory=True)
    result = run((skill, selected), "--persist")
    assert result.returncode == 0, result.stderr
    assert (output / "design-system/example/MASTER.md").is_file()


def damage_csv(path, kind):
    import csv
    import io
    rows = list(csv.reader(io.StringIO(path.read_text())))
    if kind == "empty":
        path.write_text("")
        return
    if kind == "header-only":
        rows = rows[:1]
    elif kind == "missing-header":
        required = next(name for name in ("UI_Category", "Product Type", "Style ID", "Pattern ID", "Category") if name in rows[0])
        index = rows[0].index(required)
        rows = [row[:index] + row[index + 1:] for row in rows]
    elif kind == "short-row":
        rows[1] = rows[1][:-1]
    elif kind == "long-row":
        rows[1].append("unexpected field")
    elif kind == "malformed":
        path.write_text(','.join(rows[0]) + '\n"unterminated field')
        return
    elif kind == "missing":
        path.unlink()
        return
    buffer = io.StringIO()
    csv.writer(buffer).writerows(rows)
    path.write_text(buffer.getvalue())


@pytest.mark.parametrize("filename", ["products.csv", "ui-reasoning.csv"])
@pytest.mark.parametrize("damage", ["empty", "header-only", "missing-header", "short-row", "long-row", "malformed"])
def test_invalid_required_csv_cannot_become_persisted_defaults(workspace, filename, damage):
    skill, output = workspace
    damage_csv(skill / "data" / filename, damage)
    before = tree(output)
    result = run(workspace, "--persist")
    assert result.returncode != 0, result.stdout
    assert not result.stdout
    assert filename in result.stderr
    assert "error:" in result.stderr.lower()
    assert "Traceback" not in result.stderr
    assert tree(output) == before


@pytest.mark.parametrize("flags,filename", [
    (("--domain", "ux"), "ux-guidelines.csv"),
    (("--stack", "react"), "stacks/react.csv"),
    (("--domain", "style"), "styles.csv"),
    (("--domain", "landing"), "landing.csv"),
    ((), "products.csv"),
])
@pytest.mark.parametrize("damage", ["missing", "empty", "header-only", "missing-header", "short-row", "long-row", "malformed"])
@pytest.mark.parametrize("as_json", [False, True])
def test_all_search_modes_fail_cleanly_for_invalid_data(workspace, flags, filename, damage, as_json):
    skill, output = workspace
    damage_csv(skill / "data" / filename, damage)
    result = subprocess.run(
        [sys.executable, "-B", str(skill / "scripts/search.py"), "keyboard focus", *flags,
         *(["--json"] if as_json else [])],
        cwd=output, capture_output=True, text=True, timeout=20,
    )
    assert result.returncode != 0, result.stdout
    assert not result.stdout
    assert Path(filename).name in result.stderr
    assert "error:" in result.stderr.lower()
    assert "Traceback" not in result.stderr
    assert tree(output) == {}


def test_every_bundled_search_table_accepts_valid_rows_and_optional_empty_cells(workspace):
    skill, output = workspace
    code = '''
from core import CSV_CONFIG, STACK_CONFIG, search, search_stack
for domain in CSV_CONFIG:
    result = search("keyboard focus", domain)
    assert "error" not in result, (domain, result)
    assert isinstance(result["results"], list)
for stack in STACK_CONFIG:
    result = search_stack("keyboard focus", stack)
    assert "error" not in result, (stack, result)
    assert isinstance(result["results"], list)
assert search("zzzznotacatalogentryqvx", "ux")["count"] == 0
assert search_stack("zzzznotacatalogentryqvx", "react")["count"] == 0
'''
    result = subprocess.run(
        [sys.executable, "-B", "-c", "import sys; sys.path.insert(0, " +
         repr(str(skill / "scripts")) + ");\n" + code],
        cwd=output, capture_output=True, text=True, timeout=20,
    )
    assert result.returncode == 0, result.stderr


def test_output_format_failure_precedes_persistence(workspace, monkeypatch):
    import csv
    import io
    skill, output = workspace
    palette = skill / "data/colors.csv"
    rows = list(csv.DictReader(io.StringIO(palette.read_text())))
    for row in rows:
        row["Primary"] = "#GGGGGG"
    content = io.StringIO()
    writer = csv.DictWriter(content, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
    palette.write_text(content.getvalue())
    monkeypatch.setenv("COLORTERM", "truecolor")
    before = tree(output)
    result = run(workspace, "--persist")
    assert result.returncode != 0
    assert not result.stdout
    assert "error:" in result.stderr.lower()
    assert "Traceback" not in result.stderr
    assert tree(output) == before, "Even output formatting must finish before directories or records are created"
