# Responsive and Native Adaptation

## Responsive web

Treat breakpoints as layout decisions, not device labels.

At each meaningful width, verify:

* reading order
* navigation model
* primary action visibility
* content grouping
* touch target size
* text wrapping and truncation
* table or data density
* sticky and fixed regions
* modal and drawer behavior
* image cropping
* keyboard focus order

When a desktop pattern becomes awkward on a small screen, replace the pattern rather than compressing it indefinitely.

## Pointer and keyboard

Desktop web must remain usable without precision pointer input. Preserve visible focus and logical tab order. Hover may enrich a control but cannot be its only discoverability mechanism.

## Touch

Give primary touch targets sufficient size and separation. Avoid placing destructive actions beside frequent actions without spacing or confirmation. Do not require hover to reveal essential controls.

## Native iOS

Respect platform navigation, safe areas, dynamic type, system gestures, native control behavior, and accessibility settings. Custom styling should not obscure standard interaction expectations.

## Native Android

Respect system back behavior, insets, scalable text, touch target expectations, Material interaction conventions where appropriate, and accessibility settings. Avoid importing iOS-specific navigation assumptions.

## Adaptive products

If the same product spans web and native platforms, preserve product identity while allowing platform-specific navigation and control conventions. Consistency of task and language is more important than pixel identity.

## Motion adaptation

Reduce or remove nonessential spatial motion when the environment requests reduced motion. Ensure the interface still communicates state without the animation.

## Localization stress test

Test long labels, long names, decimal and date formats, right-to-left layout where relevant, and text expansion. Avoid fixed-height text containers that assume English length.
