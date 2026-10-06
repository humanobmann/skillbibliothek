---
name: specification-readiness-audit
description: Prüfe technische Briefings, Spezifikationen, Projektordner und Coding-Agent-Handoffs streng read-only auf Vollständigkeit, Konsistenz, Autorität, Testbarkeit und Implementierungsreife. Verwenden vor Entwicklung oder Übergabe, wenn entschieden werden soll, ob die vorhandenen Unterlagen ohne unerlaubte Eigenentscheidungen umsetzbar sind. Dieser Skill repariert oder implementiert nichts.
---

# Specification Readiness Audit

## Grenze

Nur prüfen. Keine Dateien ändern, keine fehlenden Anforderungen erfinden, keine Architektur wählen und keine Spezifikation reparieren.

## Audit

1. Prüfumfang und tatsächlich inspizierte Evidenz inventarisieren.
2. Autorität, Versionen, Status, Priorität und widersprüchliche Quellen bestimmen.
3. Scope, Ziele, Non-Goals und geschütztes Verhalten prüfen.
4. Anforderungen, Schnittstellen, Daten, Zustände, Berechtigungen und Fehlerfälle auf Vollständigkeit prüfen.
5. Implementierungsgrenzen, Migration, Rollback, Observability und Betriebsanforderungen prüfen, soweit relevant.
6. Tests, Regressionen und Akzeptanzkriterien auf Objektivität und Rückverfolgbarkeit prüfen.
7. Jede Stelle markieren, an der ein Implementierer eine wesentliche Entscheidung selbst treffen müsste.
8. Nicht zugängliche oder nur referenzierte Evidenz als NICHT PRUEFBAR kennzeichnen.

## Finding-Klassen

- BLOCKER: verhindert sichere Implementierung
- MAJOR: muss vor Umsetzung geklärt werden
- MINOR: verbessert Qualität, blockiert aber nicht
- NOT_VERIFIABLE: erforderliche Evidenz fehlt oder war nicht zugänglich

Jedes Finding braucht Evidenzbezug, Auswirkung und die Art der fehlenden Entscheidung oder Information. Keine Lösung inhaltlich vorentscheiden.

## Ergebnis

1. Audit-Scope
2. Readiness-Urteil
3. Findings nach Schwere
4. Widersprüche und Autoritätslücken
5. fehlende Tests/Akzeptanz
6. erforderliche Entscheidungen mit zuständigem Owner
7. Restgates vor Implementierung

Kein PASS ohne tatsächlich geprüfte Evidenz.
