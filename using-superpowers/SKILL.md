---
name: using-superpowers
description: Route complex software-development work to the smallest relevant Superpowers workflow. Use when Superpowers is explicitly requested or when a multi-step implementation, difficult defect, test-first change, code review, or release gate materially benefits from its disciplined development process. Do not use for ordinary questions, research, writing, design-only work, connector actions, simple edits, or non-development tasks.
---

# Using Superpowers

Use Superpowers as a focused software-development workflow, not as a mandatory layer for every conversation.

## Select the smallest relevant workflow

* unclear or high-impact feature: `brainstorming`, then `writing-plans` when a written implementation plan is needed
* reproducible bug or failing test: `systematic-debugging`
* authorized feature or bug implementation: `test-driven-development`
* review requested or received: `requesting-code-review` or `receiving-code-review`
* completion claim, merge, or release: `verification-before-completion`, followed by the relevant branch or release workflow

Do not load unrelated Superpowers skills. A clear, low-risk change does not require brainstorming solely because code is involved.

## Environment boundaries

Use the current host's supported skill and workspace tools. Do not require Claude-specific tool names or claim that a tool was used without evidence. Follow repository instructions and preserve unrelated work.

Do not create subagents, worktrees, commits, pull requests, pushes, releases, or external changes unless the user has authorized that scope and the current environment permits it.

## Verification

Before claiming success, run the narrowest relevant checks available for the changed code. Report what was executed, what passed, and what could not be verified.
