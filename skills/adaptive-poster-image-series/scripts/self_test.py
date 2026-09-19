#!/usr/bin/env python3
from __future__ import annotations

import copy
from pathlib import Path

from validate_plan import validate as validate_plan
from validate_publication_plan import validate as validate_publication_plan
from validate_publication_qa import validate as validate_publication_qa


def expect_fail(label, fn):
    try:
        fn()
    except ValueError:
        print(f"PASS negative: {label}")
        return
    raise AssertionError(f"expected failure: {label}")


def production_plan():
    roles = ["hook", "context", "fact", "explanation", "finding", "contrast", "question", "demand", "evidence", "close"]
    layouts = ["editorial-split", "photo-negative-space", "number-led", "editorial-card", "signal-field", "comparison-led", "question-led", "timeline-led", "source-led", "quiet-close"]
    strategies = ["photo_editorial", "typographic_editorial", "diagrammatic_editorial", "abstract_editorial", "photo_editorial", "typographic_editorial", "abstract_editorial", "diagrammatic_editorial", "photo_editorial", "typographic_editorial"]
    design_variants = ["oversize_keyword_photo", "hero_type_photo", "number_led_poster", "type_graphic_photo", "oversize_keyword_photo", "typographic_signal", "type_graphic_photo", "number_led_poster", "hero_type_photo", "quiet_close_poster"]
    motifs = ["people", "architecture", "data", "type", "object", "data", "abstract", "data", "source", "type"]
    slots = []
    for i in range(10):
        text = f"Kernaussage Nummer {i+1}."
        slots.append({
            "slot": i+1,
            "role": roles[i],
            "eyebrow": "KONTEXT",
            "headline": text,
            "headline_lines": [text],
            "subline": "Kurze Einordnung fuer mobile Lesbarkeit.",
            "source_label": "",
            "content_type": "political_opinion",
            "claim_ids": [],
            "source_claim_id": "",
            "render_strategy": strategies[i],
            "design_variant": design_variants[i],
            "motif_type": motifs[i],
            "subject": "Eine glaubwuerdige konkrete Szene oder grafische Hauptidee passend zur Aussage.",
            "layout_family": layouts[i],
            "negative_space": "upper-left",
            "focus_x": 0.6,
            "focus_y": 0.58,
            "accent_strength": "medium" if i not in {4, 9} else "strong",
            "density": "low" if i in {0, 9} else "medium",
            "design_required": True,
            "text_block_position": "Upper-left editorial text block with about eight percent margin and a dominant stacked headline.",
            "photo_zone": "Lower fifty-eight percent as a thematic image or graphic content zone integrated with the typography.",
            "accent_elements": ["sweeping red signal curve"],
            "visible_text_required": True,
            "full_design_required": True,
            "raw_photo_forbidden": True,
            "design_brief": "A finished four-to-five editorial poster in the locked ivory red graphite reference design, with large left-aligned grotesk type in the upper area, an integrated thematic image zone below, and a visible red signal curve connecting text and image. Never output a raw photo or an empty text placeholder.",
            "image_brief": "A single fully designed editorial social image with finished typography, visible graphic design and a credible thematic visual zone.",
            "risk_overclaim": False,
            "alt_text": "A finished editorial poster with a clear visible headline, red signal accent and a thematic visual supporting the message.",
        })
    return {
        "job": {
            "series_id": "self-test-series",
            "locale": "de-AT",
            "input_mode": "theme",
            "factual_mode": False,
            "branding_mode": "none",
            "output_count": 10,
            "aspect_ratio": "4:5",
            "image_tool_only": True,
            "design_system": "civic_editorial_red_ivory",
            "design_lock": True,
            "design_required": True,
            "raw_photo_forbidden": True,
        },
        "creative_direction": {
            "design_intent": "A finished civic editorial poster series with bold type, ivory ground, signal red accents and integrated thematic visuals.",
            "visual_voice": ["editorial", "credible", "bold", "precise", "human"],
            "image_direction": "Credible thematic photography or graphic content integrated into a fully designed editorial poster, never a raw image.",
            "typography_direction": "Large left-aligned modern grotesk display type with controlled line breaks and strong mobile hierarchy.",
            "palette_direction": "Warm ivory, signal red and dark graphite as the locked visual DNA.",
            "austria_strategy": "contextual_not_symbolic",
            "reference_strategy": "principles_not_copy",
            "design_reference_mode": "anchored",
            "design_reference_profile": "austria-editorial-civic-v1",
            "style_anchor_assets": [
                "assets/style-anchors/reference-1.jpg",
                "assets/style-anchors/reference-2.jpg",
                "assets/style-anchors/reference-3.jpg",
            ],
            "anti_goals": ["raw photo", "empty text placeholder", "generic AI", "fake evidence", "crime mood", "branding", "collage", "template monotony"],
        },
        "slots": slots,
    }


def publication_plan():
    return {
        "platform": "facebook",
        "mode": "trio",
        "source_series": "self-test-series",
        "selected_slots": [1, 4, 10],
        "primary_slot": 1,
        "aspect_ratio": "1:1",
        "target_width": 1080,
        "target_height": 1080,
        "image_tool_only": True,
        "design_system": "civic_editorial_red_ivory",
        "design_reference_profile": "austria-editorial-civic-v1",
        "design_lock": True,
        "design_margin": {
            "type": "crop_resilience",
            "value_percent": 10,
            "official_platform_safe_zone": False,
        },
        "sequence": [
            {"slot": 1, "function": "hook"},
            {"slot": 4, "function": "explanation"},
            {"slot": 10, "function": "close"},
        ],
        "primary_message": "Der erste Frame traegt die Kernaussage des gesamten Bundles.",
        "first_frame_reason": "Der erste Frame erklaert Thema und Richtung ohne weitere Karte.",
        "continuation_logic": "Die zweite Karte vertieft und die dritte Karte schliesst die Argumentation.",
        "gallery_reason": None,
        "platform_assumption": "Square multi-image composition for robust readability.",
        "verified_on": "2026-09-05",
        "source_type": "current platform research",
        "confidence": "medium",
    }


def publication_qa():
    items = []
    for slot in [1, 4, 10]:
        items.append({
            "slot": slot,
            "visual_reviewed": True,
            "text_exact": True,
            "mobile_readable": True,
            "crop_resilient": True,
            "standalone_effective": True,
            "facts_exact": True,
            "no_collage": True,
            "no_unrequested_branding": True,
            "full_graphic_design_present": True,
            "reference_design_dna_present": True,
            "raw_photo_absent": True,
            "issues": [],
            "review_notes": "The actual publication image was reviewed for exact text, full poster design, reference DNA, mobile hierarchy, crop resilience and standalone clarity.",
        })
    return {
        "platform": "facebook",
        "mode": "trio",
        "items": items,
        "first_frame_strong": True,
        "sequence_coherent": True,
        "essential_message_in_early_frames": True,
        "no_late_critical_dependency": True,
        "image_tool_only_confirmed": True,
        "reference_design_dna_consistent": True,
        "bundle_notes": "The three separate images form a coherent sequence and retain the locked ivory red graphite design DNA while each remains independently understandable.",
    }


def main():
    root = Path(__file__).resolve().parents[1]
    for rel in [
        "assets/style-anchors/reference-1.jpg",
        "assets/style-anchors/reference-2.jpg",
        "assets/style-anchors/reference-3.jpg",
    ]:
        if not (root / rel).is_file():
            raise AssertionError(f"missing style anchor: {rel}")
    print("PASS positive: all three bundled style anchors exist")

    prod = production_plan()
    warnings = validate_plan(prod, None)
    print(f"PASS positive: production plan ({len(warnings)} warnings)")

    bad = copy.deepcopy(prod)
    bad["job"]["image_tool_only"] = False
    expect_fail("alternative image production enabled", lambda: validate_plan(bad, None))

    bad = copy.deepcopy(prod)
    bad["job"]["design_lock"] = False
    expect_fail("design lock disabled", lambda: validate_plan(bad, None))

    bad = copy.deepcopy(prod)
    bad["creative_direction"]["design_reference_mode"] = "none"
    expect_fail("style anchors disabled", lambda: validate_plan(bad, None))

    bad = copy.deepcopy(prod)
    bad["slots"][0]["raw_photo_forbidden"] = False
    expect_fail("raw photo allowed", lambda: validate_plan(bad, None))

    bad = copy.deepcopy(prod)
    bad["slots"][0]["visible_text_required"] = False
    expect_fail("visible text not required", lambda: validate_plan(bad, None))

    bad = copy.deepcopy(prod)
    bad["slots"][0]["full_design_required"] = False
    expect_fail("full graphic design not required", lambda: validate_plan(bad, None))

    bad = copy.deepcopy(prod)
    bad["slots"][0]["design_brief"] = "too short"
    expect_fail("design brief too short", lambda: validate_plan(bad, None))

    bad = copy.deepcopy(prod)
    bad["slots"] = bad["slots"][:9]
    expect_fail("nine slots", lambda: validate_plan(bad, None))

    pub = publication_plan()
    validate_publication_plan(pub, prod)
    print("PASS positive: trio publication plan")

    bad_pub = copy.deepcopy(pub)
    bad_pub["aspect_ratio"] = "4:5"
    expect_fail("trio with 4:5", lambda: validate_publication_plan(bad_pub, prod))

    bad_pub = copy.deepcopy(pub)
    bad_pub["image_tool_only"] = False
    expect_fail("publication uses other image tooling", lambda: validate_publication_plan(bad_pub, prod))

    bad_pub = copy.deepcopy(pub)
    bad_pub["design_lock"] = False
    expect_fail("publication design lock disabled", lambda: validate_publication_plan(bad_pub, prod))

    qa = publication_qa()
    validate_publication_qa(qa, pub)
    print("PASS positive: publication QA")

    bad_qa = copy.deepcopy(qa)
    bad_qa["image_tool_only_confirmed"] = False
    expect_fail("publication QA does not confirm image tool only", lambda: validate_publication_qa(bad_qa, pub))

    bad_qa = copy.deepcopy(qa)
    bad_qa["items"][0]["reference_design_dna_present"] = False
    expect_fail("publication image drifts from reference design", lambda: validate_publication_qa(bad_qa, pub))

    print("SELFTEST PASS: contracts enforce ten separate fully designed masters, locked reference design, Facebook bundle rules and exclusive image-tool production without generating images.")


if __name__ == "__main__":
    main()
