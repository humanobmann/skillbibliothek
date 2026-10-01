# Thematische Plugin-Pakete

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
