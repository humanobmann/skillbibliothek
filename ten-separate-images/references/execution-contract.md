# Ausführungsvertrag

## Zustandsmodell

Jeden Slot nach diesem Modell führen:

```text
pending -> active -> inspecting -> valid
                \-> retry ------/
```

Nur `valid` zählt als fertige Ausgabe.

## Harte Regeln

1. Exakt zehn gültige Slots verlangen.
2. Einen Bildaufruf pro Slot nacheinander ausführen.
3. Wiederholungen nur für den aktuell fehlerhaften Slot durchführen.
4. `n=1` verwenden.
5. Nie zwei Inhaltsquellen oder zwei Briefings in denselben Aufruf geben.
6. Nie mehrere Aufrufe parallel senden.
7. Nie eine Datei mit mehreren Panels mehrfach zählen.
8. Bereits gültige Slots unverändert lassen.
9. Ergebnisreferenzen eindeutig halten.
10. Erst nach zehn bestandenen Slots abschließen.

## Warum nicht exakt zehn Werkzeugaufrufe

Ein fehlerhafter Aufruf muss wiederholt werden können. Deshalb gilt:

```text
Werkzeugaufrufe = mindestens 10
Gültige Ausgaben = exakt 10
```

Die frühere Formulierung „exakt zehn Werkzeugaufrufe“ ist mit Wiederholungen unvereinbar und darf nicht verwendet werden.

## Serielle Ausführung

Das nächste Bildwerkzeug erst aufrufen, nachdem das vorige Ergebnis zurückgegeben und geprüft wurde. Dadurch bleiben Zielbild, Slotnummer und Fehlerbehandlung eindeutig.

## Wiederherstellung

### Mehrfachbild oder Collage

Ergebnis verwerfen. Slot auf `retry` setzen. Den Aufruf mit nur der aktuellen Quelle, `n=1` und einer noch kürzeren Slotkapsel wiederholen.

### Falsche Quelle

Nur die aktuelle Referenz-ID übergeben. Andere Batchquellen entfernen. Slot wiederholen.

### Falscher oder beschädigter Text

Das gültige Bildmotiv behalten, sofern möglich. Exakten Text anschließend deterministisch setzen. Nicht alle anderen Slots neu generieren.

### Technischer Fehler

Slot auf `retry` lassen. Bereits gültige Ergebnisse nicht verändern.

### Nahezu identische Varianten

Nur den späteren Slot mit einer deutlich anderen Perspektive, Handlung, Brennweite oder Komposition wiederholen.
