# Skillbibliothek

Dieses Repository ist die kanonische, konsolidierte Skillbibliothek. Es bündelt die relevanten Skill-Quellen in einer einzigen, wartbaren Struktur und dient als Ausgangspunkt für Agenten, Automationen und wiederverwendbare Arbeitsabläufe.

## Ziel

- eine konsistente Sammlung von Skills je Zweck
- nachvollziehbare Provenienz und gemeinsame Regeln
- saubere Frontmatter-, Pfad- und Linkkonventionen
- eine gültige, pflegebare Grundlage für die Verwendung in Agent-Workflows

## Quellen

- `c:\AI\ai-workflows-stack\skills`
- `c:\Users\PeterSchuller\.codex\skills`
- dieses Repository selbst

Die Quellen werden nur gelesen; alle konsolidierten Änderungen erfolgen hier.

## Aktueller Bestand

Der aktuelle konsolidierte Bestand umfasst 93 Skill-Verzeichnisse mit `SKILL.md`.
Davon bilden 91 Skills die zusammengeführte Fachbibliothek; `core-routing` und
`skill-security-auditor` ergänzen die Control-Plane- und Security-Gates.

### Kernbereiche

- OSINT und Untersuchung: `useosint`, `investigate-anything`, `find-anyone`, `recon-a-domain-passively`, `who-really-owns-it`, `where-was-this-taken`
- Recherche und Verifikation: `fact-check`, `deep-research`, `source-verification`, `read-deleted-pages`, `find-the-original-image`
- Design und UX: `web-design-guidelines`, `ui-design-engineering`, `ui-ux-pro-max`, `shadcn-ui`, `interaction-design`
- Automatisierung und Entwicklung: `automator`, `cli-creator`, `gh-fix-ci`, `migrate-to-codex`, `prompt-architect`
- Sicherheit und Governance: `security-best-practices`, `security-gate`, `security-threat-model`, `security-ownership-map`
- Content und Kommunikation: `facebook-text-optimizer`, `instagram-text-optimizer`, `humanizer-de`, `peter-schuller-politiker-kommunikation`, `politik-analyse`

## Weitere Dokumentation

- [CONSOLIDATION_REPORT.md](CONSOLIDATION_REPORT.md)
- [AGENTS.md](AGENTS.md)
- [ETHICS.md](ETHICS.md)

## Hinweis

Die Bibliothek enthält bereits die vollständigste bekannte Zusammenführung der drei Quellen. Weitere Erklärungen zu Herkunft, Deduplizierung und offenen Risiken finden sich im Konsolidierungsbericht.
