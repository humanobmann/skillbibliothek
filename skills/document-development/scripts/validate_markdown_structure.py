#!/usr/bin/env python3
"""Validate basic markdown document structure.

Usage:
    python scripts/validate_markdown_structure.py path/to/document.md

Checks:
- heading hierarchy jumps
- duplicate headings
- empty sections
- TODO / FIXME / needs verification markers
- approximate word count
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TODO_RE = re.compile(r"\b(TODO|FIXME|needs verification|tbd)\b", re.IGNORECASE)
WORD_RE = re.compile(r"\b[\w'-]+\b")


def analyze_markdown(text: str) -> list[str]:
    lines = text.splitlines()
    findings: list[str] = []
    headings: list[tuple[int, str, int]] = []

    for idx, line in enumerate(lines, start=1):
        match = HEADING_RE.match(line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            headings.append((level, title, idx))

    if not headings:
        findings.append("critical: no markdown headings found")
    else:
        previous_level = headings[0][0]
        for level, title, line_no in headings[1:]:
            if level > previous_level + 1:
                findings.append(
                    f"major: heading hierarchy jumps from h{previous_level} to h{level} at line {line_no}: {title}"
                )
            previous_level = level

    normalized_titles = [title.lower() for _, title, _ in headings]
    for title, count in Counter(normalized_titles).items():
        if count > 1:
            findings.append(f"minor: duplicate heading: {title}")

    for i, (level, title, line_no) in enumerate(headings):
        start = line_no
        end = headings[i + 1][2] - 1 if i + 1 < len(headings) else len(lines)
        section_text = "\n".join(lines[start:end]).strip()
        if not section_text:
            findings.append(f"minor: empty section after heading at line {line_no}: {title}")

    todo_matches = [(i, line.strip()) for i, line in enumerate(lines, start=1) if TODO_RE.search(line)]
    if todo_matches:
        findings.append(f"info: {len(todo_matches)} TODO/verification markers found")
        for line_no, line in todo_matches[:10]:
            findings.append(f"info: marker at line {line_no}: {line[:120]}")
        if len(todo_matches) > 10:
            findings.append(f"info: {len(todo_matches) - 10} additional markers not shown")

    word_count = len(WORD_RE.findall(text))
    findings.append(f"info: approximate word count: {word_count}")

    return findings


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_markdown_structure.py path/to/document.md", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"error: file not found: {path}", file=sys.stderr)
        return 2
    if not path.is_file():
        print(f"error: not a file: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    for finding in analyze_markdown(text):
        print(finding)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
