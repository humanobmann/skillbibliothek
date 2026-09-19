#!/usr/bin/env python3
"""Inspect book PDF geometry, raster images, text availability, and metadata."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any


PT_TO_MM = 25.4 / 72.0


def run(command: list[str]) -> str:
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    if result.returncode:
        return ""
    return result.stdout


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_pdfinfo(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in text.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def parse_page_size(value: str) -> tuple[float, float] | None:
    match = re.search(r"([0-9.]+)\s+x\s+([0-9.]+)\s+pts", value)
    if not match:
        return None
    return float(match.group(1)), float(match.group(2))


def parse_images(text: str) -> dict[str, Any]:
    rows = []
    for line in text.splitlines():
        if not re.match(r"\s*\d+\s+\d+\s+", line):
            continue
        parts = line.split()
        if len(parts) < 14:
            continue
        try:
            rows.append(
                {
                    "page": int(parts[0]),
                    "width": int(parts[3]),
                    "height": int(parts[4]),
                    "color": parts[5],
                    "bpc": int(parts[7]),
                    "x_ppi": int(parts[12]),
                    "y_ppi": int(parts[13]),
                }
            )
        except (ValueError, IndexError):
            continue
    return {
        "count": len(rows),
        "colors": dict(Counter(row["color"] for row in rows)),
        "ppi": dict(Counter(f"{row['x_ppi']}x{row['y_ppi']}" for row in rows)),
        "pages_with_images": len({row["page"] for row in rows}),
        "rows": rows,
    }


def inspect(path: Path, expected_pages: int | None, trim: tuple[float, float] | None) -> dict[str, Any]:
    required = [name for name in ("pdfinfo", "pdftotext", "pdffonts", "pdfimages") if not shutil.which(name)]
    if required:
        return {"status": "STOP", "errors": ["Fehlende Programme: " + ", ".join(required)]}

    info = parse_pdfinfo(run(["pdfinfo", str(path)]))
    pages = int(info.get("Pages", "0") or 0)
    size = parse_page_size(info.get("Page size", ""))
    size_mm = [round(size[0] * PT_TO_MM, 3), round(size[1] * PT_TO_MM, 3)] if size else None
    text_sample = run(["pdftotext", "-f", "1", "-l", str(min(pages, 25)), str(path), "-"])
    font_lines = [
        line for line in run(["pdffonts", str(path)]).splitlines()
        if line.strip() and not line.startswith("name") and not set(line.strip()) <= {"-", " "}
    ]
    images = parse_images(run(["pdfimages", "-list", str(path)]))
    risks: list[str] = []
    warnings: list[str] = []

    if expected_pages is not None and pages != expected_pages:
        risks.append(f"PDF hat {pages} statt erwarteter {expected_pages} Seiten.")
    bleed = None
    if trim and size_mm:
        bleed_x = round((size_mm[0] - trim[0]) / 2, 3)
        bleed_y = round((size_mm[1] - trim[1]) / 2, 3)
        bleed = [bleed_x, bleed_y]
        if bleed_x < 0 or bleed_y < 0:
            risks.append("PDF-Seite ist kleiner als das erwartete Trimformat.")
        elif abs(bleed_x - bleed_y) > 0.25:
            warnings.append("Horizontaler und vertikaler Beschnitt unterscheiden sich.")
    if not text_sample.strip():
        warnings.append("Kein extrahierbarer Text in den ersten Seiten. Das PDF ist wahrscheinlich gerastert.")
    if not font_lines:
        warnings.append("Keine PDF-Schriften gefunden. Bei Raster-PDF erwartbar, aber nicht barrierearm.")
    if images["count"] and images["pages_with_images"] != pages:
        warnings.append("Nicht jede Seite enthält ein erkanntes Rasterbild.")
    if info.get("Tagged", "").lower() == "no":
        warnings.append("PDF ist nicht getaggt.")

    return {
        "status": "STOP" if risks else ("CHECK" if warnings else "READY"),
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "pages": pages,
        "page_size_mm": size_mm,
        "expected_trim_mm": list(trim) if trim else None,
        "inferred_bleed_per_side_mm": bleed,
        "pdf_version": info.get("PDF version"),
        "encrypted": info.get("Encrypted"),
        "tagged": info.get("Tagged"),
        "producer": info.get("Producer"),
        "extractable_text_chars_first_25_pages": len(text_sample.strip()),
        "font_rows": len(font_lines),
        "images": {key: value for key, value in images.items() if key != "rows"},
        "risks": risks,
        "warnings": warnings,
    }


def markdown(result: dict[str, Any]) -> str:
    lines = [
        f"# PDF-Audit: {result.get('status', 'STOP')}",
        "",
        f"* Seiten: {result.get('pages', 0)}",
        f"* Seitengröße in mm: {result.get('page_size_mm')}",
        f"* abgeleiteter Beschnitt je Seite in mm: {result.get('inferred_bleed_per_side_mm')}",
        f"* PDF-Version: {result.get('pdf_version')}",
        f"* Textzeichen auf Seiten 1 bis 25: {result.get('extractable_text_chars_first_25_pages', 0)}",
        f"* erkannte Schriftzeilen: {result.get('font_rows', 0)}",
        f"* Rasterbilder: {result.get('images', {}).get('count', 0)}",
        f"* Farben: {result.get('images', {}).get('colors', {})}",
        f"* Auflösungen: {result.get('images', {}).get('ppi', {})}",
        "",
    ]
    for title, key in (("Stopprisiken", "risks"), ("Prüfhinweise", "warnings"), ("Fehler", "errors")):
        values = result.get(key, [])
        if values:
            lines.extend([f"## {title}", "", *[f"* {value}" for value in values], ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--expected-pages", type=int)
    parser.add_argument("--trim-mm", nargs=2, type=float, metavar=("WIDTH", "HEIGHT"))
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    parser.add_argument("--fail-on-stop", action="store_true")
    args = parser.parse_args()
    result = inspect(args.pdf, args.expected_pages, tuple(args.trim_mm) if args.trim_mm else None)
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.format == "json" else markdown(result))
    return 2 if args.fail_on_stop and result.get("status") == "STOP" else 0


if __name__ == "__main__":
    sys.exit(main())
