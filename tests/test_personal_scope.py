"""Guard the personal distribution scope without touching upstream notices."""
from pathlib import Path


def test_distribution_has_no_retired_organization_or_template_references():
    root = Path(__file__).resolve().parents[1]
    roots = ("source", "plugins", "docs", "scripts", "tests", "evals", "hooks", ".agents", ".claude-plugin", ".github")
    files = [root / name for name in ("README.md", "AGENTS.md", "catalog.json", "pyproject.toml")]
    files.extend(path for name in roots for path in (root / name).rglob("*") if path.is_file())
    forbidden = ("kong" + "labs", "kong" + "pedia", "project" + "-blueprints", "project " + "blueprints", "cop" + "ier")
    violations = []
    for path in files:
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        try:
            contents = path.read_text(encoding="utf-8").casefold()
        except UnicodeDecodeError:
            continue
        if any(term in contents for term in forbidden):
            violations.append(str(path.relative_to(root)))
    assert not violations, "Review retired project references without removing required notices: " + ", ".join(violations)
