# Retry Policy

## Grundsatz

Nur den fehlerhaften Slot mit dem normalen ChatGPT-Bilderstellungstool korrigieren. Kein anderes Bildwerkzeug als Fallback.

## Fehlerklassen

- `CONTENT`: Claim, Zahl, Quelle oder Formulierung falsch
- `CONCEPT`: Bildidee generisch, symbolisch oder unpassend
- `IMAGE`: Artefakt, Anatomie, Logo, Fake-Evidence, Blur
- `LAYOUT`: Hierarchie, Text-Bild-Verhaeltnis oder Balance schlecht
- `TYPE`: Schreibfehler, falscher Zeilenumbruch, Textfit oder Lesbarkeit
- `DESIGN`: Rohfoto, fehlende Headline, fehlendes grafisches Signal oder Abweichung von der Ivory-Rot-Graphit-Referenz-DNA
- `SERIES`: Wiederholung oder Style-Drift

## TYPE Retry

1. Bestehendes Bild mit `image_gen` editieren.
2. Exakt die fehlerhafte Textstelle und die korrekte Schreibweise angeben.
3. Restliche Komposition unveraendert verlangen.
4. Vollstaendigen Text erneut pruefen.
5. Nach zwei erfolglosen Text-Edits den Slot mit vereinfachter Typografie, aber gleicher Referenz-DNA neu erzeugen.

## DESIGN Retry

Wenn das Ergebnis nur ein Foto, ein Hintergrundbild oder eine zu schwach gestaltete Grafik ist:

1. Nicht versuchen, spaeter extern Text einzusetzen.
2. Den Slot mit `image_gen` neu erzeugen.
3. Den Pflichtstart aus `image-prompt-patterns.md` erneut vollstaendig verwenden.
4. Ivory- oder Cremegrundflaeche, Signalrot, Graphit, grosse Grotesk-Typografie, Textposition, Bildzone und rotes grafisches Signal explizit nennen.
5. Ausdruecklich schreiben: `Kein Rohfoto. Kein leerer Platz fuer spaetere Schrift. Alle Texte und Designelemente muessen im finalen Bild sichtbar sein.`
6. Erst freigeben, wenn die Referenz-DNA auf den ersten Blick erkennbar ist.

## IMAGE oder LAYOUT Retry

1. Fehlerursache konkret benennen.
2. Nur notwendigen Bereich oder die Komposition mit `image_gen` korrigieren.
3. Referenz-DNA und sichtbare Typografie dabei unveraendert beibehalten.
4. Wenn Edit instabil ist, Slot neu erzeugen.
5. Nach maximal fuenf gescheiterten Versuchen Slot nicht freigeben.

## Nicht tun

- externen Textlayer setzen
- Python, SVG, Canvas, Adobe oder Firefly zur Reparatur verwenden
- Rohfoto als akzeptable Zwischenloesung freigeben
- freie Textzone fuer spaeter akzeptieren
- Collage croppen
- Restschrift uebermalen
- Blur zur Fehlerkaschierung
- Fake-Dokument unlesbar machen statt entfernen
- alle zehn Slots neu erzeugen, wenn nur einer fehlschlaegt
