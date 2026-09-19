# Creative Direction

## Vor der Produktion entscheiden

1. Welche Aussage soll die Serie leisten?
2. Wer sieht sie in welcher Feed-Situation?
3. Welche visuelle Stimme passt zum Thema?
4. Welche Slots brauchen Fotografie, Typografie, Diagramm oder abstrakte Grafik?
5. Wie stark darf der rote oder sonstige Akzent werden?
6. Welche Informationsdichte ist mobil tragfaehig?
7. Welche visuellen Klischees muessen vermieden werden?
8. Wie wird Oesterreich glaubwuerdig gezeigt, ohne Symboltapete?
9. Welche Referenzprinzipien werden uebernommen, ohne konkrete Kampagnen zu kopieren?
10. Gibt es aktive Stilanker und welches Designprofil leiten sie aus?

## Zielstil

Standard fuer politische und gesellschaftliche Serien:

- hochwertig, zeitgenoessisch, redaktionell
- glaubwuerdig statt werblich
- pointiert, aber nicht hysterisch
- starke, saubere Typografie
- viel bewusster Negativraum
- wenige praezise Gestaltungsmittel
- mobile Lesbarkeit vor dekorativer Komplexitaet
- sichtbare Variation ohne Stilbruch
- fertiges Grafikdesign statt Bild mit Leerflaeche

## Standardprofil bei vorliegenden Stilankern

Wenn der Nutzer Bildbeispiele liefert und nichts Gegenteiliges sagt, standardmaessig folgendes Profil aktivieren:

- `design_reference_mode=anchored`
- `design_reference_profile=austria-editorial-civic-v1`

Dann gilt:

- obere helle Textbuehne oder ruhiger linker Textbereich
- grosse rote oder schwarze Headline mit klaren Zeilenumbruechen
- klarer dunkler Sekundaertext
- warmer glaubwuerdiger Bildteil
- ein praegnanter roter grafischer Akzent
- publizierter Posterlook, nicht Moodboard

## Nicht automatisch annehmen

Nicht automatisch Partei-CI, Logos, Politikerportraets, Protestoptik, Akten, Geld, Krankenhausflure oder Handschlaege einsetzen.

## Referenzstrategie

Referenzen in Prinzipien zerlegen:

- Farbtemperatur
- Kontrast
- Typografiedichte
- Bilddistanz
- Negativraum
- Formensprache
- Text-Bild-Verhaeltnis
- Rhythmus
- typografischer Held
- grafische Signatur

Nie fremden Text, Logo, Person, Claim oder konkrete Kampagnenkomposition kopieren.

## Designbindungsregel

Fuer jeden Slot vor dem eigentlichen Bildauftrag einen knappen Designfahrplan formulieren:

- Textbuehne
- Fotobuehne
- typografischer Held
- Sekundaertextblock
- roter Akzent
- zusaetzliche grafische Klammer
- zentrale Ausschluesse

## Render Strategy

Fuer jeden Slot bewusst eine `render_strategy` waehlen:

- `photo_editorial`
- `typographic_editorial`
- `diagrammatic_editorial`
- `abstract_editorial`
- `provided_image_edit`
- `template_edit`

Unabhaengig von der Strategie wird das finale Bild ausschliesslich mit dem ChatGPT-Bilderstellungstool erzeugt oder bearbeitet.
