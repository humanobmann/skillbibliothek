import copy
import json
from pathlib import Path

from scripts.validate_social_evidence import validate_document

ROOT = Path(__file__).parents[1]
SKILLS = ROOT / "skills"
CORE = SKILLS / "social-platform-algorithm-core"


def test_social_framework_and_profiles_exist():
    assert (CORE / "references" / "framework.md").is_file()
    assert (CORE / "references" / "platform-profiles.md").is_file()


def test_tiktok_separates_ranking_search_and_monetization():
    skill = (SKILLS / "tiktok-content-optimizer" / "SKILL.md").read_text(encoding="utf-8")
    evidence = json.loads((CORE / "references" / "evidence-records.json").read_text(encoding="utf-8"))
    records = {record["source_id"]: record for record in evidence["records"]}

    assert "Creator-Rewards-Metriken sind MONETIZATION" in skill
    assert "nicht als bestaetigte For-You-Ranking-Signale" in skill
    assert records["TIKTOK_FYF_RANKING_2026"]["mechanism"] == "RANKING"
    assert records["TIKTOK_SEARCH_2026"]["mechanism"] == "SEARCH"
    assert records["TIKTOK_CREATOR_REWARDS_2024"]["mechanism"] == "MONETIZATION"
    assert records["TIKTOK_FYF_RANKING_2026"]["title"] == "How TikTok recommends content"


def test_framework_models_surfaces_evidence_and_learning():
    framework = (CORE / "references" / "framework.md").read_text(encoding="utf-8")
    for token in (
        "Platform -> Surface -> Objective -> Signal",
        "Evidence Records",
        "Originality Taxonomy",
        "Social Search",
        "Account Analytics Learning Loop",
        "Experiment Framework",
        "Quality Gates",
        "Audit Score",
        "Anti-Patterns",
    ):
        assert token in framework


def test_platform_skills_use_shared_core_and_scorecards():
    for name in (
        "tiktok-content-optimizer",
        "youtube-content-optimizer",
        "linkedin-content-optimizer",
    ):
        text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
        assert "../social-platform-algorithm-core/" in text
        assert "Scorecard" in text
        assert "Anti-Patterns" in text


def test_intent_map_routes_social_skills():
    intent_map = (ROOT / "references" / "intent-map.md").read_text(encoding="utf-8")
    for name in (
        "social-platform-algorithm-core",
        "facebook-text-optimizer",
        "instagram-text-optimizer",
        "instagram-hashtag-research",
        "tiktok-content-optimizer",
        "youtube-content-optimizer",
        "linkedin-content-optimizer",
        "adaptive-poster-image-series",
    ):
        assert name in intent_map


def test_platform_profiles_reference_structured_evidence():
    profile = (CORE / "references" / "platform-profiles.md").read_text(encoding="utf-8")
    evidence = json.loads((CORE / "references" / "evidence-records.json").read_text(encoding="utf-8"))
    validate_document(evidence)

    source_ids = {record["source_id"] for record in evidence["records"]}
    assert source_ids
    for source_id in source_ids:
        assert source_id in profile

    assert "RANKING/SEARCH" not in profile


def test_evidence_records_reject_combined_mechanisms():
    evidence = json.loads((CORE / "references" / "evidence-records.json").read_text(encoding="utf-8"))
    bad = copy.deepcopy(evidence)
    bad["records"][0]["mechanism"] = "RANKING/SEARCH"

    try:
        validate_document(bad)
    except ValueError as exc:
        assert "invalid mechanism" in str(exc) or "combined mechanism" in str(exc)
    else:
        raise AssertionError("combined mechanism must fail validation")


def test_evidence_records_require_claim_scope_and_volatility():
    evidence = json.loads((CORE / "references" / "evidence-records.json").read_text(encoding="utf-8"))

    bad_scope = copy.deepcopy(evidence)
    bad_scope["records"][0]["claim_scope"] = []
    try:
        validate_document(bad_scope)
    except ValueError as exc:
        assert "claim_scope" in str(exc)
    else:
        raise AssertionError("empty claim_scope must fail validation")

    bad_volatility = copy.deepcopy(evidence)
    bad_volatility["records"][0]["volatility"] = "unknown"
    try:
        validate_document(bad_volatility)
    except ValueError as exc:
        assert "volatility" in str(exc)
    else:
        raise AssertionError("invalid volatility must fail validation")


def test_evidence_records_have_primary_source_domains():
    evidence = json.loads((CORE / "references" / "evidence-records.json").read_text(encoding="utf-8"))
    urls = "\n".join(record["url"] for record in evidence["records"])
    for domain in (
        "transparency.meta.com",
        "about.fb.com",
        "support.tiktok.com",
        "newsroom.tiktok.com",
        "support.google.com/youtube",
        "linkedin.com/help/linkedin",
        "linkedin.com/blog/engineering",
    ):
        assert domain in urls
