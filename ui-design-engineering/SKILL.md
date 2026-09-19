---
name: ui-design-engineering
description: Design, audit, document, polish, and harden production user interfaces using an evidence-first design-engineering workflow derived from ibelick/ui-skills. Use for frontend UI cleanup, spacing and hierarchy fixes, accessibility audits, metadata and social-preview fixes, animation performance, design-system reconstruction into DESIGN.md, or evidence-based interface improvement planning. Route to the smallest relevant reference and preserve the product's existing design language unless redesign is explicitly requested.
---

# UI Design Engineering

Use the smallest relevant rule set for the task. Preserve existing product identity, components, tokens, libraries, and architecture unless the user explicitly asks for a redesign or migration.

## Routing

Classify the request first:

1. For fast visual cleanup, spacing, hierarchy, typography, states, loading, empty states, or generic UI quality, read `references/baseline-ui.md`.
2. For buttons, forms, dialogs, keyboard use, focus, ARIA, semantics, contrast, or WCAG issues, read `references/accessibility.md`.
3. For titles, descriptions, canonical URLs, robots, Open Graph, Twitter cards, favicons, manifests, JSON-LD, or locale metadata, read `references/metadata.md`.
4. For stutter, jank, transitions, scroll-linked motion, filters, layout animation, or animation architecture, read `references/motion-performance.md`.
5. For creating or updating `DESIGN.md` from source code or a public site, read `references/design-md.md`.
6. For auditing an existing interface against its own design evidence and producing a bounded improvement plan, read `references/improve-ui.md`.
7. For broad UI review, combine at most three references. Prefer specific references over broad ones.

## Operating principles

- Trace the actual rendered or imported path before inferring system-wide rules.
- Treat repetition and visual similarity as evidence candidates, not proof of product intent.
- Prefer existing project primitives and tokens over introducing new abstractions.
- Avoid unrelated refactors and library migrations.
- Prefer native platform semantics and established accessible primitives over custom interaction behavior.
- Keep fixes scoped and deterministic. State assumptions when source evidence is incomplete.
- For audits, distinguish verified problems from preferences.
- For direct implementation requests, implement the requested scope unless a selected reference explicitly requires a read-only planning workflow.
- For review-only requests, do not modify source.

## Review output

When auditing code, report each confirmed issue with:

- location or exact snippet
- problem
- why it matters
- concrete correction
- severity or confidence when useful

Do not inflate the report with unsupported findings. Prioritize the highest impact issues first.

## Implementation quality gate

Before declaring completion:

1. Verify the requested interaction and responsive behavior.
2. Check keyboard access and accessible names for changed interactive controls.
3. Check loading, empty, error, disabled, and destructive states when relevant.
4. Check mobile viewport behavior and fixed-element safe areas.
5. Ensure animation does not continuously trigger expensive layout or paint on large surfaces.
6. Ensure metadata remains internally consistent when metadata was changed.
7. Preserve the project stack unless migration was requested.

## Source basis

This skill is adapted from the public MIT-licensed `ibelick/ui-skills` project. See `references/source-notes.md` for provenance and adaptation notes.
