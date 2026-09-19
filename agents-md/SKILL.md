---
name: agents-md
description: Create, review, or maintain concise AGENTS.md project instruction files for Codex and other coding agents. Use when onboarding an agent to a repository, standardizing commands and project conventions, documenting repository boundaries, consolidating duplicated agent instructions, or updating AGENTS.md after architecture, tooling, testing, security, or deployment changes.
---

# AGENTS.md Maintenance

Create the smallest useful repository instruction file.

## Inspect first

Before writing, inspect the repository for:

- package manager and build configuration
- exact test, lint, typecheck and development commands
- source and test layout
- README, CONTRIBUTING, architecture and security documentation
- generated files and files agents must not edit manually
- CI, deployment and migration surfaces
- existing AGENTS.md or other agent instruction files

Never copy secrets or values from real environment files.

## Scope

Use a root AGENTS.md for repository-wide rules. Add nested AGENTS.md only when a subtree genuinely needs different commands or constraints.

Prefer references to existing project documentation over duplicating long explanations.

## Recommended sections

Include only sections backed by repository evidence:

- Purpose and boundaries
- Package manager
- Commands
- Repository structure
- Testing
- Security and secret handling
- Generated files
- Deployment or migration constraints
- External reference files

## Writing rules

- Keep instructions concise and actionable.
- Use exact repository-relative paths.
- Use exact commands verified from project files.
- Keep one rule per bullet.
- Avoid generic advice already enforced by tooling.
- Do not list installed skills or plugins.
- Preserve curated project-specific rules unless repository evidence shows they are stale.

## Verification

Before completion confirm:

- every referenced path exists
- every command comes from repository configuration or verified documentation
- no secret values were copied
- no instruction conflicts with a closer scoped AGENTS.md
- the file is materially shorter than the documentation it references
