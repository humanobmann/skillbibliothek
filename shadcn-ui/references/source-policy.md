# Upstream Verification Policy

shadcn/ui evolves quickly. Treat remembered command flags, component APIs, presets, templates, registry behavior, and primitive-specific props as potentially stale.

When network or repository access is available, prefer these sources in order:

1. Current shadcn CLI output and `shadcn docs`.
2. Official ui.shadcn.com documentation.
3. Official `shadcn-ui/ui` GitHub repository.
4. Registry-provided documentation for third-party items.

For code updates, prefer CLI diff workflows over manually copying raw upstream files.

When citing or documenting upstream behavior, record the date or commit when practical for workflows that need reproducibility.

Do not claim that a list of templates, presets, components, or registry capabilities is exhaustive unless verified against the current release.
