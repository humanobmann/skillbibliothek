# Image Tool Only Generation Contract

## Exklusiver Produktionsweg

Jede finale Bilddatei ausschliesslich mit dem normalen ChatGPT-Bilderstellungstool `image_gen` erzeugen oder bearbeiten.

Nicht fuer Bildproduktion verwenden:

- SVG oder Vektor-Renderer
- HTML oder Canvas
- Python oder PIL
- Inkscape
- Adobe, Photoshop, Express oder Firefly
- andere Bildgeneratoren oder externe Renderer
- programmgesteuertes Cropping, Beschriften, Resizing oder Compositing

Skripte duerfen nur Textdaten und vorhandene Dateien pruefen.

## Designvertrag

Vor jedem Bildaufruf [reference-design-dna.md](reference-design-dna.md) anwenden.

Jede Ausgabe muss bereits das fertige Poster sein. `image_gen` darf nicht nur ein Basisfoto, Hintergrundbild oder eine Textzone fuer spaetere Bearbeitung liefern.

Standardmaessig gilt:

- `design_lock=true`
- `design_required=true`
- `raw_photo_forbidden=true`
- `visible_text_required=true`
- `full_design_required=true`

## Pro Aufruf

1. Exakt einen Slot bearbeiten.
2. Exakt ein Bild erzeugen oder editieren: `n=1`.
3. Nur die diesem Slot zugeordneten Referenzbilder verwenden.
4. Andere Slots nicht im Bildauftrag erwaehnen.
5. Eine einzige, eigenstaendige Endkomposition verlangen.
6. Exakten sichtbaren Text aus dem Produktionsplan angeben.
7. Exakte Textposition, Hierarchie und Zeilenumbrueche angeben.
8. Die Referenz-DNA explizit in den Bildauftrag schreiben.
9. Mindestens ein sichtbares grafisches Gestaltungsmittel verlangen.
10. Zielseitenverhaeltnis direkt anfordern.
11. Keine erfundenen Logos, Dokumente oder Beweismittel zulassen.
12. Ergebnis unmittelbar visuell pruefen.

## Referenzisolation

Bei zehn hochgeladenen Vorlagen gilt strikt Quelle 1 zu Slot 1, Quelle 2 zu Slot 2 usw. Niemals mehrere Vorlagen gleichzeitig an einen Einzelbild-Aufruf geben, ausser der Nutzer verlangt ausdruecklich eine echte Kombination innerhalb desselben Motivs.

Die drei freigegebenen Stilbeispiele definieren nur die Design-DNA. Ihre Texte, Personen, Flaggen, Landschaften und konkreten Bildinhalte nicht automatisch reproduzieren.

## Textfehler

Falsche Buchstaben, erfundene Woerter, vertauschte Zahlen, schlechte Umlaute oder zusaetzliche Schrift sind Hard Fail.

Korrektur ausschliesslich mit `image_gen`:

1. vorhandenes Bild als Editierziel verwenden
2. nur die konkrete fehlerhafte Textstelle benennen
3. restliche Komposition unveraendert verlangen
4. Ausgabe erneut vollstaendig pruefen

Wenn zwei Textkorrekturen scheitern, denselben Slot mit vereinfachter Typografie neu erzeugen. Keine externe Textueberlagerung verwenden.

## Hard Fail

- Rohfoto oder reines Hintergrundbild
- freigelassene Textzone statt fertiger Typografie
- sichtbare Headline fehlt
- grafisches Editorialdesign fehlt
- Referenz-DNA nicht erkennbar
- Collage oder Multi-Panel
- mehrere Slots in einer Datei
- falscher sichtbarer Text
- Fake-Evidence
- ungefragtes Branding
- grobe Anatomie- oder Objektfehler
- irrefuehrende visuelle Schuldzuweisung
- generischer KI-Werbelook
- unlesbare mobile Typografie
