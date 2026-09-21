# Platform Delivery Plan Schema v1

## Struktur

```json
{
  "series_id": "example-series",
  "delivery_mode": "full_social_30",
  "image_tool_only": true,
  "recompose_not_crop": true,
  "safe_zone_contract": "internal_conservative_v1",
  "official_platform_safe_zone": false,
  "outputs": [
    {
      "slot": 1,
      "variant": "feed_4x5",
      "file": "01-feed-4x5.png",
      "width": 1080,
      "height": 1350,
      "safe_area_px": {"left": 100, "right": 100, "top": 100, "bottom": 120},
      "hero_clearance_percent": 8,
      "motif_crop_reserve_percent": 12,
      "source_inside_safe_area": true,
      "recompose_not_crop": true
    }
  ]
}
```

## Modi

- `masters_only`: exakt zehn `feed_4x5` Ausgaben
- `full_social_30`: exakt dreissig Ausgaben, pro Slot genau `feed_4x5`, `square_1x1` und `vertical_9x16`

## Safe-Area-Werte

### `feed_4x5`

- 1080 x 1350
- aeusserster technischer Rand: keine kritische Information innerhalb der aeussersten 40 px
- links 100
- rechts 100
- oben 100
- unten 120

### `square_1x1`

- 1080 x 1080
- links 90
- rechts 90
- oben 90
- unten 90

### `vertical_9x16`

- 1080 x 1920
- links 90
- rechts 160
- oben 288
- unten 384

Alle Werte sind interne konservative Produktionsreserven und keine offiziellen Plattformangaben.

## Weitere Pflichtregeln

- `image_tool_only=true`
- `recompose_not_crop=true`
- `safe_zone_contract=internal_conservative_v1`
- `official_platform_safe_zone=false`
- `hero_clearance_percent >= 8`
- `motif_crop_reserve_percent >= 12`
- `source_inside_safe_area=true`
- Dateiname muss Slot und Variante eindeutig abbilden
- bei `full_social_30` muss jeder Slot genau drei Varianten besitzen
