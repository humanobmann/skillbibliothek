#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from quality_contract import finite_float, norm, norm_lower, strict_bool, strict_int

PROFILES = {
    "feed_4x5": {
        "width": 1080, "height": 1350,
        "safe": {"left": 100, "right": 100, "top": 100, "bottom": 120},
        "suffix": "feed-4x5",
    },
    "square_1x1": {
        "width": 1080, "height": 1080,
        "safe": {"left": 90, "right": 90, "top": 90, "bottom": 90},
        "suffix": "square-1x1",
    },
    "vertical_9x16": {
        "width": 1080, "height": 1920,
        "safe": {"left": 90, "right": 160, "top": 288, "bottom": 384},
        "suffix": "vertical-9x16",
    },
}


def fail(message: str) -> None:
    raise ValueError(message)


def validate(plan: dict[str, Any], production: dict[str, Any]) -> None:
    series_id = norm(plan.get("series_id"))
    prod_series = norm(production.get("job", {}).get("series_id"))
    if not series_id or series_id != prod_series:
        fail("series_id must match production plan")

    mode = norm_lower(plan.get("delivery_mode"))
    if mode not in {"masters_only", "full_social_30"}:
        fail("delivery_mode must be masters_only or full_social_30")
    if strict_bool(plan.get("image_tool_only"), "image_tool_only") is not True:
        fail("image_tool_only must be true")
    if strict_bool(plan.get("recompose_not_crop"), "recompose_not_crop") is not True:
        fail("recompose_not_crop must be true")
    if norm_lower(plan.get("safe_zone_contract")) != "internal_conservative_v1":
        fail("safe_zone_contract must be internal_conservative_v1")
    if strict_bool(plan.get("official_platform_safe_zone"), "official_platform_safe_zone") is not False:
        fail("internal safe zones must not be labelled official platform safe zones")

    outputs = plan.get("outputs")
    expected_count = 10 if mode == "masters_only" else 30
    if not isinstance(outputs, list) or len(outputs) != expected_count:
        fail(f"delivery_mode {mode} requires exactly {expected_count} outputs")

    seen_files: set[str] = set()
    per_slot: Counter[int] = Counter()

    for idx, item in enumerate(outputs, start=1):
        if not isinstance(item, dict):
            fail(f"output {idx}: object required")
        slot = strict_int(item.get("slot"), f"output {idx}.slot", 1)
        if slot > 10:
            fail(f"output {idx}: slot must be 1..10")

        variant = norm_lower(item.get("variant"))
        if variant not in PROFILES:
            fail(f"output {idx}: invalid variant")
        if mode == "masters_only" and variant != "feed_4x5":
            fail("masters_only may contain only feed_4x5 outputs")

        profile = PROFILES[variant]
        width = strict_int(item.get("width"), f"output {idx}.width", 1)
        height = strict_int(item.get("height"), f"output {idx}.height", 1)
        if (width, height) != (profile["width"], profile["height"]):
            fail(f"output {idx}: dimensions do not match {variant}")

        safe = item.get("safe_area_px")
        if not isinstance(safe, dict) or set(safe) != {"left", "right", "top", "bottom"}:
            fail(f"output {idx}: safe_area_px must contain left/right/top/bottom")
        for edge, expected in profile["safe"].items():
            actual = strict_int(safe.get(edge), f"output {idx}.safe_area_px.{edge}", 0)
            if actual < expected:
                fail(f"output {idx}: {variant} safe area on {edge} must be >= {expected}")

        if finite_float(item.get("hero_clearance_percent"), f"output {idx}.hero_clearance_percent", 0) < 8:
            fail(f"output {idx}: hero_clearance_percent must be >= 8")
        if finite_float(item.get("motif_crop_reserve_percent"), f"output {idx}.motif_crop_reserve_percent", 0) < 12:
            fail(f"output {idx}: motif_crop_reserve_percent must be >= 12")
        if strict_bool(item.get("source_inside_safe_area"), f"output {idx}.source_inside_safe_area") is not True:
            fail(f"output {idx}: source_inside_safe_area must be true")
        if strict_bool(item.get("recompose_not_crop"), f"output {idx}.recompose_not_crop") is not True:
            fail(f"output {idx}: recompose_not_crop must be true")

        expected_file = f"{slot:02d}-{profile['suffix']}.png"
        file_name = Path(norm(item.get("file"))).name
        if file_name != expected_file:
            fail(f"output {idx}: file must be {expected_file}")
        if file_name in seen_files:
            fail(f"output {idx}: duplicate file name")
        seen_files.add(file_name)
        per_slot[slot] += 1

    if set(per_slot) != set(range(1, 11)):
        fail("all ten slots must be present")
    expected_per_slot = 1 if mode == "masters_only" else 3
    if any(per_slot[slot] != expected_per_slot for slot in range(1, 11)):
        fail(f"each slot must contain exactly {expected_per_slot} output(s)")

    if mode == "full_social_30":
        by_slot = {slot: set() for slot in range(1, 11)}
        for item in outputs:
            by_slot[int(item["slot"])].add(norm_lower(item["variant"]))
        required = set(PROFILES)
        if any(by_slot[slot] != required for slot in range(1, 11)):
            fail("full_social_30 requires all three variants for every slot")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate cross-platform social delivery plan")
    p.add_argument("delivery_plan", type=Path)
    p.add_argument("production_plan", type=Path)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        delivery = json.loads(args.delivery_plan.read_text(encoding="utf-8"))
        production = json.loads(args.production_plan.read_text(encoding="utf-8"))
        if not isinstance(delivery, dict) or not isinstance(production, dict):
            fail("both roots must be objects")
        validate(delivery, production)
        print("PASS: platform delivery plan satisfies safe-zone and recomposition contract.")
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
