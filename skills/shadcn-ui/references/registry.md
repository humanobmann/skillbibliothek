# Registry Workflows

## Mental model

A source registry is authored from a root `registry.json` and source files. A built registry is the generated consumer-facing JSON output served to CLI users. Do not confuse the two forms.

Registry items can distribute UI components, blocks, hooks, utilities, pages, design tokens, configuration, documentation, rules, workflows, templates, MCP files, and other project files.

## Build and validate

```bash
npx shadcn@latest build
npx shadcn@latest build registry.json --output public/r
npx shadcn@latest registry validate ./registry.json
```

Inspect the result using CLI commands such as:

```bash
npx shadcn@latest list @acme
npx shadcn@latest search @acme -q "login"
npx shadcn@latest view @acme/login-form
npx shadcn@latest add @acme/login-form --dry-run
```

## Public GitHub registries

Current shadcn tooling can consume supported public GitHub source registries directly. Prefer the CLI address format over manually fetching moving raw branch URLs.

When implementing or reasoning about registry fetching, resolve moving refs to a commit SHA before reading source files so every file is read from one consistent snapshot.

## Registry item review

After adding third-party items:

- Read every added source file relevant to the item.
- Fix hard-coded aliases that do not match project aliases.
- Replace unsupported icon-library assumptions.
- Verify registry dependencies and package dependencies.
- Check component grouping and accessibility rules.
- Confirm styles use the project's semantic tokens.
- Run typecheck and build.

## Authoring quality

- Keep item names stable and descriptive.
- Declare dependencies explicitly.
- Keep source paths deterministic.
- Avoid project-specific secrets or environment values.
- Include all files required for the item to function.
- Validate the root registry and test installation with `--dry-run` before publishing.
