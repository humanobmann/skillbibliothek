# Evidence-based UI improvement audit

Use for read-only review of an existing product surface when the user wants findings and a handoff plan rather than direct code changes.

## Boundaries

- Do not modify product source during the audit.
- Keep generated plans in a dedicated planning location if the workspace uses one.
- Do not install dependencies, format unrelated files, commit, push, or mutate the working tree.
- Use rendered evidence only when available or explicitly requested.
- Make plans self-contained for another implementation agent.

## Select one coherent surface

Honor the user's scope. For broad requests, choose one deployable application and one coherent surface family tied to a primary user task.

Trace routes and layouts through shared components, variants, resolved tokens, and styles. Repository proximity and naming similarity do not prove shared ownership.

## Reconstruct the local system

Check current design documentation, tokens, themes, shared primitives, variants, and compositions that actually reach the selected surface. Treat drafts and migrations as future intent unless explicitly accepted.

Record:

- audited surface
- governing design sources
- documented decisions
- governing owners and consumers
- explicit exceptions

## Proof gate

Keep a candidate finding only when all three are true:

1. Contract: a binding design rule or direct contradiction establishes the expected presentation.
2. Runtime: the cited source, token, component, or behavior actually reaches the affected surface.
3. Correction: the evidence determines one concrete correction without inventing product intent.

Search results and repetition create candidates, not findings.

Reject findings whose primary correction is functional behavior, architecture, metadata, performance, accessibility, or code quality unless the user explicitly included that dimension.

## Falsification pass

Re-open evidence for every finding and try to disprove it. Delete findings when the rule does not govern the surface, counterevidence supports the difference, multiple corrections remain plausible, or another finding already captures the same root issue.

## Reporting

Return at most three findings ordered by confidence, user impact, reach, and correction cost.

Use columns for problem, evidence, proposed change, scope, and confidence. Under an `Improve first` section, select only the highest leverage surviving finding.

If no candidate survives, say that no supported finding was found rather than fabricating recommendations.

## Planning selected changes

For a selected finding, produce one self-contained plan per root change. Include current evidence, exact reusable primitives or tokens, affected surfaces, implementation steps, validation steps, and any documentation update needed.
