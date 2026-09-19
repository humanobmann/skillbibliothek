import json
import re
from pathlib import Path


ROOT = Path(__file__).parents[1]
SKILLS = ROOT / "skills"


def test_catalog_matches_skill_directories():
    catalog = json.loads((ROOT / "references" / "SKILL_CATALOG.json").read_text(encoding="utf-8"))
    folders = {
        path.name
        for path in SKILLS.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    catalog_folders = {entry["folder"] for entry in catalog["skills"]}

    assert catalog["total_skills"] == len(folders)
    assert catalog_folders == folders


def test_router_references_only_existing_skills():
    router = (SKILLS / "core-routing" / "SKILL.md").read_text(encoding="utf-8")
    referenced = set(re.findall(r"`skills/([^`/]+)`", router))

    assert referenced
    assert all((SKILLS / name / "SKILL.md").is_file() for name in referenced)


def test_all_skill_frontmatter_has_name_and_description():
    for skill_md in SKILLS.glob("*/SKILL.md"):
        text = skill_md.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.DOTALL)
        assert match, skill_md
        frontmatter = match.group(1)
        assert re.search(r"^name:\s*\S+", frontmatter, re.MULTILINE), skill_md
        assert re.search(r"^description:\s*\S+", frontmatter, re.MULTILINE), skill_md
