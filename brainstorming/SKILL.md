---
name: brainstorming
description: Explore and structure larger, ambiguous, or high-impact product and feature ideas before implementation. Use when goals, scope, users, constraints, architecture, or success criteria are materially unclear, when several viable approaches need comparison, or when the user explicitly asks to brainstorm, ideate, or design a solution. Do not use for small, clearly specified changes, routine fixes, direct content creation, or implementation tasks whose requirements are already sufficient.
---

# Brainstorming

## Purpose

Turn an unclear or consequential idea into a practical direction without slowing down straightforward work.

## Activation boundary

Use this skill only when at least one of these conditions applies:

- The user explicitly asks to brainstorm, ideate, compare approaches, or design a solution.
- The request contains multiple plausible interpretations that would materially change the result.
- The work spans several components, teams, data flows, or external systems and needs scope control.
- A high-impact architectural or product decision should be evaluated before implementation.

Do not use this skill for:

- small or clearly specified code, configuration, content, or design changes
- routine bug fixes with a sufficiently clear expected result
- direct document, image, presentation, spreadsheet, or website creation
- review-only requests
- implementation tasks with enough information to proceed safely

When the request is clear, proceed with the relevant implementation workflow. Do not force a separate design phase.

## Working method

1. Inspect relevant project context when available.
2. Summarize the goal, constraints, assumptions, and open decisions.
3. Ask at most one focused question at a time, and only when the answer would materially change the solution.
4. If the missing detail is not blocking or risky, state a reasonable assumption and continue.
5. Present two or three approaches only when genuinely distinct options exist. Lead with the recommendation and explain the trade-offs.
6. Produce a concise design or decision record scaled to the task.
7. If implementation was also requested and the design is sufficiently clear, continue under the applicable implementation workflow without requiring another approval round, unless the action is risky, externally visible, destructive, or requires a material user choice.

## Scope control

If the request combines several independent systems, identify the boundaries and propose a sensible sequence. Focus the first design on the smallest coherent outcome that delivers useful value.

For each proposed component, make clear:

- what it does
- what it depends on
- how it communicates with other components
- how failures are handled
- how success will be verified

Avoid unrelated refactoring or speculative features.

## Output

Use the smallest useful structure:

1. Goal and assumptions
2. Recommended approach
3. Alternatives and trade-offs, when relevant
4. Components or workflow
5. Risks and safeguards
6. Verification or success criteria
7. Next action

Do not create or commit a design file unless the user asks for a saved specification or the active project workflow explicitly requires one. When a file is requested, use the environment's document and persistent-storage workflow.

## Safety and autonomy

- Do not make external writes, send messages, publish content, or perform destructive actions without the authorization required by the host environment.
- Do not ask for confirmation merely because a task is creative.
- Do not require a local visual server or browser companion.
- Do not depend on a specific follow-up skill. Use the planning and implementation tools that are actually available in the environment.
