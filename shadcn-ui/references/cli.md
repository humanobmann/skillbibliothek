# CLI Reference

Use the package runner declared by the project.

## Project inspection

```bash
npx shadcn@latest info --json
```

Use the returned values for aliases, RSC mode, Tailwind version, Tailwind CSS file, style, base primitive library, icon library, resolved paths, framework, package manager, installed components, and preset metadata.

## Documentation and discovery

```bash
npx shadcn@latest docs button dialog select
npx shadcn@latest search @shadcn -q "sidebar"
npx shadcn@latest view @shadcn/button
```

Do not guess component APIs when these commands can resolve them.

## Add components

```bash
npx shadcn@latest add button card dialog
```

Before adding, verify whether the component is already installed.

## Safe updates

```bash
npx shadcn@latest add button --dry-run
npx shadcn@latest add button --diff button.tsx
```

Merge upstream changes into local customizations. Use `--overwrite` only with explicit approval.

## New projects

Typical current patterns:

```bash
npx shadcn@latest init --name my-app --preset base-nova
npx shadcn@latest init --name my-app --preset base-nova --template vite
npx shadcn@latest init --name my-app --preset base-nova --template next --monorepo
```

Available templates and presets may change. Verify with the current CLI before presenting a fixed list as exhaustive.

## Existing projects

```bash
npx shadcn@latest init --preset base-nova
```

Inspect current Tailwind, aliases, globals, and local UI files first.

## Preset switching

Preserve local changes by default. Use one of:

1. Reinstall: preset init with reinstall semantics, replacing components.
2. Merge: preset init without component reinstall, then inspect each installed component with dry-run and diff.
3. Skip: update configuration and CSS only.

Never decode preset codes manually.
