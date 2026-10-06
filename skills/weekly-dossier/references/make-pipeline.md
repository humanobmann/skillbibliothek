# Bestehende Make-Pipeline, Stand 2026-10-03

IDs nur diagnostisch verwenden; Szenarien über Namen finden.

## Architektur

### Kontinuierliche Quellenaufnahme
RSS- und Discovery-Ereignisse landen in der Excel-Tabelle `tblSourceEvents` im Blatt `Events`.

Bekannte Szenarien:
- `SPOE LAIMER 11 - Intake ORF News`, alle 2 Stunden
- `SPOE LAIMER 12 - Intake ORF NOE`, alle 2 Stunden
- `SPOE LAIMER 13 - Intake Bundesheer`, alle 2 Stunden
- `SPOE LAIMER 16 - Medien National`, stündlich; zum Analysezeitpunkt fehlerhaft
- `SPOE LAIMER 17 - Medien Wahlkreis NOE`, alle 2 Stunden
- `SPOE LAIMER 18 - Medien International`, alle 4 Stunden
- `SPOE LAIMER 19 - Parlament Discovery`, alle 6 Stunden
- `SPOE LAIMER 20 - NOE Land Discovery`, alle 6 Stunden

### Weekly Source Bundle
`SPOE LAIMER 21 - Weekly Source Bundle`, beobachtet Montag 04:30.

Ausgaben:
- `/SPOE_LAIMER_DOSSIER_SYSTEM/05_QUELLEN_RECHERCHE/MONITORING/SYNTHESIS/DOSSIER_INPUT_WEEKLY.txt`
- `/SPOE_LAIMER_DOSSIER_SYSTEM/05_QUELLEN_RECHERCHE/MONITORING/SYNTHESIS/SOURCE_EVENTS_WEEKLY.json`

### Dossier-Generation
`SPOE LAIMER 26 - Architektur B V6 100P GATE`, beobachtet Montag 05:15.

Zum Analysezeitpunkt fehlerhaft/inaktiv. Geplanter Ablauf: Wochenbundle, Baseline, AMS, Gemeinderegister, Parlamentsdiff, Dossiervertrag, Safe Reference, Draft, QA, Encoding-/Placeholder-Guard, Contentplan, CSS, HTML/PDF, Release-Status.

### Montagszustellung
`SPOE LAIMER 03 - Montag Dossier + Contentplan Gmail`, beobachtet Montag 07:00.

## Bekannte Defekte

### Defekte Modulreferenz
QA verweist auf `17.data` als VERIFIED SUPPLEMENT, obwohl Modul 17 im aktuellen Blueprint nicht mehr existiert. Nicht rekonstruieren, solange Quelle und Generierung nicht bewusst wiederhergestellt wurden.

### Veraltete AMS-URL
Die Generation war auf eine AMS-NÖ-Seite für 08/2026 hart codiert. Immer die neueste offizielle Monatsveröffentlichung dynamisch auflösen.

### Upload-Fehler
Eine Ausführung vom 2026-09-14 scheiterte beim HTML-Upload mit 404. Nachfolgende Konvertierungs- oder Release-Schritte nicht als erfolgreich annehmen.

### Release-Dateinamenskonflikt
Generator schreibt `RELEASE_STATUS.json`, Zustellung erwartet `RELEASE_STATUS_<YYYY-MM-DD>.json`. Bis zur Korrektur Produktionsblocker.

### Weekly-Manifest-Filter
Der tatsächlich beobachtete Filter ist enger als seine Beschreibung: E4, E5, LANDESVERTEIDIGUNG, PARLAMENT oder P0 plus definierter Wahlkreis-Ortsbezug. Tatsächlichen Filter als autoritativ behandeln.

### Release-Semantik
Factual Freshness, Coverage Completeness, Rollenprüfung und andere deterministische Prüfungen wurden ausdrücklich als unverified markiert. AI-QA niemals in einen deterministischen PASS umdeuten.
