"""Deterministic QA for Design & Visual director, wizard and Bergside catalog."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def test_new_skills_have_frontmatter_and_agent_metadata():
    for slug in ("design-visual-director", "guided-design-brief", "design-style-curator"):
        path = SKILLS / slug / "SKILL.md"
        assert path.is_file(), path
        text = path.read_text(encoding="utf-8")
        assert text.startswith("---\n")
        assert re.search(r"(?m)^name:\s*" + re.escape(slug) + r"\s*$", text)
        assert re.search(r"(?m)^description:\s*\S", text)
        assert (SKILLS / slug / "agents" / "openai.yaml").is_file()


def test_curated_catalog_has_67_unique_profiles_and_attribution():
    base = SKILLS / "design-style-curator" / "references"
    catalog = json.loads((base / "bergside-catalog.json").read_text(encoding="utf-8"))
    profiles = catalog["profiles"]
    slugs = [p["slug"] for p in profiles]
    assert len(profiles) == 67
    assert len(set(slugs)) == 67
    assert {"editorial", "minimal", "refined", "brutalism", "riso",
            "storytelling", "geometric", "contemporary"}.issubset(slugs)
    assert "bergside/awesome-design-skills" in json.dumps(catalog["source"])
    license_text = (base / "UPSTREAM_LICENSE.md").read_text(encoding="utf-8")
    assert "MIT License" in license_text and "Bergside" in license_text


def test_content_fidelity_and_production_handoff():
    master = (SKILLS / "design-visual-director" / "references" /
              "masterprompt-v4.md").read_text(encoding="utf-8")
    director = (SKILLS / "design-visual-director" /
                "SKILL.md").read_text(encoding="utf-8")
    for token in ("LOCKED", "Typography", "QA", "Print", "REFERENCE"):
        assert token.lower() in master.lower(), token
    for token in ("CREATE", "EDIT", "AUDIT", "REFINE", "PLAN"):
        assert token in director, token


def test_offline_wizard_eight_steps_without_remote_dependencies():
    wizard = (SKILLS / "guided-design-brief" / "assets" /
              "Designbrief-Wizard.html").read_text(encoding="utf-8")
    assert wizard.lower().startswith("<!doctype html>")
    assert 'lang="de-AT"' in wizard
    assert wizard.count("kind:'choose'") == 6
    assert wizard.count("kind:'text'") == 2
    assert "navigator.clipboard" in wizard and "JSON.stringify" in wizard
    assert "LOCKED" in wizard and "Auto entscheiden" in wizard
    assert not re.search(r"<(?:script|link)[^>]+\b(?:src|href)\s*=", wizard, re.I)
    assert not re.search(r"\b(?:fetch|XMLHttpRequest|sendBeacon)\s*\(", wizard)


def test_design_router_keeps_existing_specialist_workflows():
    router = (SKILLS / "design-workflow-router" / "SKILL.md").read_text(encoding="utf-8")
    for slug in ("design-visual-director", "guided-design-brief",
                 "design-style-curator", "adaptive-poster-image-series",
                 "affinity-designer"):
        assert slug in router, slug
