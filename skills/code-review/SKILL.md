---
name: code-review
description: Review a code diff or bounded file scope for correctness, security, maintainability, and test regressions, reporting actionable findings before praise.
metadata:
  canonical: true
  profile: engineering
  provenance: target-authored
---

# Code review

## Purpose and activation

Use for a concrete diff, pull request, or explicitly bounded set of files. Do not
pretend to have reviewed files that were not provided or inspected.

## Inputs

- diff or file paths and repository instructions;
- intended behavior and risk constraints;
- available tests and build/lint commands.

## Procedure

1. Read applicable instructions and establish the review boundary.
2. Inspect the diff and relevant call sites, data flows, and error paths.
3. Prioritize exploitable correctness, security, data-loss, and regression risks.
4. Check tests, validation, API compatibility, and observability.
5. Report findings with severity, file/line, impact, evidence, and a minimal fix;
   distinguish verified findings from questions and residual risk.

## Hard rules

- Never claim tests or tools ran unless their output was observed.
- Never expose secrets encountered during review.
- Do not rewrite code unless the user asks for implementation.
- If the boundary is insufficient, state exactly what is missing.

## Output

Return findings first (highest severity first), then assumptions, tested commands,
and a concise residual-risk summary.
