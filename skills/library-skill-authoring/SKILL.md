---
name: library-skill-authoring
description: Create or update a maintainable skill in this library with valid frontmatter, progressive disclosure, safe links, provenance, and deterministic validation.
metadata:
  canonical: true
  profile: authoring
  provenance: target-authored
---

# Library skill authoring

## Purpose and activation

Use when creating, consolidating, or materially revising a skill under
`skills/<name>/`. Activate only with a concrete purpose and source boundary.

## Inputs

- intended user goal and activation/non-activation conditions;
- source files and license/provenance information;
- required references, scripts, assets, and tests.

## Procedure

1. Inventory existing skills and select one canonical name; preserve aliases only
   when compatibility is required.
2. Write valid YAML frontmatter (`name`, concrete `description`, optional metadata).
3. Document purpose, inputs, workflow, hard rules, output, safety/privacy, and
   evidence limits appropriate to the domain.
4. Add only functionally required support files; ensure every relative link exists.
5. Record provenance without copying secrets, private paths, or unclear-licensed text.
6. Run the repository validator, tests, link checks, and applicable security scans.

## Hard rules

- Do not invent tools, APIs, paths, test results, licenses, or sources.
- Keep hard requirements separate from recommendations.
- Do not modify read-only source trees.
- A skill with a failed security gate is not active; report the failure.

## Output

Provide the changed paths, canonical/alias decision, provenance, validation
results, and known gaps.
