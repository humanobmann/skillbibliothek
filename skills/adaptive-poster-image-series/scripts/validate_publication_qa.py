#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from quality_contract import norm, norm_lower, strict_bool, strict_int

ITEM_BOOL_FIELDS = {
    "visual_reviewed", "text_exact", "mobile_readable", "crop_resilient",
    "safe_zone_profile_passed", "source_inside_safe_area", "recompose_not_crop_confirmed",
    "standalone_effective", "facts_exact", "no_collage", "no_unrequested_branding",
    "full_graphic_design_present", "reference_design_dna_present", "raw_photo_absent",
}
BUNDLE_BOOL_FIELDS = {
    "first_frame_strong", "sequence_coherent", "essential_message_in_early_frames",
    "no_late_critical_dependency", "image_tool_only_confirmed",
    "reference_design_dna_consistent",
}


def fail(message: str) -> None:
    raise ValueError(message)


def validate(report: dict[str, Any], plan: dict[str, Any]) -> None:
    if norm_lower(report.get("platform")) != "facebook":
        fail("platform must be facebook")
    if norm_lower(report.get("mode")) != norm_lower(plan.get("mode")):
        fail("report mode must match publication plan")
    selected = plan.get("selected_slots")
    items = report.get("items")
    if not isinstance(selected, list) or not isinstance(items, list) or len(items) != len(selected):
        fail("items must match selected_slots length")
    for idx, (expected_slot, item) in enumerate(zip(selected, items), start=1):
        if not isinstance(item, dict):
            fail(f"item {idx}: object required")
        if strict_int(item.get("slot"), f"item {idx}.slot", 1) != expected_slot:
            fail(f"item {idx}: slot order mismatch")
        for field in ITEM_BOOL_FIELDS:
            if strict_bool(item.get(field), f"item {idx}.{field}") is not True:
                fail(f"item {idx}: {field} must be true")
        issues = item.get("issues")
        if not isinstance(issues, list) or issues:
            fail(f"item {idx}: unresolved issues remain")
        if len(norm(item.get("review_notes"))) < 60:
            fail(f"item {idx}: review_notes too short")
    for field in BUNDLE_BOOL_FIELDS:
        if strict_bool(report.get(field), field) is not True:
            fail(f"{field} must be true")
    if len(norm(report.get("bundle_notes"))) < 80:
        fail("bundle_notes too short")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate Facebook publication QA")
    p.add_argument("publication_qa", type=Path)
    p.add_argument("publication_plan", type=Path)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        report = json.loads(args.publication_qa.read_text(encoding="utf-8"))
        plan = json.loads(args.publication_plan.read_text(encoding="utf-8"))
        if not isinstance(report, dict) or not isinstance(plan, dict):
            fail("both roots must be objects")
        validate(report, plan)
        print("PASS: publication QA is valid and confirms image-tool-only production.")
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
