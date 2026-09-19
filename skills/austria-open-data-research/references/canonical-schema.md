# Kanonisches Datenmodell

## Dataset-Metadaten

```json
{
  "dataset_id": "string",
  "title": "string",
  "publisher": "string",
  "description": "string|null",
  "issued_at": "ISO-8601|null",
  "modified_at": "ISO-8601|null",
  "retrieved_at": "ISO-8601",
  "temporal_coverage": {
    "from": "ISO-8601|null",
    "to": "ISO-8601|null"
  },
  "spatial_coverage": {
    "type": "string|null",
    "codes": [],
    "label": "string|null"
  },
  "license": "string|null",
  "keywords": [],
  "catalog_source": "string|null",
  "primary_source": "string",
  "distributions": [
    {
      "url": "string",
      "format": "string|null",
      "media_type": "string|null",
      "modified_at": "ISO-8601|null",
      "checksum_sha256": "string|null"
    }
  ],
  "provenance": {
    "retrieval_method": "api|download|wfs|jsonld|other",
    "transformation_notes": [],
    "warnings": []
  }
}
```

## Beobachtungsdaten

Bei zusammengeführten Kennzahlen zusätzlich mindestens führen:

```json
{
  "indicator": "string",
  "value": 0,
  "unit": "string",
  "reference_period": "string",
  "geography_code": "string|null",
  "geography_name": "string|null",
  "source_dataset_id": "string",
  "source_url": "string",
  "source_modified_at": "ISO-8601|null",
  "retrieved_at": "ISO-8601",
  "status": "final|provisional|revised|unknown"
}
```

## Verbindungsregeln

Zeitreihen nicht allein über Titel verbinden. Stabile IDs, Variablencodes und dokumentierte Definitionen verwenden.

Gemeinden nicht nur über Namen verbinden. Offizielle Gemeindekennziffer oder äquivalenten stabilen Gebietscode verwenden und Gebietsstand mitführen.

Prozentwerte, Indizes, absolute Werte und Raten nie ohne explizite Einheiten normalisieren.
