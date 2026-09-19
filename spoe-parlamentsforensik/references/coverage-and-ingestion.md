# Ingestion Runbook

Stand: 2026-08-24

## Ziel

Reproduzierbare, unterbrechbare und prüfbare Vollerhebung des parlamentarischen Korpus.

## Phase A: Preflight

1. Offizielle Dokumentationsseiten abrufen und Hash beziehungsweise Abrufdatum protokollieren.
2. Query Registry laden.
3. Alle Einträge mit `NEEDS_LIVE_VERIFICATION` zuerst als kleine Testabfrage ausführen.
4. Response Schema gegen erwartete Felder prüfen.
5. Erst nach PASS Massenerhebung starten.

## Phase B: Primärindex

Reihenfolge je GP:

1. Anträge NR
2. Anträge BR
3. Regierungsvorlagen
4. Ausschussberichte NR
5. Ausschussberichte BR
6. Beschlüsse soweit verfügbar
7. schriftliche Anfragen NR
8. schriftliche Anfragen BR
9. Stenoprotokolle NR
10. Stenoprotokolle BR
11. Plenarsitzungen NR
12. Plenarsitzungen BR

Danach Personen, Ausschüsse und Ausschussmitgliedschaften als Querschnittslayer.

## Phase C: Request Speicherung

Für jeden Request speichern:

```text
RUN_ID
QUERY_ID
REQUEST_URL
REQUEST_BODY
REQUESTED_AT
HTTP_STATUS
CONTENT_TYPE
BYTE_SIZE
SHA256
API_COUNT
ROWS_RECEIVED
PAGES
ERROR
RETRY_COUNT
```

Dateinamenschema:

```text
raw/<source>/<gp>/<query_id>__<run_id>__sha256_<prefix>.json
```

## Phase D: Coverage

Ein Primärbatch ist nur vollständig, wenn:

1. `count == len(rows)` oder die API Paginierung vollständig verarbeitet wurde.
2. keine unerklärte Duplicate Rate besteht.
3. der Setvergleich mit einer unabhängigen Partition übereinstimmt.
4. jede Row eine kanonische Identität besitzt oder als Parserfehler protokolliert ist.
5. Detailseitenabruf für jede Row versucht wurde.

## Phase E: Adaptive Segmentierung

Trigger:

* `count != rows`
* unerwartete maximale Zeilenzahl
* HTTP Fehler
* Parserfehlerhäufung
* Setdifferenz zwischen Kontrollpartitionen

Vorgehen:

1. DOKTYP Partition, falls vorhanden.
2. Zeitpartition.
3. Rekursive Halbierung des Zeitraums.
4. Wiederholen bis vollständiger Teilbatch oder Taggranularität erreicht.
5. Wenn Taggranularität fehlschlägt, `FAILED_COVERAGE` setzen.

## Phase F: Detail JSON

Für jeden Gegenstand:

1. relative URL kanonisieren.
2. `?json=TRUE` abrufen.
3. unverändert speichern.
4. Hash speichern.
5. `status`, `stages`, `documents`, `names`, `topics`, `headwords`, `eurovoc`, `correspondence`, `reference` und `vote` soweit vorhanden normalisieren.

## Phase G: Dokumente und Volltext

Dokumente werden nur gemäß Lizenz und Zweck verarbeitet.

Priorität:

1. HTML
2. strukturierter JSON Text
3. PDF mit Textlayer
4. OCR nur als letzter Fallback

OCR Ergebnisse immer mit `OCR=true` und Confidence kennzeichnen.

## Phase H: Sitzungen und Reden

XX bis XXV:

```text
Steno Index
→ vollständiges HTML
→ Tagesordnung
→ Sprecherwechsel
→ Zwischenrufe und Beifall
→ Rede Segmente
```

Ab XXVI:

```text
Steno Index
+ Plenarsitzungs JSON
+ Einzelrede HTML
+ vollständiges Steno HTML
```

Einzelrede und Gesamtprotokoll gegenseitig validieren.

## Phase I: Entity Resolution

Primärschlüssel für Personen ist PAD, nicht Name.

Zeitabhängig speichern:

```text
person_id
valid_from
valid_to
gremium
party_or_club
mandate
function
wahlkreis
```

Keine heutige Parteizugehörigkeit rückwirkend verwenden.

## Phase J: Normalisierung

Vier Schichten strikt trennen:

```text
RAW
NORMALIZED
DERIVED
ANALYSIS
```

Normalisierung darf keine politische Interpretation enthalten.

## Phase K: Resume und Checkpoints

Nach jedem Batch:

```text
last_successful_query
last_successful_item
open_errors
coverage_status
rows_total
details_total
details_failed
next_query
```

Ein bereits erfolgreich gehashter Raw Batch wird ohne Grund nicht erneut geladen.

## Phase L: Abschluss eines Corpus Runs

Erzeuge:

1. Corpus Manifest
2. Coverage Report
3. Error Register
4. Duplicate Register
5. License Exceptions Register
6. Query Manifest
7. Parser Version Manifest

Erst danach darf der Run an Blue Team übergeben werden.

## Erweiterte Coverage Regeln des Skills

Ein Basisscan gilt erst nach mindestens einer unabhängigen Partition als belastbar. Für Datensatz 101 ist die bevorzugte Reihenfolge:

```text
BASE: GP + Gremium + VHG
CHECK A: GP + Gremium + VHG + alle beobachteten DOKTYP einzeln
CHECK B: GP + Gremium + VHG + disjunkte Datumsfenster
```

Vergleiche nicht nur Counts, sondern die Menge der kanonischen Objekt-IDs. Bei BR-Datensätzen, die nicht an Nationalrats-GP gebunden sind, zusätzlich zeitbasierte Kontrollabfragen verwenden.

## Runtime-Fallback

Wenn der ausführbare HTTP-Client keinen Netzzugang besitzt:

1. Keine Massenerhebung simulieren.
2. Offizielle Dokumentation mit Browser/Webzugang verifizieren.
3. Query-Plan und Registry aktualisieren.
4. `RUNTIME_VERIFIED=false` speichern.
5. Coverage als `NOT_MEASURABLE` ausweisen.
6. Politische Vollkorpus-Toplisten sperren.
