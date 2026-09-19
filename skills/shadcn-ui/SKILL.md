---
name: shadcn-ui
description: Build, redesign, review, debug, maintain, and extend production React or Next.js interfaces with shadcn/ui. Use for shadcn components, components.json, registry items, presets, shadcn CLI commands, Tailwind theming, Radix or Base UI primitives, dashboards, forms, landing pages, design systems, accessibility, responsive behavior, component updates, third-party registries, Figma-to-code, GitHub code changes, or requests to modernize an existing shadcn application.
---

# shadcn/ui

Use shadcn/ui as an open-code component system and distribution platform, not as a black-box component library. Inspect the project before changing it, prefer existing components over custom markup, and preserve the project's aliases, primitive base, icon library, Tailwind version, framework, package manager, and local modifications.

## Operating workflow

1. Inspect the project before proposing code.
   - Read `components.json` when present.
   - Run the shadcn CLI `info --json` when command execution is available.
   - Determine framework, router, package manager, aliases, RSC status, Tailwind version, CSS entry file, visual style, primitive base, icon library, installed components, and resolved paths.
   - If no shadcn project exists, decide whether to initialize an existing app or create a new app.

2. Establish design intent.
   - For small fixes, preserve the current design language.
   - For redesigns or new product UI, define hierarchy, density, interaction model, responsive behavior, accessibility requirements, and component composition before implementation.
   - Prefer production-quality composition over demo-like layouts.

3. Discover before inventing.
   - Search installed and available shadcn components first.
   - Search the requested registry explicitly when the registry is known.
   - Use registry blocks and existing primitives before creating custom equivalents.
   - Do not guess a third-party registry when the user did not identify one.

4. Verify component APIs before implementation.
   - Use `shadcn docs <component>` when available.
   - Use `shadcn view` for registry items.
   - Do not rely on stale remembered APIs when current CLI or docs can resolve them.

5. Implement with project-native conventions.
   - Use the project's package runner.
   - Use the project's actual aliases and icon library.
   - Respect React Server Component boundaries.
   - Reuse semantic design tokens and component variants.
   - Keep custom CSS targeted and minimal.

6. Review the result.
   - Check component composition, responsive behavior, keyboard operation, focus states, labels, validation, loading, empty, error, disabled, destructive, and success states.
   - Check for unnecessary client components, hydration risks, excessive bundle cost, layout shift, and duplicated primitives.
   - Read all files added from third-party registries and fix hard-coded aliases or incompatible icon imports.

7. Verify before completion.
   - Run typecheck, lint, relevant tests, and production build when available.
   - For UI work, inspect the rendered interface at mobile and desktop widths when a browser or screenshot workflow is available.
   - Report unresolved limitations instead of claiming success without evidence.

## CLI rules

Use the package runner from the project. Typical forms are:

```bash
npx shadcn@latest ...
pnpm dlx shadcn@latest ...
bunx --bun shadcn@latest ...
```

Never manually decode preset codes. Pass them directly to the CLI.

Before adding components, check whether they are already installed. For upstream updates with local changes, use `--dry-run` and `--diff` first. Never use `--overwrite` unless the user explicitly approves replacing local changes.

For registry authoring, use the CLI build and validation workflow. See `references/registry.md`.

## Component and styling rules

Apply the complete rules in `references/component-rules.md` whenever writing or reviewing shadcn code.

Core requirements:

- Prefer shadcn components over custom styled HTML when an equivalent exists.
- Compose existing primitives instead of creating parallel abstractions.
- Use semantic tokens such as `bg-background`, `text-foreground`, `text-muted-foreground`, `border-border`, `bg-primary`.
- Use `gap-*` for spacing instead of `space-x-*` or `space-y-*`.
- Use `size-*` when width and height are equal.
- Use `cn()` for conditional class composition.
- Keep `className` focused on layout and supported customization rather than fighting component styles.
- Do not add manual overlay z-index unless a verified project-specific issue requires it.
- Respect the project's Base UI versus Radix APIs.
- Use the project's configured icon library instead of assuming Lucide.

## Forms

Use shadcn form composition rather than ad hoc layout.

- Use `FieldGroup` and `Field` for field structure.
- Use `FieldSet` and `FieldLegend` for related option groups.
- Use `InputGroup` with its own input or textarea subcomponents.
- Use `ToggleGroup` for small mutually related option sets where appropriate.
- Put `data-invalid` on the field wrapper and `aria-invalid` on the control.
- Connect labels, descriptions, and error messages programmatically.
- Preserve keyboard access and visible focus.

## Overlays and interactive components

- `Dialog`, `Sheet`, and `Drawer` require an accessible title.
- `TabsTrigger` belongs inside `TabsList`.
- Menu and select items belong inside their corresponding groups.
- `Avatar` requires a fallback.
- Use `AlertDialog` for destructive confirmations rather than a generic dialog.
- Use `sonner` for toast feedback unless the project deliberately uses another system.
- Use `Skeleton` for loading placeholders and `Empty` for empty states when available.

## React and Next.js

When the task touches React or Next.js architecture or performance, apply the installed React best-practices skill in addition to this skill.

- Keep client boundaries as narrow as practical.
- Do not add `"use client"` unless the component needs client-only state, effects, event handlers, or browser APIs.
- Prefer server-side data access in Next.js where appropriate.
- Avoid duplicating fetched data or state unnecessarily.
- Lazy-load expensive client-only features when beneficial.
- Preserve framework routing, metadata, and rendering conventions.

See `references/react-next.md` for project-specific checks.

## Design and UX quality

For substantial UI design, redesign, or visual polish, compose this skill with the available UI/UX design skills. This skill owns shadcn correctness; the design skill owns visual direction and product UX.

Apply these standards directly even when no companion skill is available:

- Establish a clear visual hierarchy and primary action.
- Avoid generic card grids when another information architecture is more appropriate.
- Use intentional spacing, typography, density, and alignment.
- Design all states, not only the happy path.
- Make mobile behavior explicit rather than relying on accidental wrapping.
- Use responsive navigation patterns appropriate to the content volume.
- Maintain accessible contrast and target sizes.
- Prefer progressive disclosure over overcrowded interfaces.

## Figma integration

When Figma is connected and the user wants Figma-to-code or code-to-design work:

- Inspect the relevant Figma frame, component, variables, spacing, typography, and states before coding.
- Map Figma tokens to semantic project tokens instead of hard-coding visual values repeatedly.
- Reuse existing shadcn primitives whenever they match the design intent.
- Record any deliberate deviations where Figma and the codebase use different abstractions.
- Preserve responsive behavior that may not be visible in a single static frame.

Do not claim pixel parity unless the rendered result was compared against the source design.

## GitHub integration

When GitHub is connected and the user asks to inspect or change a repository:

- Read the current branch and relevant files before editing.
- Check repository instructions and existing conventions.
- Keep changes scoped to the requested UI unless broader refactoring is necessary and justified.
- Review diffs for generated registry files, aliases, dependencies, and lockfile changes.
- Do not overwrite local customizations from upstream shadcn updates without explicit approval.
- Verify CI-relevant commands before claiming completion.

## Registry workflows

Use `references/registry.md` for creating, publishing, consuming, validating, or debugging registries and registry items.

Key rule: distinguish a source registry from its built distribution. Use the CLI to build and validate rather than assembling consumer JSON manually.

## Project creation and presets

For a new app, choose the template based on the user's stack and use the current CLI. For an existing app, initialize in place only after checking current Tailwind and alias conventions.

When switching presets in an existing project, explicitly choose one of these strategies:

- Reinstall: replace installed components with the preset versions.
- Merge: update configuration, then inspect component diffs and merge upstream changes into local customizations.
- Skip: update configuration and CSS without reinstalling components.

If the user has not specified the desired strategy and local changes exist, default to preserving local work and explain the chosen merge-safe approach.

## Debugging

Use the diagnostic sequence in `references/debugging.md` for broken imports, missing styles, hydration errors, primitive mismatches, Tailwind failures, theme issues, overlay problems, registry failures, dependency conflicts, or inaccessible interactions.

Do not fix symptoms before checking project context, actual generated files, and installed package versions.

## Output expectations

For implementation tasks, provide or apply production-ready code rather than pseudo-code unless the user asked for an outline. Keep changes cohesive and consistent with the existing project.

For review tasks, prioritize findings by severity and user impact. Distinguish confirmed defects from optional improvements.

For redesign tasks, explain the chosen structure briefly, then implement it. Avoid excessive design narration when working code is the primary deliverable.

## References

- `references/component-rules.md`: component composition, forms, icons, styling, accessibility, state rules.
- `references/cli.md`: project discovery, common CLI commands, update strategy, presets.
- `references/registry.md`: registry authoring, validation, addresses, distribution.
- `references/react-next.md`: React and Next.js integration and performance checks.
- `references/debugging.md`: deterministic troubleshooting flow.
- `references/source-policy.md`: upstream verification and freshness rules.
