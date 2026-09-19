# Claim Ledger Schema

## Zweck

Das Ledger ist die interne Quelle fuer verifizierte Aussagen. Das Bilderstellungstool darf sichtbaren Text aus dem Ledger rendern, aber keine neue Zahl, Aussage, Quelle oder Zuschreibung erfinden oder inhaltlich veraendern.

## Struktur

```json
{
  "series_id": "example-series",
  "locale": "de-AT",
  "claims": [
    {
      "id": "C01",
      "type": "fact",
      "status": "verified",
      "approved_text": "Die gepruefte Zahl betraegt 14,70 Mio. Euro.",
      "poster_source": "Quelle: Primaerquelle, 2026",
      "source_tier": "A",
      "source_note": "Titel, Abschnitt oder Fundstelle",
      "source_url": "https://example.invalid/source",
      "retrieved_at": "2026-09-03",
      "risk": "medium"
    }
  ]
}
```

## Claim-Typen

- `fact`
- `auditor_finding`
- `attributed_statement`
- `quote`
- `political_opinion`
- `question`
- `call_to_action`
- `unverified`
- `blocked`

## Status

- `verified`
- `opinion`
- `open_question`
- `unverified`
- `blocked`

Harte Tatsachenclaims brauchen `verified`, Source Tier `A` oder `B`, `source_note` und `poster_source`.

`unverified` und `blocked` nie in faktischen sichtbaren Endtext uebernehmen.

## Quellen-Tiers

- `A`: Primaerquelle, Gesetz, offizieller Bericht, amtliche Statistik, Originaldokument
- `B`: verlaessliche institutionelle Sekundaerquelle oder belastbare Fachquelle
- `C`: serioese Medien- oder Kontextquelle
- `D`: Partei, Verband, Social Media oder unbestaetigte Position

## Bildtool-Regel

Nach jeder Bildausgabe sichtbare Claims erneut mit `approved_text` und `poster_source` abgleichen. Typografische Modellfehler gelten als inhaltlicher Fehler und muessen mit demselben Bilderstellungstool korrigiert werden.
