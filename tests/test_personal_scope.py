"""Guard the personal distribution scope without touching upstream notices."""
import json
from pathlib import Path


def test_distribution_has_no_retired_organization_or_template_references():
    root = Path(__file__).resolve().parents[1]
    roots = ("provenance", "plugins", "docs", "scripts", "tests", "evals", "hooks", ".agents", ".claude-plugin", ".github")
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
        # Immutable legal/upstream derivation evidence is not distribution branding.
        if path.name in {"skill-sources.json", "provenance.json"}:
            data = json.loads(contents)
            def without_evidence(value):
                if isinstance(value, dict):
                    return {key: without_evidence(item) for key, item in value.items()
                            if key not in {"derivation", "repository", "upstream_path"}}
                if isinstance(value, list):
                    return [without_evidence(item) for item in value]
                return value
            contents = json.dumps(without_evidence(data))
        if any(term in contents for term in forbidden):
            violations.append(str(path.relative_to(root)))
    assert not violations, "Review retired project references without removing required notices: " + ", ".join(violations)
