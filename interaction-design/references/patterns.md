# Interaction Design Patterns

## Contents

1. Component feedback
2. Loading states
3. Forms and validation
4. Notifications
5. Modals and overlays
6. Drag and drop
7. Gesture interactions
8. Page and layout transitions
9. Reduced motion
10. Common anti patterns

## Component feedback

Use immediate visual response for press, selection, expansion, toggling, or mode changes. Keep hover optional because touch devices do not have it. Focus visible is mandatory for keyboard use and must not be removed just because a custom hover style exists.

## Loading states

Use skeletons when the final structure is predictable and content loading would otherwise cause layout jumps. Use spinners for local indeterminate operations. Use progress bars only when progress is real or can be estimated honestly.

Avoid showing a spinner for work that normally completes too fast to perceive. A delayed loader can prevent flicker when operations usually complete within a few hundred milliseconds.

## Forms and validation

Validate at the point where feedback helps the user correct an issue. Avoid aggressive error messages while the user is still typing unless the rule can be evaluated without creating noise. Preserve entered values after recoverable failures.

When submitting:

* prevent duplicate submissions without making the whole screen inert
* show pending state on the submit control
* preserve context
* focus or announce the first meaningful error when submission fails

## Notifications

Use toasts for transient, low risk confirmation. Do not use a disappearing toast as the only place for critical information. Provide enough time to read, pause timers on hover or focus when practical, and avoid stacking large numbers of notifications.

## Modals and overlays

Use modals for focused tasks that truly require interruption. Trap focus only while the modal is active, restore focus when it closes, support Escape when safe, and make the close action easy to find.

Use a drawer or inline expansion when context preservation matters more than interruption.

## Drag and drop

Provide a visible drag handle when reordering is not obvious. Show drop targets and live position feedback. Support keyboard reordering for accessible applications. Avoid making precision dragging the only way to complete an important task.

## Gesture interactions

For swipe to dismiss or reveal actions, require a deliberate threshold and provide undo for destructive outcomes. Do not hide essential features behind undocumented gestures.

## Page and layout transitions

Use opacity and transform for lightweight transitions. Avoid animating every route change. Preserve orientation when navigating between related views, such as list to detail, tab to tab, or expanding cards into panels.

For high frequency product UI, prioritize speed and continuity over cinematic motion.

## Reduced motion

On the web, use `@media (prefers-reduced-motion: reduce)` to shorten or remove nonessential movement. Keep state feedback intact. A reduced motion alternative can use quick fades, immediate replacement, or nonmoving emphasis.

## Common anti patterns

* motion added without a communication purpose
* animations that block input
* long hover animations on frequently used controls
* loaders that replace stable content unnecessarily
* skeletons whose shape does not match final content
* success toasts for every trivial action
* error states that disappear before the user can act
* focus rings removed for visual cleanliness
* gesture only controls without alternatives
* animating layout properties at high frequency
* infinite decorative motion in task focused interfaces
* bounce or spring effects that conflict with product tone

## Source lineage

This skill was adapted from the public `interaction-design` skill in `wshobson/agents`, with the original implementation guidance generalized for ChatGPT workflows and cross framework use.
