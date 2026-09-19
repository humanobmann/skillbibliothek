# Anti-slop pass

Use this pass when the user asks to remove generic AI-generated UI traits or rapidly polish an existing interface.

## Detect

Look for:

- identical rounded cards repeated across every section
- sidebar plus topbar plus metric-card layouts that could belong to any SaaS app
- excessive use of gray borders
- default system or Inter typography without a deliberate reason
- arbitrary gradients or multiple accent colors
- overly large radii on small controls
- decorative icons with no information role
- repeated utility strings instead of components or variants
- inconsistent spacing such as 14px, 17px, 22px mixed without a grid
- generic placeholder copy, empty states, or stock illustrations
- missing hover, focus, disabled, loading, empty, and error states
- mismatched component heights
- inputs brighter than their surrounding surface in dark UI
- sidebars using a disconnected background color
- large dramatic shadows or mixed border/shadow elevation strategies
- full-width forms with no information hierarchy
- equally weighted headings, cards, and actions

## Replace

Prefer:

- one strong focal structure rather than many equal cards
- product-specific information groupings
- semantic tokens and a stable spacing grid
- one depth strategy
- quieter boundaries
- stronger type hierarchy through weight and opacity
- domain-derived palette decisions
- reusable variants for repeated components
- meaningful empty and error states
- compact controls where the product is operational and data-heavy
- more breathing room only where the task benefits from calm or reading

## Diff discipline

When working on an existing branch or codebase, make the smallest set of changes that materially improves craft. Preserve behavior, routing, data contracts, and established component APIs unless the task explicitly includes refactoring them.

Do not redesign unrelated screens merely because they are nearby in the codebase.

## Approval bar

The pass is complete only when the interface no longer reads as a default template, the main task has a clear visual lead, spacing and component values form a system, and interaction states are complete enough to feel intentional.
