# Skillbibliothek Agent Rules

Dieses Dokument verweist auf die kanonischen Architektur- und Verhaltensregeln der Bibliothek unter [references/AGENTS.md](references/AGENTS.md).

## Verbindliche Quellen

- `c:\AI\ai-workflows-stack\skills` (Read-only)
- `c:\Users\PeterSchuller\.codex\skills` (Read-only)
- dieses Repository selbst (Kanonische Single Source of Truth)

## Primäre Strukturregeln

- Alle Fachskills liegen isoliert unter `skills/<skill-name>/` mit `SKILL.md`.
- `SKILL.md` beginnt mit gültigem YAML-Frontmatter (`name`, `description`).
- Relative Links, Referenzen, Skripte und Assets müssen auf existierende Dateien zeigen.
- Progressive Disclosure: Discovery (~100 Tokens) -> Activation -> Execution.
- Strikte Sicherheitsgates gemäß [references/SECURITY_POLICY.md](references/SECURITY_POLICY.md).
- Ausführliche Richtlinien: siehe [references/AGENTS.md](references/AGENTS.md).