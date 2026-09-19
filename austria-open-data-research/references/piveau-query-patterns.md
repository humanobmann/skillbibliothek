# Piveau Query Patterns

## Discovery

Basis der data.gv.at-Suche:

`https://www.data.gv.at/api/hub/search`

Eine aktuelle Suchroute kann beispielsweise unter `/search` liegen. Vor produktiver Nutzung OpenAPI oder Portal-Dokumentation prüfen.

Typische Suchparameter können enthalten:

- `q`
- `filters`
- `fields`
- `includes`
- `limit`
- `page`
- `aggregation`
- `scroll`
- `searchAfter`

Nicht alle Parameter oder Pfade blind hardcodieren. Instanzdokumentation prüfen.

## Projektion

Wenn nur wenige Felder benötigt werden, Rückgabe mit `includes` oder vergleichbarer Projektion begrenzen. So unnötige Metadaten und große Distributionseinträge vermeiden.

## Große Ergebnismengen

Normale Seitennummern können sich während laufender Indexänderungen verschieben. Für große stabile Durchläufe bevorzugen:

1. `searchAfter`, wenn verfügbar
2. `scroll`, wenn verfügbar
3. Hub Repo Harvesting für Katalog- und Metadatenvollerhebungen

## Hub Repo

Hub Repo unterstützt Dataset-Listen mit `limit` und `offset`; je nach Instanz kann `valueType=metadata` verwendet werden. Maximalwerte und unterstützte Response-Formate vor Abruf prüfen.

Beispielmuster:

`GET /api/hub/repo/datasets?valueType=metadata&limit=5000&offset=0`

Danach Offset erhöhen, bis keine weiteren Datensätze geliefert werden. Nicht aus einem Beispiel ableiten, dass jede produktive Instanz exakt denselben Host oder dieselbe maximale Seitengröße verwendet.

## Metadatenformate

DCAT-AP und Linked Data bevorzugen. JSON-LD ist für agentische Weiterverarbeitung meist praktikabel. RDF/XML oder Turtle verwenden, wenn semantische Verarbeitung oder vorhandene Toolchains dies erfordern.
