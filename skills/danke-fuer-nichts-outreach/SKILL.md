---
name: danke-fuer-nichts-outreach
description: Plane, prüfe und dokumentiere individuellen Presse-, Podcast-, Organisations-, Rezensions- und Buchhandels-Outreach für „Danke für nichts“. Verwende den Skill für Kontaktprüfung, Zustellbarkeitsgates, segmentierte Kleinstwellen, persönliche Mailentwürfe, HubSpot- und Outlook-Routing, Versandledger, Bounce-Klassifikation, Antworten, Follow-ups und Wiederanlauf nach Zwischenfällen. Verwende ihn nicht für allgemeines Kampagnenmanagement, Publishing-Daten, Massenmail oder Vereins- und Parteikontakte ohne ausdrücklichen Buchbezug.
---

# Danke für nichts Outreach

## Sicherheitsmodus

Outreach ist individuelle Beziehungspflege, kein Listenversand. Solange ein Spam-, Absender- oder Zustellbarkeitsvorfall aktiv ist, keine neue Welle vorbereiten oder senden. Zuerst `references/deliverability-response.md` anwenden.

Diese Regeln gelten kanalübergreifend. Ein Wechsel von Outlook zu HubSpot setzt Zähler, Sperren und Empfängerhistorie nicht zurück.

## Kanal- und Absenderlogik

| Kanal | Zweck | Nicht zulässig |
|---|---|---|
| HubSpot | CRM, Aktivitätsverlauf, Aufgaben und ausdrücklich freigegebene Einzelaktionen | Marketingkontaktstatus als Einwilligung interpretieren, ungeprüfte Listen oder Serien ohne Vorschau |
| privates Outlook `schuller.peter@outlook.at` | Antworten und manuell geprüfte Einzelkommunikation | Burst-Versand, BCC-Wellen, Serienbriefe, TNEF oder `winmail.dat` |
| andere Systeme | nur nach aktueller Identitäts- und Zweckprüfung | Organisations- oder Parteikonto still übernehmen |

Als private Autorenkampagne auftreten. Absender, Reply-to, Signatur und Kontoprofil vor jedem Versand live prüfen.

## Zustellbarkeitsgate

Vor jedem Entwurf folgende Zeiträume über alle sendenden Systeme prüfen:

* letzte 30 Tage für Versandzahl, Wiederholungen, Antworten und Bounces
* letzte 7 Tage für Tages- und Kurzzeitspitzen
* vollständiger Thread für jeden geplanten Empfänger

`STOP`, wenn mindestens eines zutrifft:

* Spam- oder Policyblock ist ungeklärt
* mehr als acht neue Erstkontakte am selben Tag vorgesehen sind
* mehr als acht Nachrichten in zehn Minuten entstanden oder geplant sind
* derselbe oder nur ortsangepasste Betreff serienhaft verwendet wird
* `winmail.dat` oder `application/ms-tnef` auftritt
* Versandhistorie ist unvollständig oder liegt außerhalb des CRM
* Absenderidentität oder Versandstatus ist unbekannt

Das mitgelieferte Skript `scripts/audit_outreach_export.py` kann CSV- oder XLSX-Exporte auf diese Risiken prüfen. Es ersetzt nicht den Liveabgleich mit Threads und CRM.

## Kontaktprüfung

Vor Aufnahme prüfen:

1. Person, Organisation, aktuelle Rolle und berufliche Adresse
2. Domain, Land, Segment, Quelle und Prüfdatum
3. Kontakt- und Organisationsdubletten
4. bisherige Kontakte in CRM und Mailbox
5. Antwort, Absage, Opt-out, Bounce und Zustellstatus
6. plausibler individueller Pitchwinkel und aktueller Anlass
7. rechtmäßige, verhältnismäßige und reputationsverträgliche Nutzung

Eine öffentlich sichtbare E-Mail-Adresse ist keine Newslettereinwilligung. Ein nicht gesetztes Opt-out ist ebenfalls keine Einwilligung. Marketingkontaktstatus, rechtlicher Kontext und redaktionelle Ansprache getrennt führen.

Kontaktqualität:

* `A`: konkrete Person oder Redaktion, aktuelle Quelle, klarer Anlass, individueller Pitch
* `B`: passende Organisation und Adresse, aber Person oder Anlass noch zu präzisieren
* `C`: nur allgemeine Adresse oder schwache Passung, nicht versandbereit
* `X`: Opt-out, falsche Rolle, politische Quarantäne, ungeklärte Identität oder unzulässiger Zweck

## Kanonisches Outreach-Ledger

CRM und Mailbox müssen in einen gemeinsamen operativen Status übersetzt werden. Pro Empfänger mindestens führen:

| Feld | Inhalt |
|---|---|
| Kontakt und Organisation | normalisierter Name und Domain |
| Segment und Land | genau ein primäres Segment |
| Quelle | URL oder belastbare Herkunft plus Prüfdatum |
| Pitchwinkel | ein individueller Satz |
| rechtlicher Kontext | redaktionell, bestehende Beziehung, Einwilligung oder offen |
| Status | kontrolliertes Vokabular |
| letzter Versand | Zeit, Kanal, Betreff und Assetversion |
| Zustellung | zugestellt, unbekannt, Bounceklasse |
| Antwort | Datum, Ergebnis und Zitat nur soweit nötig |
| nächste Aktion | Aktion, Termin und Verantwortlichkeit |

Statusvokabular:

`RECHERCHIERT`, `ENTWURF`, `BEREIT`, `GESENDET`, `GEANTWORTET`, `ABGESAGT`, `KEINE_ANTWORT`, `SPAM_BLOCK`, `HARD_INVALID`, `SOFT_BOUNCE`, `OPT_OUT`, `PAUSIERT`, `ABGESCHLOSSEN`.

Eine Absage wird abgeschlossen, nicht als Verkaufsverlust behandelt. Ein Spamblock macht eine Adresse nicht automatisch ungültig. Dubletten auch auf Organisationsebene prüfen.

## Wellenworkflow

1. Zustellbarkeitsgate durchführen.
2. Vorhandene Kontakte, Threads und Aktivitäten lesen.
3. Welle auf höchstens fünf bis acht individuell geprüfte Empfänger begrenzen.
4. Solange die Reputation nicht durch mindestens drei saubere Pilotwellen bestätigt ist, insgesamt höchstens acht neue Erstkontakte pro Kalendertag.
5. Segmente nicht mischen. Pro Welle ein Anlass und ein überprüfbarer Nutzen.
6. Pro Empfänger Quelle, Pitchwinkel, Status, Entwurf und nächste Aktion führen.
7. Empfänger- und Organisationsdubletten sowie Suppressionen prüfen.
8. Empfängerliste und vollständige Entwürfe vor Versand zeigen.
9. Nur nach erforderlicher Freigabe senden.
10. Versand per Readback verifizieren und sofort im Ledger dokumentieren.

## Nachrichtenstandard

Erstkontakt standardmäßig als Klartext oder sehr leichtes HTML:

* individueller Betreff ohne serielle Ortspräfix-Logik
* persönliche, belegbare Einleitung
* höchstens ein Kernargument
* kurzer konkreter CTA
* höchstens ein verifizierter Link
* keine Trackingpixel bei journalistischer Kaltansprache
* keine unaufgeforderte große Anlage
* niemals `winmail.dat`

Eine aktuelle Presse-PDF nur anhängen, wenn der Empfänger Presseunterlagen erwartet oder der konkrete Pitch sie benötigt. Sonst verlinken oder nach Interesse anbieten. Keine alten oder ungeprüften Assets.

Vor Versand Format in der tatsächlich gesendeten Nachricht prüfen, nicht nur im Entwurfseditor.

## Bounces, Antworten und Follow-ups

SMTP-Code und Originaldiagnose bewahren.

* `HARD_INVALID`: eindeutig nicht bestehende oder nicht routbare Adresse
* `SPAM_BLOCK`: Inhalts-, Richtlinien- oder Reputationsblock, etwa `5.7.x`
* `SOFT_BOUNCE`: temporäre Zustellung, volles Postfach oder vorübergehender Serverfehler
* `OPT_OUT`: ausdrücklicher Widerspruch, getrennt von Bounce führen

Bei `SPAM_BLOCK` nicht sofort erneut senden und nicht auf eine andere Adresse derselben Organisation ausweichen. Zuerst Incident-Workflow.

Antworten chronologisch lesen und als Ergebnis klassifizieren:

* konkrete Zusage oder Interesse
* Weiterleitung intern
* bestellbar, aber nicht lagernd
* gelistet oder im Webshop sichtbar
* Absage oder keine Sortimentsaufnahme
* allgemeine Empfangsbestätigung

Keine stärkere Aussage ableiten als die Antwort trägt. `bestellbar`, `gelistet`, `lagernd` und `Sortimentszusage` strikt unterscheiden.

Ein Follow-up frühestens nach sieben Kalendertagen, nur einmal und nur mit neuem Anlass oder konkreter Frage. Nach zwei erfolglosen individuellen Kontakten pausieren.

## CRM-Regeln

Vor Write vorhandene Eigenschaften und Objektfähigkeiten lesen. Fehlende benutzerdefinierte Felder nicht durch erfundene Properties ersetzen. Bis zu einer ausdrücklich beauftragten Schemaerweiterung Standardfelder, Notes und Tasks sauber nutzen.

Keine Marketingkontaktkennzeichnung, Einwilligung, Kampagnenzuordnung oder Bouncebereinigung still verändern. Unbekannten Write-Status per Readback klären.

## Autonomie

Lesen, Prüfen, Klassifizieren und Entwürfe autonom durchführen. CRM-Änderung oder Versand nur bei konkretem Auftrag. Externe Zustellung immer als eigenständige Aktion behandeln.

Bei fehlendem Connector, unklarer Rechtsgrundlage, unbekanntem Absender, widersprüchlichem Kontaktstatus, politischer Rollenvermischung oder aktivem Zwischenfall stoppen und die Lücke konkret nennen.

## Definition of Done

Eine Welle ist `BEREIT`, wenn:

1. Zustellbarkeitsgate grün ist
2. jeder Empfänger und jede Organisation individuell geprüft sind
3. Quelle, Segment, rechtlicher Kontext und Pitchwinkel vorliegen
4. Opt-outs, Absagen und Bounces berücksichtigt sind
5. Absender, Format, Link und Assetversion verifiziert sind
6. vollständige Entwürfe und Freigabestatus sichtbar sind
7. Dokumentation und Readback nach Versand vorgesehen sind

Eine vorbereitete Welle ist nicht gleichbedeutend mit versendet.
