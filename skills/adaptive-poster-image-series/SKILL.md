---
name: adaptive-poster-image-series
description: >-
  Erzeuge genau zehn getrennte, hochwertige Editorial-, Fakten-, NGO-, politische
  oder gesellschaftliche Social-Media-Bilder aus einem Thema, zehn Texten oder zehn
  Vorlagen. Verwende den Skill auch fuer Facebook-, Instagram-, Story-, Reel- und TikTok-Adaptionen mit verbindlichen internen Sicherheitsbereichen.
  Fuer jede finale Bilddatei ausschliesslich das normale ChatGPT-Bilderstellungstool
  verwenden: ein Slot, ein Aufruf, ein Bild, n=1; keine SVG-, Canvas-, Adobe-, Firefly-,
  Python- oder sonstige externe Bildproduktion. Arbeite standardmaessig mit einem
  fest gebundenen Referenzdesign mit den drei mitgelieferten Stilankern. Die
  Designsprache aus Ivory, Signalrot, Graphit, grosser Grotesk-Typografie und
  integrierter Bildzone ist Standard fuer jedes Motiv. Fakten vorab verifizieren, sichtbaren Text nach jeder Ausgabe exakt pruefen, nur fehlerhafte Slots
  mit demselben Bildtool korrigieren und niemals Collagen, Kontaktboegen,
  Mehrfachpanels, Fake-Evidence oder ungefragtes Branding als Endprodukt liefern.
---

# Adaptive Poster Image Series

## Ziel

Genau zehn eigenstaendige, veroeffentlichungsreife Mastermotive liefern. Die zehn Dateien gehoeren sichtbar zusammen, muessen aber funktional und kompositorisch eigenstaendig sein.

Fuer die eigentliche Bildproduktion gilt ein exklusiver Werkzeugvertrag:

1. Finale Bilder nur mit dem normalen ChatGPT-Bilderstellungstool `image_gen` erzeugen oder bearbeiten.
2. Kein SVG-, HTML-, Canvas-, Python-, Inkscape-, Photoshop-, Adobe-, Firefly- oder sonstiger alternativer Bildgenerator oder Renderer.
3. Skripte duerfen nur Plaene, Claims, Metadaten und vorhandene Ausgabedateien pruefen. Sie duerfen keine Endbilder erzeugen, zusammensetzen, beschriften, croppen, skalieren oder reparieren.
4. Wenn das Bilderstellungstool einen Fehler nicht sauber beheben kann, den Slot nicht mit einem anderen Bildwerkzeug retten.

## Harte Grundregeln

1. Genau zehn Mastermotive erzeugen.
2. Pro Bildtool-Aufruf genau einen Slot und genau ein Bild bearbeiten. `n=1` verwenden.
3. Niemals mehrere Slots gleichzeitig an das Bildtool uebergeben.
4. Im einzelnen Bildauftrag keine anderen Slots, keine Zehnerserie, kein Storyboard, keinen Kontaktbogen und kein Mehrfachraster beschreiben.
5. Jede finale Datei ist ein einzelnes Motiv. Keine Collage, kein Split Screen, kein Multi-Panel, kein Grid und kein Kontaktbogen.
6. Sichtbarer Text muss aus dem freigegebenen Plan stammen. Keine erfundenen Woerter, Zahlen, Namen, Quellen oder Zitate akzeptieren.
7. Textfehler niemals extern ueberdecken oder nachtraeglich programmatisch setzen. Nur mit dem Bilderstellungstool korrigieren oder neu erzeugen.
8. Keine Fake-Dokumente, Fake-Screenshots, Fake-E-Mails, erfundenen Zeitungsausschnitte, Amtssiegel oder Beweismittel erzeugen.
9. Verifizierte Dokumente duerfen Recherchequelle sein, aber nicht durch das Bildmodell als angeblicher Originalbeleg nachgebaut werden.
10. Ungefragtes Branding blockieren. Standard ist `branding_mode=none`.
11. Oesterreich-Kontext glaubwuerdig, nicht dekorativ einsetzen. Flagge, Wappen oder rot-weiss-rote Symbolik nur bei inhaltlicher Notwendigkeit, explizitem Designprofil oder ausdruecklichem Wunsch.
12. Jede Ausgabe tatsaechlich visuell pruefen. Technische Metadaten ersetzen keine Art-Direction-QA.
13. Nur fehlerhafte Slots wiederholen.
14. Keine Fertigmeldung, solange ein sichtbarer Text-, Fakten-, Layout-, Crop-, Branding- oder Serienfehler offen ist.
15. Die drei gebuendelten Stilanker und das Profil `austria-editorial-civic-v1` sind standardmaessig fuer jede Ausgabe verbindlich. Die Anlehnung betrifft nur Design: Layoutsprache, Typografiecharakter, Farbklima, Proportionen und grafische Mittel.
16. Fehlende Schrift oder fehlendes Grafikdesign ist ein Hard Fail. Ein blosses Hintergrundbild oder Rohfoto ist nie freigabefaehig.
17. Jede Grafik muss sichtbar als vollstaendig gestaltetes Editorialposter erscheinen: warme helle Grundflaeche, Signalrot, Graphit, grosse Grotesk-Typografie, klare Hierarchie und mindestens ein grafisches Signal- oder Bewegungselement.
18. Referenzinhalt niemals automatisch kopieren. Flagge, Menschen, Landschaft, Parlament oder Referenztext nur verwenden, wenn der aktuelle Inhalt dies verlangt.
19. Sicherheitsbereiche sind Release-Gates. Fuer 4:5, 1:1 und 9:16 gelten die konservativen internen Profile aus [references/platform-safe-zones.md](references/platform-safe-zones.md); sie duerfen nie als offizielle Plattform-Safe-Zones bezeichnet werden.
20. Plattformvarianten werden immer neu komponiert. Automatisches Cropping, blosses Resizing oder das Verschieben bereits zu randnaher Typografie ist unzulaessig.
21. Wenn der Nutzer Facebook und Instagram plus Story/Reel/TikTok oder sinngemaess alle Social-Formate verlangt, ist `delivery_mode=full_social_30`: zehn 4:5, zehn 1:1 und zehn 9:16 Enddateien.

## Workflow

### 1. Eingabemodus bestimmen

Genau einen Modus setzen:

- `theme`: ein Thema in zehn kommunikative Funktionen uebersetzen.
- `ten_texts`: zehn Texte oder Briefings genau zehn Slots zuordnen.
- `ten_templates`: zehn Vorlagen source-preserving bearbeiten.

Bei `ten_templates` jede Vorlage nur dem zugeordneten Slot als Bildreferenz geben. Referenzen zwischen Slots nicht vermischen.

### 2. Factual Mode bestimmen

Factual Mode aktivieren bei Politik, Recht, Verwaltung, aktuellen Ereignissen, Budgets, Zahlen, Zitaten, Institutionen, historischen Tatsachen, Vorwuerfen oder anderen extern pruefbaren Aussagen.

Dann [references/factual-visual-integrity.md](references/factual-visual-integrity.md) und [references/claim-ledger-schema.md](references/claim-ledger-schema.md) lesen. Vor der Bildproduktion `claim-ledger.json` anlegen und validieren:

```bash
python scripts/validate_claim_ledger.py claim-ledger.json
```

`unverified` und `blocked` duerfen nicht als faktischer sichtbarer Text verwendet werden.

### 3. Creative Direction und Designbindung festlegen

[references/creative-direction.md](references/creative-direction.md), [references/style-system.md](references/style-system.md), [references/design-reference-profile.md](references/design-reference-profile.md), [references/reference-design-dna.md](references/reference-design-dna.md), [references/typography-system.md](references/typography-system.md), [references/composition-library.md](references/composition-library.md) und [references/anti-patterns.md](references/anti-patterns.md) lesen.

Vor Slot 1 festlegen:

- Kommunikationsziel und Zielgruppe
- visuelle Stimme
- Foto-, Typografie-, Diagramm- oder abstrakte Strategie
- Typografiehierarchie
- Palette und Akzentlogik
- Informationsdichte
- Oesterreich-Kontextstrategie
- Branding-Modus
- explizite Anti-Ziele
- `design_reference_mode`
- `design_reference_profile`
- `style_anchor_assets`
- konkrete Designmerkmale, die in jeder Ausgabe sichtbar sein muessen

Standard ist immer:

- `design_system=civic_editorial_red_ivory`
- `design_lock=true`
- `design_required=true`
- `raw_photo_forbidden=true`
- `design_reference_mode=anchored`
- `design_reference_profile=austria-editorial-civic-v1`
- alle drei `style_anchor_assets` aktiv

Referenzen nur in Prinzipien uebersetzen. Keine konkrete fremde Kampagne kopieren.

### 4. Zehn Slots planen

[references/series-dramaturgy.md](references/series-dramaturgy.md) und [references/production-plan-schema.md](references/production-plan-schema.md) verwenden.

Exakt zehn Slots anlegen. Jeder Slot braucht mindestens:

- Serienrolle
- exakten sichtbaren Text
- Claim-Verweise bei Factual Mode
- `render_strategy`
- Motiv und Layoutfamilie
- Fokus und Negativraum
- Dichte und Akzentstaerke
- einen eigenstaendigen Einzelbild-Brief
- Alt-Text
- `design_required=true`
- `visible_text_required=true`
- `full_design_required=true`
- `raw_photo_forbidden=true`
- `design_variant` aus dem Referenzprofil
- `text_block_position`
- `photo_zone` oder grafische Inhaltszone
- `accent_elements`
- `design_brief` mit mindestens Typografie, Farbklima, Bildintegration und grafischem Signal

Plan validieren:

```bash
python scripts/validate_plan.py production-plan.json
```

Factual Mode:

```bash
python scripts/validate_plan.py production-plan.json --claims claim-ledger.json
```

Ein Hard Fail blockiert die Bildproduktion.

### 5. Finales Einzelbild direkt mit dem Bilderstellungstool erzeugen

[references/generation-contract.md](references/generation-contract.md) und [references/image-prompt-patterns.md](references/image-prompt-patterns.md) lesen.

Slot fuer Slot:

1. Nur den aktuellen Slot und seine erlaubten Bildreferenzen verwenden.
2. Exakt ein eigenstaendiges finales Social-Media-Motiv erzeugen.
3. Exakt den freigegebenen sichtbaren Text verlangen.
4. Zielseitenverhaeltnis und Komposition direkt im Bildauftrag festlegen.
5. Den Bildauftrag mit dem Pflichtsatz aus `image-prompt-patterns.md` als vollstaendig fertig gestaltete Grafik beginnen.
6. Die Referenz-DNA explizit in denselben Einzelbildauftrag schreiben: Ivory oder Creme, Signalrot, Graphit, grosse linksausgerichtete Grotesk-Typografie, obere Typografiezone, thematische Bildzone und sichtbares rotes grafisches Signal.
7. Exakte Textposition, Hierarchie, Zeilenumbrueche, Bildzone und `accent_elements` aus dem Slotplan nennen.
8. Keine freie Textflaeche fuer spaeteren Einbau erlauben.
9. Die drei Stilanker nur als Designreferenz behandeln, nie als Inhaltsvorlage.
10. `image_gen` mit `n=1` verwenden.
11. Ergebnis sofort visuell pruefen.
12. Rohfoto, fehlende Headline, fehlendes Grafikdesign oder fehlende Referenz-DNA sofort als FAIL werten.
13. Bei PASS Slot akzeptieren und zum naechsten wechseln.
14. Bei FAIL nur diesen Slot gemaess [references/retry-policy.md](references/retry-policy.md) mit dem Bilderstellungstool korrigieren.

Kein Zwischenasset ist Pflicht. Das Bildtool erzeugt das Endmotiv direkt.

### 6. Text und Fakten nach jedem Bild pruefen

Jede sichtbare Zeichenfolge mit dem Plan vergleichen:

- Headline
- Eyebrow
- Subline
- Zahlen und Einheiten
- Namen
- Zitatzeichen und Zitattext
- kurze Quellenzeile, falls verwendet

Ein einziger falscher Buchstabe, eine erfundene Zahl oder ein zusaetzliches Wort ist ein Hard Fail.

Bei langen Quellen keine winzige URL in das Bild zwingen. Quellen vollstaendig im begleitenden Quellenmanifest halten; im Bild nur eine kurze, vorab freigegebene Quellenkennung verwenden, wenn sie lesbar bleibt.

### 7. Design-QA und Master-QA

[references/art-direction-rubric.md](references/art-direction-rubric.md), [references/visual-qa.md](references/visual-qa.md) und [references/qa-report-schema.md](references/qa-report-schema.md) anwenden.

Zusaetzlich immer pruefen:

- steht die Headline sichtbar und dominant im Bild
- wirkt das Ergebnis wie eine fertige Grafik und nicht wie ein Rohfoto
- sind Ivory oder Creme, Signalrot, Graphit und grosse Grotesk-Typografie als gemeinsame DNA erkennbar
- ist mindestens ein bewusstes rotes grafisches Signal integriert
- ist die Designsprache sichtbar an das aktive Referenzprofil angelehnt
- sind Divider, Farbklima, Typografiecharakter und grafische Akzente sauber integriert
- wurde kein exakter Beispielinhalt kopiert

Alle zehn Bilder einzeln pruefen und anschliessend die Serienwirkung ohne Kontaktbogen-Datei beurteilen. Keine neue QA-Grafik erzeugen.

Falls Dateipfade verfuegbar sind, technische Inspektion optional ausfuehren:

```bash
python scripts/inspect_outputs.py release/masters --count 10 --aspect-ratio 4:5
```

Die technische Pruefung darf keine Bilddatei veraendern.

### 8. Plattform-Ausgabe und Sicherheitsbereiche planen

Immer [references/platform-safe-zones.md](references/platform-safe-zones.md) lesen. Wenn der Nutzer mehrere Plattformformate oder alle Social-Formate verlangt, zusaetzlich [references/platform-delivery-schema.md](references/platform-delivery-schema.md) verwenden. Fuer Facebook-Mehrbildsets weiterhin [references/facebook-publication-strategy.md](references/facebook-publication-strategy.md) und [references/publication-plan-schema.md](references/publication-plan-schema.md) verwenden.

Bei plattformuebergreifender Ausgabe `platform-delivery.json` separat vom Masterplan anlegen und validieren:

```bash
python scripts/validate_platform_delivery.py platform-delivery.json production-plan.json
```

Bei Facebook-Mehrbildsets zusaetzlich `publication-plan.json` anlegen und validieren:

```bash
python scripts/validate_publication_plan.py publication-plan.json production-plan.json
```

Unterstuetzte Modi:

- `single`
- `pair`
- `trio`
- `quad`
- `gallery`
- `auto`

Weniger Bilder bevorzugen, wenn sie die Aussage vollstaendig tragen.

### 9. Plattformvarianten ebenfalls nur mit dem Bilderstellungstool erzeugen

Adaptionen fuer Facebook, Instagram, Stories, Reels oder TikTok niemals programmatisch croppen oder umformatieren. Jede Variante ist eine eigenstaendige Neu-Komposition innerhalb ihres Safe-Zone-Profils.

Fuer jede Publikationsdatei:

1. genau einen ausgewaehlten Master-Slot verwenden
2. Zielverhaeltnis im Bildtool neu komponieren
3. bei 1:1 den Text und die Bildhierarchie fuer Quadrat neu anordnen
4. Crop-Resilienz beruecksichtigen
5. das aktive Designprofil und die Stilanker sichtbar beibehalten
6. nur das Bilderstellungstool verwenden
7. wieder `n=1`
8. jede Datei separat visuell pruefen

Mehrbildmodus bedeutet mehrere getrennte Dateien, niemals ein Rasterbild.

### 10. Publication-QA

[references/publication-qa-schema.md](references/publication-qa-schema.md) verwenden.

Pruefen:

- Reihenfolge
- First-Frame-Staerke
- mobile Lesbarkeit
- Crop-Resilienz
- eigenstaendige Verstaendlichkeit
- keine Informationsluecke in den ersten Bildern
- keine zentrale Aussage nur in spaeten Gallery-Slots
- Text- und Faktenidentitaet zum Master
- sichtbare Designkonsistenz zum aktiven Referenzprofil

Validieren:

```bash
python scripts/validate_publication_qa.py publication-qa.json publication-plan.json
```

### 11. Nur fehlerhafte Slots wiederholen

Bei Text-, Layout- oder Bildfehlern nur die betroffene Datei mit `image_gen` editieren oder neu erzeugen. Nie alle zehn Bilder neu erzeugen, wenn nur ein Slot fehlschlaegt.

### 12. Abschluss

Nur freigeben, wenn:

1. exakt zehn eigenstaendige Masterbilder vorhanden und visuell PASS sind
2. Factual Mode keine ungeprueften Claims enthaelt
3. jeder sichtbare Text exakt ist
4. keine Collage oder Mehrfachdatei als Endbild vorliegt
5. keine Fake-Evidence oder ungefragtes Branding vorliegt
6. Serienvariation und Stilzusammenhalt PASS sind
7. die Designbindung an das aktive Referenzprofil sichtbar ist
8. optionale Facebook-Dateien einzeln neu komponiert und separat PASS sind
9. keine alternative Bildproduktionsmethode verwendet wurde

## Regressionstest

Nach jeder Skill-Aenderung ausfuehren:

```bash
python scripts/self_test.py
```

Der Test prueft Claims, Zehn-Slot-Plan, Safe-Zone- und Plattform-Delivery-Vertrag, Facebook-Publication-Plan und QA-Vertraege. Er erzeugt bewusst keine Bilder; Bildproduktion bleibt exklusiv dem Bilderstellungstool vorbehalten.
