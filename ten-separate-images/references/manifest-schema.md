# Slotmanifest

## Struktur

Das Manifest enthält exakt zehn Einträge:

```json
{
  "version": 2,
  "expected_outputs": 10,
  "mode": "ten-sources",
  "requested_aspect": "4:5",
  "items": [
    {
      "slot": 1,
      "source_id": "file_source_01",
      "source_path": "",
      "brief": "",
      "instruction": "Bearbeite nur die aktuelle Quelle als ein einzelnes Hochformat.",
      "output_name": "01.png",
      "status": "pending",
      "attempts": 0,
      "tool_call_id": "",
      "output_file_id": "",
      "output_path": "",
      "review": {
        "single_scene": false,
        "correct_slot": false,
        "content_preserved": false,
        "requirements_met": false,
        "no_cross_slot_leakage": false,
        "no_unrequested_text": false,
        "no_unrequested_branding": false,
        "technical_quality": false,
        "passed": false
      }
    }
  ]
}
```

## Regeln

1. `expected_outputs` muss 10 sein.
2. `items` muss exakt zehn Einträge enthalten.
3. `slot` muss genau die Zahlen 1 bis 10 enthalten.
4. Pro Slot mindestens `source_id`, `source_path` oder `brief` befüllen.
5. Eine Quelle als einzelner String erfassen, niemals als Liste.
6. `output_name` eindeutig und mit zweistelliger Slotnummer beginnen lassen.
7. Nur einen Slot gleichzeitig auf `active` setzen.
8. Nach bestandener Prüfung `status` auf `valid` setzen.
9. Ergebnisreferenzen und Dateipfade eindeutig halten.
10. Sämtliche Prüffelder nur nach tatsächlicher Sichtprüfung auf `true` setzen.
