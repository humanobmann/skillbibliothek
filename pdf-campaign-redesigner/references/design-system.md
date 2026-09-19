# SPÖ Sektion VII - logo-freies Editorial-Dossier-Designsystem

Diese Regeln sind verbindlich fuer optimierte PDFs. Sie sind aus dem hochgeladenen SPÖ-Sektion-VII-Designsystem verdichtet und fuer A4-Dossiers priorisiert.

## Haltung

- Ruhig, erwachsen, publizistisch belastbar; eher Hintergrundanalyse als Parteibroschuere.
- Lesbarkeit vor Effekt; Inhalt fuehrt, Gestaltung strukturiert.
- Eine Idee pro Seite oder Abschnitt; Weissraum ist Teil der Argumentation.
- Belegbarkeit muss sichtbar sein: Quellenzeilen, Tabellenfussnoten und Statuslabels sind Pflichtbestandteile.
- Keine Dekoration ohne Funktion: keine Verlaeufe, Schatten, Cartoon-Icons, Clipart, runde Marketing-Karten, Wasserzeichen.
- Logo-frei: kein Logo, Signet, Emblem, Monogramm, Ersatzzeichen oder Logo-Platzhalter auf PDF-Seiten, Tabellen, Grafiken, Kopf-/Fusszeilen.

## Farbrollen

Verwende Token statt loser Hex-Werte.

| Rolle | Token | Wert | Einsatz |
|---|---|---:|---|
| Papier | `--paper` | `#FBFAF8` | Grundflaeche |
| Panel | `--paper-panel` | `#F4F1ED` | Faktenbox, Karten |
| Panel tief | `--paper-deep` | `#ECE7E1` | dezente Struktur |
| Text primaer | `--ink` | `#16110F` | Fliesstext, Headlines, Achsen |
| Text sekundaer | `--ink-2` | `#4A4441` | Sekundaertext |
| Text gedaempft | `--ink-3` | `#8A8380` | Captions, Quellen |
| Akzentrot | `--red` | `#E42612` | Kicker, Regeln, Kapitelnummern, eine Kernaussage |
| Risikorot | `--red-deep` | `#9C1608` | STOP, Risiko, Sperre |
| Risiko-Wash | `--red-wash` | `#FCF1EF` | Risikobox-Hintergrund |
| Hairline | `--hairline` | `#E2DCD6` | Tabellenlinien, Kartenrahmen |

Rot nie als grossflaechigen Hintergrund hinter Lauftext nutzen. Rot markiert Kanten, Kicker, Regeln und eine zentrale Aussage. Risiko-Rot bleibt exklusiv fuer Warnungen/Sperren.

## Typografie

- Dossier-Titel: Source Serif 4 / Georgia / Times, 40 pt, 600, line-height 1.04. Optional Area nur fuer Titelzeile, wenn legal verfuegbar.
- Kapitelnummer: Inter/system-ui, 13 pt, 700, getrackt, Versal, Rot.
- Kapitel-Titel: Serif, 26 pt, 600.
- H2: Serif, 18 pt, 600.
- H3: Sans, 12 pt, 700.
- Eyebrow/Kicker: Sans, 8.5 pt, 600, getrackt, Versal, Rot.
- Lead: Serif, 13 pt, line-height 1.5, max. 62 Zeichen.
- Fliesstext: Serif, 10.5 pt, line-height 1.55, max. 70 Zeichen.
- Captions, Quellen, Fussnoten: Sans, 8.5 pt, gedaempft.
- Tabellen: Kopf Sans 8.5 pt 700 Versal; Zellen Sans 9.5 pt; Zahlen rechtsbuendig mit tabular nums.

Keine Fontdateien ausgeben oder in Skills/Artefakten teilen. Webfonts sind optional; Fallbacks muessen das Layout tragen.

## Layout

- Format: A4 Hochformat, 210 x 297 mm, print-first.
- Raender: oben 22 mm, unten 20 mm, innen 24 mm, aussen 20 mm.
- Satzspiegel: 166 x 255 mm.
- Hilfsraster: 12 Spalten, 5 mm Gutter; Lauftext primaer links, Randnotizen rechts.
- Basislinie: ca. 16.5 px; Tabellen/Figuren/Callouts nicht zerreissen.
- Seitentypen: Titel, Inhalts-/Statusseite, Kapitelauftakt, Standardseite, Belege/Tabellen, Infografikseite, Quellenapparat, Schlussseite.
- Inhaltsseiten erhalten Running Head, Kolumnentitel und Seitenzahl; Titel-/Schlussseite nicht.

## Komponenten

- Faktenbox: Panel, dunkle linke Kante, Label `FAKT`.
- Zitatbox: rote linke Kante, kurze belegte Zitate; keine unbelegten Redezitate.
- Risikobox: Risiko-Wash, tiefrote Kante, Label `RISIKO` oder `STOP`.
- Pruefpunkt: Hairline-Rahmen, Label `PRUEFEN`.
- Jede datentragende Karte: Status-Chip -> Titel -> Inhalt -> Quellenzeile.
- Status nie nur ueber Farbe kommunizieren; immer Textlabel verwenden.

## Tabellen

- Roter 2-pt-Kopfstrich; Hairline-Zeilen; dezente Zebra-Zeilen.
- Werte rechtsbuendig; Quellenkuerzel in eigener Spalte, Aufloesung im Quellenapparat.
- Tabellenwand vermeiden. Tabellen nur dort, wo Vergleich/Pruefung dadurch schneller wird.
- Tabellen immer mit Caption und Quellen-/Standzeile.

## Infografiken

Infografiken sind Beweismittel, keine Deko. Erlaubt:

- horizontale Balken, Zeitachsen, Prozessdiagramme, Vergleichsmatrizen, Risikoraster, Belegfluss, Akteurskarten, Quellenlandkarten.
- Ink + ein Rot-Akzent + warme Graustufen; max. 4 Serienfarben.
- Zahl direkt am Element, nicht nur in Legende.
- Jede Grafik mit Titel, Aussage, Quellenzeile, Stand-Datum.

Verboten:

- 3D, Verlaeufe, Drop-Shadows, Cartoon-Icons, Clipart, dekorative Kreise, Donuts als Hauptbeweis, mehrteilige Tortendiagramme, Farbe ohne Textlabel.

## PDF-Export

- Hintergrundgrafiken aktiv, 100 %, A4, print-color-adjust exact.
- Schriften einbetten, wenn legal und technisch moeglich.
- Tagged PDF/PDF-UA nur behaupten, wenn Lesereihenfolge und Tags geprueft sind.
- Vor Abgabe rendern und visuell pruefen: keine Ueberlaeufe, keine abgeschnittenen Zahlen, keine verwaisten Headlines, keine zerbrochenen Tabellen.
