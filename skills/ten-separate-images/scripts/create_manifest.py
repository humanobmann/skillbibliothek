#!/usr/bin/env python3
"""Create a complete ten-slot manifest for isolated image operations."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

MODES = {
    "ten-sources",
    "one-concept-ten-variants",
    "ten-briefs",
    "style-plus-ten-sources",
    "mixed",
}

REVIEW_TEMPLATE = {
    "single_scene": False,
    "correct_slot": False,
    "content_preserved": False,
    "requirements_met": False,
    "no_cross_slot_leakage": False,
    "no_unrequested_text": False,
    "no_unrequested_branding": False,
    "technical_quality": False,
    "passed": False,
}


def load_list(path: Path | None, label: str) -> list[str]:
    if path is None:
        return [""] * 10
    data: Any = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list) or len(data) != 10:
        raise ValueError(f"{label} must be a JSON array with exactly 10 strings")
    values: list[str] = []
    for index, value in enumerate(data, start=1):
        if not isinstance(value, str):
            raise ValueError(f"{label} item {index} must be a string")
        values.append(value.strip())
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=sorted(MODES), required=True)
    parser.add_argument("--aspect", default="4:5")
    parser.add_argument("--extension", default="png", choices=["png", "jpg", "jpeg", "webp"])
    parser.add_argument("--sources-json", type=Path)
    parser.add_argument("--briefs-json", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    try:
        sources = load_list(args.sources_json, "sources")
        briefs = load_list(args.briefs_json, "briefs")
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))

    items: list[dict[str, Any]] = []
    for slot in range(1, 11):
        source = sources[slot - 1]
        source_id = source if source.startswith("file_") else ""
        source_path = "" if source_id else source
        items.append(
            {
                "slot": slot,
                "source_id": source_id,
                "source_path": source_path,
                "brief": briefs[slot - 1],
                "instruction": (
                    f"Aktueller Bildschritt {slot:02d}: Erzeuge nur das zugeordnete "
                    "einzelne Bild und erhalte alle festgelegten Merkmale."
                ),
                "output_name": f"{slot:02d}.{args.extension}",
                "status": "pending",
                "attempts": 0,
                "tool_call_id": "",
                "output_file_id": "",
                "output_path": "",
                "review": dict(REVIEW_TEMPLATE),
            }
        )

    manifest = {
        "version": 2,
        "expected_outputs": 10,
        "mode": args.mode,
        "requested_aspect": args.aspect,
        "items": items,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Created complete ten-slot manifest: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
