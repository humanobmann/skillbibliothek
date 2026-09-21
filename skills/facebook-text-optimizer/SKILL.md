---
name: facebook-text-optimizer
description: Überarbeite Facebook-Beiträge und Captions für Klarheit, Glaubwürdigkeit, mobile Lesbarkeit und einen passenden Handlungsimpuls. Verwenden bei Facebook-Posts für persönliche, politische, Vereins-, Kampagnen- oder Informationskommunikation. Aktuelle oder strittige Aussagen vor einer Verstärkung prüfen; keine Reichweitenversprechen, Clickbait oder Engagement-Bait erzeugen.
---

# Facebook Text Optimizer

## Auftrag

Optimiere zuerst Nutzen, Klarheit, Belege und Stimme; Plattformwirkung folgt daraus und ist kein Trick. Bewahre explizite Rollen- und Stilvorgaben. Dieser Skill entwirft und prüft Texte, veröffentlicht aber nichts.

## Routing

1. Bei aktuellen, politischen, rechtlichen, wirtschaftlichen oder strittigen Aussagen zuerst belastbare Fakten klären; bei einem fertigen Text mit relevanten Claims `fact-check` als letzten Sachpass nutzen.
2. Für Peter Schullers politische oder Vereinsrolle zuerst den passenden Rollenskill verwenden.
3. `humanizer-de` nur einsetzen, wenn eine zusätzliche Natürlichkeitsredaktion verlangt wird; danach Claims erneut nicht stärken.
4. Nur diesen Plattform-Optimierer laden, niemals parallel `instagram-text-optimizer`.
5. Bei Algorithmus-, Reichweiten-, Format- oder maximaler Optimierungsfrage, Feed-Ranking, Originalitaet, Recommendation Eligibility oder Text-Bild-Strategie zwingend `social-platform-algorithm-core` und dessen kanonische [meta-feed-strategy.md](../social-platform-algorithm-core/references/meta-feed-strategy.md) als gemeinsame Evidenzschicht verwenden. Keine lokale, davon abweichende Algorithmus-Behauptung treffen.

## Arbeitsweise

1. Bestimme intern Beitragstyp, Zielgruppe, Zielhandlung und eine dominierende Kernaussage.
2. Erstelle für materielle Aussagen eine Claim-Karte: belegter Fakt, aktuelle Tatsache, Attribution, Schlussfolgerung, Meinung oder Forderung.
3. Überarbeite von außen nach innen: Kernbotschaft, sichtbarer Einstieg, Reihenfolge, Relevanz, Belege, Schluss, Stimme, Kürzung und Korrektur.
4. Prüfe bei Bild oder Video, ob Caption und Medium denselben Kern transportieren.
5. Führe bei politischer oder konflikthafter Kommunikation einen Gegencheck durch: Kontextverlust, schwächste Behauptung, Kausalität, Motivunterstellung, Verallgemeinerung und Screenshot-Risiko.

## Facebook-spezifische Regeln

- Die ersten ein bis drei sichtbaren Zeilen müssen Thema und Grund zum Weiterlesen vermitteln, ohne einen künstlichen Neugierdefekt zu bauen.\n- Bei algorithmischer Optimierung explizit auf Relevanz, vorhergesagte Betrachtungsdauer, Share-Wert, Originalitaet und negative Signale pruefen, soweit aktuell offiziell dokumentiert.
- Formuliere für Handy-Lesbarkeit: kurze Absätze, klare Subjekte, konkrete Folgen und nur ein Hauptjob pro Absatz.
- Ergänze fremde Inhalte durch eigene Einordnung, regionale Relevanz, überprüften Kontext oder konkrete Konsequenz. Keine nur minimal veränderte Übernahme. Meta beschreibt duplizierte oder nur geringfuegig veraenderte Inhalte als nachteilig fuer Empfehlungen; substantialer eigener Analyse- oder Informationswert ist vorzuziehen.
- Keine Forderung nach Likes, Kommentaren, Markierungen oder Teilen um der Interaktion willen. Eine Frage oder Aufforderung ist nur zulässig, wenn sie inhaltlich sinnvoll ist.
- Hashtags und Erwähnungen sind optional und nur bei echter Relevanz zulässig. Es gibt keine feste Ideal-Textlänge und keine garantierte Reichweite.
- Plattformwissen ist vergänglich: Bei ausdrücklicher Algorithmus-, Reichweiten- oder Richtlinienfrage die aktuelle offizielle Meta-Dokumentation nach [Plattform-Rechercheprotokoll](references/platform-research-protocol.md) und die gemeinsame Evidenzschicht `social-platform-algorithm-core` pruefen. Nie eine Empfehlung als garantierten Algorithmuseffekt darstellen.

## Politische und sensible Beiträge

- Trenne Fakt, Einordnung, Wertung und Forderung klar.
- Nenne Verantwortung, Absicht, Kausalität oder Schuld nur, soweit sie belegt ist.
- Kürze keine notwendige Einschränkung nur für einen stärkeren Hook.
- Bei Wahl-, Sozial-, Gesundheits-, Rechts- oder Sicherheitsbehauptungen: entweder prüfen, neutralisieren oder die Unsicherheit sichtbar machen.

## Ausgabe

Wenn nur ein Text verlangt wird, liefere ausschließlich den finalen Beitrag. Sonst in dieser Reihenfolge:

1. **Fertiger Facebook-Beitrag**
2. **Länge:** Zeichenzahl und Wortzahl des Beitrags
3. **Faktenstatus:** `geprüft`, `keine prüfbaren Aussagen`, `Prüfung empfohlen` oder `Unsicherheit sichtbar formuliert`
4. **Veröffentlichungscheck:** höchstens zwei konkrete Hinweise, nur wenn nötig

Bei Audit, Vergleich oder maximaler Optimierung zusätzlich eine kompakte Punktzahl aus [Scorecard](references/scorecard.md), die drei wichtigsten Befunde und anschließend die fertige Fassung liefern.

## Qualitätsgates

Ein Beitrag ist erst fertig, wenn:

- eine Kernaussage klar bleibt;
- Einstieg, Aufbau und Schluss die Kommunikationsaufgabe erfüllen;
- überprüfbare Aussagen belegt, begrenzt oder als offen markiert sind;
- Rolle, Ton und Absender stimmen;
- kein Clickbait, Engagement-Bait, erfundener Beleg oder unpassender Hashtag enthalten ist;
- Text und gegebenes Medium einander nicht widersprechen;
- Grammatik, Namen, Zahlen und Zeichen sauber sind.
