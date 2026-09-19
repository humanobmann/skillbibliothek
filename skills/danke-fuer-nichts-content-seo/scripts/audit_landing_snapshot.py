#!/usr/bin/env python3
"""Audit a saved HTML landing-page snapshot for structural release risks."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


class SnapshotParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.lang = ""
        self.title = ""
        self._in_title = False
        self._current_heading: tuple[int, list[str]] | None = None
        self.headings: list[tuple[int, str]] = []
        self.meta: dict[str, str] = {}
        self.canonicals: list[str] = []
        self.links: list[dict[str, str]] = []
        self._current_link: int | None = None
        self.images: list[dict[str, str]] = []
        self.forms = 0
        self.jsonld: list[str] = []
        self._in_script = False
        self._in_jsonld = False
        self._jsonld_parts: list[str] = []
        self.text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key.lower(): value or "" for key, value in attrs}
        tag = tag.lower()
        if tag == "html":
            self.lang = data.get("lang", "")
        elif tag == "title":
            self._in_title = True
        elif re.fullmatch(r"h[1-6]", tag):
            self._current_heading = (int(tag[1]), [])
        elif tag == "meta":
            key = (data.get("name") or data.get("property") or data.get("http-equiv") or "").lower()
            if key:
                self.meta[key] = data.get("content", "")
        elif tag == "link" and "canonical" in data.get("rel", "").lower():
            self.canonicals.append(data.get("href", ""))
        elif tag == "a":
            self.links.append({"href": data.get("href", ""), "text": ""})
            self._current_link = len(self.links) - 1
        elif tag == "img":
            self.images.append({"src": data.get("src", ""), "alt": data.get("alt", "")})
        elif tag == "form":
            self.forms += 1
        elif tag == "script":
            self._in_script = True
            if data.get("type", "").lower() == "application/ld+json":
                self._in_jsonld = True
                self._jsonld_parts = []

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self._in_title = False
        elif re.fullmatch(r"h[1-6]", tag) and self._current_heading:
            level, parts = self._current_heading
            self.headings.append((level, " ".join(parts).strip()))
            self._current_heading = None
        elif tag == "script":
            if self._in_jsonld:
                self.jsonld.append("".join(self._jsonld_parts).strip())
            self._in_jsonld = False
            self._in_script = False
        elif tag == "a":
            self._current_link = None

    def handle_data(self, data: str) -> None:
        if self._in_script:
            if self._in_jsonld:
                self._jsonld_parts.append(data)
            return
        text = re.sub(r"\s+", " ", data).strip()
        if not text:
            return
        self.text_parts.append(text)
        if self._in_title:
            self.title += (" " if self.title else "") + text
        if self._current_heading:
            self._current_heading[1].append(text)
        if self._current_link is not None:
            current = self.links[self._current_link]
            current["text"] += (" " if current["text"] else "") + text


def jsonld_types(blocks: list[str]) -> tuple[list[str], int]:
    types: list[str] = []
    invalid = 0

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            kind = value.get("@type")
            if isinstance(kind, str):
                types.append(kind)
            elif isinstance(kind, list):
                types.extend(str(item) for item in kind)
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    for block in blocks:
        try:
            walk(json.loads(block))
        except (json.JSONDecodeError, TypeError):
            invalid += 1
    return types, invalid


def audit(html: str, expected_isbns: list[str]) -> dict[str, Any]:
    parser = SnapshotParser()
    parser.feed(html)
    visible = " ".join(parser.text_parts)
    risks: list[str] = []
    warnings: list[str] = []

    h1 = [text for level, text in parser.headings if level == 1]
    levels = [level for level, _ in parser.headings]
    heading_jumps = sum(1 for previous, current in zip(levels, levels[1:]) if current > previous + 1)
    missing_alt = [image["src"] for image in parser.images if not image["alt"].strip()]
    empty_links = [link for link in parser.links if not link["href"].strip()]
    insecure_links = [link["href"] for link in parser.links if link["href"].startswith("http://")]
    legal_hrefs = [
        link["href"] for link in parser.links
        if any(term in link["text"].lower() for term in ("impressum", "datenschutz"))
    ]
    duplicate_legal = {href: count for href, count in Counter(legal_hrefs).items() if href and count > 1}
    types, invalid_jsonld = jsonld_types(parser.jsonld)

    if len(h1) != 1:
        risks.append(f"Erwartet ist genau eine H1, gefunden wurden {len(h1)}.")
    if not parser.title:
        risks.append("Seitentitel fehlt.")
    if not parser.meta.get("description"):
        risks.append("Meta-Description fehlt.")
    if len(parser.canonicals) != 1 or not parser.canonicals[0]:
        risks.append("Canonical fehlt oder ist nicht eindeutig.")
    if invalid_jsonld:
        risks.append(f"{invalid_jsonld} JSON-LD-Blöcke sind ungültig.")
    if "Book" not in types:
        warnings.append("Kein Book-Typ in JSON-LD gefunden.")
    if not parser.lang.lower().startswith("de"):
        warnings.append("HTML-Sprache ist nicht als Deutsch ausgewiesen.")
    if heading_jumps:
        warnings.append(f"{heading_jumps} Sprünge in der Überschriftenhierarchie.")
    if missing_alt:
        warnings.append(f"{len(missing_alt)} Bilder ohne Alt-Text.")
    if empty_links:
        warnings.append(f"{len(empty_links)} Links ohne Ziel.")
    if insecure_links:
        warnings.append(f"{len(insecure_links)} unsichere HTTP-Links.")
    if duplicate_legal:
        warnings.append("Doppelte Impressum- oder Datenschutzlinks gefunden.")
    if visible.count("©") > 1:
        warnings.append("Mehrere Copyright-Zeichen deuten auf doppelten Footer hin.")
    for isbn in expected_isbns:
        digits = re.sub(r"\D", "", isbn)
        pattern = r"(?<!\d)" + r"[-\s]*".join(re.escape(char) for char in digits) + r"(?!\d)"
        if digits and not re.search(pattern, visible):
            risks.append(f"Erwartete ISBN {isbn} ist im sichtbaren Text nicht gefunden worden.")

    return {
        "status": "STOP" if risks else ("CHECK" if warnings else "READY"),
        "lang": parser.lang,
        "title": parser.title,
        "meta_description": parser.meta.get("description", ""),
        "canonical": parser.canonicals,
        "h1": h1,
        "heading_counts": dict(Counter(f"h{level}" for level, _ in parser.headings)),
        "heading_jumps": heading_jumps,
        "links": len(parser.links),
        "images": len(parser.images),
        "images_missing_alt": len(missing_alt),
        "forms": parser.forms,
        "jsonld_blocks": len(parser.jsonld),
        "jsonld_types": sorted(set(types)),
        "duplicate_legal_links": duplicate_legal,
        "risks": risks,
        "warnings": warnings,
    }


def markdown(result: dict[str, Any]) -> str:
    lines = [
        f"# Landingpage-Audit: {result.get('status', 'STOP')}",
        "",
        f"* Titel: {result.get('title', '')}",
        f"* H1: {result.get('h1', [])}",
        f"* Canonical: {result.get('canonical', [])}",
        f"* Bilder ohne Alt-Text: {result.get('images_missing_alt', 0)}",
        f"* JSON-LD-Typen: {result.get('jsonld_types', [])}",
        f"* Formulare: {result.get('forms', 0)}",
        "",
    ]
    for title, key in (("Stopprisiken", "risks"), ("Prüfhinweise", "warnings")):
        values = result.get(key, [])
        if values:
            lines.extend([f"## {title}", "", *[f"* {value}" for value in values], ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path)
    parser.add_argument("--expected-isbn", action="append", default=[])
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    parser.add_argument("--fail-on-stop", action="store_true")
    args = parser.parse_args()
    result = audit(args.html.read_text(encoding="utf-8"), args.expected_isbn)
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.format == "json" else markdown(result))
    return 2 if args.fail_on_stop and result.get("status") == "STOP" else 0


if __name__ == "__main__":
    sys.exit(main())
