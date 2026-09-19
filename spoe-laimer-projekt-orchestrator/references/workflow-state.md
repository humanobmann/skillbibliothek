# Workflow State, Idempotenz und Wiederaufnahme

## Wann State fuehren

Nur wenn mindestens eines gilt:

* mehr als zwei materielle Handoffs
* mindestens ein externer Write geplant
* Unterbrechung/Wiederaufnahme realistisch
* mehrere Systeme muessen abgeglichen werden
* hoher Risikostatus

## Minimaler Work State

* `goal`
* `context`
* `success`
* `risk`
* `data_class`
* `route`
* `sources_checked`
* `claims_open`
* `writes_planned`
* `writes_done`
* `authorizations`
* `blockers`
* `next_safe_step`

Keine umfangreiche interne Projektdatenbank erzeugen.

## Statusmodell

`planned -> ready -> executing -> verified -> complete`

Fehlerpfade: `blocked`, `partial`, `unknown_write_state`.

Ein Schritt darf erst `verified` werden, wenn sein fachliches Ergebnis oder externer Effekt ausreichend bestaetigt ist.

## Idempotenz

Vor wiederholbarem Write einen fachlich geeigneten Idempotenzschluessel bilden, zum Beispiel aus Zielsystem + Zielobjekt + normalisierter Aktion + externer Referenz. Vor Neuanlage nach bestehendem Objekt suchen, wenn Duplikate plausibel und relevant sind.

Bei `unknown_write_state` zwingend Readback oder Suche vor Retry.

## Handoff Packet

Nur uebergeben:

1. Teilschrittziel
2. relevante bestaetigte Eingaben
3. Claim-/Quellenstatus
4. Rolle und Datenklasse
5. erlaubte externe Aktion/Autorisierung
6. erwartetes Ausgabeformat
7. offene Unsicherheit

Keine kompletten Rohdaten, wenn minimierte Zusammenfassung reicht.

## Wiederaufnahme

1. letzte verifizierte Aktion identifizieren
2. aktuellen Zielsystemzustand lesen, wenn er sich geaendert haben koennte
3. erledigte Writes nicht wiederholen
4. Quellen-/Claimstatus auf Aktualitaet pruefen, wenn zeitkritisch
5. Blocker aktualisieren
6. beim naechsten sicheren Schritt fortsetzen

## Abschluss

State beenden, wenn Zieloutput geliefert, erforderliche Writes verifiziert und keine blockierende Unsicherheit offen ist. Dauerhaften Audit Trail nur speichern, wenn Nutzer oder Fachworkflow dies verlangt.
