# Visual QA

## Grundsatz

Jede tatsaechliche Endausgabe einzeln ansehen. Kein JSON, Score oder Dateitest ersetzt die visuelle Pruefung.

## Hard Gates pro Bild

- genau ein eigenstaendiges Bild
- vollstaendig fertig gestaltetes Editorialposter
- sichtbare Headline vorhanden
- kein Rohfoto oder blosses Hintergrundbild
- keine freie Textzone fuer spaeteren Einbau
- Referenz-DNA aus Ivory oder Creme, Signalrot, Graphit und grosser Grotesk-Typografie sichtbar
- mindestens ein bewusstes rotes grafisches Signal integriert
- thematischer Bild- oder Grafikinhaltsbereich sauber in die Gestaltung eingebunden
- keine Collage, kein Grid, kein Multi-Panel
- sichtbarer Text exakt
- Zahlen, Namen und Zuordnungen exakt
- keine zusaetzlichen erfundenen Woerter
- kontrollierter deutscher Zeilenumbruch
- keine abgeschnittene Typografie
- mobile Lesbarkeit
- ausreichender Kontrast
- sichere Innenraender gemaess aktivem Safe-Zone-Profil
- Hero-Zahl oder dominantes Keyword mit mindestens 8 % optischer Reserve
- zentraler Motivkern mit mindestens 12 % Crop-Reserve
- Quellenzeile vollstaendig innerhalb des sicheren Bereichs
- keine automatische Crop-/Resize-Adaption als finale Plattformvariante
- klare Hierarchie
- professionelle Typografiewirkung
- Motiv passt zur Aussage
- glaubwuerdige Anatomie und Objekte
- keine Fake-Evidence
- keine unbelegte visuelle Schuldzuweisung
- kein ungefragtes Branding
- kein generischer KI-Werbelook
- keine Symbolueberladung
- eigenstaendig innerhalb der Serie
- publizierbare Gesamtwirkung

## Designvergleich mit Stilankern

Bei jeder Ausgabe nur die Gestaltung mit den Stilankern vergleichen:

- aehnliche Typografieproportion
- aehnliche Ruhe im hellen Textbereich
- aehnliche Dominanz von Rot und Graphit
- aehnliche Klarheit der Text-Bild-Trennung
- aehnlicher hochwertiger redaktioneller Finish

Nicht verlangen, dass derselbe Inhalt, dieselbe Szene oder dieselbe Flaggen-, Familien- oder Landschaftsdarstellung vorkommt.

## Zeichenpruefung

Bei jedem Bild Text bewusst zoomen und abgleichen:

1. Eyebrow
2. Headline
3. Subline
4. Zahlen und Einheiten
5. Namen
6. Zitat
7. Quellenkennung

Besonders auf Umlaute, `ss`, Prozentzeichen, Kommata und Zahlendreher achten.

## Mobile QA

Bild als kleine Feedansicht beurteilen, ungefaehr entsprechend 360 CSS px Breite:

- Headline sofort erfassbar
- Hauptmotiv klar
- rote Signalfuehrung noch erkennbar
- kleine Texte noch lesbar
- keine konkurrierenden Blickpunkte
- keine fuer das Verstaendnis notwendigen Mikrodetails

## Serien-QA ohne Kontaktbogen-Datei

Alle zehn akzeptierten Bilder nacheinander beziehungsweise in der vorhandenen UI vergleichen. Keine neue Kontaktbogen-Grafik erzeugen.

Pruefen:

- funktionale Layoutvariation
- gemeinsame Ivory-Rot-Graphit-Design-DNA
- stabile Typografieproportion
- visuelle Rhythmik
- keine Near-Duplicates
- kein schleichender Farb- oder Dunkelheitsdrift
- keine zehn identischen Fotoideen
- Hook und Schluss klar verschieden
- Stilanker bleiben als Designreferenz erkennbar

## Plattform-Safe-Zone-QA

Vor Freigabe jede konkrete Datei gegen [platform-safe-zones.md](platform-safe-zones.md) pruefen.

- 4:5 bei 1080 x 1350: mindestens 100 px links/rechts, 100 px oben, 120 px unten fuer kritischen Text; keine kritische Information innerhalb der aeussersten 40 px.
- 1:1 bei 1080 x 1080: kritischer Inhalt innerhalb des zentrierten 900 x 900 px Bereichs.
- 9:16 bei 1080 x 1920: mindestens 90 px links, 160 px rechts, 288 px oben, 384 px unten fuer kritische Information.
- Diese Werte sind interne konservative Produktionsreserven und duerfen nicht als offizielle Plattform-Safe-Zones bezeichnet werden.
- Bei staerkerer UI-Ueberlagerung oder konkretem Placement immer den groesseren Abstand verwenden.

## Facebook Bundle QA

Bei Mehrbildsets zusaetzlich:

- Bild 1 ist der staerkste Einstieg
- jedes Bild funktioniert allein
- Reihenfolge ergibt Sinn
- die ersten Bilder enthalten bereits den wesentlichen Kern
- bei 1:1 liegen zentrale Inhalte ausreichend weit vom Rand
- kein spaeter Slot ist fuer die Korrektheit der ersten Bilder zwingend notwendig
- Referenz-DNA bleibt bei der Neu-Komposition erhalten
