# Quellenrouting Österreich

## Grundsatz

Immer die fachlich zuständige Primärquelle bevorzugen. data.gv.at primär als nationalen Discovery- und Metadaten-Layer behandeln.

## Routing-Tabelle

| Bedarf | Primärquelle | Zweitquelle / Discovery | Hinweise |
| --- | --- | --- | --- |
| allgemeine Open-Data-Suche | data.gv.at Piveau | Herausgeberportal | Danach Originaldistribution wählen |
| amtliche Statistik | data.statistik.gv.at | data.gv.at | STATcube REST API kann Abo und API-Key erfordern |
| parlamentarische Gegenstände | parlament.gv.at Open Data | data.gv.at | JSON-Export und datensatzspezifische Filter-APIs bevorzugen |
| Rechtsinformation | RIS | data.gv.at | ELI, Dokumentnummer und Fassung erhalten |
| Geodaten | zuständige Behörde, Land, Gemeinde, Geoland/OGC | data.gv.at | WFS/GeoJSON vor PDF, CRS dokumentieren |
| kommunale Daten | offizielle Gemeinde oder Land | data.gv.at | Gebietsstand und Gemeindekennziffer prüfen |
| Bundesdaten | zuständiges Ministerium oder Behörde | data.gv.at | Originalquelle vor Spiegel |

## Statistik Austria

Open-Data-Portal: `https://data.statistik.gv.at`

Geeignet für frei verfügbare, maschinenlesbare Datensätze. Metadaten enthalten häufig eindeutige Identifikatoren, Aktualisierungsdaten, Attributbeschreibungen und CSV-Distributionen.

STATcube REST API nur als getrennten Zugangsweg behandeln. Vor Nutzung prüfen, ob ein aktives Abonnement und API-Key vorhanden sind.

## Parlament

Open-Data-Einstieg: `https://www.parlament.gv.at/recherchieren/open-data`

Filter- und Exportseiten liefern datensatzspezifische API-Angaben. Detailseiten können systematisch als JSON verfügbar sein. Niemals API-Parameter eines Datensatztyps ungeprüft auf einen anderen übertragen.

## RIS

Für Rechtsdaten stabile Rechtsidentifikatoren bewahren. Bei konsolidierten Normen sowohl aktuelle Fassung als auch maßgeblichen Stichtag festhalten. Historische Fassung und aktuelle Konsolidierung getrennt behandeln.

## Länder und Gemeinden

Bei regionalen Daten zusätzlich Gemeindekennziffer, Bezirk, Bundesland und Gebietsstand erfassen. Namensgleiche Gemeinden oder historische Gebietsstände nie nur über Klartextnamen verbinden.
