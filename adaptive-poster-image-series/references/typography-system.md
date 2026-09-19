# Typography System for Image-Tool Rendering

## Grundsatz

Die finale Typografie wird direkt vom normalen ChatGPT-Bilderstellungstool im Endbild erzeugt. Kein externer Textlayer und kein SVG-Fallback.

Typografie ist in diesem Skill ein verpflichtender Bestandteil des finalen Designs, nicht ein spaeterer Zusatz.

## Referenzhierarchie

Standardmaessig an der freigegebenen Referenz-DNA orientieren:

1. kleinerer Kicker oder erste Headline-Zeile in Signalrot
2. sehr grosse Hauptphrase oder grosses Schluesselwort in Signalrot oder Ink
3. kompakte Subline in dunklem Graphit
4. kurze Quellenkennung nur wenn notwendig

Moderne fette Grotesk-Typografie verwenden. Keine dekorative Display-Schrift, keine Serifenschrift als Standard und keine Effekt-Typografie.

## Position

Bei 4:5 normalerweise:

- Textblock linksbuendig
- linker Rand ungefaehr 7 bis 9 Prozent
- oberer Rand ungefaehr 6 bis 9 Prozent
- Haupttypografie im oberen Drittel bis oberen 45 Prozent
- grosse Hauptphrase darf 50 bis 85 Prozent der nutzbaren Breite einnehmen
- Bild und Grafik duerfen die untere Textkante dynamisch beruehren, Text aber nicht ueberdecken

## Headline-Regeln

1. Headline ist sichtbar und dominant.
2. Normalerweise ein bis drei Zeilen, vier nur wenn unvermeidbar.
3. Bewusste Zeilenumbrueche aus `headline_lines` exakt uebernehmen.
4. Keine automatische Silbentrennung verlangen.
5. Kein winziger Headline-Block ueber einem dominanten Foto.
6. Keine 3D-, Neon-, Outline-, Grunge- oder Schlagschatten-Schrift als Standard.
7. Text nicht in perspektivisch verzerrte Flaechen zwingen.

## Textmenge

Je weniger Text, desto hoeher die Chance auf perfekte Darstellung. Bei frei entwickeltem Content lieber auf mehrere Slots verteilen.

Bei vom Nutzer vorgegebenem Text nichts still kuerzen. Wenn die Menge problematisch ist, Bildanteil reduzieren und der Typografie mehr Raum geben.

## Pflicht

Fehlende sichtbare Headline, bloss freigelassene Textzone oder Rohfoto ohne fertig integrierte Schrift sind Hard Fail.

## Text-QA

Nach jeder Ausgabe Wort fuer Wort und Zeichen fuer Zeichen kontrollieren:

- Umlaute
- Bindungen
- Zahlen
- Prozentzeichen
- Kommas und Punkte
- Namen
- Anfuehrungszeichen
- Quellenkennung

Ein Fehler bedeutet Retry mit dem Bilderstellungstool.
