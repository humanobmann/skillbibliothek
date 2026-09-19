from pathlib import Path

ROOT = Path(__file__).parents[1]
SKILLS = ROOT / "skills"
CORE = SKILLS / "social-platform-algorithm-core"


def test_social_framework_and_profiles_exist():
    assert (CORE / "references" / "framework.md").is_file()
    assert (CORE / "references" / "platform-profiles.md").is_file()


def test_tiktok_separates_ranking_search_and_monetization():
    skill = (SKILLS / "tiktok-content-optimizer" / "SKILL.md").read_text(encoding="utf-8")
    profile = (CORE / "references" / "platform-profiles.md").read_text(encoding="utf-8")
    assert "Creator-Rewards-Metriken sind MONETIZATION" in skill
    assert "nicht als bestaetigte For-You-Ranking-Signale" in skill
    assert "TIKTOK_CREATOR_REWARDS_2024 | MONETIZATION" in profile
    assert "How TikTok recommends content" in profile


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


def test_platform_profiles_have_primary_source_domains():
    profile = (CORE / "references" / "platform-profiles.md").read_text(encoding="utf-8")
    for domain in (
        "transparency.meta.com",
        "support.tiktok.com",
        "newsroom.tiktok.com",
        "support.google.com/youtube",
        "linkedin.com/help/linkedin",
        "linkedin.com/blog/engineering",
    ):
        assert domain in profile
