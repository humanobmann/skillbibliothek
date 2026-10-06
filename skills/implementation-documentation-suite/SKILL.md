---
name: implementation-documentation-suite
description: Architekturiere und steuere eine kontrollierte Multi-Dokument-Spezifikationssuite für komplexe Software-, Produkt-, Design-, AI- oder bereichsübergreifende Vorhaben mit mehreren Quellen, Fachautoren, Abhängigkeiten und Prioritätsregeln. Verwenden, wenn eine einzelne technische Spezifikation nicht ausreicht. Nicht für kleine Änderungen, reine Projektplanung oder read-only Audits verwenden.
---

# Implementation Documentation Suite

## Suite-Entscheidung

Nur verwenden, wenn mindestens zwei Punkte zutreffen:

- mehrere Implementierungsdomänen
- mehrere autoritative Quellen
- mehrere Fachautoren
- nicht triviale Prioritäts- oder Override-Regeln
- mehrere Releases/Phasen
- Cross-Document-Traceability erforderlich
- Coding Agent muss ohne versteckten Chatkontext arbeiten

Sonst zu `implementation-specification` routen.

## Lifecycle

1. **Planning Master**: Ziel, Scope, Non-Goals, Constraints, Entscheidungen, Annahmen, Unbekannte, Workstreams und Gates.
2. **Documentation Blueprint**: Dokumente, Owner, Zweck, Inputs, Outputs, Abhängigkeiten, Autorität und Akzeptanz definieren.
3. **Specialist Specifications**: Inhalte vom engsten geeigneten Fachskill erstellen lassen.
4. **Reconciliation**: Quellenkonflikte und dokumentierte Overrides sichtbar auflösen.
5. **Readiness Audit**: gesamte Suite mit `specification-readiness-audit` read-only prüfen.
6. **Gap Closure**: Findings durch zuständige Autoren beheben; Audit erneut ausführen.
7. **First Read / Handoff**: eine kontrollierende Einstiegsdatei mit Read Order, Source Manifest, Status, offenen Entscheidungen, QA und Definition of Done erstellen.

## Kontrollregeln

Jedes kontrollierte Artefakt führt mindestens ID, Titel, Version, Status, Owner, Datum, Quellen, Abhängigkeiten und gegebenenfalls supersedes/overrides.

Keine Datei darf still eine andere überschreiben. Historische und superseded Quellen bleiben nachvollziehbar. Ein schönes Layout ist kein Beweis für Finalität.

## Stop-Regel

Wenn eine wesentliche Entscheidung nicht autorisiert oder ein Quellenkonflikt nicht auflösbar ist, den betroffenen Bereich blockieren statt eine plausible Entscheidung zu erfinden.

## Ausgabe

- Planning Master
- Documentation Blueprint
- Source-/Decision-/Dependency-Register
- Spezifikationssuite
- Audit- und Gap-Closure-Log
- Coding-Agent First Read
- offene Entscheidungen und nächste sichere Aktion
