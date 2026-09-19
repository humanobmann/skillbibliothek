# Baseline UI

Use for fast UI cleanup and implementation polish.

## Stack and primitives

- Prefer existing project components and primitives first.
- For keyboard or focus-bearing interactions, use established accessible primitives such as Base UI, React Aria, or Radix rather than hand-rolled behavior.
- Do not mix primitive systems within one interaction surface unless the existing product already requires it.
- In Tailwind projects, prefer the existing theme and default scales before arbitrary custom values.
- Use the project's class composition utility. In common Tailwind React stacks this is typically a `cn` helper backed by `clsx` and `tailwind-merge`.

## Interaction

- Use a confirmation dialog for destructive or irreversible actions.
- Use structural skeletons when loading preserves predictable layout.
- Prefer dynamic viewport units for full-height mobile layouts.
- Respect safe-area insets for fixed controls.
- Place errors close to the action or field that caused them.
- Never block paste in text fields.
- Give empty states one obvious next action.

## Typography and data

- Improve heading wrapping and paragraph readability with the project's supported text-wrap utilities.
- Use tabular numerals for aligned numeric data.
- Use truncation or line clamping deliberately in dense interfaces.
- Avoid arbitrary letter spacing unless the design system explicitly uses it.

## Layout

- Use a documented z-index scale instead of arbitrary stacking values.
- Prefer a single size utility for square elements when the framework supports it.
- Keep accent color use restrained within a view.
- Prefer existing theme tokens, shadows, radii, spacing, and colors.

## Visual restraint

Do not introduce gradients, glow-heavy affordances, novel shadows, or extra visual effects merely to make the interface look more designed. Preserve the product's visual language unless redesign is requested.

## React hygiene

Avoid effects for values that can be derived during render. Do not add persistent `will-change` hints outside active animation needs.
