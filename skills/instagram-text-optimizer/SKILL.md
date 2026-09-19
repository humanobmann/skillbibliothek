---
name: instagram-text-optimizer
description: Überarbeite kurze Instagram-Captions für Feed, Carousel oder Reel mit klarer Kernbotschaft, mobiler Lesbarkeit, transparenter Textlänge und verpflichtender aktueller Hashtag-Recherche. Verwenden bei persönlichen, Vereins-, politischen, Kampagnen- oder Informationsposts für Instagram. Keine Reichweitenversprechen, erfundenen Trenddaten oder unpassenden Hashtag-Blöcke erzeugen.
---

# Instagram Text Optimizer

## Auftrag

Erstelle eine kurze, eigenständige Caption, die das Medium ergänzt statt es zu wiederholen. Optimiere für Klarheit, Vertrauen und Anschluss an die vorhandene Zielgruppe; nicht für vermeintliche Algorithmus-Tricks. Der Skill veröffentlicht nichts.

## Routing

1. Bei aktuellen oder strittigen Aussagen zuerst Recherche bzw. `politik-analyse`; bei einem fertigen Text mit prüfbaren Claims als letzten Sachpass `fact-check` nutzen.
2. Bei Peter Schullers Rollenkommunikation zuerst den politischen oder Vereins-Rollenskill einsetzen.
3. Nutze genau einen Plattform-Optimierer: Instagram statt Facebook.
4. `humanizer-de` ist nur ein optionaler Stil-Endpass und darf keinen Claim verstärken.
5. Bei Algorithmus-, Reichweiten-, Reel-, Explore- oder Maximaloptimierung `social-platform-algorithm-core` als Evidenzschicht verwenden.

## Format und Länge

Bestimme Feed, Carousel oder Reel. Fehlt die Angabe, verwende **Feed** und nenne die Annahme knapp.

- Reel oder starkes Einzelmotiv: 150–300 Zeichen Haupttext ohne Hashtags.
- Feed oder Carousel: 300–700 Zeichen Haupttext ohne Hashtags.
- Bis 1.000 Zeichen nur, wenn geprüfter Kontext sonst irreführend verloren ginge.
- Die ersten sichtbaren Zeilen tragen Kernaussage und Nutzen. Kein künstlicher Cliffhanger, keine Wiederholung des Bildtexts ohne Mehrwert.

## Arbeitsweise

1. Bestimme Zielgruppe, Format, Kommunikationsziel und eine Kernbotschaft.
2. Prüfe materielle Aussagen: Fakt, Attribution, Einordnung, Meinung oder Forderung.
3. Baue Caption als Hook mit Aussage -> konkrete Bedeutung oder Kontext -> natürlicher Schluss bzw. passende Handlung.
4. Kürze zuerst Wiederholungen, Nebenthemen und Leerformeln; nicht notwendige Fakteneinschränkungen.
5. Prüfe Stimme, mobile Scannbarkeit, Bild-Text-Passung, Rechte/Marken sowie bei politischen Texten Kontextverlust, Kausalität und Angriffsfähigkeit.\n6. Bei Reels zusaetzlich erste Sekunden, fruehe Skips, Watch Time, Completion, Shares/Sends und Originalitaet pruefen, soweit aktuell offiziell dokumentiert.\n7. Bei Feed/Explore zusaetzlich Save-Wert, Betrachtungsdauer, Themenpassung und Empfehlungseignung pruefen.

## Verpflichtende Hashtag-Recherche

Für **jeden** Instagram-Auftrag die aktuelle Recherche nach [Hashtag-Protokoll](references/hashtag-research-protocol.md) durchführen. Wähle standardmäßig drei bis fünf Tags mit echter Themen-, Sprach-, Orts- oder Kampagnenpassung.

- Keine erfundenen Trend-, Reichweiten- oder Volumenangaben.
- Keine generischen oder irrelevanten Reichweiten-Tags. Hashtags dienen primaer Kontext und Auffindbarkeit; sie ersetzen weder Originalitaet noch Retention, Saves oder Shares.
- Keine problematischen, gesperrten oder inhaltlich missverständlichen Tags, soweit dies aktuell prüfbar ist.
- Ist Live-Recherche nicht möglich oder kein Tag tragfähig, offen nennen und keine Pseudorecherche ausgeben.

### Offline-Fallback

Ohne Live-Recherche wird weder Popularität noch Aktualität, Sperrfreiheit oder Reichweitenwirkung eines Hashtags behauptet. Kennzeichne die Einschränkung im Recherchehinweis und verwende nur Tags, deren rein semantische Passung aus dem Auftrag eindeutig ist—oder liefere keine Hashtag-Zeile.

## Politische und sensible Beiträge

Trenne Fakt, Einordnung, Wertung und Forderung. Politische Sichtbarkeit ist personalisiert und nicht garantierbar; die Caption soll bestehende und passende Zielgruppen klar informieren, nicht Nicht-Follower-Reichweite versprechen. Keine unbelegte Schuld-, Motiv- oder Kausalbehauptung und keine irreführende Kürzung.

## Ausgabe

Wenn nur die Caption verlangt wird, liefere Caption einschließlich der ausgewählten Hashtags. Sonst:

1. **Instagram-Caption** mit Hashtags am Ende
2. **Format:** Feed, Carousel oder Reel; Annahme nur falls nötig
3. **Länge:** Haupttext: Zeichen/Wortzahl; Hashtags: Zeichen/Wortzahl; Gesamt: Zeichen/Wortzahl
4. **Hashtag-Recherche:** Prüfdatum, Suchbasis, ausgewählte Tags und höchstens eine relevante Einschränkung
5. **Faktenstatus:** `geprüft`, `keine prüfbaren Aussagen`, `Prüfung empfohlen` oder `Unsicherheit sichtbar formuliert`

Bei Audit oder maximaler Optimierung zusätzlich die kompakte [Scorecard](references/scorecard.md) und maximal drei Befunde ausgeben.

## Qualitätsgates

- Eine Kernbotschaft ist innerhalb der ersten sichtbaren Zeilen verständlich.
- Textlänge passt zum Format oder eine notwendige Ausnahme ist benannt.
- Caption ergänzt das Medium, erfindet aber keine Details dazu.
- Materiale Claims sind belegt, begrenzt oder klar unsicher.
- Hashtag-Recherche ist aktuell dokumentiert oder ihre fehlende Verfügbarkeit transparent.
- Keine Engagement-Manipulation, kein Clickbait, keine gefälschten Metriken und keine zufälligen Hashtags.
