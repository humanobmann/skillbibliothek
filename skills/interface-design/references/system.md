# Design system memory

Use this reference when creating, reading, or updating `.interface-design/system.md`.

## Recommended structure

```markdown
# Interface Design System

## Direction
Personality: [specific product feel]
Primary user: [actual person or role]
Primary task: [dominant verb]
Signature: [product-specific visual or interaction pattern]

## Foundations
Depth: [borders-only | subtle-shadows | layered-shadows | surface-shifts]
Spacing base: [4px | 8px]
Density: [compact | balanced | spacious] with concrete component padding values
Radius scale: [small / medium / large values]

## Typography
Typeface: [family]
Base size: [px]
Scale ratio: [e.g. 1.2 / 1.25 / 1.333]
Primary text: [weight / opacity]
Secondary text: [weight / opacity]
Tertiary text: [weight / opacity]
Muted text: [weight / opacity]
Numeric treatment: tabular numerals where applicable

## Color tokens
Canvas: [token/value]
Surface 1: [token/value]
Surface 2: [token/value]
Foreground: [token/value]
Secondary foreground: [token/value]
Border: [token/value]
Accent: [token/value]
Success: [token/value]
Warning: [token/value]
Destructive: [token/value]
Focus: [token/value]

## Control tokens
Input background: [token/value]
Input border: [token/value]
Input focus: [token/value]
Disabled: [token/value]

## Reusable patterns
### [Pattern name]
Purpose: [why it exists]
Measurements: [height, padding, gap, radius, type]
States: [hover/focus/active/disabled/loading/etc.]
Usage: [where to use]

## Visual references
[Only references that materially influenced the design]
```

## Update rules

Preserve existing decisions unless the current task intentionally changes the system.

Record reusable patterns when they appear more than once, have stable measurements, or materially define the product identity.

Prefer semantic token names tied to the product's language rather than generic numbered grays when the project supports meaningful naming.

When the implementation disagrees with the system file, identify whether the code drifted or the system evolved. Resolve the mismatch explicitly rather than silently normalizing both.
