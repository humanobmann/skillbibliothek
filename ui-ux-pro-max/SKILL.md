---
name: ui-ux-pro-max
description: Define and implement the UI system for a new interface or broad redesign across web, mobile, or desktop, or perform a requested P0-to-P3 product-wide UI audit. Use when visual direction, information hierarchy, responsive and accessible states, component rules, and frontend stack guidance must be decided together. Do not use for a small polish pass, isolated motion or interaction, shadcn mechanics, guideline-only compliance, or backend, database, infrastructure, and non-UI automation work.
---

# UI UX Pro Max

Create UI that is intentional, usable, accessible, resilient, and specific to the product rather than generically attractive.

This is a ChatGPT-native adaptation of the open-source `nextlevelbuilder/ui-ux-pro-max-skill`. Preserve the upstream MIT attribution in `references/upstream.md` and `LICENSE`.

## Operating contract

1. Inspect the supplied UI, codebase, screenshot, requirements, or artifact before prescribing changes.
2. Infer product type, user task, platform, target viewport, implementation stack, content density, brand constraints, and accessibility needs from available context. Ask only when a missing fact materially blocks correctness.
3. Select exactly one primary mode:
   - **System design** for a new page, product, redesign, or broad visual direction.
   - **Focused search** for one UI concern such as forms, focus, charts, typography, color, motion, or responsive behavior.
   - **Audit** for an existing interface or implementation.
   - **Implementation** when code or concrete edits are requested.
4. Ground recommendations with the bundled catalog or references before improvising. Treat catalog output as design evidence, not as authority over user requirements or repository rules.
5. Separate semantic UX outcomes from framework implementation details. Resolve the UX need first, then apply stack guidance.
6. Prefer the smallest change that produces a coherent improvement. Do not redesign unrelated areas unless the user asks for a redesign.
7. Verify the final result against the quality gates before claiming completion.

## System design workflow

For a new interface, redesign, landing page, dashboard, or product-wide visual direction, run:

```bash
python3 scripts/search.py "<product industry tone task>" --design-system --project-name "<name>" --json
```

Use 2 to 5 meaningful query terms plus one useful constraint. Examples:

```bash
python3 scripts/search.py "nonprofit civic participation trustworthy" --design-system -p "Community Portal" --json
python3 scripts/search.py "analytics operations dashboard dense" --design-system -p "Ops Console" --density 8 --json
python3 scripts/search.py "creative portfolio editorial bold" --design-system -p "Studio" --variance 8 --motion 6 --json
```

Synthesize the result rather than copying it mechanically. Check that the selected profile fits the actual product and audience.

### Design dials

Use optional 1 to 10 dials only when they improve the requested direction:

- `--variance 1-3`: centered, restrained, systematic.
- `--variance 4-7`: balanced contemporary composition.
- `--variance 8-10`: more asymmetric, editorial, bento, or neo-brutal composition.
- `--motion 1-3`: essential state feedback only.
- `--motion 4-7`: standard product transitions and modest reveal choreography.
- `--motion 8-10`: expressive staged motion, still interruptible and reduced-motion safe.
- `--density 1-3`: spacious marketing, editorial, or premium presentation.
- `--density 4-7`: normal product density.
- `--density 8-10`: compact operational dashboard or admin density.

Do not use a dial to override task needs. A dense healthcare form still needs readable labels and targets. A luxury page still needs obvious actions.

### Persisting a design system

Persist only after the design direction has been checked against the project:

```bash
python3 scripts/search.py "<query>" --design-system --project-name "<name>" --persist --output-dir "<project-root>"
```

For a page-specific override:

```bash
python3 scripts/search.py "<query>" --design-system --project-name "<name>" --persist --page "dashboard" --output-dir "<project-root>"
```

Read the existing `design-system/<project>/MASTER.md` before using `--force`. Do not overwrite prior design decisions without explicit authorization.

## Focused search workflow

Use one dominant concern per query:

```bash
python3 scripts/search.py "<query>" --domain <domain>
```

Domains:

- `product`: product archetype and strategic UI priorities.
- `style`: visual system and composition direction.
- `color`: semantic palette direction.
- `typography`: type pairing and hierarchy direction.
- `landing`: page structure and conversion flow.
- `chart`: analytical visualization choice.
- `ux`: accessibility, interaction, forms, navigation, state, layout, resilience.
- `stack`: framework or platform implementation guidance.

For a known stack:

```bash
python3 scripts/search.py "<implementation concern>" --stack nextjs
```

Search the semantic outcome first, then the stack. Examples:

```bash
python3 scripts/search.py "form validation error recovery" --domain ux
python3 scripts/search.py "server rendered form validation" --stack nextjs

python3 scripts/search.py "chip badge long text wrapping" --domain ux
python3 scripts/search.py "responsive chip overflow" --stack html-tailwind
```

If a result is clearly off-topic, rewrite the query once with a narrower intent. If it still does not fit, state that the local catalog has no verified match and use general UI expertise rather than pretending the match is authoritative.

## Audit workflow

Read `references/quality-gates.md` for full checks. Audit in this order:

1. Task and information hierarchy.
2. Accessibility and interaction semantics.
3. Responsive and content resilience.
4. Forms, feedback, loading, empty, error, disabled, success, permission, offline, and destructive states where applicable.
5. Typography, color, spacing, icons, elevation, and component consistency.
6. Motion and perceived performance.
7. Stack-specific implementation quality.
8. Visual distinctiveness and avoidance of generic AI design patterns.

Report findings by severity:

- **P0 blocker**: prevents core task, creates serious accessibility failure, data loss, or dangerous ambiguity.
- **P1 high**: materially harms completion, comprehension, responsiveness, or accessibility.
- **P2 medium**: inconsistency or friction with a clear user impact.
- **P3 polish**: visual refinement with low functional risk.

For each finding, identify the evidence, consequence, and concrete fix. Do not produce a vague aesthetics critique.

## Implementation workflow

When code changes are requested:

1. Inspect existing design tokens, component primitives, dependencies, routing, state model, and responsive conventions.
2. Preserve working behavior unless the user asked to change it.
3. Reuse existing components before adding parallel primitives.
4. Centralize repeated values into semantic tokens instead of scattering raw colors, spacing, radius, and z-index values.
5. Use native semantic elements and framework accessibility primitives before custom role emulation.
6. Implement all relevant states, not only the happy-path screenshot.
7. Keep responsive ordering aligned with logical reading and keyboard order.
8. Avoid fixed heights for text-bearing components unless overflow behavior is explicitly designed.
9. Optimize measured bottlenecks rather than adding memoization or animation libraries by reflex.
10. Run available tests, linters, type checks, and visual checks after changes.

For current React or Next.js performance details, prefer current official documentation or a dedicated current React best-practices skill when available. Do not treat the bundled catalog as a version oracle.

## Visual direction rules

Read `references/design-system-playbook.md` when making broad visual choices. Apply these defaults unless product context overrides them:

- Establish one dominant visual idea and one dominant task per screen.
- Use typography, spacing, and layout before adding decorative containers.
- Avoid wrapping every section in a rounded card.
- Avoid generic purple-pink AI gradients, sparkle icon clichés, decorative blobs, and identical three-card feature rows unless evidence supports them.
- Use authentic or purposeful imagery. Do not invent branding, logos, organization names, or campaign marks unless requested.
- Prefer a consistent vector icon family. Never use emoji as structural navigation or control icons.
- Keep one primary action visually dominant. Subordinate secondary actions.
- Make density task-specific instead of globally spacious or globally compact.
- Treat dark mode as its own semantic token mapping, not a color inversion.
- Treat glass and blur as hierarchy tools, not default decoration.
- Preserve text legibility over images and translucent surfaces.

## Accessibility and resilient UI

Read `references/quality-gates.md` for detailed checks. At minimum:

- Keep normal text at or above 4.5:1 contrast and meaningful non-text UI at or above 3:1 where applicable.
- Keep keyboard focus visible, logical, and unobscured.
- Give icon controls accessible names and relevant state.
- Hide decorative icons from the accessibility tree.
- Do not communicate meaning through color alone.
- Provide keyboard and single-pointer alternatives for essential drag or swipe actions.
- Respect reduced-motion preferences.
- Support text enlargement, zoom, narrow widths, localization expansion, and long tokens without clipping essential content.
- Prefer wrapping to truncation. When truncation is unavoidable, provide an operable way to access the complete value.
- Keep failed form values, show errors near fields, and use a linked error summary for multi-error forms when appropriate.
- Allow password managers and paste in authentication flows.

## Charts and data interfaces

Choose a chart from the analytical question, not from visual novelty:

```bash
python3 scripts/search.py "trend over time" --domain chart
python3 scripts/search.py "compare categories ranking" --domain chart
python3 scripts/search.py "distribution outliers" --domain chart
```

Prefer a table when users need exact values, auditability, sorting, filtering, copying, or dense comparison. Never rely on color alone. Include units, period, denominator, and comparison baseline for headline metrics.

## Stack routing

Read `references/stack-routing.md` when implementation details depend on the framework. Supported local routes include React, Next.js, Vue, Svelte, Astro, HTML with Tailwind, shadcn/ui, Angular, Nuxt, React Native, Flutter, SwiftUI, Jetpack Compose, Three.js, Laravel, JavaFX, WPF, WinUI, Avalonia, Uno, and legacy UWP.

Do not assume a stack from the visual request. Infer it from project files or explicit context when available.

## Output expectations

Match the deliverable to the request:

- For a design request, provide a concrete hierarchy, design system, component/state decisions, responsive behavior, and implementation direction.
- For a critique, provide prioritized findings and fixes, not a replacement design unless requested.
- For implementation, edit or provide production-ready code and verify it.
- For a design-system request, provide tokens plus behavioral rules and component states, not colors alone.
- For a chart request, state the analytical question, chosen encoding, fallback, and accessibility notes.

Do not expose internal catalog searches as filler. Use them to improve the final design decision.

## Final quality gate

Before completion, verify the relevant items in `references/quality-gates.md`. At minimum confirm hierarchy, semantics, focus, contrast, responsive reflow, long content, component states, reduced motion, token consistency, and absence of unnecessary decorative patterns.
