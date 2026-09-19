---
name: fact-check
description: Verify factual claims in an existing draft against external sources as a separate review pass. Use for publishable books, reports, political texts, educational content, decision support, statistics, dates, quotations, attributions, historical claims, legal or technical assertions, or whenever the user asks to fact-check, verify, validate, source, audit, or check a finished text. Do not use as the primary drafting workflow.
---

# Fact Check

Run verification only after a draft or claim set exists.

## Workflow

1. Extract every externally verifiable claim.
2. Classify each claim as hard fact, soft fact, attribution, inference, or opinion presented as fact.
3. Check hard facts against primary or authoritative sources whenever available.
4. Check dates and current-status claims for recency.
5. Record one of: confirmed, partially supported, contradicted, outdated, or unverified.
6. Correct contradicted claims. Narrow partially supported claims. Mark unverified claims explicitly.
7. Recheck quotations and named attributions against the original source.
8. Surface material disagreements between credible sources instead of choosing silently.

## Source hierarchy

Prefer, in order:

1. statutes, official records, original documents, datasets, specifications, first-party documentation
2. peer-reviewed research and established statistical institutions
3. high-quality reporting with named evidence
4. secondary summaries only when primary material is unavailable

Do not verify a claim from model memory alone.

## Output

For substantial reviews, provide a compact verification ledger with:

- claim
- status
- source
- correction or qualification when needed

Then provide the corrected text if the user asked for a publishable result.

## Quality gates

Before completion, confirm:

- all material claims were considered
- numbers and dates match the cited source
- current claims use current evidence
- quotations were not reconstructed from memory
- unsupported precision was removed
- unverified claims are visibly marked

## Composition

Use after research, document-development, politik-analyse, non-fiction-revision, or other drafting workflows. Keep this as a distinct verification stage.
