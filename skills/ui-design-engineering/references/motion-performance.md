# Motion Performance

Use for jank, animation architecture, scroll-linked effects, layout transitions, filters, and performance-sensitive motion.

## Rendering cost model

Prefer compositor-friendly animation such as transforms and opacity. Treat paint-heavy effects as more expensive and continuous layout animation as highest risk.

## Critical rules

- Do not interleave layout reads and writes repeatedly in one frame.
- Avoid continuous animation of layout properties on large or important surfaces.
- Do not drive animation from raw scroll events or constant scroll-position polling when a browser timeline or observer can express the behavior.
- Every animation loop needs a stop condition.
- Do not combine multiple animation systems that independently measure and mutate the same layout.

## Mechanism selection

- Default to transform and opacity.
- Use JavaScript-driven motion only when the interaction requires it.
- Keep paint or layout animation limited to small isolated surfaces and short effects.
- Prefer a cheaper technique over removing meaningful motion outright.

## Measurement

- Measure once, then animate using compositor properties when possible.
- Batch DOM reads before writes.
- Avoid repeated geometry reads during active animation.
- Use FLIP-style techniques for layout-like transitions when appropriate.

## Scroll

- Prefer CSS Scroll or View Timelines when suitable and supported by the target environment.
- Use IntersectionObserver for visibility-driven activation, pausing, and cleanup.
- Pause or stop off-screen animations.
- Avoid scroll-linked effects that continuously repaint or relayout large surfaces.

## Layers and filters

- Do not assume transforms are automatically cheap. Layer count and surface size matter.
- Use `will-change` briefly and only where justified.
- Avoid many large promoted layers.
- Keep blur small, short, and local. Never continuously animate large blur surfaces.

## Library boundary

Do not migrate animation libraries unless the user asks. Fix performance inside the existing animation system first.
