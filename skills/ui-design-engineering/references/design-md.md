# DESIGN.md reconstruction

Use when documenting the design language of an existing product repository or observable public website.

## Boundaries

- Modify only `DESIGN.md` unless the user requests broader implementation work.
- Document governing design intent, not every implementation value.
- Do not convert repeated local styling into system intent without evidence.
- Do not invent brand rationale, audience assumptions, token names, or component ownership.

## Mode selection

### Repository mode

Prefer source when available. Inspect, in order:

1. existing `DESIGN.md` and explicit repository guidance
2. tokens, themes, variables, and global styles
3. shared primitives and variants
4. representative routes and rendered consumers
5. local implementations

Only treat a source as governing when the audited product actually imports, inherits, references, or renders it.

### URL mode

Use rendered browser evidence. Inspect representative desktop and mobile views, DOM, computed styles, and loaded public stylesheets. Screenshots can support interpretation but should not be the sole source for exact values.

For site-wide claims, sample multiple distinct templates. Label the result as reconstructed.

## Evidence model

For every candidate design rule, establish:

`role -> value -> source -> scope -> recurrence -> confidence`

Promote exact values only when they are measured or tied to an observable loaded declaration. Omit uncertain, one-off, or purely aesthetic guesses.

## Content rules

- Keep frontmatter sparse and schema-consistent.
- Preserve semantic token names that genuinely exist in the governing source.
- Do not generate fake scales from one base token.
- Put exact normative values in structured frontmatter when the selected DESIGN.md tooling supports them.
- Put implementation guidance and rationale in Markdown.
- Outside the overview, keep only prose that changes implementation decisions.
- Preserve accepted existing decisions unless current governing evidence or the user explicitly replaces them.

## Validation

When `@google/design.md` is available, inspect its current spec, lint the document, and run one compatible export. Do not claim success when populated token categories disappear during export.

When updating an existing `DESIGN.md`, compare against the previous version and restore accepted decisions that were removed without evidence.

## Report

Return the mode, audited product or URL, created or updated document, governing sources, omitted unsupported areas, and validation result.
