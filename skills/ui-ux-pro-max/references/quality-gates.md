# UI Quality Gates

Use this reference for audits and final verification. Apply only checks relevant to the product and platform.

## Priority 1: Accessibility and semantics

### Text and non-text contrast

- Normal body text: target at least 4.5:1.
- Large text may use the applicable lower threshold, but do not classify ordinary UI labels as large text merely to pass.
- Meaningful icons, focus boundaries, and graphical controls: target at least 3:1 against adjacent colors where the criterion applies.
- Test light and dark themes independently.
- Do not use disabled-state low contrast as a substitute for disabled semantics.

### Focus and keyboard

- Keep visible focus indication.
- Ensure tab order follows the logical and visual order.
- Ensure sticky headers, chat launchers, cookie banners, drawers, and overlays do not obscure the focused control.
- Trap focus only inside true modal contexts and restore focus to a sensible trigger when the modal closes.
- Support Escape or an obvious equivalent where dismissal is expected.

### Icons and images

- Hide decorative icons from the accessibility tree.
- Give meaningful non-text content an appropriate text alternative.
- Give icon-only controls accessible names.
- Expose selected, pressed, expanded, invalid, busy, and disabled state programmatically where applicable.
- Use a consistent vector icon family. Do not use emoji as structural controls.

### Color and state

Never use color as the sole carrier for error, warning, success, selection, chart category, or status. Add text, iconography, shape, pattern, or position.

### Authentication

- Permit paste and password managers.
- Provide accessible recovery.
- Avoid cognitive puzzles as the only authentication path.
- Make password requirements available before failure.

## Priority 2: Interaction

### Targets

Use comfortable click and touch targets. For native mobile, follow platform target guidance and enlarge hit areas around small visual icons. On web, avoid small isolated glyph targets and tightly packed destructive actions.

### Feedback

- Acknowledge taps and clicks quickly.
- Distinguish hover, focus, pressed, selected, disabled, loading, success, and error where relevant.
- Prevent accidental duplicate submissions without trapping users in a permanently disabled state after failure.
- Preserve user input after validation or network errors.

### Gestures

- Do not make essential tasks hover-only, swipe-only, or drag-only.
- Provide visible and keyboard-operable alternatives.
- Avoid nested gesture regions that conflict with scroll or system navigation.

### Destructive actions

- Prefer undo when feasible.
- For irreversible actions, state the target and consequence explicitly.
- Do not use vague confirmation copy.

## Priority 3: Responsive and content resilience

### Reflow

- No essential content should require horizontal page scrolling at narrow widths.
- Do not disable browser zoom.
- Keep responsive reading order aligned with DOM or semantic order.
- Let text-bearing controls grow vertically when labels wrap.
- Avoid fixed component heights that clip localized or enlarged text.

### Long text

- Prefer wrapping to truncation.
- Use safe long-token wrapping for URLs, IDs, filenames, and user content.
- If truncation is unavoidable, provide full content through an operable disclosure, tooltip, detail view, or equivalent accessible mechanism.
- Chips and badges should remain semantically whole when practical. Collections may wrap or use an operable `+n` disclosure.

### Localization

- Expect string expansion.
- Use locale-aware dates, times, numbers, currency, and pluralization.
- Support RTL where the product requires it.
- Do not place important text inside raster images.

## Priority 4: Layout and hierarchy

- The primary task is visually dominant.
- Related items are grouped by proximity and alignment.
- Spacing follows a small repeatable scale.
- Large desktop widths retain readable text measure rather than stretching paragraphs edge to edge.
- Sticky UI reserves space and does not cover scroll content.
- Z-index follows a documented layer scale.
- Modals, menus, popovers, tooltips, toasts, and drawers have a clear stacking relationship.

## Priority 5: Typography and color system

- Use semantic type roles and a limited scale.
- Body text is comfortably readable on the target device.
- Use line height appropriate to reading length.
- Keep line length reasonable for long-form content.
- Use tabular numerals for aligned numeric data.
- Use semantic color tokens rather than raw per-component hex values.
- Design light and dark token mappings separately.

## Priority 6: Forms

- Every field has a persistent accessible label.
- Placeholder text is supplementary, never the only label.
- Required and optional status is clear.
- Error text identifies the problem and recovery.
- Validation does not fire aggressively before the user has meaningfully interacted unless there is a clear reason.
- Multi-error submissions should provide an accessible summary linked to fields when appropriate.
- Preserve entered values after errors.
- Group related fields semantically.
- Use the correct input type, autocomplete tokens, keyboard type, and input mode.
- Do not split values such as credit card or one-time codes into inaccessible micro-fields without robust keyboard and paste behavior.

## Priority 7: Loading, empty, failure, and permission states

Design states intentionally:

- loading,
- partial loading,
- empty first use,
- empty after filtering,
- offline,
- permission denied,
- expired session,
- validation error,
- server error,
- rate limit,
- success,
- destructive pending state.

Do not use a spinner as the only answer to an operation that may take a long time. Preserve context and explain what the user can do next.

## Priority 8: Motion

- Motion communicates relationship, state, or emphasis.
- Prefer opacity and transform over layout-heavy animation when possible.
- Avoid animating every visible element.
- Do not delay primary task completion for decorative choreography.
- Respect reduced-motion preferences.
- Rapid repeated interaction must end in the correct semantic state even when prior animations are interrupted.

## Priority 9: Performance and perceived stability

- Reserve media dimensions to reduce layout shift.
- Optimize responsive images and noncritical media.
- Avoid loading unnecessary third-party scripts early.
- Split heavy feature code when it materially improves initial interaction.
- Virtualize large datasets only when useful, while preserving keyboard and screen-reader behavior.
- Keep input feedback immediate.
- Use skeletons only when they improve orientation; do not create fake precision about content shape.

## Priority 10: Charts and data

### Analytical fit

- Trend: line.
- Category comparison or ranking: bar.
- Distribution: histogram, box, or violin depending on audience.
- Relationship: scatter.
- Composition: stacked bar when both total and composition matter.
- Exact comparison: table.
- Geography: map only if place is analytically meaningful.
- Flow: Sankey only for a manageable number of meaningful flows.

### Chart quality

- State unit, period, denominator, and baseline.
- Avoid color-only series differentiation.
- Prefer direct labels when practical.
- Provide accessible summaries or tables for critical data.
- Do not use 3D perspective for quantitative comparison.
- Do not use pie charts with many small slices.
- Do not truncate axes or manipulate scale without explicit analytical justification.

## Priority 11: Native mobile specifics

Apply only to native or native-like mobile UI:

- Respect safe areas and system gesture regions.
- Test Dynamic Type or equivalent text scaling.
- Use platform navigation conventions.
- Use platform-appropriate touch targets.
- Do not assume web hover states exist.
- Avoid copying desktop menu density into mobile.
- Test portrait and landscape when supported.

## Priority 12: Distinctiveness and anti-slop

Reject visual choices that have no product rationale. Typical signals of generic generated UI:

- purple-pink gradient identity by default,
- excessive rounded cards,
- identical feature grids,
- decorative sparkles everywhere,
- giant vague headline and no product evidence,
- arbitrary glass surfaces,
- placeholder stock icons and emoji,
- too many simultaneous accent colors,
- every section centered,
- excessive entrance animation,
- fake metrics or fake customer logos,
- invented branding.

Replace decoration with product-specific hierarchy, real content, authentic evidence, task-aware density, and a coherent visual idea.

## Completion checklist

Before claiming completion, confirm:

1. Primary task and hierarchy are clear.
2. Semantic HTML or native semantics are preserved.
3. Focus and keyboard paths work.
4. Relevant contrast thresholds are met.
5. Responsive reflow and long text do not break essential UI.
6. Relevant loading, empty, error, disabled, success, and destructive states exist.
7. Motion is reduced-motion safe.
8. Tokens are consistent.
9. Charts are analytically appropriate when present.
10. No unrelated branding or generic AI visual clichés were introduced.
