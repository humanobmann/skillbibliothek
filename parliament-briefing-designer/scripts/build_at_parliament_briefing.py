#!/usr/bin/env python3
"""Build an Austrian parliamentary briefing PDF from structured JSON.

Usage:
    python build_at_parliament_briefing.py input.json output.pdf

The JSON schema is intentionally simple and matches references/sample-input.example.json.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

PAGE_W, PAGE_H = A4

PALETTE = {
    "red": colors.HexColor("#C8102E"),
    "deep_red": colors.HexColor("#7A0019"),
    "graphite": colors.HexColor("#202124"),
    "slate": colors.HexColor("#5B6068"),
    "warm_white": colors.HexColor("#FAF8F4"),
    "stone": colors.HexColor("#EFE8DE"),
    "soft_grey": colors.HexColor("#F3F4F6"),
    "line": colors.HexColor("#D7D2C8"),
    "brass": colors.HexColor("#B08A2E"),
    "white": colors.white,
}


def _first_existing(paths: Sequence[str]) -> str | None:
    for item in paths:
        if item and os.path.exists(item):
            return item
    return None


def register_fonts() -> Dict[str, str]:
    """Register local fonts when available. Do not bundle fonts in the skill."""
    regular = _first_existing([
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
    ])
    bold = _first_existing([
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
    ])
    if regular:
        pdfmetrics.registerFont(TTFont("DocSans", regular))
        if bold:
            pdfmetrics.registerFont(TTFont("DocSansBold", bold))
        else:
            pdfmetrics.registerFont(TTFont("DocSansBold", regular))
        return {"regular": "DocSans", "bold": "DocSansBold"}
    return {"regular": "Helvetica", "bold": "Helvetica-Bold"}


def clean_text(value: Any) -> str:
    text = "" if value is None else str(value)
    replacements = {
        "\u2013": "-",
        "\u2014": "-",
        "\u00a0": " ",
        "\ufeff": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text.strip()


def html_text(value: Any) -> str:
    return escape(clean_text(value)).replace("\n", "<br/>")


def make_styles(fonts: Dict[str, str]) -> Dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    regular = fonts["regular"]
    bold = fonts["bold"]

    def style(name: str, parent: str = "Normal", **kwargs: Any) -> ParagraphStyle:
        return ParagraphStyle(name, parent=base[parent], **kwargs)

    return {
        "label": style(
            "label",
            fontName=bold,
            fontSize=8.5,
            leading=10,
            textColor=PALETTE["deep_red"],
            spaceAfter=3,
            alignment=TA_LEFT,
        ),
        "title": style(
            "title",
            fontName=bold,
            fontSize=27,
            leading=31,
            textColor=PALETTE["graphite"],
            spaceAfter=7,
        ),
        "subtitle": style(
            "subtitle",
            fontName=regular,
            fontSize=12.5,
            leading=16,
            textColor=PALETTE["slate"],
            spaceAfter=12,
        ),
        "h2": style(
            "h2",
            fontName=bold,
            fontSize=13.5,
            leading=16,
            textColor=PALETTE["graphite"],
            spaceBefore=8,
            spaceAfter=6,
        ),
        "body": style(
            "body",
            fontName=regular,
            fontSize=9.7,
            leading=13.2,
            textColor=PALETTE["graphite"],
            spaceAfter=6,
        ),
        "small": style(
            "small",
            fontName=regular,
            fontSize=8.1,
            leading=10.4,
            textColor=PALETTE["slate"],
            spaceAfter=4,
        ),
        "small_bold": style(
            "small_bold",
            fontName=bold,
            fontSize=8.2,
            leading=10.4,
            textColor=PALETTE["graphite"],
            spaceAfter=4,
        ),
        "card_label": style(
            "card_label",
            fontName=bold,
            fontSize=7.7,
            leading=9.2,
            textColor=PALETTE["deep_red"],
            spaceAfter=2,
        ),
        "card_value": style(
            "card_value",
            fontName=bold,
            fontSize=13.5,
            leading=15.5,
            textColor=PALETTE["graphite"],
            spaceAfter=3,
        ),
        "card_note": style(
            "card_note",
            fontName=regular,
            fontSize=7.8,
            leading=9.5,
            textColor=PALETTE["slate"],
        ),
        "quote": style(
            "quote",
            fontName=bold,
            fontSize=10.4,
            leading=14,
            textColor=PALETTE["graphite"],
        ),
        "footer": style(
            "footer",
            fontName=regular,
            fontSize=7.2,
            leading=8,
            textColor=PALETTE["slate"],
            alignment=TA_CENTER,
        ),
    }


def para(text: Any, styles: Dict[str, ParagraphStyle], name: str = "body") -> Paragraph:
    return Paragraph(html_text(text), styles[name])


def section(title: str, styles: Dict[str, ParagraphStyle], number: str | None = None) -> Table:
    label = f"{number}. {title}" if number else title
    tbl = Table(
        [[Paragraph(html_text(label), styles["h2"])]],
        colWidths=[170 * mm],
        hAlign="LEFT",
    )
    tbl.setStyle(TableStyle([
        ("LINEBEFORE", (0, 0), (0, -1), 3, PALETTE["red"]),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    return tbl


def metadata_panel(metadata: Dict[str, Any], styles: Dict[str, ParagraphStyle], width: float) -> Table:
    rows: List[List[Any]] = []
    for key, value in metadata.items():
        rows.append([
            Paragraph(html_text(key.upper()), styles["card_label"]),
            Paragraph(html_text(value), styles["small_bold"]),
        ])
    if not rows:
        rows = [[Paragraph("STATUS", styles["card_label"]), Paragraph("Arbeitsfassung", styles["small_bold"])] ]
    tbl = Table(rows, colWidths=[width * 0.26, width * 0.74], hAlign="LEFT")
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALETTE["stone"]),
        ("BOX", (0, 0), (-1, -1), 0.4, PALETTE["line"]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, PALETTE["line"]),
    ]))
    return tbl


def info_box(title: str, body: Any, styles: Dict[str, ParagraphStyle], width: float, mode: str = "stone") -> Table:
    bg = PALETTE["stone"] if mode == "stone" else PALETTE["soft_grey"]
    tbl = Table(
        [[Paragraph(html_text(title.upper()), styles["card_label"])], [Paragraph(html_text(body), styles["body"])]],
        colWidths=[width],
        hAlign="LEFT",
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (-1, -1), 3, PALETTE["red"]),
        ("BOX", (0, 0), (-1, -1), 0.35, PALETTE["line"]),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return tbl


def fact_cards(facts: Sequence[Dict[str, Any]], styles: Dict[str, ParagraphStyle], width: float) -> Table:
    card_w = (width - 8 * mm) / 2
    cards: List[Any] = []
    for fact in facts:
        card = Table([
            [Paragraph(html_text(fact.get("label", "Fakt")), styles["card_label"])],
            [Paragraph(html_text(fact.get("value", "")), styles["card_value"])],
            [Paragraph(html_text(fact.get("note", "")), styles["card_note"])],
        ], colWidths=[card_w])
        card.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), PALETTE["soft_grey"]),
            ("BOX", (0, 0), (-1, -1), 0.35, PALETTE["line"]),
            ("LINEABOVE", (0, 0), (-1, 0), 2, PALETTE["red"]),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]))
        cards.append(card)

    rows: List[List[Any]] = []
    for i in range(0, len(cards), 2):
        row = cards[i:i+2]
        if len(row) == 1:
            row.append(Paragraph("", styles["body"]))
        rows.append(row)
    if not rows:
        rows = [[Paragraph("Keine Fakten uebergeben.", styles["body"]), Paragraph("", styles["body"])]]

    grid = Table(rows, colWidths=[card_w, card_w], hAlign="LEFT")
    grid.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("COLBACKGROUNDS", (0, 0), (-1, -1), [colors.transparent, colors.transparent]),
    ]))
    return grid


def bewertung_table(data: Dict[str, Any], styles: Dict[str, ParagraphStyle], width: float) -> Table:
    labels = ["Fakt", "Politische Bewertung", "Parlamentarische Schlussfolgerung"]
    rows = []
    for label in labels:
        rows.append([
            Paragraph(html_text(label), styles["card_label"]),
            Paragraph(html_text(data.get(label, "zu pruefen")), styles["body"]),
        ])
    tbl = Table(rows, colWidths=[width * 0.28, width * 0.72], hAlign="LEFT")
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALETTE["white"]),
        ("BOX", (0, 0), (-1, -1), 0.4, PALETTE["line"]),
        ("LINEBEFORE", (0, 0), (0, -1), 3, PALETTE["red"]),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, PALETTE["line"]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return tbl


def objections_table(items: Sequence[Dict[str, Any]], styles: Dict[str, ParagraphStyle], width: float) -> Table:
    rows: List[List[Any]] = [[
        Paragraph("EINWAND", styles["card_label"]),
        Paragraph("ANTWORTLINIE", styles["card_label"]),
    ]]
    for item in items:
        rows.append([
            Paragraph(html_text(item.get("einwand", "")), styles["body"]),
            Paragraph(html_text(item.get("antwort", "")), styles["body"]),
        ])
    tbl = Table(rows, colWidths=[width * 0.42, width * 0.58], repeatRows=1, hAlign="LEFT")
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), PALETTE["stone"]),
        ("BOX", (0, 0), (-1, -1), 0.4, PALETTE["line"]),
        ("GRID", (0, 0), (-1, -1), 0.25, PALETTE["line"]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return tbl


def numbered_sequence(items: Sequence[Any], styles: Dict[str, ParagraphStyle], width: float) -> Table:
    rows: List[List[Any]] = []
    for idx, item in enumerate(items, start=1):
        token = Table([[Paragraph(str(idx), ParagraphStyle(
            "token",
            fontName=styles["card_label"].fontName,
            fontSize=8,
            leading=9,
            alignment=TA_CENTER,
            textColor=PALETTE["white"],
        ))]], colWidths=[8 * mm], rowHeights=[8 * mm])
        token.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), PALETTE["deep_red"]),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ]))
        rows.append([token, Paragraph(html_text(item), styles["body"])])
    if not rows:
        rows = [[Paragraph("", styles["body"]), Paragraph("Keine Schritte uebergeben.", styles["body"])]]
    tbl = Table(rows, colWidths=[11 * mm, width - 11 * mm], hAlign="LEFT")
    tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return tbl


def questions_list(items: Sequence[Any], styles: Dict[str, ParagraphStyle], width: float) -> Table:
    rows: List[List[Any]] = []
    for idx, item in enumerate(items, start=1):
        rows.append([
            Paragraph(f"{idx:02d}", styles["card_label"]),
            Paragraph(html_text(item), styles["small"]),
        ])
    if not rows:
        rows = [[Paragraph("", styles["card_label"]), Paragraph("Keine Fragen uebergeben.", styles["small"])]]
    tbl = Table(rows, colWidths=[10 * mm, width - 10 * mm], hAlign="LEFT")
    tbl.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.35, PALETTE["line"]),
        ("LINEBEFORE", (0, 0), (0, -1), 3, PALETTE["red"]),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, PALETTE["line"]),
        ("BACKGROUND", (0, 0), (-1, -1), PALETTE["white"]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return tbl


def draw_page(canvas, doc, label: str, title: str) -> None:
    canvas.saveState()
    canvas.setFillColor(PALETTE["warm_white"])
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    # Red-white-red state rule.
    y = PAGE_H - 8 * mm
    canvas.setFillColor(PALETTE["red"])
    canvas.rect(0, y, PAGE_W, 2.2 * mm, stroke=0, fill=1)
    canvas.setFillColor(PALETTE["white"])
    canvas.rect(0, y - 1.2 * mm, PAGE_W, 1.2 * mm, stroke=0, fill=1)
    canvas.setFillColor(PALETTE["red"])
    canvas.rect(0, y - 3.4 * mm, PAGE_W, 2.2 * mm, stroke=0, fill=1)

    # Footer.
    footer_y = 10 * mm
    canvas.setStrokeColor(PALETTE["line"])
    canvas.setLineWidth(0.4)
    canvas.line(18 * mm, footer_y + 4 * mm, PAGE_W - 18 * mm, footer_y + 4 * mm)
    canvas.setFillColor(PALETTE["slate"])
    font = "DocSans" if "DocSans" in pdfmetrics.getRegisteredFontNames() else "Helvetica"
    canvas.setFont(font, 7.2)
    footer_left = f"{clean_text(label)} | {clean_text(title)[:68]}"
    canvas.drawString(18 * mm, footer_y, footer_left)
    canvas.drawRightString(PAGE_W - 18 * mm, footer_y, f"Seite {doc.page}")
    canvas.restoreState()


def build_story(data: Dict[str, Any], styles: Dict[str, ParagraphStyle], width: float) -> List[Any]:
    story: List[Any] = []
    label = clean_text(data.get("document_label", "PARLAMENTARISCHES BRIEFING"))
    title = clean_text(data.get("title", "Briefing Note"))
    subtitle = clean_text(data.get("subtitle", "Parlamentarische Arbeitsfassung"))

    story.append(Spacer(1, 6 * mm))
    story.append(para(label.upper(), styles, "label"))
    story.append(para(title, styles, "title"))
    story.append(para(subtitle, styles, "subtitle"))
    story.append(metadata_panel(data.get("metadata", {}), styles, width))
    story.append(Spacer(1, 7 * mm))

    if data.get("purpose"):
        story.append(info_box("Zweck", data["purpose"], styles, width, "stone"))
        story.append(Spacer(1, 6 * mm))

    story.append(section("Kurzlage", styles, "1"))
    story.append(para(data.get("kurzlage", "Kurzlage zu pruefen."), styles, "body"))
    story.append(Spacer(1, 4 * mm))

    story.append(info_box("Politische Hauptlinie", data.get("politische_hauptlinie", "zu pruefen"), styles, width, "soft"))
    story.append(Spacer(1, 6 * mm))

    story.append(section("Zentrale Fakten", styles, "2"))
    story.append(fact_cards(data.get("facts", []), styles, width))
    story.append(Spacer(1, 6 * mm))

    story.append(section("Bewertung", styles, "3"))
    story.append(bewertung_table(data.get("bewertung", {}), styles, width))
    story.append(Spacer(1, 7 * mm))

    story.append(section("Line to Take", styles, "4"))
    story.append(info_box("Sprechlinie", data.get("line_to_take", "zu pruefen"), styles, width, "soft"))
    story.append(Spacer(1, 7 * mm))

    objections = data.get("gegenargumente", [])
    if objections:
        story.append(section("Erwartbare Gegenargumente und Antwortlinie", styles, "5"))
        story.append(objections_table(objections, styles, width))
        story.append(Spacer(1, 7 * mm))

    hebel = data.get("hebel", [])
    story.append(section("Parlamentarische Hebel", styles, "6"))
    story.append(numbered_sequence(hebel, styles, width))
    story.append(Spacer(1, 7 * mm))

    fragen = data.get("fragen", [])
    if fragen:
        story.append(section("Konkrete Fragen fuer eine parlamentarische Anfrage", styles, "7"))
        story.append(questions_list(fragen, styles, width))
        story.append(Spacer(1, 7 * mm))

    if data.get("kernforderung"):
        story.append(info_box("Kernforderung", data["kernforderung"], styles, width, "stone"))
        story.append(Spacer(1, 6 * mm))

    sources = data.get("sources", [])
    if sources:
        story.append(section("Quellen und Statushinweis", styles, None))
        for source in sources:
            story.append(para(source, styles, "small"))

    return story


def build_pdf(data: Dict[str, Any], output_pdf: Path) -> None:
    fonts = register_fonts()
    styles = make_styles(fonts)
    label = clean_text(data.get("document_label", "PARLAMENTARISCHES BRIEFING"))
    title = clean_text(data.get("title", "Briefing Note"))

    margin_left = 18 * mm
    margin_right = 18 * mm
    margin_top = 20 * mm
    margin_bottom = 18 * mm
    frame = Frame(
        margin_left,
        margin_bottom + 6 * mm,
        PAGE_W - margin_left - margin_right,
        PAGE_H - margin_top - margin_bottom - 12 * mm,
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    doc = BaseDocTemplate(
        str(output_pdf),
        pagesize=A4,
        leftMargin=margin_left,
        rightMargin=margin_right,
        topMargin=margin_top,
        bottomMargin=margin_bottom,
        title=title,
        author="Parliament Briefing Designer",
    )
    doc.addPageTemplates([PageTemplate(id="briefing", frames=[frame], onPage=lambda c, d: draw_page(c, d, label, title))])
    story = build_story(data, styles, PAGE_W - margin_left - margin_right)
    doc.build(story)


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("Input JSON must be an object.")
    validate_input(data)
    return data


def validate_input(data: Dict[str, Any]) -> None:
    """Reject structurally invalid briefing inputs before PDF generation."""
    required_text = ("title", "kurzlage", "politische_hauptlinie", "line_to_take")
    for key in required_text:
        value = data.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"'{key}' must be a non-empty string.")

    for key in ("facts", "hebel", "fragen", "sources", "gegenargumente"):
        value = data.get(key, [])
        if not isinstance(value, list):
            raise ValueError(f"'{key}' must be a list when provided.")

    if not isinstance(data.get("metadata", {}), dict):
        raise ValueError("'metadata' must be an object when provided.")
    if not isinstance(data.get("bewertung", {}), dict):
        raise ValueError("'bewertung' must be an object when provided.")

    for index, fact in enumerate(data.get("facts", []), start=1):
        if not isinstance(fact, dict):
            raise ValueError(f"facts[{index}] must be an object.")
        for key in ("label", "value", "note"):
            if key not in fact:
                raise ValueError(f"facts[{index}] is missing '{key}'.")

    for index, item in enumerate(data.get("gegenargumente", []), start=1):
        if not isinstance(item, dict) or "einwand" not in item or "antwort" not in item:
            raise ValueError(f"gegenargumente[{index}] needs 'einwand' and 'antwort'.")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build an Austrian parliamentary briefing PDF from JSON.")
    parser.add_argument("input_json", type=Path, help="Path to briefing JSON input")
    parser.add_argument("output_pdf", type=Path, help="Output PDF path")
    args = parser.parse_args(argv)

    try:
        data = load_json(args.input_json)
        args.output_pdf.parent.mkdir(parents=True, exist_ok=True)
        build_pdf(data, args.output_pdf)
    except Exception as exc:  # pragma: no cover
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Created {args.output_pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
