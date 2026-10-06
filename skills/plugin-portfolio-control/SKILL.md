---
name: plugin-portfolio-control
description: Inventarisiere, konsolidiere, migriere und überprüfe ein ChatGPT/Codex Plugin- und Skill-Portfolio mit klarer Trennung von sichtbaren Plugin-Namen, Backend-IDs, Skillpaketen, Releases und GitHub-Quellen. Verwenden für Plugin-Aufräumen, Redundanzanalyse, Migration, Versionierung, Berechtigungsprüfung und sichere Entfernung nach Null-Verlust-Gates.
---

# Plugin Portfolio Control

## Grundsatz

Nicht nach Namen löschen. Erst Identität und Ersatz beweisen.

## Inventar

Für jede Komponente erfassen:
- sichtbarer Name
- Backend Plugin-ID
- interner Paketname
- Scope
- Version und Release-ID
- enthaltene Skills
- Quelle / Repository
- Abhängigkeiten
- Berechtigungen
- Nutzungssignal
- zukünftiger Owner

Technische Skill-URIs sind kein Beweis für einen sichtbaren Plugin-Namen.

## Konsolidierung

1. bestehende Hauptplugins bevorzugen
2. identische, ähnliche und nur gleichnamige Skills unterscheiden
3. vollständige Skillordner inklusive References, Scripts, Assets und Agent-Metadaten berücksichtigen
4. Source of Truth festlegen
5. Migration in kleinen Wellen durchführen
6. Versionen erhöhen und bestehenden Plugin-IDs erhalten
7. nach jedem Update installierten Release zurücklesen

## Null-Verlust-Gate

Vor Entfernung:
- Ersatzskill vorhanden
- funktionale Abdeckung geprüft
- relevante Dateien/Dependencies vorhanden
- Zielplugin installiert und verifiziert
- Release-ID/Backup oder reproduzierbare Quelle vorhanden
- exaktes zu entfernendes Plugin identifiziert
- Entfernung ausdrücklich autorisiert

Wenn Plugin Management meldet, dass ein Paket nicht installiert oder nicht deinstallierbar ist, nicht raten. Quelle, Workspace-Policy oder extern verwalteten Installationsweg klären.

## Destruktive Grenze

Keine Plugin-Entfernung, keine Veröffentlichung und keine weitreichende Berechtigungsänderung ohne eindeutigen Zielbezug und Autorisierung. Reversible Inventar-, Vergleichs- und Validierungsschritte dürfen selbstständig erfolgen.

## Ausgabe

- Ist-Inventar
- Crosswalk
- Zielarchitektur
- Migrationsmatrix
- Verifikation
- Entfernungsergebnis
- offene Plattformblocker
