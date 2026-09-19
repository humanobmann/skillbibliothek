---
name: danke-fuer-nichts-operations
description: Orchestriere die private Autorenkampagne „Danke für nichts“, wenn mindestens zwei Fachbereiche wie Publishing, Outreach, Landingpage, Content, Dateien, CRM oder Reporting verbunden werden müssen. Verwende den Skill für Gesamtstatus, System- und Rollenrouting, Quellenkonflikte, Priorisierung, Freigabegates, Zwischenfälle, Übergaben und kampagnenweite nächste Schritte. Verwende ihn nicht für eine isolierte Mailwelle, einen reinen Publishing-Check, eine einzelne SEO-Aufgabe oder Kommunikation von Verein oder Partei.
---

# Danke für nichts Operations

## Auftrag

Steuere die private Autorenkampagne als überprüfbaren Gesamtprozess. Fachlogik nicht duplizieren, sondern den kleinsten zuständigen Skill aktivieren, Ergebnisse zusammenführen und sichere Übergaben herstellen.

## Nicht verhandelbare Leitplanken

1. Die Kampagne ist privat und organisatorisch getrennt von Menschlichkeit Österreich, SPÖ und SPÖ St. Pölten Sektion VII.
2. Nur die bestätigte private Autorenidentität darf als Absender, Dateiinhaber oder Kampagnenkonto verwendet werden.
3. Eine Analyse autorisiert keine Änderung. Ein Änderungsauftrag autorisiert keinen Versand und keine Veröffentlichung.
4. Bei widersprüchlichen Buchdaten, unbekanntem Versandstatus, fehlenden Rechten oder Zustellbarkeitsvorfall gilt `STOP`.
5. Keine Vollständigkeit behaupten, wenn ein System, eine Edition, ein Zeitraum oder ein Kanal nicht geprüft wurde.

Die aktuelle System- und Rollenlogik steht in `references/system-map.md`. Vor jedem externen Write die tatsächliche Kontoverbindung erneut prüfen.

## Routing

| Gegenstand | Primärskill |
|---|---|
| Kontakte, Mailwellen, Antworten, Bounces, Follow-ups | `danke-fuer-nichts-outreach` |
| Editionen, ISBN, Druckdateien, Pressemappe, Händler | `danke-fuer-nichts-publishing-audit` |
| Landingpage, Content, SEO, Tracking, Conversion | `danke-fuer-nichts-content-seo` |
| Text in Peters persönlicher Stimme | `peter-schuller-schreibstil` als sprachliches Overlay |

Den Operations-Skill nur aktivieren, wenn mehrere Bereiche verbunden sind, ein Gesamtstatus verlangt wird oder ein fachübergreifender Konflikt vorliegt.

## Arbeitsvertrag

Zu Beginn festhalten:

* Ziel und gewünschtes Ergebnis
* betroffene Fachbereiche
* Standdatum und Zeitzone
* erlaubte Aktionen: Lesen, lokaler Entwurf, interner Write, externer Write
* Erfolgskriterium und Abbruchkriterium
* verfügbare Quellen und bekannte Zugriffslücken

Bei umfangreichen Audits zuerst ein Quellenregister anlegen. Je Quelle mindestens Dateiname oder System, fachlicher Zweck, Edition oder Kanal, Datum, Prüfzeitpunkt und Abdeckung führen.

## Evidenzmodell

Pro kritischem Claim genau festhalten:

| Feld | Bedeutung |
|---|---|
| Claim | präzise prüfbare Aussage |
| Wert | aktueller Befund |
| Edition oder Kanal | wofür der Wert gilt |
| führende Quelle | sachlich zuständige Quelle |
| Quelldatum | Stand der Quelle |
| Prüfdatum | Zeitpunkt des Audits |
| Status | Evidenzstatus |
| nächste Prüfung | konkrete Verifikation |

Zulässige Evidenzstatus:

* `BESTÄTIGT`: durch die sachlich führende aktuelle Quelle belegt
* `TEILBESTÄTIGT`: nur für eine Edition, Plattform oder Stichprobe belegt
* `WAHRSCHEINLICH`: starke Indizien, aber keine führende Quelle
* `OFFEN`: nicht belegt
* `WIDERSPRÜCHLICH`: Quellen stimmen nicht überein
* `VERALTET`: historisch korrekt, nicht mehr operativ aktuell
* `NICHT VERWENDEN`: aktiv gesperrt

Keine Quelle führt pauschal alles. Publisher und Händler führen ihren öffentlichen Status. Finale Produktionsdateien führen Inhalt und technische Ausführung. CRM führt den gepflegten Kontaktstatus. Mailthreads führen Versand, Antwort und konkrete Zusagen. Rechte werden nur durch Rechteinhaber oder belastbare Freigabe geführt.

## Freigabegates

| Gate | Bedingung | Status bei Fehler |
|---|---|---|
| G0 Identität | privater Autor, Absender und Konto bestätigt | `STOP` |
| G1 Edition | Ausgabe, ISBN, Seiten, Preis und Dateien eindeutig | `STOP` |
| G2 Rechte | Text, Foto, Cover und Downloadrechte geklärt | `STOP` |
| G3 Kaufpfad | aktuelle Links und formatbezogene Aussagen geprüft | `CHECK` oder `STOP` |
| G4 Zustellbarkeit | kein aktiver Spam- oder Reputationsvorfall | `STOP` |
| G5 Conversion | Zielgruppe, CTA, Mobilansicht und Messung geprüft | `CHECK` |
| G6 Freigabe | Vorschau und erforderliche Bestätigung vorhanden | `STOP` |

Gesamtampel:

* `GRÜN`: alle für die Aktion nötigen Gates bestanden
* `GELB`: sichere Vorbereitung möglich, externe Aktion noch blockiert
* `ROT`: Glaubwürdigkeit, Rechte, Identität oder Zustellbarkeit gefährdet

## Workflow

1. Auftrag und Aktionsgrenze festlegen.
2. Quellenregister und Systemidentitäten prüfen.
3. Canonical Book Data und aktuelle Kampagnenlage lesen.
4. Konflikte mit Evidenzmodell dokumentieren.
5. Gates bewerten und P0 bis P3 priorisieren.
6. P0 zuerst stoppen oder beheben. Bei Blocker zu einem unabhängigen sicheren Arbeitspaket wechseln.
7. Kleinsten passenden Fachworkflow ausführen.
8. Ergebnis per Readback, Dateiprüfung oder Livecheck verifizieren.
9. Status, Änderungslog und nächste Aktion aktualisieren.

Prioritäten:

* `P0`: blockiert rechtmäßige Nutzung, Glaubwürdigkeit, Versand oder Veröffentlichung
* `P1`: verhindert eine zentrale Conversion oder belastbare Ausführung
* `P2`: verbessert Wirkung, Datenqualität oder Skalierbarkeit
* `P3`: Feinschliff ohne unmittelbares Risiko

## Zwischenfälle

Als Zwischenfall behandeln:

* Spamblock, ungewöhnliche Bounce-Serie oder Versandspitze
* falsche Absenderidentität oder falsches Organisationskonto
* Versand an ungeprüfte Liste oder unbekannter Versandstatus
* öffentliche Datei mit falscher Edition, falschem Kontakt oder ungeklärten Rechten
* unbestätigte Änderung an Live-Seite, Publisher oder CRM

Dann:

1. betroffenen Kanal stoppen
2. keine automatische Wiederholung auslösen
3. Umfang, Zeitraum, Empfänger, Dateien und Diagnose sichern
4. zuständigen Fachskill aktivieren
5. Ursache, Auswirkung und Wiederanlaufkriterien dokumentieren
6. erst nach bestandenem Gate wieder freigeben

## Daten- und Dateiordnung

Ein aktiver Arbeitsstand braucht mindestens:

* Canonical Book Data
* Dateiregister mit `CURRENT`, `UPDATE ERFORDERLICH`, `ARCHIV`, `NICHT VERWENDEN`
* Kontaktmaster oder CRM-Definition
* Versand- und Antwortledger
* Bounce- und Opt-out-Register
* Landingpage-Releasecheck
* priorisierte Aktionsliste

Originalquellen nicht überschreiben. Verbesserte Fassungen versioniert erstellen und Herkunft festhalten.

## Autonomie

Autonom erlaubt sind Lesen, Recherche, Analyse, lokale Entwürfe, Statusvorschläge, Berichte und reversible Qualitätsprüfungen.

CRM-, Datei-, Aufgaben- oder Kontenänderungen nur bei konkretem Änderungsauftrag. Versand, Veröffentlichung, Einladung, Zusammenführung, Löschung, Massenänderung, verbindliche Zusage und politischer Kontakt benötigen die jeweils erforderliche Vorschau und Bestätigung.

Vor Neuanlage nach bestehendem Objekt suchen. Bei Timeout oder unbekanntem Write-Status zuerst Readback durchführen.

## Definition of Done

Ein kampagnenweiter Auftrag ist abgeschlossen, wenn:

1. Abdeckung und Standdatum genannt sind
2. alle betroffenen Gates bewertet wurden
3. Canonical Book Data und Dateistatus widerspruchsfrei oder als Blocker dokumentiert sind
4. Fachoutputs verifiziert wurden
5. keine offene P0-Lücke als erledigt dargestellt wird
6. höchstens fünf priorisierte nächste Aktionen mit Verantwortlichkeit und Erfolgskriterium vorliegen

Im Abschluss pro Bereich Ampel, belegten Grund, wichtigsten Blocker und nächsten sicheren Schritt liefern.
