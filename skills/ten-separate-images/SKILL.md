---
name: ten-separate-images
description: "Erzeugt oder bearbeitet exakt zehn eigenständige Bilddateien in zehn getrennten, seriellen Slots. Verwenden bei Anfragen wie zehn Bilder, 10 Bilder, ten separate images, zehn Varianten, zehn hochgeladene Vorlagen, zehn Poster oder zehn Social Media Motive. Ordnet jede Quelle oder jedes Briefing genau einem Ausgabeslot zu, isoliert Bildreferenzen pro Werkzeugaufruf, verhindert Collagen, Raster, Kontaktbögen, Storyboards und Mehrfachpanels, prüft jede Ausgabe einzeln und beendet den Auftrag erst nach zehn unterschiedlichen gültigen Dateien. Regelt ausschließlich Trennung, Zuordnung, Ausführung und Kontrolle. Inhalt und visueller Stil kommen aus dem Nutzerauftrag oder einem zusätzlich aktiven Fachskill."
---

# Ten Separate Images

## Ergebnisvertrag

Exakt zehn gültige, eigenständige Bilddateien liefern.

Ein gültiger Slot besteht aus genau einer Datei mit genau einem beabsichtigten Motiv oder einer zusammenhängenden Szene. Eine Datei mit mehreren Bildern, Panels, Varianten, Ansichten oder Szenen ist ungültig und zählt nicht.

Zwischen gültigen Ausgaben und Werkzeugversuchen unterscheiden:

1. Exakt zehn gültige Ausgaben verlangen.
2. Mindestens zehn serielle Einzelbildaufrufe durchführen.
3. Wiederholungen dürfen die Zahl der Werkzeugaufrufe erhöhen.
4. Pro Aufruf nur einen Slot bearbeiten und nur eine Datei anfordern.
5. Niemals einen Gesamtaufruf für alle Slots verwenden.
6. Niemals mehrere Bildaufrufe parallel starten.
7. Niemals eine Collage oder Vorschau als Ersatz liefern.

## Vor Beginn laden

Diese Dateien lesen:

1. `references/execution-contract.md`
2. `references/image-gen-protocol.md`
3. `references/manifest-schema.md`
4. `references/quality-gate.md`

Bei verfügbarem Dateisystem ein Slotmanifest erzeugen und vor der Produktion prüfen:

```bash
python scripts/create_manifest.py --mode ten-sources --output batch.json
python scripts/validate_plan.py batch.json
```

## Eingabemodus festlegen

Genau einen Modus wählen:

1. **Zehn Quellen zu zehn Bearbeitungen:** Quelle 01 führt zu Ausgabe 01, Quelle 02 zu Ausgabe 02 und so weiter. In jedem Bildaufruf nur die aktuelle Quelle referenzieren.
2. **Ein Konzept zu zehn Varianten:** Nur notwendige Identitäts-, Produkt- oder Ortsreferenzen wiederverwenden. Perspektive, Aktion, Ausschnitt, Licht oder Moment sinnvoll variieren.
3. **Zehn Briefings zu zehn Bildern:** Pro Slot genau ein Briefing verwenden. Andere Briefings im aktuellen Aufruf nicht erwähnen.
4. **Eine Stilvorlage plus zehn Inhaltsquellen:** Den Stil zuerst in Textregeln übersetzen. Die Stilvorlage nicht als weiteren Inhaltsslot behandeln.
5. **Gemischter Auftrag:** Jedem Slot genau eine Inhaltsquelle oder genau ein Einzelbriefing zuordnen.

Zehn hochgeladene Bilder niemals stillschweigend als gemeinsame Stilcollage interpretieren.

## Zehn Slots anlegen

Vor dem ersten Bildaufruf intern die Slots 01 bis 10 anlegen. Pro Slot erfassen:

1. aktuelle Quelle, Dateiname oder Referenz-ID
2. Einzelbriefing
3. unveränderliche Merkmale
4. zulässige Variation
5. Format und Auflösung
6. verbotene Ergänzungen
7. geplanter Ausgabename
8. Status `pending`, `active`, `retry` oder `valid`
9. Werkzeugergebnis und Ausgabereferenz
10. Einzelprüfung

Immer nur einen Slot gleichzeitig auf `active` setzen.

## Jeden Slot seriell ausführen

Für Slot 01 bis Slot 10:

1. Nur den aktuellen Slot aktivieren.
2. Unmittelbar vor dem Bildwerkzeug eine knappe Slotkapsel setzen.
3. Nur die aktuelle Inhaltsquelle oder das aktuelle Einzelbriefing nennen.
4. Genau einen Bildaufruf mit `n=1` ausführen.
5. Das Ergebnis sofort visuell prüfen.
6. Nur bei bestandener Prüfung als `valid` markieren.
7. Bei Fehlern ausschließlich denselben Slot wiederholen.
8. Erst danach zum nächsten Slot wechseln.

Die Slotkapsel darf weder die Gesamtzahl noch andere Quellen oder Briefings enthalten.

Beispiel:

```text
Aktueller Bildschritt 04: Bearbeite nur Vorlage 04 als ein einzelnes Hochformat. Erhalte Person, Handlung und Kernaussage. Wende ausschließlich die für diesen Slot festgelegte Änderung an.
```

## Referenzen strikt isolieren

Bei zehn hochgeladenen Zielbildern pro Aufruf genau die Referenz-ID des aktuellen Zielbildes übergeben. Andere neun Zielbilder aus demselben Aufruf ausschließen.

Eine wiederkehrende Identitätsreferenz nur ergänzen, wenn sie für Kontinuität notwendig ist. Niemals andere Inhaltsquellen des Batches als Referenzen hinzufügen.

Mehrere Stilbeispiele zuerst als schriftliche Designspezifikation zusammenfassen. Möglichst keine mehrteilige Stiltafel an das Bildwerkzeug übergeben, weil sie Mehrfachausgaben begünstigen kann.

## Jede Ausgabe prüfen

Eine Ausgabe nur zählen, wenn alle Kriterien aus `references/quality-gate.md` erfüllt sind. Besonders prüfen:

1. genau eine zusammenhängende Szene
2. richtige Quelle oder richtiges Briefing
3. kein vermischter Inhalt aus anderen Slots
4. korrektes Format
5. geforderte Identität, Objekte, Textinhalte und Marken
6. keine unbeauftragten Texte, Logos oder Wasserzeichen
7. keine beschädigte Anatomie, Werkzeuge, Maschinen oder Produkte
8. ausreichende Abweichung zu anderen Slots, falls Varianten verlangt sind

Ein ungültiges Ergebnis erhöht den Zähler nicht.

## Abschluss technisch absichern

Bei verfügbarem Dateisystem das Ergebnismanifest aktualisieren und prüfen:

```bash
python scripts/validate_results.py batch.json --strict --report validation.json
```

Nur abschließen, wenn:

1. Slots 01 bis 10 auf `valid` stehen
2. zehn unterschiedliche Werkzeugergebnisse oder Dateireferenzen vorliegen
3. jede manuelle Einzelprüfung bestanden ist
4. vorhandene Dateien lesbar und technisch gültig sind
5. keine exakten Duplikate vorliegen

Die zehn Einzeldateien in numerischer Reihenfolge ausgeben. Eine zusätzliche Übersicht nur nach gesondertem Auftrag und erst nach erfolgreicher Lieferung der zehn Einzelbilder erstellen.
