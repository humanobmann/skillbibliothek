#!/usr/bin/env python3
"""Validate ten reviewed image results and optional output files."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from itertools import combinations
from pathlib import Path
from typing import Any

try:
    from PIL import Image, ImageOps, ImageStat
except ImportError as exc:
    raise SystemExit("Pillow is required: python -m pip install Pillow") from exc

SUPPORTED = {".png", ".jpg", ".jpeg", ".webp"}
REVIEW_FIELDS = (
    "single_scene",
    "correct_slot",
    "content_preserved",
    "requirements_met",
    "no_cross_slot_leakage",
    "no_unrequested_text",
    "no_unrequested_branding",
    "technical_quality",
    "passed",
)


def parse_aspect(value: str) -> float:
    match = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*:\s*(\d+(?:\.\d+)?)\s*", value)
    if not match:
        raise argparse.ArgumentTypeError("aspect must use W:H, for example 4:5")
    width, height = float(match.group(1)), float(match.group(2))
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("aspect values must be positive")
    return width / height


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def dhash(image: Image.Image, hash_size: int = 16) -> int:
    gray = ImageOps.grayscale(image).resize(
        (hash_size + 1, hash_size), Image.Resampling.LANCZOS
    )
    pixels = (
        list(gray.get_flattened_data())
        if hasattr(gray, "get_flattened_data")
        else list(gray.getdata())
    )
    value = 0
    row_width = hash_size + 1
    for row in range(hash_size):
        offset = row * row_width
        for column in range(hash_size):
            value = (value << 1) | int(
                pixels[offset + column] > pixels[offset + column + 1]
            )
    return value


def hamming(left: int, right: int) -> int:
    return (left ^ right).bit_count()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--aspect", type=parse_aspect)
    parser.add_argument("--aspect-tolerance", type=float, default=0.015)
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    parser.add_argument("--near-duplicate-distance", type=int, default=8)
    parser.add_argument("--fail-near-duplicates", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    details: list[dict[str, Any]] = []

    try:
        data: Any = json.loads(args.manifest.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: manifest not found: {args.manifest}", file=sys.stderr)
        return 2
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read manifest: {exc}", file=sys.stderr)
        return 1

    items = data.get("items") if isinstance(data, dict) else None
    if not isinstance(items, list):
        errors.append("manifest must contain an items array")
        items = []
    if len(items) != 10:
        errors.append(f"exactly 10 items required, found {len(items)}")

    expected_aspect = args.aspect
    if expected_aspect is None and isinstance(data, dict):
        requested = data.get("requested_aspect")
        if isinstance(requested, str):
            try:
                expected_aspect = parse_aspect(requested)
            except argparse.ArgumentTypeError:
                warnings.append("requested_aspect is invalid and was not checked")

    slots: set[int] = set()
    result_ids: set[str] = set()
    output_paths: set[Path] = set()
    output_names: set[str] = set()
    byte_hashes: dict[str, str] = {}
    perceptual: dict[str, int] = {}

    for position, raw in enumerate(items, start=1):
        label = f"item {position}"
        if not isinstance(raw, dict):
            errors.append(f"{label} must be an object")
            continue
        slot = raw.get("slot")
        if not isinstance(slot, int) or not 1 <= slot <= 10:
            errors.append(f"{label}: invalid slot")
        elif slot in slots:
            errors.append(f"{label}: duplicate slot {slot}")
        else:
            slots.add(slot)

        if raw.get("status") != "valid":
            errors.append(f"{label}: status must be 'valid'")
        attempts = raw.get("attempts")
        if not isinstance(attempts, int) or attempts < 1:
            errors.append(f"{label}: attempts must be at least 1")

        review = raw.get("review")
        if not isinstance(review, dict):
            errors.append(f"{label}: review must be an object")
        else:
            for field in REVIEW_FIELDS:
                if review.get(field) is not True:
                    errors.append(f"{label}: review.{field} must be true")

        tool_call_id = str(raw.get("tool_call_id", "") or "").strip()
        output_file_id = str(raw.get("output_file_id", "") or "").strip()
        output_path_value = str(raw.get("output_path", "") or "").strip()
        result_key = output_file_id or tool_call_id
        if args.strict and not tool_call_id:
            errors.append(f"{label}: tool_call_id is required in strict mode")
        if args.strict and not (output_file_id or output_path_value):
            errors.append(f"{label}: output_file_id or output_path is required")
        if result_key:
            if result_key in result_ids:
                errors.append(f"{label}: duplicate result identifier {result_key!r}")
            result_ids.add(result_key)

        output_name = str(raw.get("output_name", "") or "").strip()
        if output_name:
            key = output_name.casefold()
            if key in output_names:
                errors.append(f"{label}: duplicate output_name {output_name!r}")
            output_names.add(key)
            if isinstance(slot, int) and not output_name.startswith(f"{slot:02d}"):
                errors.append(f"{label}: output_name does not match slot prefix")

        record: dict[str, Any] = {
            "slot": slot,
            "tool_call_id": tool_call_id,
            "output_file_id": output_file_id,
            "output_path": output_path_value,
        }
        if output_path_value:
            path = Path(output_path_value).expanduser().resolve()
            if path in output_paths:
                errors.append(f"{label}: duplicate output path {path}")
            output_paths.add(path)
            if path.suffix.casefold() not in SUPPORTED:
                errors.append(f"{label}: unsupported extension {path.suffix}")
            elif not path.is_file():
                errors.append(f"{label}: output file not found: {path}")
            else:
                try:
                    with Image.open(path) as opened:
                        image = ImageOps.exif_transpose(opened).convert("RGB")
                        image.load()
                        width, height = image.size
                        record.update({"width": width, "height": height, "format": opened.format})
                        if args.width is not None and width != args.width:
                            errors.append(f"{label}: width {width}, expected {args.width}")
                        if args.height is not None and height != args.height:
                            errors.append(f"{label}: height {height}, expected {args.height}")
                        if expected_aspect is not None:
                            if abs(width / height - expected_aspect) > args.aspect_tolerance:
                                errors.append(
                                    f"{label}: aspect {width}:{height} does not match requested ratio"
                                )
                        variance = sum(ImageStat.Stat(image.resize((64, 64))).var) / 3
                        if variance < 8:
                            warnings.append(f"{label}: unusually low visual variance")
                        perceptual[path.name] = dhash(image)
                    digest = sha256(path)
                    record["sha256"] = digest
                    if digest in byte_hashes:
                        errors.append(f"{label}: exact duplicate of {byte_hashes[digest]}")
                    else:
                        byte_hashes[digest] = path.name
                except OSError as exc:
                    errors.append(f"{label}: cannot decode output file: {exc}")
        details.append(record)

    if slots != set(range(1, 11)):
        errors.append("slots must be exactly 1 through 10")
    if args.strict and len(result_ids) != 10:
        errors.append(f"strict mode requires 10 unique result identifiers, found {len(result_ids)}")
    if output_paths and len(output_paths) != 10:
        errors.append(f"when output paths are used, all 10 slots must provide unique paths")

    near_duplicates: list[dict[str, Any]] = []
    for left, right in combinations(sorted(perceptual), 2):
        distance = hamming(perceptual[left], perceptual[right])
        if distance <= args.near_duplicate_distance:
            message = f"possible near-duplicate: {left} and {right} (dHash distance {distance})"
            near_duplicates.append({"left": left, "right": right, "distance": distance})
            if args.fail_near_duplicates:
                errors.append(message)
            else:
                warnings.append(message)

    report = {
        "valid": not errors,
        "expected_outputs": 10,
        "actual_items": len(items),
        "unique_result_identifiers": len(result_ids),
        "unique_output_paths": len(output_paths),
        "files": details,
        "near_duplicates": near_duplicates,
        "warnings": warnings,
        "errors": errors,
        "manual_single_scene_review_required": True,
    }
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("PASS: ten valid reviewed slots with unique results passed validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
