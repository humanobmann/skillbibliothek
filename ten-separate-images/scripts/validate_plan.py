#!/usr/bin/env python3
"""Validate the plan phase of a ten-slot isolated image batch."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

VALID_MODES = {
    "ten-sources",
    "one-concept-ten-variants",
    "ten-briefs",
    "style-plus-ten-sources",
    "mixed",
}
VALID_STATUSES = {"pending", "active", "retry", "valid"}
VALID_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
FORBIDDEN_IN_SLOT_INSTRUCTION = {
    "10 images",
    "ten images",
    "10 bilder",
    "zehn bilder",
    "alle bilder",
    "all images",
    "alle motive",
    "all motifs",
    "contact sheet",
    "kontaktbogen",
    "collage",
    "grid",
    "raster",
    "montage",
    "multi-panel",
    "multipanel",
    "storyboard",
    "gesamtübersicht",
    "overview of all",
}


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def source_key(item: dict[str, Any]) -> str:
    for field in ("source_id", "source_path"):
        value = item.get(field)
        if nonempty_string(value):
            return str(value).strip()
    return ""


def validate_manifest(data: Any, check_source_paths: bool = False) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["Manifest root must be a JSON object"]
    if data.get("expected_outputs") != 10:
        errors.append("expected_outputs must be exactly 10")
    mode = data.get("mode")
    if mode not in VALID_MODES:
        errors.append(f"mode must be one of {sorted(VALID_MODES)}")
    aspect = data.get("requested_aspect")
    if not isinstance(aspect, str) or not re.fullmatch(r"\d+(?:\.\d+)?:\d+(?:\.\d+)?", aspect.strip()):
        errors.append("requested_aspect must use W:H, for example 4:5")

    items = data.get("items")
    if not isinstance(items, list):
        return errors + ["items must be a JSON array"]
    if len(items) != 10:
        errors.append(f"items must contain exactly 10 entries, found {len(items)}")

    slots: set[int] = set()
    output_names: set[str] = set()
    source_keys: list[str] = []
    active_count = 0

    for position, raw in enumerate(items, start=1):
        label = f"item {position}"
        if not isinstance(raw, dict):
            errors.append(f"{label} must be a JSON object")
            continue
        slot = raw.get("slot")
        if not isinstance(slot, int) or not 1 <= slot <= 10:
            errors.append(f"{label}: slot must be an integer from 1 to 10")
        elif slot in slots:
            errors.append(f"{label}: duplicate slot {slot}")
        else:
            slots.add(slot)

        for field in ("source_id", "source_path", "brief", "instruction"):
            value = raw.get(field, "")
            if isinstance(value, list) or isinstance(value, dict):
                errors.append(f"{label}: {field} must be one string, not a collection")
            elif value is not None and not isinstance(value, str):
                errors.append(f"{label}: {field} must be a string")

        current_source = source_key(raw)
        brief = str(raw.get("brief", "") or "").strip()
        if not current_source and not brief:
            errors.append(f"{label}: source_id, source_path or brief is required")
        if current_source:
            source_keys.append(current_source)
        if check_source_paths and nonempty_string(raw.get("source_path")):
            path = Path(str(raw["source_path"])).expanduser()
            if not path.is_file():
                errors.append(f"{label}: source_path not found: {path}")

        instruction = str(raw.get("instruction", "") or "").strip()
        if not instruction:
            errors.append(f"{label}: instruction is required")
        folded = instruction.casefold()
        for term in FORBIDDEN_IN_SLOT_INSTRUCTION:
            if term.casefold() in folded:
                errors.append(f"{label}: instruction contains batch term {term!r}")

        output_name = str(raw.get("output_name", "") or "").strip()
        if not output_name:
            errors.append(f"{label}: output_name is required")
        else:
            path = Path(output_name)
            if path.name != output_name:
                errors.append(f"{label}: output_name must be a filename without directories")
            if path.suffix.casefold() not in VALID_EXTENSIONS:
                errors.append(f"{label}: unsupported output extension {path.suffix!r}")
            if isinstance(slot, int) and not output_name.startswith(f"{slot:02d}"):
                errors.append(f"{label}: output_name must begin with slot prefix {slot:02d}")
            key = output_name.casefold()
            if key in output_names:
                errors.append(f"{label}: duplicate output_name {output_name!r}")
            output_names.add(key)

        status = raw.get("status", "pending")
        if status not in VALID_STATUSES:
            errors.append(f"{label}: invalid status {status!r}")
        if status == "active":
            active_count += 1

        attempts = raw.get("attempts", 0)
        if not isinstance(attempts, int) or attempts < 0:
            errors.append(f"{label}: attempts must be a non-negative integer")

    if slots != set(range(1, 11)):
        errors.append("slots must be exactly the integers 1 through 10")
    if active_count > 1:
        errors.append(f"at most one slot may be active, found {active_count}")
    if mode in {"ten-sources", "style-plus-ten-sources"}:
        if len(source_keys) != 10:
            errors.append(f"mode {mode!r} requires one source for every slot")
        elif len(set(source_keys)) != 10:
            errors.append(f"mode {mode!r} requires ten distinct content sources")
    if mode == "ten-briefs":
        missing = [
            str(raw.get("slot", "?"))
            for raw in items
            if isinstance(raw, dict) and not nonempty_string(raw.get("brief"))
        ]
        if missing:
            errors.append(f"ten-briefs mode requires a brief in every slot: {', '.join(missing)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--check-source-paths", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    try:
        data: Any = json.loads(args.manifest.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: manifest not found: {args.manifest}", file=sys.stderr)
        return 2
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read manifest: {exc}", file=sys.stderr)
        return 1

    errors = validate_manifest(data, check_source_paths=args.check_source_paths)
    report = {"valid": not errors, "errors": errors}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("PASS: complete ten-slot plan with isolated instructions and unique outputs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
