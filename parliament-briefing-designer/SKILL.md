---
name: parliament-briefing-designer
description: Creates and finalizes concise Austrian parliamentary briefing PDFs from dossiers, research notes, Markdown, or structured JSON. Use for a professional Briefing Note, parlamentarisches Briefing, Abgeordnetenbriefing, Ausschussvorbereitung, source-backed parliamentary question pack, opposition/response lines, or a sober Austrian institutional briefing design. Do not use for political research without a briefing deliverable, generic PDF redesign, party campaign dossiers, or claims that still require substantive verification before condensation.
---

# Parliament Briefing Designer

## Core rule

Create a concise, source-backed, visually polished Austrian parliamentary Briefing Note. Treat the long dossier as the evidence base and the PDF as an executive working document, not as a campaign folder.

Before creating or modifying a PDF, use the PDF skill that is actually available in the current environment and follow its render, inspect, revise, and verify loop. Do not guess a filesystem path or claim that a PDF workflow was loaded when it was not. This skill adds the Austrian parliamentary design system and briefing structure on top of the active PDF workflow.

## Default output

Produce a 3 to 5 page A4 PDF unless the user requests another format. The long research file should remain a background paper or appendix. The briefing itself should be compact, executive, and parliamentary.

Use these sections in this order unless the source material demands a minor adjustment:

1. Zweck
2. Kurzlage
3. Politische Hauptlinie
4. Zentrale Fakten
5. Bewertung
6. Line to Take
7. Erwartbare Gegenargumente und Antwortlinie
8. Parlamentarische Hebel
9. Konkrete Fragen fuer eine parlamentarische Anfrage
10. Ergebnis oder naechster Schritt

Consult `references/briefing-structure.md` for the full content model.

## Design direction

Use an Austrian parliamentary design language:

- Red-white-red as state reference, not party branding.
- Warm white, stone, graphite, muted red, and restrained gold or brass accents.
- No official Parliament logo, coat of arms, party logo, ministry logo, or fake official seal unless the user provides explicit permission and assets.
- Make the document look like an internal high-level parliamentary working paper.
- Prefer strong typography, spacing, hierarchy, source discipline, and quiet data cards over decorative graphics.

Consult `references/design-system.md` before designing pages.

## Content handling

1. Use the user-provided source material as the primary basis.
2. Do not invent facts, dates, functions, figures, sources, or political positions.
3. Mark unsupported points as `zu pruefen` or `offen`.
4. Preserve the distinction between fact, assessment, political conclusion, and proposed wording.
5. Keep security-sensitive information aggregated. Do not expose operationally sensitive stocks, site-level capabilities, readiness patterns or protected location details merely because they appear in source material.
6. Keep the document neutral-parliamentary unless the user explicitly asks for a party-internal version.

## Production workflow

1. Extract the source claims and identify the political working purpose.
2. Build a concise briefing model with the standard sections.
3. Select the correct visual density:
   - 2 pages for a quick office note.
   - 3 to 5 pages for a proper Briefing Note.
   - Separate appendix for long tables and full research.
4. Use `scripts/build_at_parliament_briefing.py` when the content can be represented as structured JSON.
5. If using another PDF pipeline, still apply the design system and the PDF skill render checks.
6. Render the final PDF to PNG pages and inspect for clipping, overlaps, awkward spacing, weak hierarchy, unreadable tables, or unprofessional density.
7. Iterate until the rendered pages look clean.

If no renderer is available, stop short of claiming visual verification. Deliver the validated source package and state the remaining render gate.

Consult `references/pdf-production.md` for the exact PDF QA gates.

## Structured script workflow

When enough content is available, create a JSON input and run:

```bash
python scripts/build_at_parliament_briefing.py input.json output.pdf
```

The script accepts fields such as `title`, `subtitle`, `metadata`, `purpose`, `kurzlage`, `politische_hauptlinie`, `facts`, `bewertung`, `line_to_take`, `gegenargumente`, `hebel`, `fragen`, `kernforderung`, and `sources`.

Use `references/sample-input.example.json` as a starting point.

## Quality gate

Before delivering the PDF, confirm all of the following:

- The visual style fits Austria and Parliament without pretending to be an official Parliament publication.
- The red-white-red motif is restrained and not party-political.
- The first page explains purpose, topic, recipient, status, and stand.
- The document is scannable in under two minutes.
- Every number and factual claim is either source-backed or marked as open.
- Tables and boxes have enough padding and no clipped text.
- The final PDF has been rendered and visually checked.
