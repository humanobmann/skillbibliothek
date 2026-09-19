# Skillbibliothek Agent Rules

## Zweck

Dieses Repository ist die kanonische, konsolidierte Skillbibliothek. Skills werden aus den definierten Quellbäumen übernommen, bereinigt und hier wartbar abgelegt.

## Verbindliche Quellen

- `c:\AI\ai-workflows-stack\skills`
- `c:\Users\PeterSchuller\.codex\skills`
- dieses Repository selbst

Quellbäume sind nur zu lesen. Alle konsolidierten Änderungen werden ausschließlich hier geschrieben.

## Strukturregeln

- Jeder Skill liegt in einem eigenen Verzeichnis mit `SKILL.md`.
- `SKILL.md` beginnt mit gültigem YAML-Frontmatter und enthält `name` sowie eine konkrete `description`.
- Relative Links, Referenzen, Skripte und Assets müssen auf existierende Dateien zeigen.
- Duplikate werden zusammengeführt, nicht blind überschrieben. Entscheidungen und Provenienz werden dokumentiert.
- Keine Geheimnisse, privaten Zugangsdaten, lokalen Tokens oder unklar lizenzierten Inhalte übernehmen.
- Generierte oder temporäre Dateien gehören nicht in die Skillbibliothek.

## Arbeitsablauf

1. Alle drei Quellen rekursiv inventarisieren.
2. Skills nach Zweck clustern und Konflikte nachvollziehbar entscheiden.
3. Die kanonische Fassung samt funktional nötigen Begleitdateien ins Repo übernehmen.
4. Index, Provenienz und Konsolidierungsbericht aktualisieren.
5. Frontmatter, Links, Pfade und vorhandene Validatoren prüfen.
6. Im Abschlussbericht Zahlen, Änderungen, Validierungen und offene Risiken nennen.

## Abschluss

Nach einem vollständigen und validierten Lauf keine weiteren Änderungen beginnen. Auf eine neue Anweisung warten.