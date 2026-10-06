# Thematische Plugin-Pakete

Siehe auch [PLUGIN_MASTERPLAN.md](PLUGIN_MASTERPLAN.md) für Zielarchitektur, Releaseprozess, externe Spezialisten und Null-Verlust-Gates.

Die kanonische Skillbibliothek bleibt die Quelle. Der Build unter `scripts/build_plugin_bundles.py` erzeugt daraus elf kleinere, thematisch getrennte private Plugin-Pakete:

1. Research & Verification
2. OSINT & Investigations
3. Social Content
4. Design & Visual
5. Software Development
6. Security & Platform
7. Politik Österreich
8. Publishing & Writing
9. Automation & Workflows
10. Danke für nichts
11. Vereinskommunikation

Jeder Skill wird genau einem Paket zugeordnet. Skills werden inklusive ihrer References, Scripts, Tests, Assets und Agent-Metadaten übernommen. Die Build-Definition bricht ab, sobald ein Skill fehlt, doppelt zugeordnet oder unbekannt ist.

## Aktueller Stand

| Paket | Skills | Version |
|---|---:|---:|
| skillbibliothek-research | 10 | 1.0.2 |
| skillbibliothek-osint | 28 | 1.0.0 |
| skillbibliothek-social | 12 | 1.0.2 |
| skillbibliothek-design | 6 | 1.0.1 |
| skillbibliothek-development | 23 | 1.0.1 |
| skillbibliothek-security | 11 | 1.0.0 |
| skillbibliothek-politik-at | 7 | 1.0.2 |
| skillbibliothek-publishing | 5 | 1.0.0 |
| skillbibliothek-automation | 15 | 1.0.3 |
| skillbibliothek-danke-fuer-nichts | 4 | 1.0.0 |
| skillbibliothek-verein | 1 | 1.0.0 |

Gesamt: **122 Skills**, genau einmal gebündelt.
