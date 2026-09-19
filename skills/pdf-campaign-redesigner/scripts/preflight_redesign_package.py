#!/usr/bin/env python3
"""Lightweight preflight for a PDF redesign deliverable folder."""
from __future__ import annotations

import argparse
import pathlib
import sys

FORBIDDEN_EXTENSIONS = {".otf", ".ttf", ".woff", ".woff2"}
FORBIDDEN_NAME_PARTS = {"logo", "watermark", "final_final"}


def scan(root: pathlib.Path) -> list[str]:
    issues: list[str] = []
    pdfs = list(root.glob("*.pdf"))
    if not pdfs:
        issues.append("no pdf found in deliverable root")
    for path in root.rglob("*"):
        if path.is_file():
            low = path.name.lower()
            if path.suffix.lower() in FORBIDDEN_EXTENSIONS:
                issues.append(f"font file must not be bundled: {path.relative_to(root)}")
            for part in FORBIDDEN_NAME_PARTS:
                if part in low:
                    issues.append(f"review filename for forbidden/default branding or bad versioning: {path.relative_to(root)}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("deliverable_dir")
    args = parser.parse_args()
    root = pathlib.Path(args.deliverable_dir)
    if not root.exists() or not root.is_dir():
        print(f"deliverable directory not found: {root}", file=sys.stderr)
        return 2
    issues = scan(root)
    if issues:
        for issue in issues:
            print(f"ISSUE: {issue}")
        return 1
    print("preflight ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
