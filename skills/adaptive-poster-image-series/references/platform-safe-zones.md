# Platform Safe Zones and Delivery Contract v1

## Zweck

Diese Werte sind konservative interne Produktionsreserven fuer robuste Social-Media-Ausgaben. Sie sind **keine behaupteten offiziellen Safe Zones** von Meta, Instagram oder TikTok.

Wenn aktuelle Plattformdokumentation, reale UI-Tests oder ein konkreter Placement-Typ mehr Platz benoetigen, gilt immer der groessere Sicherheitsabstand.

## Verbindliche Masterformate

### Feed 4:5

- Canvas: 1080 x 1350 px
- Profil: `feed_4x5`
- kritischer Text links: mindestens 72 px
- kritischer Text rechts: mindestens 72 px
- kritischer Text oben: mindestens 90 px
- kritischer Text unten: mindestens 110 px
- Hero-Zahlen oder dominante Keywords: mindestens 8 % zusaetzlicher optischer Freiraum
- Quelle vollstaendig innerhalb des sicheren Innenbereichs
- zentrale Gesichter, Haende, Maschinen oder andere Motive: mindestens 12 % Crop-Reserve um den relevanten Motivkern

### Feed 1:1

- Canvas: 1080 x 1080 px
- Profil: `square_1x1`
- kritischer Inhalt innerhalb eines zentrierten 900 x 900 px Bereichs
- daraus resultierender Innenrand: 90 px an allen Seiten
- Quelle nicht naeher als 90 px an den unteren Rand
- Hero-Zahlen oder dominante Keywords: mindestens 8 % zusaetzlicher optischer Freiraum
- zentrale Motive: mindestens 12 % Crop-Reserve

### Story / Reel / TikTok 9:16

- Canvas: 1080 x 1920 px
- Profil: `vertical_9x16`
- linker Innenrand fuer kritischen Text: mindestens 90 px
- rechter UI-Reservebereich: mindestens 160 px
- obere Reserve: mindestens 288 px, entsprechend 15 %
- untere Reserve: mindestens 384 px, entsprechend 20 %
- kritische Text- und Quelleninformation bleibt innerhalb des verbleibenden zentralen Bereichs
- Hero-Zahlen oder dominante Keywords: mindestens 8 % zusaetzlicher optischer Freiraum
- zentrale Motive: mindestens 12 % Crop-Reserve
- wenn ein Placement mehr UI ueberlagert, Reserve vergroessern

## Harte Regeln

1. Varianten werden neu komponiert. Kein automatisches Cropping oder blosses Skalieren eines anderen Seitenverhaeltnisses.
2. Text darf nicht nur technisch innerhalb des Canvas liegen, sondern muss mit sichtbarer optischer Reserve gesetzt sein.
3. Headlines, Hero-Zahlen, Quellen und zentrale Motive duerfen keine Schnittkante beruehren.
4. Bei Faktenmotiven darf eine Quellenzeile nie in eine unsichere UI-Zone verschoben werden.
5. Ein Motiv ist erst freigabefaehig, wenn die konkrete Ausgabe visuell gegen ihr Safe-Zone-Profil geprueft wurde.
6. Safe-Zone-Konformitaet ist ein Release-Gate, kein optionaler Gestaltungshinweis.

## Cross-Platform-Ausgabe

Wenn der Nutzer Facebook und Instagram plus Story/Reel/TikTok oder sinngemaess `alle Social-Formate` verlangt, gilt `delivery_mode=full_social_30`.

Dann entstehen aus zehn Master-Slots exakt 30 getrennte Enddateien:

- 10 x `feed_4x5`
- 10 x `square_1x1`
- 10 x `vertical_9x16`

Keine der 20 Adaptionen ist ein automatischer Crop des 4:5 Masters.

## Dateinamen

Pro Slot:

- `01-feed-4x5.png`
- `01-square-1x1.png`
- `01-vertical-9x16.png`

bis Slot 10.

## Politische und faktische Inhalte

Safe Zones aendern keine Fakten- oder Quellenanforderungen. Factual Mode, Claim Ledger, sichtbarer Text und Quellenkennzeichnung bleiben fuer jede Variante identisch verbindlich.
