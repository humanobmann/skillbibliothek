---
name: austria-open-data-research
description: Recherchiere, inventarisiere, extrahiere und normalisiere maschinenlesbare öffentliche Daten aus Österreich mit reproduzierbarer Provenienz. Verwenden bei Anfragen zu data.gv.at, Piveau, DCAT-AP, Statistik Austria, RIS, Parlament, Länder- oder Gemeindedaten, Open-Data-APIs, JSON/CSV/GeoJSON/WFS, Vollerhebungen, Delta-Abfragen, Gemeinde- und Regionalprofilen, Datenkatalogen oder belastbaren Datenquellen für nachgelagerte Analysen. Nicht für reine Textrecherche verwenden, wenn keine strukturierte Datenquelle oder reproduzierbare Datenerhebung erforderlich ist.
---

# Austria Open Data Research

## Ziel

Österreichische öffentliche Daten so erheben, dass Ergebnis, Quelle, Zeitpunkt, Lizenz, Datenstand und Transformationsschritte nachvollziehbar bleiben. Primärquellen und maschinenlesbare Originaldaten vor Webseiten-Zusammenfassungen bevorzugen.

## Arbeitsablauf

1. Auftrag klassifizieren: Discovery, Einzelabfrage, Zeitreihe, Geodaten, Rechtsdaten, Parlamentsdaten, Vollerhebung, Delta-Update oder Quellenvergleich.
2. Passende Primärquelle anhand `references/source-routing.md` wählen.
3. Bei unbekannter Quelle data.gv.at als Discovery-Layer verwenden, nicht automatisch als eigentliche Nutzdatenquelle.
4. Metadaten erfassen: Dataset-ID, Titel, Publisher, Lizenz, erstellt, geändert, zeitliche und räumliche Abdeckung, Distributionen und Originalquelle.
5. Beste Distribution nach dem tatsächlichen Analysezweck auswählen.
6. Daten direkt bei der veröffentlichenden Stelle abrufen, wenn dort eine offizielle API oder Originaldistribution existiert.
7. Struktur, Einheiten, Codes, Zeitraum, Aktualität, fehlende Werte und Revisionsstatus prüfen.
8. Daten in das kanonische Schema aus `references/canonical-schema.md` überführen, wenn mehrere Quellen verbunden oder Ergebnisse weiterverarbeitet werden.
9. Bei Vollerhebungen Coverage-Audit durchführen und Abrufgrenzen dokumentieren.
10. Ergebnis mit Quellenledger und offenen Unsicherheiten ausgeben.

## data.gv.at und Piveau

Für neue Integrationen die Piveau- und DCAT-AP-Struktur verwenden. CKAN-kompatible Schnittstellen nur verwenden, wenn eine konkrete Altintegration dies erfordert.

Für Discovery bevorzugen:

`https://www.data.gv.at/api/hub/search`

Für große Katalogabzüge oder Metadaten-Harvesting Hub Repo verwenden. Bei paginierten Vollerhebungen nicht blind nur `page` und `limit` verwenden. Für große Suchmengen `searchAfter` oder `scroll` verwenden, wenn die jeweilige Instanz dies unterstützt.

Metadaten bevorzugt als JSON beziehungsweise JSON-LD verarbeiten. RDF/XML, Turtle, N-Triples oder andere DCAT-AP-Serialisierungen nur verwenden, wenn sie für den Auftrag einen Vorteil bieten.

Vor produktiven oder wiederholten API-Aufrufen aktuelle Endpoint-Dokumentation prüfen. Keine veraltete Beispiel-URL als garantiert stabil behandeln.

Siehe `references/piveau-query-patterns.md`.

## Distribution auswählen

Nicht pauschal nach Dateiendung entscheiden. Nach Nutzbarkeit für die konkrete Analyse priorisieren:

1. dokumentierte Original-API mit stabilen IDs und Filtern
2. JSON oder JSON-LD
3. CSV oder TSV
4. GeoJSON, WFS oder andere geeignete OGC-Schnittstellen für Geodaten
5. XML
6. XLSX
7. PDF nur, wenn keine strukturierte Originalquelle verfügbar ist

Bei Geodaten zusätzlich CRS, Geometrie-Typ, räumliche Auflösung und Stichtag dokumentieren.

## Quellenspezifische Regeln

### Statistik Austria

Freie maschinenlesbare Daten über `data.statistik.gv.at` bevorzugen. Die kostenpflichtige STATcube REST API nur verwenden, wenn ein gültiger Zugang vorhanden ist und ihr Einsatz für die Aufgabe notwendig ist. Nicht annehmen, dass die STATcube API frei zugänglich ist.

### Parlament Österreich

Offizielle Open-Data-JSON-Schnittstellen und Exportfunktionen bevorzugen. Bei Detailseiten kann eine JSON-Repräsentation verfügbar sein. Filterlogik und Datensatz-spezifische API-Beschreibung vor Abruf prüfen. IDs, Gesetzgebungsperiode, Datum, Gremium und Fraktion getrennt normalisieren.

### RIS

Offizielle maschinenlesbare RIS-Daten und aktuelle Distributionen bevorzugen. Dokumentnummern, ELI, Rechtsquelle, Fassung, Kundmachungsdatum und Aktualisierungsstand getrennt erfassen. Konsolidierte Rechtslage nicht mit historischer Fassung verwechseln.

### Länder und Gemeinden

Offizielle Landes- und Gemeindeportale bevorzugen. Falls dieselben Daten zugleich auf data.gv.at und beim Herausgeber liegen, Herausgeber als Datenquelle und data.gv.at als Katalogquelle dokumentieren.

## Vollerhebung

Eine Vollerhebung ist erst abgeschlossen, wenn:

1. der definierte Quellenraum vollständig beschrieben ist,
2. Pagination oder Harvesting bis zum dokumentierten Ende durchlaufen wurde,
3. Dubletten anhand stabiler IDs oder kanonischer URLs behandelt wurden,
4. fehlerhafte oder nicht erreichbare Distributionen separat protokolliert wurden,
5. Anzahl gefundener und erfolgreich verarbeiteter Datensätze ausgewiesen wird,
6. zeitliche und räumliche Coverage überprüft wurde,
7. Ausschlüsse und technische Grenzen genannt werden.

Eine Suchtrefferliste allein nicht als Vollerhebung bezeichnen.

## Delta-Updates

Für wiederholte Abrufe stabile Dataset-IDs, `modified`, ETag oder Last-Modified verwenden, soweit vorhanden. Nur geänderte Quellen erneut laden. Bei fehlendem Änderungsindikator konservativ neu prüfen und diesen Umstand dokumentieren.

## Provenienz

Für jede verwendete Quelle mindestens speichern oder ausgeben:

- source_url
- publisher
- dataset_id oder stabile Quell-ID
- retrieved_at
- source_modified_at, falls vorhanden
- license, falls vorhanden
- distribution_format
- checksum, wenn Dateien lokal verarbeitet werden
- transformation_notes

Keine Zahl oder Kennzahl aus mehreren Quellen zusammenführen, bevor Einheit, Bezugszeitraum, Gebietsstand und Definition kompatibel sind.

## Konflikte zwischen Quellen

Bei widersprüchlichen Werten in dieser Reihenfolge prüfen:

1. gleiche Definition?
2. gleicher Stichtag oder Zeitraum?
3. gleicher Gebietsstand?
4. Revision oder vorläufiger Wert?
5. Primärquelle oder Spiegel?
6. Aktualisierungszeitpunkt?

Nicht stillschweigend einen Wert auswählen. Konflikt und Auswahlregel dokumentieren.

## Ausgabe

Standardmäßig liefern:

1. kurze Antwort auf die eigentliche Datenfrage
2. verwendete Primärquelle oder Primärquellen
3. Datenstand und zeitliche Abdeckung
4. relevante methodische Einschränkungen
5. bei umfangreicher Erhebung eine kompakte Coverage-Zusammenfassung

Bei maschinenlesbarer Ausgabe das Schema aus `references/canonical-schema.md` verwenden.

Bei Dateninventaren pro Datensatz mindestens ID, Titel, Publisher, modified, Format, Lizenz und Originalquelle ausgeben.

## Übergabe an andere Skills

Dieser Skill erhebt und normalisiert Daten. Politische Bewertung, parlamentarische Forensik, Kampagnenstrategie oder Kommunikation nicht selbst ausführen, wenn dafür ein spezifischerer Skill verfügbar ist. Stattdessen die geprüften Datensätze, Quellen, Abdeckungsgrenzen und Unsicherheiten strukturiert übergeben.

## Qualitätsregeln

Keine Portalzahl, Endpoint-Eigenschaft oder Lizenz als dauerhaft annehmen, wenn sie sich ändern kann. Bei aktuellen oder produktionskritischen Aufgaben offizielle Dokumentation erneut prüfen.

Keine Webseite scrapen, wenn dieselbe Information über eine dokumentierte API oder strukturierte Distribution erhältlich ist.

Keine PDF-Auswertung als Primärweg wählen, wenn strukturierte Originaldaten vorhanden sind.

Keine nicht dokumentierten Felder semantisch erraten. Felddefinitionen aus Metadaten oder offizieller Dokumentation ableiten.

Keine Vollständigkeit behaupten, solange Coverage-Audit, Pagination und Fehlerledger nicht abgeschlossen sind.
