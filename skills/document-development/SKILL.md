---
name: document-development
description: Develop, restructure, review, and finalize substantial long-form documents from rough notes, outlines, transcripts, drafts, or briefings. Use for reports, specifications, policies, manuals, proposals, decision papers, project documentation, and other multi-section documents where content architecture and editorial development are central. Do not use for short messages, ordinary email, simple rewrites, or file-format conversion without substantive document work.
---

# Document Development

## Purpose

Use this skill to turn incomplete material into clear, structured, usable long-form documents. Focus on the document itself. Keep diagnosis, assumptions, and process notes brief unless the user explicitly asks for them.

## Operating Principles

- Preserve the user's intent and factual meaning unless explicitly asked to rewrite freely.
- Do not invent facts, citations, legal claims, technical claims, statistics, dates, names, or commitments.
- Mark uncertain or missing content as `TODO`, `needs verification`, or `assumption`.
- Prefer direct, useful prose over decorative language.
- Keep headings meaningful and paragraphs short.
- Make decisions, assumptions, risks, and open questions visible.
- If enough information is available, proceed with stated assumptions instead of blocking on clarifying questions.
- Ask only when a missing decision would materially change the document, create risk, or affect an external commitment.
- When the user asks for a finished file, hand the developed content to the active document or PDF artifact workflow and return the requested file rather than markdown alone.
- In Work Mode, save requested files through the persistent Library workflow unless the user specifies another destination or the files belong to an externally synced repository.

## Workflow Decision Tree

1. Determine the request type:
   - **New document from notes or briefing** -> use the creation workflow.
   - **Existing draft needs improvement** -> use the editing workflow.
   - **Document needs checking only** -> use the review workflow.
   - **Document needs final formatting or export preparation** -> use the finalization workflow.

2. Determine the document type:
   - report
   - technical specification
   - policy or procedure
   - manual or guide
   - proposal
   - decision paper
   - project documentation
   - knowledge-base article
   - other structured document

3. Consult references only when needed:
   - `references/document-types.md` for common structures.
   - `references/quality-checklist.md` for review criteria.
   - `references/style-rules.md` for prose standards.
   - Start from `assets/report-template.md`, `assets/specification-template.md`, or `assets/policy-template.md` only when that document type matches and the user has not supplied a binding template.

## Creation Workflow

For new documents, infer purpose, audience, assumptions, and structure internally. Return the completed document first. Include open questions or verification notes only when they remain material.

When source material is messy, first normalize it into:

- facts provided by the user
- inferred assumptions
- missing information
- decisions required
- risks or dependencies

Then draft the document.

## Editing Workflow

For existing drafts, provide the revised document first. Add a concise change summary and remaining verification needs only when useful.

When editing, preserve all important claims and constraints. Do not silently remove meaningful content. If content is cut, mention it in the change summary.

## Review Workflow

For review-only tasks, return:

1. **Overall assessment**
2. **Prioritized issues**
3. **Actionable fixes**
4. **Optional improved outline or sample rewrite**

Use severity labels when helpful:

- `critical`: blocks use or creates risk
- `major`: should be fixed before publication
- `minor`: improves clarity or polish

## Finalization Workflow

For final output preparation:

- Ensure a clean heading hierarchy.
- Remove unresolved drafting notes unless the user wants them preserved.
- Keep final TODOs in a clearly labeled section.
- Prepare clean text or markdown when no file format is requested.
- If the user asks for DOCX, PDF, or another artifact, follow the active document/PDF tooling instructions, render the artifact, verify it, and persist it through the Library workflow in Work Mode.
- Treat content development and artifact production as one handoff: this skill owns structure and prose; the artifact workflow owns layout, rendering, validation, and storage.
- If the user wants a strict template, preserve that structure even when a different structure might be better.

## Output Contracts

### New document

Return the complete document in its intended reading order. Do not wrap it in a generic development report. Add a short `Offene Punkte` or `Prüfhinweise` section only when needed.

### Existing draft rewrite

Use this compact default structure:

```markdown
## Revised Version
[Full revised text.]

## Change Summary
- [Major change]

## Remaining Issues
- [Open item]
```

Omit the change summary and remaining issues when the user asked only for a clean final version and nothing material remains unresolved.

### Review only

Use this default structure:

```markdown
## Overall Assessment
[Brief conclusion.]

## Issues
| Severity | Area | Issue | Suggested Fix |
|---|---|---|---|
| critical/major/minor | [area] | [issue] | [fix] |

## Recommended Next Version
[Optional outline or rewrite direction.]
```

## Handling Missing Information

Do not over-question. Ask only when the missing information would materially change the document, create a publication risk, or introduce a commitment. Otherwise proceed with clearly marked assumptions.

When assumptions must be visible, keep them concise:

```markdown
Assumptions:
- [assumption]

Open points:
- [question]
```

## Examples

### Example 1: rough notes to report

Input: "Make a report from these meeting notes about a delayed project."

Output approach:
- Identify goal and audience.
- Extract facts, delays, causes, risks, and next steps.
- Create a report with summary, status, causes, impact, options, recommendation, and next actions.
- Mark missing dates, owners, and evidence as TODOs.

### Example 2: draft improvement

Input: "This policy draft is messy. Make it usable."

Output approach:
- Diagnose ambiguity and structure problems.
- Rebuild into purpose, scope, rules, roles, exceptions, review cycle.
- Preserve original obligations unless unsafe or contradictory.
- List unresolved policy decisions.

### Example 3: specification review

Input: "Review this technical spec before I send it."

Output approach:
- Check goals, non-goals, requirements, architecture, interfaces, error cases, testing, rollout, and open questions.
- Flag unverifiable or underspecified claims.
- Provide a severity-based issue table and a revised outline if needed.

## Optional Script

Use `scripts/validate_markdown_structure.py` when a markdown document needs a mechanical structure check. It can report heading hierarchy issues, duplicate headings, TODO markers, empty sections, and approximate word count.

Do not use the script as a substitute for factual, legal, editorial, or visual review. Report only checks that were actually run.
