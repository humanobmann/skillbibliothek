---
name: pdf-campaign-redesigner
description: Prüft oder gestaltet bereitgestellte PDF-Dossiers ausdrücklich im logo-freien Editorialstil der SPÖ St. Pölten Sektion VII. Nutze diesen Skill nur, wenn der Nutzer diesen konkreten Sektionsstil verlangt oder ein bereits in diesem Stil erstelltes Dossier prüfen oder weiterbearbeiten will. Respektiere reine Prüfaufträge und erstelle nur bei ausdrücklich gewünschter Überarbeitung eine neue PDF.
---

# PDF Campaign Redesigner

Use this skill to audit or redesign a provided PDF under the SPÖ Sektion VII dossier design system. Match the requested mode exactly: audit-only requests produce findings without changing the PDF; redesign requests produce a revised PDF.

## Non-negotiables

- Work in German (`de-AT`) unless the user explicitly asks otherwise.
- Apply the SPÖ Sektion VII **logo-free editorial dossier system** exactly. Load `references/design-system.md` before design work.
- Apply the audit/redesign standard from `references/audit-standard.md` before rebuilding pages.
- Never add logos, party marks, watermarks, decorative icons, branding footers, or font files unless the user explicitly asks and rights are clear.
- Do not distribute or expose font files. If Area fonts are already available in the current project and licensed, use only as allowed; otherwise use the documented fallback stacks.
- Treat every number, quote, and causal claim as unsafe until it has a source/status. If a claim lacks a source, preserve it in working material and mark it `PRUEFEN` or `UNSICHER`. Do not remove, rewrite, merge, or suppress substantive content without explicit authorization or a clearly documented, reversible proposal.
- Default to one core message per page. Replace table walls with evidence graphics, structured cards, and concise source lines.
- Social assets or export checklists are **only** produced when the user asks for them. For those, load `references/social-export-checklist.md`.

## Default workflow

1. **Intake and render**
   - Identify source PDF, requested scope, publication status, and whether sources are supplied.
   - Render the input PDF to images first, inspect layout/page screenshots, then extract text. For PDF operations, follow the host PDF workflow: render -> inspect -> operate -> re-render/verify.

2. **Audit**
   - Load `references/audit-standard.md` before every audit, including audit-only requests.
   - Create a short page inventory: page number, purpose, core message, evidence status, visual problem, risk level.
   - Flag: missing source lines, contradictory figures, unproven claims, too-dense tables, weak hierarchy, inaccessible contrast, text overflow, non-logo-free elements, decorative diagrams.
   - Use the 5 gates: source, content/method, text, design, political/publication release.
   - If the request is audit-only, stop after delivering the findings and prioritized recommendations. Do not edit, rebuild, export, or replace the source PDF.

3. **Rebuild plan**
   - Propose whether to keep, merge, split, rewrite, or remove each page. Preserve all source content by default.
   - Choose the shortest evidence-led page sequence that preserves the argument and all required proof. Use this order as a menu, not a fixed page count: problem -> facts -> who pays -> what hurts -> what is protected -> investment -> alternatives -> attacks -> fact-check -> production -> gates -> sources.
   - Place the hardest/most honest constraints before the positive proof, not after it.

4. **Produce the optimized PDF**
   - Run this step only when the user asked for a redesign, rebuild, optimization, or edited export.
   - Prefer HTML/CSS-to-PDF or slide-like authoring when layout is visual; use bundled `assets/dossier-template.html` and `assets/dossier-styles.css` as the starting point.
   - Build the new PDF with exact A4 portrait layout, source lines, callouts, table styles, and infographic rules from the design system.
   - Use `scripts/render_html_to_pdf.py` when HTML-to-PDF conversion is appropriate and the runtime supports Playwright or WeasyPrint.

5. **Verify**
   - Re-render the optimized PDF and inspect visible pages.
   - Fix clipped text, overflow, broken glyphs, missing page numbers, weak contrast, orphaned headings, split tables, unlabelled color, and missing sources.
   - Deliver the optimized PDF plus a concise changelog. Include the audit report only if useful; do not let it replace the PDF deliverable.

## Output defaults

For audit-only requests, return a concise, page-referenced audit with prioritized findings and no modified PDF.

For redesign requests, return:

1. `optimized.pdf` or a descriptive German filename for the rebuilt PDF.
2. A concise changelog: biggest structural changes, source/risk changes, design improvements, remaining blockers.

Do **not** return social exports, asset packages, carousels, or export checklists unless the user asks.

## Work-Mode handoff

- Keep temporary renders and intermediate files in scratch storage.
- Use the Library skill for new durable files unless the user selected another verified destination. Do not duplicate files that already belong to an externally synchronized Git repository.
- Deliver the final file with an openable absolute sandbox link.
- If the requested PDF cannot be created or saved, state that clearly and provide the verified audit or source package that is available.
- Do not claim that pages were visually verified unless the rendered output was actually inspected.

## Mandatory references

- `references/design-system.md` - exact color, type, layout, table, callout, infographic, and PDF export rules.
- `references/audit-standard.md` - audit criteria, publication gates, page-dramaturgy, and redesign priorities.
- `references/pdf-rebuild-workflow.md` - practical rebuild workflow and verification checklist.
- `references/social-export-checklist.md` - only when social assets/checklists are explicitly requested.

## Bundled scripts and assets

- `assets/dossier-template.html` - minimal A4 dossier shell.
- `assets/dossier-styles.css` - strict logo-free editorial CSS tokens and components.
- `scripts/render_html_to_pdf.py` - HTML-to-PDF helper using Playwright or WeasyPrint when available.
- `scripts/preflight_redesign_package.py` - checks expected deliverable files and common forbidden package contents.
