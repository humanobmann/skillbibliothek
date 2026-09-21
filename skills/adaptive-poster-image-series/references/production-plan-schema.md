# Production Plan Schema v6

## Grundstruktur

```json
{
  "job": {
    "series_id": "example-series",
    "locale": "de-AT",
    "input_mode": "theme",
    "factual_mode": true,
    "branding_mode": "none",
    "output_count": 10,
    "aspect_ratio": "4:5",
    "image_tool_only": true,
    "design_system": "civic_editorial_red_ivory",
    "design_lock": true,
    "design_required": true,
    "raw_photo_forbidden": true,
    "safe_zone_profile": "feed_4x5",
    "safe_zone_contract": "internal_conservative_v1",
    "official_platform_safe_zone": false
  },
  "creative_direction": {
    "design_intent": "Eine fertig gestaltete Editorialserie mit grosser Typografie, warmer Ivory-Grundflaeche, Signalrot und integriertem thematischem Bildraum.",
    "visual_voice": ["editorial", "credible", "bold", "precise", "human"],
    "image_direction": "Thematisch konkrete Fotografie oder Grafik als Teil eines vollstaendig gestalteten Posters, niemals Rohfoto.",
    "typography_direction": "Sehr grosse moderne Grotesk-Typografie, linksbuendig, mit klarer Hierarchie und kontrollierten Zeilenumbruechen.",
    "palette_direction": "Warm Ivory, Signalrot und dunkles Graphit als verbindliche Referenz-DNA.",
    "austria_strategy": "contextual_not_symbolic",
    "reference_strategy": "principles_not_copy",
    "design_reference_mode": "anchored",
    "design_reference_profile": "austria-editorial-civic-v1",
    "style_anchor_assets": [
      "assets/style-anchors/reference-1.jpg",
      "assets/style-anchors/reference-2.jpg",
      "assets/style-anchors/reference-3.jpg"
    ],
    "anti_goals": [
      "raw photo as final image",
      "empty text placeholder",
      "generic AI advertising",
      "fake evidence",
      "crime thriller mood",
      "unrequested branding",
      "collage or multi-panel imagery",
      "template monotony"
    ]
  },
  "slots": [
    {
      "slot": 1,
      "role": "hook",
      "eyebrow": "KONTEXT",
      "headline": "Eine klare Hauptaussage.",
      "headline_lines": ["Eine klare", "Hauptaussage."],
      "subline": "Optionale kurze Einordnung.",
      "source_label": "Quelle: Institution, 2026",
      "content_type": "fact",
      "claim_ids": ["C01"],
      "source_claim_id": "C01",
      "render_strategy": "photo_editorial",
      "design_variant": "oversize_keyword_photo",
      "motif_type": "architecture",
      "subject": "Eine glaubwuerdige thematisch passende oesterreichische oder mitteleuropaeische Szene.",
      "layout_family": "editorial-split",
      "negative_space": "upper-left",
      "focus_x": 0.65,
      "focus_y": 0.58,
      "accent_strength": "strong",
      "density": "low",
      "design_required": true,
      "text_block_position": "upper-left, 8 percent margin, stacked headline hierarchy",
      "photo_zone": "lower 58 percent, edge-to-edge, integrated below typography",
      "accent_elements": ["sweeping red signal curve", "short red underline"],
      "visible_text_required": true,
      "full_design_required": true,
      "raw_photo_forbidden": true,
      "hero_clearance_percent": 8,
      "motif_crop_reserve_percent": 12,
      "source_inside_safe_area": true,
      "design_brief": "Fertiges 4:5 Editorialposter im verbindlichen Ivory-Rot-Graphit-Referenzdesign. Grosse linksausgerichtete Headline im oberen Bereich, thematisches Foto darunter, rote geschwungene Signalform als Verbindung. Kein Rohfoto und kein Platzhalter fuer spaetere Schrift.",
      "image_brief": "Ein einzelnes vollstaendig gestaltetes 4:5 Social-Media-Editorialmotiv mit fertiger Typografie, sichtbarer Grafikgestaltung und thematisch glaubwuerdigem Bildraum.",
      "risk_overclaim": false,
      "alt_text": "Beschreibung des fertig gestalteten Editorialmotivs und seiner sichtbaren Kernaussage."
    }
  ]
}
```

`slots` muss exakt zehn Eintraege enthalten.

## Pflichtwerte `job`

- `series_id`: dateisicher, 2 bis 64 Zeichen
- `locale`: `de-AT`
- `input_mode`: `theme`, `ten_texts`, `ten_templates`
- `factual_mode`: Boolean
- `branding_mode`: `none` oder `user_provided`
- `output_count`: exakt `10`
- `aspect_ratio`: standardmaessig `4:5`
- `image_tool_only`: exakt `true`
- `design_system`: exakt `civic_editorial_red_ivory`
- `design_lock`: exakt `true`, ausser der Nutzer verlangt ausdruecklich einen anderen Stil
- `design_required`: exakt `true`
- `raw_photo_forbidden`: exakt `true`
- `safe_zone_profile`: exakt `feed_4x5` fuer die Masterserie
- `safe_zone_contract`: exakt `internal_conservative_v1`
- `official_platform_safe_zone`: exakt `false`; die Werte sind interne konservative Produktionsreserven
- `creative_direction.design_reference_mode`: exakt `anchored`
- `creative_direction.design_reference_profile`: exakt `austria-editorial-civic-v1`
- `creative_direction.style_anchor_assets`: exakt die drei gebuendelten Stilanker

## Render Strategies

- `photo_editorial`
- `typographic_editorial`
- `diagrammatic_editorial`
- `abstract_editorial`
- `provided_image_edit`
- `template_edit`

Alle Strategien erzeugen das finale Bild ausschliesslich mit `image_gen`. Auch `photo_editorial` bedeutet fertiges Poster, niemals Rohfoto.

## Design Variants

- `hero_type_photo`
- `oversize_keyword_photo`
- `type_graphic_photo`
- `number_led_poster`
- `typographic_signal`
- `quiet_close_poster`

Alle Varianten muessen die gleiche Referenz-DNA aus Ivory, Signalrot, Graphit, grosser Grotesk-Typografie und einer klaren grafischen Signalform erhalten.

## Layoutfamilien

- `editorial-split`
- `photo-negative-space`
- `editorial-card`
- `signal-field`
- `number-led`
- `source-led`
- `question-led`
- `comparison-led`
- `timeline-led`
- `quiet-close`

## Pflichtwerte pro Slot

Jeder Slot braucht zusaetzlich zu Inhalt und Layout:

- `design_variant`
- `design_required=true`
- `text_block_position` mit konkreter Position und Hierarchie
- `photo_zone` oder grafische Inhaltszone
- `accent_elements` mit ein bis drei sichtbaren Gestaltungselementen
- `visible_text_required=true`
- `full_design_required=true`
- `raw_photo_forbidden=true`
- `hero_clearance_percent >= 8`
- `motif_crop_reserve_percent >= 12`
- `source_inside_safe_area=true`
- `design_brief` mit konkreter Typografie, Bildintegration und grafischem Element

Ein `design_brief` darf nicht nur `freie Textzone`, `Negativraum fuer Text` oder `Foto mit Platz fuer Schrift` verlangen. Fuer 4:5 Master gelten zusaetzlich die verbindlichen internen Sicherheitsbereiche aus [platform-safe-zones.md](platform-safe-zones.md): 100 px links/rechts, 100 px oben, 120 px unten bei 1080 x 1350, mit keiner kritischen Information innerhalb der aeussersten 40 px. Hero-Elemente brauchen mindestens acht Prozent optische Reserve; zentrale Motive mindestens zwoelf Prozent Crop-Reserve.

## Sichtbarer Text

`headline_lines` enthaelt ein bis vier bewusst gesetzte Zeilen. Zusammengefuegt muessen sie exakt `headline` ergeben.

`source_label` ist optional und kurz zu halten. Keine langen URLs oder vollstaendigen Literaturangaben in das Bild zwingen.

Das Bildtool darf keine zusaetzlichen Woerter erfinden.

## Claims

Factual Mode: `fact`, `auditor_finding`, `attributed_statement` und `quote` brauchen verifizierte Claim-IDs. Zahlen im sichtbaren Text muessen in den verknuepften Claims vorkommen.

## Serienvariation

Bei `theme` und `ten_texts` normalerweise:

- mindestens fuenf Layoutfamilien
- keine Layoutfamilie mehr als dreimal
- mindestens zwei Render Strategies, wenn inhaltlich sinnvoll
- mindestens drei unterschiedliche Motivtypen oder grafische Hauptideen
- mindestens drei Design Variants
- `strong` nur fuer wenige dramaturgische Peaks

Variation darf die verbindliche Referenz-DNA nicht aufbrechen.
