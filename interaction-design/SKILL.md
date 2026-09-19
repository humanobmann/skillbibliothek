---
name: interaction-design
description: Design, review, and implement interaction behavior for digital interfaces, including microinteractions, motion, transitions, loading and empty states, feedback, gestures, drag and drop, hover and focus behavior, notifications, perceived performance, and reduced motion accessibility. Use when a user asks to improve interaction polish, define component states, specify animation timing, design feedback after actions, create loading or progress behavior, audit interaction quality, or implement interaction patterns in web or app UI.
---

# Interaction Design

Design interactions that communicate state, preserve orientation, confirm actions, and reduce user effort. Treat motion as functional feedback first and decoration second.

## Workflow

1. Identify the user action, system response, and success or failure condition.
2. Define all relevant states before adding motion.
3. Choose the lightest feedback mechanism that makes the state change obvious.
4. Set timing according to interaction scale and expected frequency.
5. Verify keyboard, focus, reduced motion, touch, and interruption behavior.
6. Check performance on realistic devices and avoid layout thrashing.
7. When implementing code, match the project's framework and existing design system instead of introducing a new animation library without need.

## State Model

For interactive components, consider these states where applicable:

* default
* hover
* focus visible
* pressed or active
* selected or checked
* loading or pending
* disabled
* success
* warning
* error
* empty
* skeleton or placeholder

Do not invent visual states that do not communicate a meaningful change. Keep focus visible independently of hover.

## Purposeful Motion

Use motion for one or more of these purposes:

* confirm that an action occurred
* explain where content came from or where it went
* direct attention to a meaningful change
* maintain spatial continuity
* reveal hierarchy or causality
* communicate progress or waiting

Remove motion that only adds delay, blocks input, repeats excessively, or competes with the user's task.

## Timing Guidance

Use these ranges as defaults, then adjust for distance, complexity, platform conventions, and frequency:

| Duration | Typical use |
| --- | --- |
| 100 to 150 ms | hover, press, tiny feedback |
| 180 to 300 ms | toggles, dropdowns, compact component transitions |
| 300 to 500 ms | modals, panels, larger layout or page transitions |
| above 500 ms | rare, choreographed, or explanatory motion only |

Prefer faster exits than entrances when that reduces perceived delay. Keep frequent interactions shorter than occasional ones.

## Easing

Use deceleration for entering elements, acceleration for exiting elements, and symmetric easing for movement between established positions. Springs can work for direct manipulation or playful UI, but avoid visible bounce in serious or high frequency workflows unless the product language already supports it.

## Loading and Progress

Choose feedback by expected wait:

* near instant: update immediately, usually without a spinner
* short wait: use subtle pending feedback or local spinner
* uncertain multi second wait: preserve layout with skeletons or show progress context
* determinate work: show actual progress when the backend can report it

Keep the previous content visible when possible. Avoid replacing an entire screen with a loader for a local update.

## Feedback Hierarchy

Match feedback to consequence:

* local control change: inline state change
* background action: unobtrusive status or toast
* validation problem: inline message near the field plus accessible summary when needed
* destructive or irreversible action: stronger confirmation and clear recovery path
* persistent failure: keep the error near the affected content and provide retry or next action

Never rely on color alone to communicate success or error.

## Gestures and Direct Manipulation

For swipe, drag, reorder, or touch gestures:

* provide a visible affordance or discoverable cue
* preserve keyboard and pointer alternatives where relevant
* use thresholds that prevent accidental activation
* show live feedback during manipulation
* make cancel and reversal possible when practical
* avoid hidden gestures for critical functionality

## Navigation and Transitions

Use transitions to preserve context, not to mask latency. Keep route or panel changes interruptible. Avoid long sequential animations that force the user to wait before interacting.

## Accessibility

Always respect `prefers-reduced-motion` on the web or the equivalent platform setting. Reduced motion should preserve meaning using opacity, instant state changes, or minimal transitions rather than simply removing all feedback.

Ensure:

* focus remains visible and logical
* animation does not trap focus
* content remains usable with motion disabled
* flashing or rapid repetitive motion is avoided
* gesture interactions have alternatives
* loading, success, and error states are exposed to assistive technology when appropriate

## Performance

Prefer transform and opacity for animated movement and fades. Avoid continuously animating layout properties such as width, height, top, or left when a transform can express the same change. Use `will-change` sparingly and clean up timers, listeners, observers, and animation controllers.

## Review Checklist

Before approving an interaction, verify:

1. The user can predict what the control will do.
2. The system acknowledges the action quickly.
3. The user can distinguish pending, success, and failure.
4. Motion explains change instead of creating delay.
5. The interaction works with keyboard, touch, pointer, and reduced motion where relevant.
6. Errors provide recovery rather than dead ends.
7. Repeated use does not become tiring or slow.
8. The implementation follows the existing product's component and motion conventions.

## Implementation Guidance

When code is requested, inspect the existing stack first. Use native CSS transitions or platform primitives for simple interactions. Use an animation library only when coordinated sequences, gesture physics, layout animation, or interruption handling materially benefit from it.

For framework specific patterns, practical examples, and anti patterns, read `references/patterns.md`.
