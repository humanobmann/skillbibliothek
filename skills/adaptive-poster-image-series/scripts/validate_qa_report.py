#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from quality_contract import END_GATES, SCORE_KEYS, SERIES_GATES, norm, strict_bool, strict_int

SUPPORTED = {".png", ".jpg", ".jpeg", ".webp"}


def fail(message: str) -> None:
    raise ValueError(message)


def validate(data: dict[str, Any], factual_mode: bool = False, output_dir: Path | None = None) -> None:
    items = data.get("items")
    if not isinstance(items, list) or len(items) != 10:
        fail("exactly 10 QA items are required")
    expected_files: list[str] = []
    note_keys: set[str] = set()
    for expected, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            fail(f"slot {expected}: object required")
        if strict_int(item.get("slot"), f"slot {expected}.slot") != expected:
            fail(f"slot order mismatch at {expected}")
        file_name = Path(str(item.get("file", ""))).name
        if not file_name or Path(file_name).suffix.lower() not in SUPPORTED:
            fail(f"slot {expected}: valid image file required")
        expected_files.append(file_name)
        if strict_bool(item.get("visual_reviewed"), f"slot {expected}.visual_reviewed") is not True:
            fail(f"slot {expected}: visual_reviewed must be true")
        notes = norm(item.get("review_notes"))
        if len(notes) < 60:
            fail(f"slot {expected}: review_notes too short")
        key = notes.casefold()
        if key in note_keys:
            fail("duplicate review_notes are not allowed")
        note_keys.add(key)
        issues = item.get("issues")
        if not isinstance(issues, list) or issues:
            fail(f"slot {expected}: unresolved issues remain")
        gates = item.get("hard_gates")
        if not isinstance(gates, dict) or set(gates) != END_GATES:
            fail(f"slot {expected}: hard_gates must exactly match schema")
        for name in END_GATES:
            if strict_bool(gates.get(name), f"slot {expected}.hard_gates.{name}") is not True:
                fail(f"slot {expected}: failed hard gate {name}")
        scores = item.get("scores")
        if not isinstance(scores, dict) or set(scores) != SCORE_KEYS:
            fail(f"slot {expected}: scores must exactly match schema")
        total = 0
        for name in SCORE_KEYS:
            value = scores.get(name)
            if type(value) is not int or value not in {4, 5}:
                fail(f"slot {expected}: score {name} must be 4 or 5")
            total += value
        if total < 44:
            fail(f"slot {expected}: total score below 44/50")

    if len(set(expected_files)) != 10:
        fail("QA report must reference ten unique files")
    if len(norm(data.get("series_review_notes"))) < 80:
        fail("series_review_notes too short")
    series = data.get("series_gates")
    if not isinstance(series, dict) or set(series) != SERIES_GATES:
        fail("series_gates must exactly match schema")
    for name in SERIES_GATES:
        if strict_bool(series.get(name), f"series_gates.{name}") is not True:
            fail(f"failed series gate {name}")
    if factual_mode and strict_bool(data.get("evidence_gate"), "evidence_gate") is not True:
        fail("factual mode requires evidence_gate=true")
    if output_dir is not None:
        if not output_dir.is_dir():
            fail("output directory does not exist")
        actual = sorted(p.name for p in output_dir.iterdir() if p.is_file() and p.suffix.lower() in SUPPORTED)
        if sorted(expected_files) != actual:
            fail("QA report file list does not match output directory")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate final ten-image QA report")
    p.add_argument("report", type=Path)
    p.add_argument("--factual-mode", action="store_true")
    p.add_argument("--output-dir", type=Path)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        data = json.loads(args.report.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            fail("report root must be object")
        validate(data, args.factual_mode, args.output_dir)
        print("PASS: final QA report satisfies image-tool-only visual gates.")
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
