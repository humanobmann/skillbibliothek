#!/usr/bin/env python3
"""Render a local HTML file to PDF using Playwright or WeasyPrint.

Usage:
  python render_html_to_pdf.py input.html output.pdf

This script intentionally does not download fonts or assets. Keep font licensing
and embedding decisions in the project files.
"""
from __future__ import annotations

import argparse
import pathlib
import sys


def render_with_playwright(src: pathlib.Path, dst: pathlib.Path) -> bool:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except Exception:
        return False
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1200, "height": 1600})
            page.goto(src.resolve().as_uri(), wait_until="networkidle")
            page.pdf(
                path=str(dst),
                format="A4",
                print_background=True,
                prefer_css_page_size=True,
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            )
            browser.close()
        return True
    except Exception:
        return False


def render_with_weasyprint(src: pathlib.Path, dst: pathlib.Path) -> bool:
    try:
        from weasyprint import HTML  # type: ignore
    except Exception:
        return False
    HTML(filename=str(src)).write_pdf(str(dst))
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_html")
    parser.add_argument("output_pdf")
    args = parser.parse_args()

    src = pathlib.Path(args.input_html)
    dst = pathlib.Path(args.output_pdf)
    if not src.exists():
        print(f"input html not found: {src}", file=sys.stderr)
        return 2
    dst.parent.mkdir(parents=True, exist_ok=True)

    if render_with_playwright(src, dst):
        print(f"wrote {dst} with playwright")
        return 0
    if render_with_weasyprint(src, dst):
        print(f"wrote {dst} with weasyprint")
        return 0

    print(
        "no supported html-to-pdf renderer found. install/use playwright or weasyprint, "
        "or export via the host pdf/slides/docx workflow.",
        file=sys.stderr,
    )
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
