# Copilot Instructions

Dieses Repository baut eine konsolidierte Skillbibliothek aus drei lesbaren Quellen auf:

- `c:\AI\ai-workflows-stack\skills`
- `c:\Users\PeterSchuller\.codex\skills`
- das Zielrepository selbst

Bei Änderungen gelten folgende Regeln:

- Schreibe ausschließlich in das Zielrepository.
- Scanne alle erreichbaren Skill-Verzeichnisse rekursiv, bevor du Duplikate oder Varianten bewertest.
- Behandle `SKILL.md` als kanonische Einstiegdatei eines Skills.
- Bewahre funktional nötige `references/`, `scripts/`, `assets/` und Tests.
- Prüfe YAML-Frontmatter, interne Links, Pfade und referenzierte Dateien.
- Übernimm keine Geheimnisse oder unklar lizenzierten Inhalte.
- Dokumentiere Provenienz, Zusammenführungen, ausgelassene Varianten und offene Konflikte.
- Führe vorhandene lokale Validierungen aus und erfinde keine Testergebnisse.
- Nach erfolgreicher Konsolidierung und Validierung warten, bis eine neue Anweisung eingeht.

Für den vollständigen Konsolidierungslauf ist `.github/agents/skillbibliothek-optimizer.agent.md` zu verwenden.