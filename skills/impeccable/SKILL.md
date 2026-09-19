---
name: impeccable
description: Create or apply an evidence-backed visual craft and UX quality pass when a frontend needs a distinctive design direction, critique, hardening, final polish, or removal of generic AI styling. Use as the visual quality layer for websites, landing pages, product interfaces, and design systems when intentional aesthetics materially matter. Do not use as the default for ordinary frontend implementation, framework mechanics, an isolated interaction issue, guideline-only compliance, or backend work.
---

# Impeccable

Produce frontend work with a clear visual point of view, strong product reasoning, and production quality execution. Avoid generic template output. Preserve the user's brief, product truth, and existing constraints while making deliberate design choices.

## Core principles

1. Finish the requested surface. Do not stop at a sketch when the user asked for implementation.
2. Make the design specific to the product, audience, and task. Generic SaaS styling is a failure mode.
3. Treat the brief as authoritative. Do not replace requested aesthetics with personal taste.
4. Preserve behavior and factual copy during refinement unless the user explicitly asks to change them.
5. Separate refinement from redesign. Refinement improves the existing visual world. Redesign may replace it while preserving product truth and function.
6. Use evidence from the project before editing. Inspect the target and at least one source of visual truth such as tokens, theme, CSS, components, screenshots, or assets.
7. Accessibility, responsive behavior, and interaction clarity are part of craft, not cleanup.
8. Verify in bounded passes. Build fully, inspect desktop and mobile together, fix the discovered issues in one batch, confirm once, then stop polishing.

## Start every task

1. Classify the request as new work, refinement, evaluation, extraction or documentation.
2. Determine the surface mode from the user's goal:
   * Persuade: landing pages, pricing, campaigns, marketing. Optimize attention, trust, and action.
   * Operate: dashboards, editors, admin, settings, tools. Optimize scanability, speed, consistency, and task completion.
   * Read: documentation, articles, help, guides, changelogs. Optimize comprehension and reading rhythm.
   * Experience: portfolios, galleries, showcases. Let the artifact dominate and keep interface chrome restrained.
3. Inspect the target and incumbent visual system before changing code.
4. Load exactly the reference needed for the current step:
   * New surface or full redesign: `references/new-work.md`
   * Any implementation or styling pass: `references/craft-floor.md`
   * Critique or audit: `references/evaluation.md`
   * Explicit command: `references/command-playbooks.md`
   * Responsive or native adaptation: `references/responsive-native.md`
5. If code execution is available, run the bundled linter on the target before the final polish pass:
   `python <skill-base-dir>/scripts/ui_lint.py <target>`

Do not load every reference preemptively.

## Command routing

Support these command concepts whether the user names them explicitly or describes the same intent in ordinary language.

| Command | Purpose |
| --- | --- |
| `craft` | Build a new surface with a deliberate visual world |
| `shape` | Plan UX and UI before implementation |
| `init` | Capture durable product and audience context |
| `document` | Derive a reusable design description from existing code |
| `extract` | Consolidate repeated UI patterns into components and tokens |
| `critique` | Evaluate UX quality, hierarchy, clarity, and visual coherence |
| `audit` | Check accessibility, responsive behavior, robustness, and performance risks |
| `polish` | Perform the final visual and interaction quality pass |
| `bolder` | Increase hierarchy, identity, contrast, scale, or composition confidence |
| `quieter` | Reduce visual noise, competing emphasis, decoration, and cognitive load |
| `distill` | Remove nonessential controls, copy, containers, and visual complexity |
| `harden` | Handle errors, loading, empty states, long content, i18n, and edge cases |
| `onboard` | Improve first run, activation, guidance, and empty states |
| `animate` | Add purposeful motion tied to state, hierarchy, or feedback |
| `colorize` | Introduce strategic color with semantic and accessibility discipline |
| `typeset` | Improve font selection, hierarchy, measure, rhythm, and text contrast |
| `layout` | Improve grouping, spacing, alignment, density, and reading order |
| `delight` | Add restrained personality, micro interactions, and memorable moments |
| `overdrive` | Push a concept beyond conventional composition while retaining usability |
| `clarify` | Improve labels, instructions, validation, errors, and UX copy |
| `adapt` | Adapt the interface across device classes, breakpoints, and native expectations |
| `optimize` | Diagnose and improve perceived and actual UI performance |
| `live` | Generate focused visual variants for a selected element or region |

When two commands fit equally well, choose the narrower one. Ask only when choosing incorrectly would materially change the requested result.

## New work workflow

Use `references/new-work.md`.

1. Establish product truth: audience, task, content priority, constraints, and required states.
2. Choose one coherent visual direction rather than blending several unrelated styles.
3. Define hierarchy before decoration: reading order, primary action, supporting content, and navigation.
4. Implement the complete responsive surface.
5. Apply `references/craft-floor.md` immediately before the final styling pass.
6. Run bounded QA across the relevant device classes and interaction states.

## Refinement workflow

1. Preserve existing identity, behavior, data, and scope unless replacement is requested.
2. Diagnose the dominant problem before editing. Examples: weak hierarchy, excessive chrome, cramped density, bland typography, inconsistent spacing, unclear actions.
3. Use the smallest command that owns the problem.
4. Make coherent changes across the whole affected region rather than isolated cosmetic tweaks.
5. Verify that the result still belongs to the incumbent design system.

## Evaluation workflow

Use `references/evaluation.md`.

For critique, prioritize product and design judgment. For audit, prioritize verifiable implementation risk. Do not mix subjective preference into technical severity.

Every finding should contain:

1. Severity: critical, high, medium, or low.
2. Evidence: exact component, screen, selector, behavior, or code pattern.
3. Impact: what becomes harder, slower, less accessible, or less credible for the user.
4. Fix: a concrete change, not a vague recommendation.

Prefer a short ranked list of consequential findings over a long inventory of trivialities.

## Quality floor

Use `references/craft-floor.md` before editing UI. At minimum:

* Avoid defaulting to Inter, purple to blue gradients, excessive rounded cards, card nesting, decorative icon tiles, glassmorphism, and generic hero patterns unless the brief specifically calls for them.
* Do not use low contrast gray text on colored surfaces.
* Do not use motion without purpose or ignore `prefers-reduced-motion` for meaningful animation.
* Do not hide focus indicators or substitute clickable nonsemantic containers for real controls.
* Do not create responsive behavior by simply shrinking desktop layout.
* Do not add invented product claims, testimonials, metrics, or factual copy.
* Do not add a new design system solely because one file is missing. First inspect the existing visual authority.

## Optional deterministic lint

The bundled `scripts/ui_lint.py` performs a fast static scan for several recurring frontend quality risks. Use it as evidence, not as a substitute for visual inspection.

Typical invocation:

```bash
python <skill-base-dir>/scripts/ui_lint.py path/to/src
python <skill-base-dir>/scripts/ui_lint.py path/to/component.tsx --json
```

Fix only findings relevant to the user's task unless the user requested a broad audit.

## Working with other skills

Treat Impeccable as the visual design and UX layer. When a framework, accessibility, React, testing, or deployment skill is also active, follow its technical constraints while keeping this skill's visual quality floor. If instructions conflict, correctness, accessibility, explicit user requirements, and platform conventions outrank aesthetic ambition.

## Source and attribution

This ChatGPT adaptation is based on the open source Impeccable project by Paul Bakaus. Read `references/source-and-license.md` for upstream provenance, adaptation notes, and licensing.
