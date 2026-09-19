# Publication Plan Schema v3

## Struktur

```json
{
  "platform": "facebook",
  "mode": "trio",
  "source_series": "example-series",
  "selected_slots": [1, 4, 8],
  "primary_slot": 1,
  "aspect_ratio": "1:1",
  "target_width": 1080,
  "target_height": 1080,
  "image_tool_only": true,
  "design_system": "civic_editorial_red_ivory",
  "design_reference_profile": "austria-editorial-civic-v1",
  "design_lock": true,
  "safe_zone_profile": "square_1x1",
  "safe_area_px": {"left": 90, "right": 90, "top": 90, "bottom": 90},
  "recompose_not_crop": true,
  "official_platform_safe_zone": false,
  "sequence": [
    {"slot": 1, "function": "hook"},
    {"slot": 4, "function": "evidence"},
    {"slot": 8, "function": "close"}
  ],
  "primary_message": "Die Kernaussage von Bild 1.",
  "first_frame_reason": "Bild 1 erklaert Thema und Konflikt ohne Folgekarte.",
  "continuation_logic": "Bild 2 vertieft, Bild 3 schliesst.",
  "gallery_reason": null,
  "platform_assumption": "Square multi-image composition chosen for robust readability.",
  "verified_on": "2026-09-05",
  "source_type": "current platform research",
  "confidence": "medium"
}
```

## Modi und Bildanzahl

- `single`: exakt 1 Slot, 4:5
- `pair`: exakt 2 Slots, 1:1
- `trio`: exakt 3 Slots, 1:1
- `quad`: exakt 4 Slots, 1:1
- `gallery`: 5 bis 10 Slots
- `auto`: nur als Planungszustand; vor Bildproduktion in einen konkreten Modus aufloesen

## Designbindung

Jede Facebook-Adaption bleibt an dasselbe Designprofil wie die Masterserie gebunden:

- `design_system` muss mit dem Production Plan uebereinstimmen.
- `design_reference_profile` muss mit dem Production Plan uebereinstimmen.
- `design_lock` muss `true` sein.
- 1:1 Varianten werden neu komponiert, aber nicht stilistisch neu erfunden.
- Ivory, Signalrot, Graphit, grosse Grotesk-Typografie und das grafische Signal bleiben sichtbar.

## Regeln

- `primary_slot` muss in `selected_slots` enthalten sein.
- `sequence` muss dieselben Slots genau einmal enthalten.
- `image_tool_only` muss `true` sein.
- Pair, Trio und Quad muessen 1:1 verwenden.
- Single standardmaessig 4:5.
- Gallery braucht `gallery_reason` mit konkreter Begruendung.
- Bei Gallery duerfen zentrale unverzichtbare Aussagen nicht nur in spaeten Slots liegen.
- `safe_zone_profile` muss zum Seitenverhaeltnis passen: `feed_4x5` fuer 4:5, `square_1x1` fuer 1:1.\n- `safe_area_px` muss mindestens die Werte aus `platform-safe-zones.md` einhalten.\n- `recompose_not_crop` muss `true` sein.\n- `official_platform_safe_zone` muss `false` sein.
