# PDF Production Workflow

This skill must inherit the PDF skill workflow before producing the final file.

## Required base step

Before creating or editing PDFs, use the PDF skill and rendering tools actually available in the current environment. Apply their design standards and render, inspect, revise, verify loop. Do not assume a fixed skill URI or filesystem path.

## Preferred creation path

Use the bundled script for structured briefing PDFs:

```bash
python scripts/build_at_parliament_briefing.py input.json output.pdf
```

Then render with the active PDF workflow. Inspect every rendered page. Fix problems and rerender.

## Visual QA checklist

Check:

- no clipped umlauts or special characters
- no text outside cards or tables
- no excessive red areas
- no unbalanced empty page bottoms
- page 1 identifies topic, purpose, recipient, stand, and status
- facts are visually separated from assessment
- objection/answer table is readable
- final request or next action is immediately visible
- footer and page numbers are consistent

## Source QA checklist

Check:

- all numbers came from the source material or are marked as open
- political claims are labelled as interpretation or proposed wording
- data gaps are not converted into claims
- no false official publication status
- no unauthorised use of official emblems or logos

## If the document becomes too long

Do not squeeze text. Cut the briefing and move details to appendix.

Priority order:

1. Keep Kurzlage, Hauptlinie, facts, Line to Take, Hebel, next step.
2. Shorten background explanation.
3. Reduce facts from 5 to 3.
4. Move full questions catalogue to appendix.
5. Keep citations and caveats.
