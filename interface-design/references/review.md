# Interface review

Run this checklist before presenting non-trivial UI work or when the user asks for a review.

## 1. Product fit

Check whether the design reflects the actual product domain rather than a generic SaaS template.

Pass only if:

- the primary user and task are obvious
- the signature is visible in at least several concrete elements
- the palette, typography, density, and proportions make sense for the domain
- replacing the product name would not make the design equally plausible for any unrelated app

## 2. Hierarchy

Check one clear focal point per view.

Confirm that size, weight, contrast, opacity, and whitespace form distinct information tiers. Squint or blur the interface mentally or visually. The hierarchy must remain readable while borders and decoration recede.

## 3. Composition

Reject monotonous card grids, equal spacing everywhere, arbitrary panel widths, and excessive visible separators.

Check that proportions communicate relationships between navigation, primary work area, secondary context, and controls.

## 4. Typography

Check for a deliberate type scale, coherent weights, meaningful opacity levels, readable line height, appropriate tracking, balanced wrapping, and tabular numerals where useful.

Flag default typography when the rest of the interface claims a distinctive direction but the type system does not support it.

## 5. Color and surfaces

Check one coherent hue family and one main accent unless the product genuinely requires more.

Reject decorative color without semantic or identity purpose. Reject harsh borders and dramatic elevation jumps.

Verify surface hierarchy for canvas, cards, menus, dialogs, and inputs.

## 6. Tokens and consistency

Compare code against the established design system.

Flag:

- arbitrary hex values
- repeated raw spacing values
- one-off radii
- duplicate long utility strings
- inconsistent component heights
- different depth strategies on adjacent components
- undocumented variants that should be reusable

## 7. Interaction states

Verify default, hover, active, focus, and disabled states for controls.

Verify loading, empty, error, and populated states for data surfaces.

Check keyboard access, focus visibility, semantic structure, ARIA requirements, and reduced-motion behavior.

## 8. Motion

Animation must be fast, purposeful, and restricted to properties that do not cause unnecessary layout work. Flag `transition: all`, sluggish easing, excessive entrance choreography, or animation on frequently repeated actions.

## 9. Responsive behavior

Check at least a representative desktop and mobile width for non-trivial interfaces.

Look for overlap, clipped controls, broken tables, unreadable density, hidden primary actions, awkward wrapping, and missing overflow strategies.

## 10. Final tests

Run four explicit tests:

1. Swap test: if the typeface, layout, or card treatment were replaced with a standard template, would the interface materially lose identity?
2. Squint test: does hierarchy remain obvious while details recede?
3. Signature test: can at least five concrete manifestations of the product signature be named?
4. Token test: do the design tokens form a coherent system rather than a collection of literals?

## Output format for audits

Return findings in priority order:

1. Critical usability or accessibility issues
2. High-impact hierarchy or product-fit issues
3. System consistency issues
4. Polish issues
5. Concrete recommended changes

Give exact component, token, spacing, typography, or state changes whenever possible.
