#!/usr/bin/env python3
"""Fast dependency-free UI static lint for common frontend quality risks."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TEXT_EXTENSIONS = {".html", ".htm", ".css", ".scss", ".sass", ".less", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte"}

RULES = [
    {
        "id": "generic-purple-gradient",
        "severity": "low",
        "extensions": TEXT_EXTENSIONS,
        "pattern": re.compile(r"(?:linear|radial)-gradient\([^\n]*(?:#(?:7c3aed|8b5cf6|6366f1|4f46e5)|purple)[^\n]*(?:#(?:2563eb|3b82f6|0ea5e9)|blue)", re.I),
        "message": "Generic purple-to-blue gradient detected. Keep only when the brief intentionally calls for it.",
    },
    {
        "id": "inter-default",
        "severity": "low",
        "extensions": {".css", ".scss", ".sass", ".less", ".html", ".tsx", ".jsx", ".vue", ".svelte"},
        "pattern": re.compile(r"font-family\s*:\s*['\"]?Inter\b", re.I),
        "message": "Inter is used as a primary font. Verify that this is a deliberate product choice rather than a default.",
    },
    {
        "id": "transition-all",
        "severity": "medium",
        "extensions": {".css", ".scss", ".sass", ".less", ".html", ".tsx", ".jsx", ".vue", ".svelte"},
        "pattern": re.compile(r"transition(?:-property)?\s*:\s*all\b", re.I),
        "message": "Avoid transition: all. Transition only the properties that should animate.",
    },
    {
        "id": "focus-outline-removed",
        "severity": "high",
        "extensions": {".css", ".scss", ".sass", ".less", ".html", ".tsx", ".jsx", ".vue", ".svelte"},
        "pattern": re.compile(r"outline\s*:\s*(?:none|0)\s*;", re.I),
        "message": "Focus outline is removed. Confirm an equally visible keyboard focus treatment is provided.",
    },
    {
        "id": "clickable-div",
        "severity": "medium",
        "extensions": {".jsx", ".tsx"},
        "pattern": re.compile(r"<div\b[^>]*\bonClick\s*=", re.I),
        "message": "Clickable div detected. Prefer a semantic button or link unless full keyboard semantics are implemented.",
    },
    {
        "id": "clickable-span",
        "severity": "medium",
        "extensions": {".jsx", ".tsx"},
        "pattern": re.compile(r"<span\b[^>]*\bonClick\s*=", re.I),
        "message": "Clickable span detected. Prefer a semantic button or link unless full keyboard semantics are implemented.",
    },
    {
        "id": "img-without-alt-html",
        "severity": "high",
        "extensions": {".html", ".htm"},
        "pattern": re.compile(r"<img\b(?![^>]*\balt\s*=)[^>]*>", re.I | re.S),
        "message": "Image without an alt attribute detected. Add meaningful alt text or alt=\"\" for decorative images.",
    },
    {
        "id": "img-without-alt-jsx",
        "severity": "high",
        "extensions": {".jsx", ".tsx"},
        "pattern": re.compile(r"<img\b(?![^>]*\balt\s*=)[^>]*?/?>", re.I | re.S),
        "message": "Image without an alt prop detected. Add meaningful alt text or alt=\"\" for decorative images.",
    },
    {
        "id": "fixed-100vh",
        "severity": "low",
        "extensions": {".css", ".scss", ".sass", ".less", ".html", ".tsx", ".jsx", ".vue", ".svelte"},
        "pattern": re.compile(r"(?:height|min-height)\s*:\s*100vh\b", re.I),
        "message": "100vh detected. Verify mobile browser chrome does not cause clipping; consider modern viewport units when appropriate.",
    },
    {
        "id": "excessive-blur",
        "severity": "low",
        "extensions": {".css", ".scss", ".sass", ".less", ".html", ".tsx", ".jsx", ".vue", ".svelte"},
        "pattern": re.compile(r"backdrop-filter\s*:\s*blur\((?:2[4-9]|[3-9]\d|\d{3,})px\)", re.I),
        "message": "Large backdrop blur detected. Verify readability, performance, and whether the effect is product-specific.",
    },
]


def iter_files(target: Path):
    if target.is_file():
        if target.suffix.lower() in TEXT_EXTENSIONS:
            yield target
        return
    for path in target.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if any(part in {"node_modules", ".git", "dist", "build", ".next", "coverage"} for part in path.parts):
            continue
        yield path


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def scan(target: Path):
    findings = []
    for path in iter_files(target):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        ext = path.suffix.lower()
        for rule in RULES:
            if ext not in rule["extensions"]:
                continue
            for match in rule["pattern"].finditer(text):
                findings.append(
                    {
                        "rule": rule["id"],
                        "severity": rule["severity"],
                        "file": str(path),
                        "line": line_number(text, match.start()),
                        "message": rule["message"],
                    }
                )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Static UI lint for common frontend quality risks.")
    parser.add_argument("target", help="File or directory to scan")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    if not target.exists():
        parser.error(f"target does not exist: {target}")

    findings = scan(target)
    if args.json:
        print(json.dumps({"target": str(target), "findings": findings}, indent=2))
    else:
        if not findings:
            print("No configured UI lint findings.")
        else:
            for item in findings:
                print(f"{item['severity'].upper():6} {item['file']}:{item['line']} [{item['rule']}] {item['message']}")
            print(f"\n{len(findings)} finding(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
