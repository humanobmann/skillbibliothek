# Connector-Playbook

## Auswahlregel

Connectoren dynamisch nach benötigter Fähigkeit auswählen. Namen in Beispielen sind keine Verfügbarkeitszusage. Vor Nutzung prüfen, ob der konkrete Connector in der aktuellen Umgebung vorhanden, verbunden und für die benötigte Lese- oder Schreibaktion geeignet ist.

## Preflight

1. Quelle, Zielsystem und benötigte Daten bestimmen.
2. Passenden vorhandenen Connector suchen.
3. Mit einer minimalen Leseaktion Zugriff, Objektidentität und Datenumfang verifizieren.
4. Führendes System pro Datentyp festlegen.
5. Schreibklasse, Reversibilität, Duplikatrisiko und Verifikationsweg bestimmen.
6. Erst danach den Workflow ausführen oder als Entwurf dokumentieren.

Bei fehlendem Zugriff keine benachbarte App auf Verdacht verwenden. Keine Rechte, Felder oder APIs erfinden.

## Fähigkeitsmatrix

| Fähigkeit | Typische Systeme | Lesen | Schreiben |
|---|---|---|---|
| E-Mail | Outlook, Gmail oder anderer verbundener Maildienst | Nachrichten, Threads, Anhänge, Status | Entwurf, Antwort, Versand, Markierung |
| Kalender | verbundener Kalender | Termine, Verfügbarkeit, Fristen | Termin, Erinnerung, Einladung |
| Aufgaben | verbundenes Aufgaben- oder Projekttool | Status, Verantwortliche, Fälligkeit | Aufgabe, Unteraufgabe, Statusupdate |
| CRM | HubSpot, CiviCRM oder anderes bestätigtes CRM | Kontakt, Unternehmen, Aktivität, Einwilligung | Notiz, Aufgabe, Status, Zuordnung |
| Dateien | SharePoint, Google Drive, Library oder Repository | suchen, lesen, Version prüfen | erstellen, aktualisieren, verschieben |
| Teamkommunikation | Teams, Slack oder anderer Dienst | Threads, Entscheidungen, offene Punkte | Nachricht, Zusammenfassung, Reminder |
| Entwicklung | GitHub oder anderes Repositorysystem | Code, Issues, Pull Requests | Issue, Kommentar, Dateiänderung |
| Design | Canva, Adobe oder Figma | bestehende Designs und Assets | Entwurf, Variante, Export |

Nur tatsächlich verfügbare Systeme verwenden. Finanz-, Zahlungs-, Spenden-, Gesundheits-, Rechts- und Mitgliedsdaten als besonders sensibel behandeln.

## Idempotenz

Vor Erstellung eines Objekts einen Schlüssel aus Zielsystem, Zielkontext, normalisierter Aktion und externer Referenz bilden. Nach vorhandenen offenen oder aktiven Treffern suchen, wenn Duplikate relevant sind. Einen ähnlichen Treffer aktualisieren oder verlinken statt neu anlegen.

Nach jedem Write Toolbestätigung oder Readback prüfen. Bei unbekanntem Ergebnis den Zielzustand lesen, bevor ein Retry erfolgt.

## Freigaben

* Lesen und lokale Analyse: innerhalb des Nutzerauftrags autonom
* Entwurf oder lokaler Workflowplan: autonom
* reversible externe Änderung: nur bei konkretem Umsetzungsauftrag
* Versand, Veröffentlichung, Einladung, Massenaktion, Zahlung, Löschung oder schwer reversible Änderung: exakte Vorschau und erforderliche Bestätigung

Strengere Regeln des Zielsystems oder Fachskills gehen vor.

## Sichere Degradation

Wenn ein Connector fehlt oder nur lesen kann:

1. erreichbaren Teil vollständig liefern
2. fehlende Fähigkeit konkret nennen
3. ausführbaren manuellen Schritt oder Importformat anbieten
4. keinen technischen Erfolg behaupten
