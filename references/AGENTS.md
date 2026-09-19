# Skillbibliothek Agent Rules & Architecture Standard

## 1. Zweck & Geltungsbereich

Dieses Repository ist die kanonische, konsolidierte Agent-Skills-Bibliothek. Es vereint Fachskills, Steuerungsmuster (Control Plane) und ausführende Werkzeuge (Execution Plane) in einer modularen, plattformübergreifenden Struktur für autonome KI-Agenten (Codex, Claude Code, Cursor, Open Agent Runtimes).

## 2. Verbindliche Quellen

- `c:\AI\ai-workflows-stack\skills` (Arbeitskopie / Read-only)
- `c:\Users\PeterSchuller\.codex\skills` (Codex-Sammlung / Read-only)
- dieses Repository selbst (Kanonische Single Source of Truth)

Quellbäume sind ausschließlich lesend zu verwenden. Alle Änderungen, Härtungen und Validierungen erfolgen hier.

## 3. Ziel-Verzeichnisstruktur

Das Repository ist strikt nach funktionalen Schichten gegliedert:

```
.
├── .github/workflows/   # CI/CD-Pipelines (skill-ci.yml, security-scan.yml)
├── agents/              # Runtime-Metadaten (openai.yaml, claude.yaml)
├── references/          # Globale Vorgaben, Regeln, Policies und Schemas
├── scripts/             # Globale deterministische Validierungs- & Benchmark-Skripte
├── skills/              # Fach-Skills in isolierten Modul-Verzeichnissen
└── tests/               # Automatisierte Test- und Evaluationssuiten
```

## 4. Modulaufbau für Skills (`skills/<skill-name>/`)

Jeder Skill muss isoliert in einem eigenen Verzeichnis unter `skills/` liegen:
- `SKILL.md`: Kanonische Einstiegsdatei mit YAML-Frontmatter (`name`, `description`).
- `references/`: Spezifische Richtlinien, Schemas, Checklisten (nur bei Bedarf).
- `scripts/`: Deterministische Helper-Skripte (Python, Shell, PowerShell).
- `assets/`: Vorlagen, Templates, statische Ressourcen.
- `tests/`: Spezifische Komponententests.

## 5. Progressive Disclosure

1. **Discovery**: Der globale Startkontext lädt ausschließlich Metadaten (`name`, `description`) aus dem Index/Katalog (~100 Tokens pro Skill).
2. **Activation**: Vollständige `SKILL.md`-Instruktionen werden erst geladen, wenn der Skill über seinen Intent aktiviert wurde.
3. **Execution**: Spezialreferenzen und Skripte werden bedarfsgesteuert ("on demand") zur Laufzeit abgerufen.

## 6. Sicherheits- und Qualitätsanforderungen (P0)

- Keine hartcodierten Secrets, privaten Tokens oder Credentials.
- Keine versteckten Unicode-Steuerzeichen (Zero-Width, Bidirectional Overrides).
- Keine Prompt Injections oder ungesicherte dynamische Befehlsausführungen (`eval`, `exec`, `shell=True`).
- Verbindliche Einhaltung von `references/SECURITY_POLICY.md` mit den Statuswerten `PASS`, `WARN`, `FAIL`.
- Relative Markdown-Links müssen auf existierende Dateien zeigen.

## 7. Arbeitsablauf für Änderungen

1. Validierung des Bestands via `python scripts/validate_skills.py`.
2. Härtung und Bereinigung von Konflikten / Overlaps.
3. Ausführung der Testsuite via `pytest tests/`.
4. Sicherheitsprüfung via `skill-security-auditor`.
5. Aktualisierung von Dokumentation, Provenienz und Konsolidierungsbericht.
6. Nach Abschluss keine weiteren Änderungen beginnen; auf neue Anweisung warten.