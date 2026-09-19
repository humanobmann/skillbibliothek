# Debugging Workflow

## 1. Confirm project context

Read `components.json` and run shadcn `info --json`. Record framework, package manager, aliases, base primitive library, icon library, Tailwind version, global CSS path, and installed components.

## 2. Classify the failure

Choose the primary category:

- import or alias failure
- missing component file
- missing dependency
- Tailwind not generating styles
- theme or CSS variable failure
- Radix versus Base UI API mismatch
- server versus client boundary failure
- hydration mismatch
- overlay or portal failure
- form accessibility or validation issue
- registry resolution or registry item issue
- runtime state bug

## 3. Inspect generated and local files

Read the actual files involved. Do not assume the current upstream shadcn version matches local generated code.

## 4. Verify upstream usage

Use `shadcn docs` for installed components or `shadcn view` for registry items. For update-related problems, compare with `--dry-run` and `--diff`.

## 5. Apply the smallest coherent fix

Preserve local styles and behavior unless they are the source of the defect. Do not reset components wholesale as a first-line fix.

## 6. Verify

Run typecheck, lint, tests, and build as appropriate. Reproduce the original interaction in a browser when possible.

## Common patterns

### Import alias error

Compare imports against `aliases` and `resolvedPaths` from project info. Third-party registry components commonly hard-code `@/components/ui/...`.

### Unstyled component

Check Tailwind version, global CSS import, token definitions, content/source scanning, and whether the component's required CSS variables were installed.

### Hydration mismatch

Look for browser-only state, timestamps, random values, theme-dependent rendering, invalid HTML nesting, or client/server branches that produce different markup.

### Dialog or popover appears behind content

First check whether custom app styles introduced stacking contexts. Avoid blindly raising overlay z-index.

### Component prop does not exist

Confirm whether the project uses Base UI or Radix and inspect current docs. Do not transfer API assumptions between the two primitive bases.
