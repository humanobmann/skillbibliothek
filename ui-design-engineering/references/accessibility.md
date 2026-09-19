# Accessibility

Apply minimal, targeted fixes. Prefer native HTML before ARIA.

## Priority 1: accessible names

- Every interactive control needs an accessible name.
- Icon-only controls need `aria-label` or an equivalent accessible naming mechanism.
- Inputs, selects, and textareas need labels.
- Link text must describe its destination or action.
- Decorative icons should be hidden from assistive technology.

## Priority 2: keyboard access

- Prefer native buttons and links over clickable `div` or `span` elements.
- All interactive controls must be keyboard reachable.
- Focus must remain visibly discernible.
- Avoid positive `tabindex` values.
- Dialogs and overlays should support Escape where expected.

## Priority 3: focus and dialogs

- Keep focus within a modal while it is open.
- Move initial focus to an appropriate control or content target.
- Restore focus to the trigger after close.
- Avoid unexpected page scrolling when opening overlays.

## Semantics

- Use native semantic elements where possible.
- When assigning ARIA roles, provide required states and properties.
- Use real list, heading, and table structures.
- Keep heading hierarchy coherent.

## Forms and errors

- Associate helper and error text with fields.
- Mark invalid fields programmatically.
- Ensure required state is conveyed accessibly.
- Explain why an action is unavailable rather than relying on a disabled button alone.
- Do not rely only on toasts for critical errors.

## Dynamic state

- Announce important validation or loading changes when needed.
- Expandable controls should expose expansion state and controlled region.
- Disabled and selected states must not depend on color alone.

## Media and motion

- Use meaningful alt text for informative images and empty alt text for decorative images.
- Provide captions when spoken video content requires them.
- Respect reduced-motion preferences for nonessential motion.
- Avoid autoplaying audio.

## Boundary

Do not add redundant ARIA where native semantics already solve the problem. Do not migrate component libraries only to fix accessibility unless requested.
