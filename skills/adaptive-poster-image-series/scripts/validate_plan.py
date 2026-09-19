#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from quality_contract import (
    ACCENT_STRENGTHS, AUSTRIA_STRATEGIES, BRANDING_MODES, DENSITIES,
    DESIGN_SYSTEMS, DESIGN_VARIANTS, HARD_CLAIM_TYPES, INPUT_MODES, LAYOUT_FAMILIES,
    MOTIF_TYPES, NEGATIVE_SPACE, REFERENCE_STRATEGIES, RENDER_STRATEGIES, SLOT_ROLES,
    VISIBLE_CONTENT_TYPES,
    finite_float, norm, norm_lower, numeric_tokens, strict_bool, strict_int,
)
from validate_claim_ledger import validate as validate_claims

SERIES_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{1,63}$")


def fail(message: str) -> None:
    raise ValueError(message)


def load_claims(path: Path | None) -> dict[str, dict[str, Any]] | None:
    if path is None:
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("claim ledger root must be an object")
    return validate_claims(data)


def validate(data: dict[str, Any], claims: dict[str, dict[str, Any]] | None = None) -> list[str]:
    warnings: list[str] = []
    job = data.get("job")
    cd = data.get("creative_direction")
    slots = data.get("slots")
    if not isinstance(job, dict):
        fail("job must be an object")
    if not isinstance(cd, dict):
        fail("creative_direction must be an object")
    if not isinstance(slots, list) or len(slots) != 10:
        fail("exactly 10 slots are required")

    series_id = norm_lower(job.get("series_id"))
    if not SERIES_ID_RE.match(series_id):
        fail("job.series_id must be 2..64 lowercase filename-safe characters")
    if job.get("locale") != "de-AT":
        fail("job.locale must be 'de-AT'")
    if norm_lower(job.get("input_mode")) not in INPUT_MODES:
        fail("invalid job.input_mode")
    factual_mode = strict_bool(job.get("factual_mode"), "job.factual_mode")
    if norm_lower(job.get("branding_mode")) not in BRANDING_MODES:
        fail("invalid job.branding_mode")
    if strict_int(job.get("output_count"), "job.output_count") != 10:
        fail("job.output_count must be 10")
    if job.get("aspect_ratio") != "4:5":
        fail("job.aspect_ratio must be '4:5'")
    if strict_bool(job.get("image_tool_only"), "job.image_tool_only") is not True:
        fail("job.image_tool_only must be true")
    if norm_lower(job.get("design_system")) not in DESIGN_SYSTEMS:
        fail("job.design_system must be civic_editorial_red_ivory")
    if strict_bool(job.get("design_lock"), "job.design_lock") is not True:
        fail("job.design_lock must be true")
    if strict_bool(job.get("design_required"), "job.design_required") is not True:
        fail("job.design_required must be true")
    if strict_bool(job.get("raw_photo_forbidden"), "job.raw_photo_forbidden") is not True:
        fail("job.raw_photo_forbidden must be true")
    if norm_lower(job.get("safe_zone_profile")) != "feed_4x5":
        fail("job.safe_zone_profile must be feed_4x5")
    if norm_lower(job.get("safe_zone_contract")) != "internal_conservative_v1":
        fail("job.safe_zone_contract must be internal_conservative_v1")
    if strict_bool(job.get("official_platform_safe_zone"), "job.official_platform_safe_zone") is not False:
        fail("internal safe-zone contract must not be labelled official")

    if len(norm(cd.get("design_intent"))) < 20:
        fail("creative_direction.design_intent is too short")
    voice = cd.get("visual_voice")
    if not isinstance(voice, list) or not 3 <= len(voice) <= 8 or any(not norm(v) for v in voice):
        fail("creative_direction.visual_voice must contain 3..8 entries")
    for key in ("image_direction", "typography_direction", "palette_direction"):
        if len(norm(cd.get(key))) < 18:
            fail(f"creative_direction.{key} is too short")
    if norm_lower(cd.get("austria_strategy")) not in AUSTRIA_STRATEGIES:
        fail("invalid creative_direction.austria_strategy")
    if norm_lower(cd.get("reference_strategy")) not in REFERENCE_STRATEGIES:
        fail("creative_direction.reference_strategy must be principles_not_copy")
    design_reference_mode = norm_lower(cd.get("design_reference_mode"))
    if design_reference_mode != "anchored":
        fail("creative_direction.design_reference_mode must be anchored")
    if norm_lower(cd.get("design_reference_profile")) != "austria-editorial-civic-v1":
        fail("creative_direction.design_reference_profile must be austria-editorial-civic-v1")
    anchor_assets = cd.get("style_anchor_assets")
    expected_anchors = {
        "assets/style-anchors/reference-1.jpg",
        "assets/style-anchors/reference-2.jpg",
        "assets/style-anchors/reference-3.jpg",
    }
    if not isinstance(anchor_assets, list) or set(map(norm, anchor_assets)) != expected_anchors:
        fail("creative_direction.style_anchor_assets must contain exactly the three bundled style anchors")
    anti = cd.get("anti_goals")
    if not isinstance(anti, list) or len(anti) < 6 or any(not norm(x) for x in anti):
        fail("creative_direction.anti_goals must contain at least six entries")

    roles, layouts, strategies, motifs, design_variants = [], [], [], [], []
    seen_slots: set[int] = set()
    for expected, slot in enumerate(slots, start=1):
        if not isinstance(slot, dict):
            fail(f"slot {expected}: object required")
        n = strict_int(slot.get("slot"), f"slot {expected}.slot")
        if n != expected or n in seen_slots:
            fail(f"slot order mismatch or duplicate at {expected}")
        seen_slots.add(n)

        role = norm_lower(slot.get("role"))
        if role not in SLOT_ROLES:
            fail(f"slot {expected}: invalid role")
        roles.append(role)

        headline = norm(slot.get("headline"))
        if not headline:
            fail(f"slot {expected}: headline required")
        lines = slot.get("headline_lines")
        if not isinstance(lines, list) or not 1 <= len(lines) <= 4 or any(not norm(x) for x in lines):
            fail(f"slot {expected}: headline_lines must contain 1..4 lines")
        if norm(" ".join(lines)) != headline:
            fail(f"slot {expected}: headline_lines do not reproduce headline exactly")

        source_label = norm(slot.get("source_label"))
        if len(source_label) > 120:
            fail(f"slot {expected}: source_label too long for image-tool typography")

        content_type = norm_lower(slot.get("content_type"))
        if content_type not in VISIBLE_CONTENT_TYPES:
            fail(f"slot {expected}: invalid content_type")

        claim_ids = slot.get("claim_ids")
        if not isinstance(claim_ids, list) or any(not norm(x) for x in claim_ids):
            fail(f"slot {expected}: claim_ids must be an array of ids")
        source_claim_id = norm(slot.get("source_claim_id"))

        strategy = norm_lower(slot.get("render_strategy"))
        if strategy not in RENDER_STRATEGIES:
            fail(f"slot {expected}: invalid render_strategy {strategy!r}")
        strategies.append(strategy)

        design_variant = norm_lower(slot.get("design_variant"))
        if design_variant not in DESIGN_VARIANTS:
            fail(f"slot {expected}: invalid design_variant {design_variant!r}")
        design_variants.append(design_variant)

        motif = norm_lower(slot.get("motif_type"))
        if motif not in MOTIF_TYPES:
            fail(f"slot {expected}: invalid motif_type")
        motifs.append(motif)

        layout = norm_lower(slot.get("layout_family"))
        if layout not in LAYOUT_FAMILIES:
            fail(f"slot {expected}: invalid layout_family")
        layouts.append(layout)

        if norm_lower(slot.get("negative_space")) not in NEGATIVE_SPACE:
            fail(f"slot {expected}: invalid negative_space")
        finite_float(slot.get("focus_x"), f"slot {expected}.focus_x", 0, 1)
        finite_float(slot.get("focus_y"), f"slot {expected}.focus_y", 0, 1)
        if norm_lower(slot.get("accent_strength")) not in ACCENT_STRENGTHS:
            fail(f"slot {expected}: invalid accent_strength")
        if norm_lower(slot.get("density")) not in DENSITIES:
            fail(f"slot {expected}: invalid density")
        if strict_bool(slot.get("design_required"), f"slot {expected}.design_required") is not True:
            fail(f"slot {expected}: design_required must be true")
        if not norm(slot.get("text_block_position")):
            fail(f"slot {expected}: text_block_position required")
        if not norm(slot.get("photo_zone")):
            fail(f"slot {expected}: photo_zone required")
        accent_elements = slot.get("accent_elements")
        if not isinstance(accent_elements, list) or not 1 <= len(accent_elements) <= 3 or any(not norm(x) for x in accent_elements):
            fail(f"slot {expected}: accent_elements must contain 1..3 entries")
        strict_bool(slot.get("risk_overclaim"), f"slot {expected}.risk_overclaim")
        if strict_bool(slot.get("visible_text_required"), f"slot {expected}.visible_text_required") is not True:
            fail(f"slot {expected}: visible_text_required must be true")
        if strict_bool(slot.get("full_design_required"), f"slot {expected}.full_design_required") is not True:
            fail(f"slot {expected}: full_design_required must be true")
        if strict_bool(slot.get("raw_photo_forbidden"), f"slot {expected}.raw_photo_forbidden") is not True:
            fail(f"slot {expected}: raw_photo_forbidden must be true")
        if finite_float(slot.get("hero_clearance_percent"), f"slot {expected}.hero_clearance_percent", 0) < 8:
            fail(f"slot {expected}: hero_clearance_percent must be >= 8")
        if finite_float(slot.get("motif_crop_reserve_percent"), f"slot {expected}.motif_crop_reserve_percent", 0) < 12:
            fail(f"slot {expected}: motif_crop_reserve_percent must be >= 12")
        if strict_bool(slot.get("source_inside_safe_area"), f"slot {expected}.source_inside_safe_area") is not True:
            fail(f"slot {expected}: source_inside_safe_area must be true")
        if len(norm(slot.get("design_brief"))) < 120:
            fail(f"slot {expected}: design_brief too short")
        if len(norm(slot.get("image_brief"))) < 50:
            fail(f"slot {expected}: image_brief too short")
        if len(norm(slot.get("alt_text"))) < 30:
            fail(f"slot {expected}: alt_text too short")

        if factual_mode and content_type in HARD_CLAIM_TYPES:
            if claims is None:
                fail(f"slot {expected}: factual hard claim requires claim ledger")
            if not claim_ids:
                fail(f"slot {expected}: hard claim requires claim_ids")
            if source_claim_id not in claim_ids:
                fail(f"slot {expected}: source_claim_id must reference claim_ids")
            for cid in claim_ids:
                if cid not in claims:
                    fail(f"slot {expected}: unknown claim id {cid}")
            claim_text = " ".join(norm(claims[cid].get("approved_text")) for cid in claim_ids)
            poster_text = " ".join([
                norm(slot.get("eyebrow")), headline, norm(slot.get("subline")), source_label
            ])
            missing_numbers = numeric_tokens(poster_text) - numeric_tokens(claim_text + " " + " ".join(norm(claims[cid].get("poster_source")) for cid in claim_ids))
            if missing_numbers:
                fail(f"slot {expected}: visible numeric tokens not present in claims: {sorted(missing_numbers)}")
        elif factual_mode and claim_ids and claims is not None:
            for cid in claim_ids:
                if cid not in claims:
                    fail(f"slot {expected}: unknown claim id {cid}")

    if len(set(roles)) < 6:
        warnings.append("series uses fewer than six distinct dramaturgical roles")
    layout_counts = Counter(layouts)
    if max(layout_counts.values()) > 3:
        fail("no layout_family may appear more than three times")
    if len(set(layouts)) < 5:
        warnings.append("series uses fewer than five layout families")
    if len(set(strategies)) < 2:
        warnings.append("series uses only one render strategy")
    if len(set(motifs)) < 3:
        warnings.append("series uses fewer than three motif types")
    if len(set(design_variants)) < 3:
        warnings.append("series uses fewer than three design variants")
    return warnings


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate image-tool-only ten-slot production plan")
    p.add_argument("plan", type=Path)
    p.add_argument("--claims", type=Path)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        data = json.loads(args.plan.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            fail("plan root must be an object")
        claims = load_claims(args.claims)
        warnings = validate(data, claims)
        print("PASS: ten-slot image-tool-only production plan is structurally valid.")
        for warning in warnings:
            print(f"WARN: {warning}")
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
