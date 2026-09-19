# Upstream and provenance

## Source

This ChatGPT-native skill is adapted from:

`nextlevelbuilder/ui-ux-pro-max-skill`

Repository:

`https://github.com/nextlevelbuilder/ui-ux-pro-max-skill`

Upstream license: MIT.

Copyright notice from the upstream LICENSE:

`Copyright (c) 2024 Next Level Builder`

The full MIT license text is included at the skill root in `LICENSE`.

## Snapshot reviewed

Reviewed on 2026-08-29 from the public `main` branch.

The upstream project describes a design-intelligence workflow that combines product, style, color, landing-pattern, typography, UX, chart, motion, icon, font, React-performance, native-interface, and stack-specific guidance. Its source includes a local Python search engine and a design-system generator with product reasoning, optional variance/motion/density controls, and persisted master/page design-system files.

## ChatGPT adaptation choices

This package is intentionally not a byte-for-byte copy of the repository.

It keeps the high-value workflow and interface concepts while adapting them to ChatGPT Skills:

1. A compact `SKILL.md` acts as the control plane.
2. Detailed quality, stack, and design guidance is progressively loaded from `references/`.
3. `scripts/search.py` is standard-library-only and requires no network access.
4. A compact offline catalog replaces very large upstream font and icon catalogs so the skill remains lightweight and fast.
5. The generator supports system design, focused domain search, stack routing, variance/motion/density dials, and optional `MASTER.md` persistence.
6. Exact current framework-version claims are deliberately excluded from the offline catalog. Current APIs should be verified against project manifests and official documentation.

## Upstream concepts preserved

- Start with the product and user task.
- Generate a coherent design system before ad hoc component styling for broad design work.
- Search one dominant intent at a time.
- Resolve semantic UX outcomes before framework implementation details.
- Retry a mismatched lookup once with narrower terms instead of treating weak results as authoritative.
- Separate visual style, palette, typography, page pattern, charts, UX guidance, and stack implementation.
- Use design dials for controlled variance, motion, and density.
- Support a master design system plus page-specific overrides.
- Apply accessibility, text resilience, reduced motion, responsive behavior, and state design as production requirements.

## Scope difference

The upstream repository contains significantly larger catalogs, including extensive Google Font and icon data plus more granular product/style records. This ChatGPT package uses a deliberately compact curated catalog because the model can synthesize project-specific choices from high-value rules without carrying the entire upstream database into every skill package.
