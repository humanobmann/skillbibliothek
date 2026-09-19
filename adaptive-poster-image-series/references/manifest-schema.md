# Release Manifest Schema v4

## Zweck

Nur Metadaten der mit dem Bilderstellungstool erzeugten Endbilder dokumentieren. Kein Asset-Handoff und keine Vektormaster.

```json
{
  "series_id": "example-series",
  "image_tool_only": true,
  "masters": [
    {
      "slot": 1,
      "file": "01.png",
      "aspect_ratio": "4:5",
      "render_strategy": "photo_editorial",
      "visual_reviewed": true,
      "text_exact": true
    }
  ],
  "facebook_publications": []
}
```

Exakt zehn Mastereintraege. `image_tool_only` muss `true` sein.
