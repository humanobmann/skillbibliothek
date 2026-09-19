---
name: interface-design
description: Design, build, review, audit, and refine production product interfaces such as dashboards, admin panels, SaaS applications, tools, settings pages, data interfaces, and interactive software. Use when visual hierarchy, product-specific design direction, tokens, spacing, typography, states, motion, accessibility, component consistency, design-system memory, UI critique, or removal of generic AI-generated interface patterns matters. Do not use for marketing pages, campaign sites, landing pages, or brand-only work unless the task is specifically about product UI inside them.
---

# Interface Design

Design product interfaces as coherent systems, not collections of generic components. Make every visible choice traceable to the product, the user's task, and the established design language.

## Core workflow

1. Inspect the existing interface, codebase, component library, design tokens, styling conventions, and `.interface-design/system.md` when available.
2. Identify the actual user, the primary task, and the intended feel of the interface.
3. Explore the product domain before choosing visual direction. Produce:
   - at least five domain concepts or metaphors
   - at least five colors or material cues that naturally belong to that domain
   - one signature visual, structural, or interaction idea unique to this product
   - three obvious interface defaults to avoid and a stronger alternative for each
4. Define the interface direction. State the focal point, hierarchy, palette logic, depth strategy, surface system, typography strategy, spacing base, and density.
5. Reuse existing native controls, design-system components, and accessible headless primitives before creating new behavior.
6. Implement or revise the interface consistently with the established direction.
7. Verify the result visually and technically. Run build, typecheck, tests, and responsive checks when available.
8. Run the review checks in `references/review.md` before presenting the result.
9. Offer to save reusable decisions to `.interface-design/system.md` when the work establishes or changes a reusable pattern.

## Product-specific direction

Avoid generic descriptors such as "clean", "modern", or "professional" unless they are translated into concrete decisions. Connect every major visual choice to the product domain and task.

Before major UI work, define:

```text
Intent: user + task + intended feel
Focal point: the one element that must win visually
Hierarchy: how size, weight, contrast, and space create ordering
Palette: colors and materials grounded in the product domain
Depth: borders, subtle shadows, layered shadows, or surface shifts
Surfaces: elevation levels and interaction between canvas, panels, overlays, and controls
Typography: typeface, type scale, weights, opacity hierarchy, number treatment
Spacing: 4px or 8px base grid plus chosen density
Signature: one recurring product-specific element
```

For greenfield screens, major redesigns, or ambiguous direction, show or generate a compact visual specimen when a suitable rendering or image tool is available. Use visual tools for direction boards, UI references, critique paintovers, or raster assets. Do not substitute those previews for implementation.

## Hierarchy and composition

Create one dominant focal point per view. Demote secondary information deliberately.

Use a type ratio rather than arbitrary sizes. Favor weight, contrast, opacity, and spacing as much as size. Use tabular numerals for dynamic or aligned numeric data.

Treat density as a deliberate system. Keep closely related controls tight and separate major groups with more space. Avoid identical cards, identical gaps, and identical visual weight across the whole screen.

Use color sparingly. Keep the majority of the interface structurally neutral and reserve accent color for action, status, or identity. Prefer whitespace and tonal shifts over visible dividers.

## Components and accessibility

Follow this control priority:

1. Native semantic HTML when it can express the interaction correctly.
2. Existing project components and design-system primitives.
3. Battle-tested accessible headless primitives for stateful controls.
4. Custom behavior only when no suitable primitive exists.

Never recreate buttons, links, inputs, dialogs, menus, tabs, selects, comboboxes, popovers, or tooltips with non-semantic elements when appropriate primitives already exist.

When custom behavior is unavoidable, implement the full keyboard, focus, ARIA, escape, click-outside, and overlay behavior contract.

Use the project's existing styling system. Extract repeated styling into reusable components or variants. Bind interface styling to semantic tokens rather than arbitrary literals.

## Design-system rules

Use `references/system.md` when establishing or evolving the design system.

Always preserve:

- semantic color tokens for foreground, background, border, brand, and statuses
- four text hierarchy levels: primary, secondary, tertiary, muted
- a spacing grid based on 4px or 8px
- one depth strategy across the product
- a consistent radius scale
- dedicated control tokens for interactive fields
- dark-mode behavior derived from the same hierarchy rather than an unrelated theme

If `.interface-design/system.md` already exists, treat it as the current design contract unless the user explicitly asks to redesign it.

## States and polish

Every interactive element must account for default, hover, active, focus, and disabled states. Data-bearing areas must account for loading, empty, error, and populated states when applicable.

Maintain adequate hit areas, optical alignment, balanced text wrapping, concentric radius relationships, and stable numeric layout.

Use motion only when it improves feedback or spatial understanding. Prefer fast enter transitions, exact animated properties, transform and opacity, origin-aware popovers, and reduced-motion support. Avoid `transition: all` and avoid animating layout properties unless necessary.

## Review modes

When the user asks for an audit, review, critique, design review, UI quality check, or consistency check, run the full review in `references/review.md`.

When the user asks to clean up generic AI UI, remove visual slop, polish a branch, or make the interface feel less generated, run the anti-slop pass in `references/deslop.md`.

When the user asks for design status, system extraction, or drift analysis, inspect `.interface-design/system.md` plus the current UI and report mismatches, repeated ad hoc values, missing tokens, and reusable patterns.

## Communication

Keep design reasoning concise and actionable. Do not narrate hidden internal process. Surface the recommendation, the critical decisions, the highest-impact issues, and concrete fixes.

For ambiguous direction that would be costly to reverse, propose a clear direction and ask for confirmation. If the user has provided enough context or explicitly asks for autonomous execution, proceed using a responsible assumption and state it briefly.

## Saving design memory

When reusable patterns are established, offer to save them to `.interface-design/system.md` using the structure in `references/system.md`.

Save only durable decisions such as:

- direction and product feel
- palette and semantic tokens
- depth strategy
- spacing base and density
- typography hierarchy
- focal patterns
- reusable component measurements and variants
- selected visual references that materially shaped the system

Do not save one-off nudges or temporary experiment values.
