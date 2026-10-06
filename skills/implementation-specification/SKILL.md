---
name: implementation-specification
description: Erstelle eine umsetzungsreife technische Spezifikation für eine klar abgegrenzte Software-, Web-, API-, Automations-, Daten-, AI-, Migrations- oder Refactoring-Änderung. Verwenden vor der Implementierung, wenn Anforderungen, betroffene Komponenten, Schnittstellen, Zustände, Fehlerfälle, Tests, Akzeptanzkriterien und geschützte Bereiche präzise festgelegt werden müssen. Nicht für die Implementierung selbst oder für komplette Multi-Dokument-Spezifikationssuiten verwenden.
---

# Implementation Specification

## Auftrag

Erzeuge aus belegtem Projektkontext einen implementierbaren technischen Vertrag. Trenne bestätigte Fakten, Entscheidungen, Annahmen und offene Punkte. Erfinde keine Architektur oder bestehende Systemzustände.

## Workflow

1. Ziel, Nutzerwirkung, Scope und Non-Goals bestimmen.
2. Aktuellen Zustand aus bereitgestellten Dateien, Code, Tickets oder Dokumentation erfassen.
3. Anforderungen mit stabilen IDs festhalten.
4. Betroffene Komponenten, Dateien oder Verantwortungsbereiche benennen.
5. Schnittstellen, Daten, Zustände, Validierung, Berechtigungen und Fehlerverhalten spezifizieren.
6. Relevante Edge Cases, Migration, Rollback und Observability definieren.
7. Tests und objektiv prüfbare Akzeptanzkriterien vor der Implementierung festlegen.
8. Offene Entscheidungen als Blocker markieren statt sie still zu treffen.
9. Mit einem Coding-Agent-Handoff und Source/Evidence-Index abschließen.

## Scope-Kontrolle

Getrennt ausweisen:

- Create
- Modify
- Preserve unchanged
- Prohibited without approval
- Delete/deprecate nur bei ausdrücklicher Autorisierung

Produktverhalten, Schnittstellen, Sicherheit, Daten, Invarianten und Akzeptanz exakt festlegen, soweit Evidenz vorhanden ist. Reine Implementierungsdetails dürfen als bounded engineering discretion offenbleiben.

## Qualitätsgate

Eine Spezifikation ist erst bereit, wenn ein kompetenter Entwickler die Änderung umsetzen kann, ohne eine wesentliche Produkt-, Architektur-, Sicherheits- oder Datenentscheidung selbst erfinden zu müssen.

## Ausgabe

1. Ziel und Scope
2. aktueller Zustand
3. Anforderungen
4. technisches Design
5. betroffene Bereiche
6. Fehler- und Randfälle
7. Test- und Akzeptanzvertrag
8. Entscheidungen/Annahmen/Blocker
9. Implementierungs-Handoff
10. Quellenindex
