#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from quality_contract import norm, norm_lower, strict_bool, strict_int

MODE_COUNTS = {"single": 1, "pair": 2, "trio": 3, "quad": 4}
SAFE_PROFILES = {
    "feed_4x5": {"left": 100, "right": 100, "top": 100, "bottom": 120},
    "square_1x1": {"left": 90, "right": 90, "top": 90, "bottom": 90},
}


def fail(message: str) -> None:
    raise ValueError(message)


def validate(plan: dict[str, Any], production: dict[str, Any]) -> None:
    if norm_lower(plan.get("platform")) != "facebook":
        fail("platform must be facebook")
    mode = norm_lower(plan.get("mode"))
    if mode not in {"single", "pair", "trio", "quad", "gallery", "auto"}:
        fail("invalid publication mode")
    if mode == "auto":
        fail("mode=auto must be resolved before validation for production")
    if strict_bool(plan.get("image_tool_only"), "image_tool_only") is not True:
        fail("image_tool_only must be true")
    if norm_lower(plan.get("design_system")) != norm_lower(production.get("job", {}).get("design_system")):
        fail("publication design_system must match production plan")
    if norm_lower(plan.get("design_reference_profile")) != norm_lower(production.get("creative_direction", {}).get("design_reference_profile")):
        fail("publication design_reference_profile must match production plan")
    if strict_bool(plan.get("design_lock"), "design_lock") is not True:
        fail("publication design_lock must be true")

    source_series = norm(plan.get("source_series"))
    prod_series = norm(production.get("job", {}).get("series_id"))
    if not source_series or source_series != prod_series:
        fail("source_series must match production plan")

    selected = plan.get("selected_slots")
    if not isinstance(selected, list) or not selected:
        fail("selected_slots must be a non-empty array")
    if any(type(x) is not int or x < 1 or x > 10 for x in selected):
        fail("selected_slots must contain integers 1..10")
    if len(set(selected)) != len(selected):
        fail("selected_slots must be unique")

    if mode in MODE_COUNTS and len(selected) != MODE_COUNTS[mode]:
        fail(f"mode {mode} requires exactly {MODE_COUNTS[mode]} selected slots")
    if mode == "gallery" and not 5 <= len(selected) <= 10:
        fail("gallery requires 5..10 selected slots")

    primary = strict_int(plan.get("primary_slot"), "primary_slot", 1)
    if primary not in selected:
        fail("primary_slot must be in selected_slots")

    aspect = norm(plan.get("aspect_ratio"))
    if mode == "single" and aspect != "4:5":
        fail("single must use 4:5")
    if mode in {"pair", "trio", "quad"} and aspect != "1:1":
        fail(f"{mode} must use 1:1")
    if mode == "gallery" and aspect not in {"1:1", "4:5"}:
        fail("gallery aspect_ratio must be 1:1 or 4:5")

    width = strict_int(plan.get("target_width"), "target_width", 1)
    height = strict_int(plan.get("target_height"), "target_height", 1)
    if aspect == "1:1" and width != height:
        fail("1:1 target must be square")
    if aspect == "4:5" and width * 5 != height * 4:
        fail("4:5 target dimensions must match 4:5")

    expected_profile = "feed_4x5" if aspect == "4:5" else "square_1x1"
    profile = norm_lower(plan.get("safe_zone_profile"))
    if profile != expected_profile:
        fail(f"safe_zone_profile must be {expected_profile} for aspect ratio {aspect}")
    safe = plan.get("safe_area_px")
    if not isinstance(safe, dict) or set(safe) != {"left", "right", "top", "bottom"}:
        fail("safe_area_px must contain left/right/top/bottom")
    for edge, minimum in SAFE_PROFILES[profile].items():
        actual = strict_int(safe.get(edge), f"safe_area_px.{edge}", 0)
        if actual < minimum:
            fail(f"safe_area_px.{edge} must be >= {minimum}")
    if strict_bool(plan.get("recompose_not_crop"), "recompose_not_crop") is not True:
        fail("recompose_not_crop must be true")
    if strict_bool(plan.get("official_platform_safe_zone"), "official_platform_safe_zone") is not False:
        fail("internal safe zone must not be labelled an official platform safe zone")

    sequence = plan.get("sequence")
    if not isinstance(sequence, list) or len(sequence) != len(selected):
        fail("sequence must match selected_slots length")
    seq_slots = []
    for idx, item in enumerate(sequence, start=1):
        if not isinstance(item, dict):
            fail(f"sequence {idx}: object required")
        slot = strict_int(item.get("slot"), f"sequence {idx}.slot", 1)
        if not norm(item.get("function")):
            fail(f"sequence {idx}: function required")
        seq_slots.append(slot)
    if seq_slots != selected:
        fail("sequence slots must exactly match selected_slots in order")

    for field in ("primary_message", "first_frame_reason", "continuation_logic"):
        if len(norm(plan.get(field))) < 20:
            fail(f"{field} is too short")

    if mode == "gallery" and len(norm(plan.get("gallery_reason"))) < 30:
        fail("gallery requires a concrete gallery_reason")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate Facebook publication plan")
    p.add_argument("publication_plan", type=Path)
    p.add_argument("production_plan", type=Path)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        pub = json.loads(args.publication_plan.read_text(encoding="utf-8"))
        prod = json.loads(args.production_plan.read_text(encoding="utf-8"))
        if not isinstance(pub, dict) or not isinstance(prod, dict):
            fail("both roots must be objects")
        validate(pub, prod)
        print("PASS: Facebook publication plan is valid and image-tool-only.")
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
