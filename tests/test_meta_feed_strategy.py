import json
import re
import subprocess
import sys
from pathlib import Path

from scripts.validate_social_evidence import validate_document

ROOT = Path(__file__).parents[1]
SKILLS = ROOT / "skills"
CORE = SKILLS / "social-platform-algorithm-core"
STRATEGY = CORE / "references" / "meta-feed-strategy.md"
EVIDENCE = CORE / "references" / "evidence-records.json"

REQUIRED_REJECTED_MYTHS = [
    "Hashtags erhoehen automatisch die Reichweite.",
    "Facebook bestraft grundsaetzlich jeden externen Link.",
    "Mehr Text im Bild reduziert automatisch die organische Reichweite.",
    "Kommentare sind immer wichtiger als Likes.",
    "4:5 erhaelt automatisch mehr Reichweite als 1:1.",
    "Meta erkennt KI-Bilder und reduziert deshalb automatisch die Reichweite.",
    "Bearbeitete Beitraege werden generell bestraft.",
    "Das Wort 'Link' im Text reduziert die Reichweite.",
    "Der Link muss in den ersten Kommentar gesetzt werden.",
    "Die ersten 60 Minuten entscheiden endgueltig ueber die Reichweite eines Posts.",
    "Viele Kommentare bedeuten automatisch hochwertigen Content.",
    "Gesichter erhalten automatisch einen Rankingbonus.",
    "Alt-Text erzeugt automatisch zusaetzliche Reichweite.",
]

# Banned prose patterns: these myths may only ever appear inside meta-feed-strategy.md
# (as explicitly rejected examples) or evidence-records.json (as status="rejected" claims).
# Anywhere else in a Facebook/Instagram-relevant skill file is a regression.
BANNED_PATTERNS = [
    r"hashtags?[^.\n]{0,25}(erh[oö]h(t|en)|boost(en)?)[^.\n]{0,20}reichweite",
    r"(jeder|jede|jedes)\s+externe[rn]?\s+link[^.\n]{0,25}(bestraft|strafe)",
    r"mehr\s+text[^.\n]{0,35}(reduziert|senkt)[^.\n]{0,20}reichweite",
    r"kommentare?\s+(sind|ist)\s+(immer\s+)?wichtiger\s+als\s+likes",
    r"4:5[^.\n]{0,25}(automatisch|garantiert)[^.\n]{0,20}(mehr\s+reichweite|rankingbonus)",
    r"(ki|ai)[- ]?bild[^.\n]{0,35}(automatisch|generell)[^.\n]{0,20}(reduziert|strafe|bestraft|schlechter)",
    r"bearbeitete\s+beitr[aä]ge[^.\n]{0,25}(generell|automatisch)\s+bestraft",
    r"link[^.\n]{0,20}(muss|soll)[^.\n]{0,20}ersten\s+kommentar",
    r"erste[n]?\s+(60\s+minuten|stunde)[^.\n]{0,35}(entscheid|endgueltig)",
    r"golden\s+hour",
    r"viele\s+kommentare[^.\n]{0,20}automatisch[^.\n]{0,20}hochwertig",
    r"gesichter?[^.\n]{0,25}automatisch(en)?\s+rankingbonus",
    r"alt.?text[^.\n]{0,35}automatisch[^.\n]{0,20}reichweite",
]

EXEMPT_FILES = {STRATEGY, EVIDENCE, Path(__file__)}

RELEVANT_DIRS = [
    CORE,
    SKILLS / "facebook-text-optimizer",
    SKILLS / "instagram-text-optimizer",
    SKILLS / "instagram-hashtag-research",
    SKILLS / "adaptive-poster-image-series",
]


def _relevant_text_files():
    for directory in RELEVANT_DIRS:
        for path in directory.rglob("*"):
            if not path.is_file() or path in EXEMPT_FILES:
                continue
            if path.suffix not in {".md", ".py", ".yaml", ".yml"}:
                continue
            if "__pycache__" in path.parts:
                continue
            yield path


def test_meta_feed_strategy_file_exists_and_is_canonical():
    assert STRATEGY.is_file()
    text = STRATEGY.read_text(encoding="utf-8")
    for token in (
        "Inventory / Retrieval",
        "Candidate Reduction",
        "Personalized Value Scoring",
        "Integrity / Eligibility",
        "Diversity / Final Composition",
        "maximal 5 Hashtags",
        "1080 x 1350",
        "Recommendation eligible",
        "eingeschraenkt distribuiert",
    ):
        assert token in text, f"meta-feed-strategy.md missing canonical token: {token}"


def test_evidence_records_validate_with_status_and_claims():
    document = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    validate_document(document)
    assert "status" in document["records"][0]
    assert isinstance(document.get("claims"), list) and document["claims"]
    for record in document["records"]:
        assert record["status"] in {"active", "superseded", "deprecated", "rejected"}


def test_all_auftrag_myths_are_rejected_claims():
    document = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    rejected_claims = {c["claim"] for c in document["claims"] if c["status"] == "rejected"}
    for myth in REQUIRED_REJECTED_MYTHS:
        assert myth in rejected_claims, f"myth not present as a rejected claim: {myth}"


def test_active_claims_never_cite_inactive_sources():
    document = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    status_by_id = {r["source_id"]: r["status"] for r in document["records"]}
    for claim in document["claims"]:
        if claim["status"] in {"active", "superseded"}:
            assert status_by_id[claim["source_id"]] not in {"deprecated", "rejected"}, (
                f"active claim cites an inactive source: {claim['claim']}"
            )


def test_no_monetization_only_ranking_claims():
    document = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    for claim in document["claims"]:
        if claim["mechanism"] == "MONETIZATION" and claim["status"] not in {"deprecated", "rejected"}:
            lowered = claim["claim"].lower()
            assert not any(term in lowered for term in ("ranking", "recommendation", "reach", "distribution"))


def test_facebook_and_instagram_route_to_canonical_meta_strategy():
    fb = (SKILLS / "facebook-text-optimizer" / "SKILL.md").read_text(encoding="utf-8")
    ig = (SKILLS / "instagram-text-optimizer" / "SKILL.md").read_text(encoding="utf-8")
    assert "meta-feed-strategy.md" in fb
    assert "social-platform-algorithm-core" in fb
    assert "meta-feed-strategy.md" in ig
    assert "social-platform-algorithm-core" in ig


def test_instagram_hashtag_cap_is_five_everywhere():
    hashtag_skill_dir = SKILLS / "instagram-hashtag-research"
    for md in hashtag_skill_dir.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        assert "bis 8" not in text, f"stale >5 hashtag cap found in {md}"
    skill_md = (hashtag_skill_dir / "SKILL.md").read_text(encoding="utf-8")
    assert "maximal 5" in skill_md


def test_instagram_and_facebook_hashtag_protocols_cap_at_five():
    ig_protocol = (SKILLS / "instagram-text-optimizer" / "references" / "hashtag-research-protocol.md").read_text(encoding="utf-8")
    assert "fünf" in ig_protocol or "5" in ig_protocol
    assert "sechs" not in ig_protocol.lower()


def test_feed_4x5_safe_zone_values_match_canonical_mandate():
    poster_skill = SKILLS / "adaptive-poster-image-series"
    for path in (
        poster_skill / "references" / "platform-safe-zones.md",
        poster_skill / "references" / "platform-delivery-schema.md",
        poster_skill / "references" / "production-plan-schema.md",
        poster_skill / "references" / "visual-qa.md",
        poster_skill / "references" / "facebook-publication-strategy.md",
        poster_skill / "scripts" / "validate_platform_delivery.py",
        poster_skill / "scripts" / "validate_publication_plan.py",
        poster_skill / "scripts" / "self_test.py",
    ):
        text = path.read_text(encoding="utf-8")
        assert "72 px" not in text and '"left": 72' not in text and '"left":72' not in text, path
    safe_zones = (poster_skill / "references" / "platform-safe-zones.md").read_text(encoding="utf-8")
    assert "mindestens 100 px" in safe_zones
    assert "mindestens 120 px" in safe_zones
    assert "40 px" in safe_zones


def test_adaptive_poster_series_self_test_passes_including_auftrag_test_10():
    poster_scripts = SKILLS / "adaptive-poster-image-series" / "scripts"
    result = subprocess.run(
        [sys.executable, "self_test.py"],
        cwd=poster_scripts,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "SELFTEST PASS" in result.stdout
    assert "critical text at x=70 must not be feed_4x5-safe" in result.stdout


def test_no_rejected_myths_restated_as_active_prose_outside_canonical_source():
    compiled = [re.compile(p, re.IGNORECASE) for p in BANNED_PATTERNS]
    violations = []
    for path in _relevant_text_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in compiled:
            if pattern.search(text):
                violations.append(f"{path.relative_to(ROOT)}: matched /{pattern.pattern}/")
    assert not violations, "myth restated outside meta-feed-strategy.md:\n" + "\n".join(violations)
