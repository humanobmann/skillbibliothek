import json
import re
from pathlib import Path


ROOT = Path(__file__).parents[1]
SKILLS = ROOT / "skills"


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    assert match, path
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields, text


def test_intent_map_targets_and_transitive_aliases_exist():
    intent_map = (ROOT / "references" / "intent-map.md").read_text(encoding="utf-8")
    targets = set(re.findall(r"`([a-z0-9-]+)`", intent_map))
    assert targets
    assert all((SKILLS / name / "SKILL.md").is_file() for name in targets)
    alias_text = (SKILLS / "grill-me" / "SKILL.md").read_text(encoding="utf-8")
    assert re.search(r"canonical_skill:\s*grilling", alias_text)


def test_catalog_matches_directories_and_profiles_are_declared():
    catalog = json.loads((ROOT / "references" / "SKILL_CATALOG.json").read_text(encoding="utf-8"))
    folders = {p.name for p in SKILLS.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()}
    assert catalog["total_skills"] == len(folders)
    assert {entry["folder"] for entry in catalog["skills"]} == folders
    for name in ("core-routing", "deep-research", "grilling", "code-review",
                 "library-skill-authoring", "skill-security-auditor"):
        fields, _ = frontmatter(SKILLS / name / "SKILL.md")
        assert "metadata" in (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
        assert fields["name"] == name


def test_router_has_no_retired_targets_or_self_cycle():
    router = (SKILLS / "core-routing" / "SKILL.md").read_text(encoding="utf-8")
    assert "code-review-excellence" not in router
    assert "skills/prompts" not in router
    assert "skills/skills" not in router
    rows = (ROOT / "references" / "intent-map.md").read_text(encoding="utf-8").splitlines()
    assert not any("| `core-routing` |" in row for row in rows)


def test_progressive_disclosure_budget_for_new_control_skills():
    for name in ("core-routing", "deep-research", "code-review",
                 "library-skill-authoring", "skill-security-auditor"):
        fields, _ = frontmatter(SKILLS / name / "SKILL.md")
        assert len(fields["description"]) <= 300
