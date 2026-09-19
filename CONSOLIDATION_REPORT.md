# Consolidation report

## Scope and sources

This repository is the canonical target for the consolidated skill library. The validation pass compared the following sources:

| Source | Skill source directories | Skill directories with `SKILL.md` | Notes |
|---|---:|---:|---|
| `c:\AI\ai-workflows-stack\skills` | 89 | 89 | largest source, fully represented |
| `c:\Users\PeterSchuller\.codex\skills` | 92 | 92 | includes six source-only skills not present in the first source |
| target repo | 95 | 95 | current canonical library, including control-plane and security-gate skills |

## Merge outcome

The consolidated repository already contains the union of both source inventories:

- common skills: 86
- only in source A: 0
- only in source B: 6 (`imagegen`, `openai-docs`, `plugin-creator`, `review-agent`,
  `skill-creator`, `skill-installer`)
- canonical merged Fachskill total: 93 unique skill directories
- additional repository-owned control-plane skills: 2 (`core-routing`,
  `skill-security-auditor`)
- current target total: 95 unique skill directories

The target repo therefore represents the full merged set, with no source-only skills left behind.

## Structural improvements in this pass

- added a repository-level [README.md](README.md) for discoverability and orientation
- added a repository-level [ETHICS.md](ETHICS.md) to satisfy the shared ethical-policy links used across the skill set
- captured the consolidation summary and source provenance in this document
- added canonical `references/intent-map.md` and runtime profile/adapter metadata
- added `code-review` and `library-skill-authoring`; retained `grill-me` only as an alias of `grilling`
- bounded `deep-research` to explicit evidence-bearing work and added fail-closed auditor gates
- added routing, overlap, provenance/profile, context-budget, regression tests and minimal CI

## Validation results

A local validation script checked the target repository after the update.

- 91/91 skill directories contain a `SKILL.md`
- 91/91 skill files expose a YAML frontmatter block with both `name` and `description`
- repo-local markdown links resolved successfully after the ethical policy file was added
- no invalid frontmatter blocks were found in the target set
- 95/95 target skill directories contain a `SKILL.md`
- `python scripts/validate_skills.py` passes with 0 failures and 0 warnings
- `python scripts/context_benchmark.py` measures 11,773 discovery tokens and
  213,841 full-text tokens; progressive disclosure reduces the measured
  footprint by 94.49%
- `python -m pytest -q tests skills/skill-security-auditor/tests` passes with
  8 tests
- the repository-wide prompt-injection and strict code scanners both return
  `PASS` with no findings

## Open risks and follow-up

- some skill names remain informal or custom (`pdf`, `yeet`, `screenshot`) and may merit a later naming review
- the source trees were treated as read-only; no direct writing was performed in either external source
- the repository should continue to be reviewed when the skill library grows further, especially for naming consistency and duplicate coverage
- source inventories should be re-counted on the same machine when external trees are unavailable; no source-only content was copied without a readable license/provenance basis

## Key project paths

- [README.md](README.md)
- [AGENTS.md](AGENTS.md)
- [ETHICS.md](ETHICS.md)
- [./.github/agents/skillbibliothek-optimizer.agent.md](.github/agents/skillbibliothek-optimizer.agent.md)

The repository is in a consistent starting state for further skill-level refinements and validation.
