# Runtime profiles and adapters

Profiles are descriptive metadata, not permission grants. A runtime adapter must
enforce the same hard rules as the canonical skill and must not silently broaden
tool access.

| Profile | Canonical skills | Minimum adapter contract |
|---|---|---|
| `control-plane` | `core-routing` | resolve only existing targets; reject cycles and unknown targets |
| `research` | `deep-research` | provide source URLs, retrieval dates, and an evidence boundary |
| `security-gate` | `skill-security-auditor` | fail closed on scanner errors, high/critical findings, or incomplete evidence |
| `engineering` | `code-review` | preserve review boundary and distinguish observed from assumed tests |
| `authoring` | `library-skill-authoring` | validate frontmatter, links, provenance, and source immutability |

Supported adapters are intentionally runtime-neutral: `codex`, `claude`, and
`cursor` may load the same `SKILL.md`; adapter-specific configuration belongs in
the host runtime and must not be invented in this repository.
