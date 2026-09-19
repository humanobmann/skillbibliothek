# Publication QA Schema v2

```json
{
  "platform": "facebook",
  "mode": "trio",
  "items": [
    {
      "slot": 1,
      "visual_reviewed": true,
      "text_exact": true,
      "mobile_readable": true,
      "crop_resilient": true,
      "standalone_effective": true,
      "facts_exact": true,
      "no_collage": true,
      "no_unrequested_branding": true,
      "full_graphic_design_present": true,
      "reference_design_dna_present": true,
      "raw_photo_absent": true,
      "issues": [],
      "review_notes": "Konkrete Beobachtung zu Text, fertigem Grafikdesign, Referenz-DNA, Hierarchie und Randresilienz."
    }
  ],
  "first_frame_strong": true,
  "sequence_coherent": true,
  "essential_message_in_early_frames": true,
  "no_late_critical_dependency": true,
  "image_tool_only_confirmed": true,
  "reference_design_dna_consistent": true,
  "bundle_notes": "Konkrete Beobachtung zur Reihenfolge, Variation und gemeinsamen Designwirkung."
}
```

`items` muss exakt die im `publication-plan.json` ausgewaehlten Slots enthalten.

Jede Publikationsdatei muss ein vollstaendig gestaltetes Poster sein. Rohfoto, fehlende sichtbare Typografie oder sichtbarer Stilbruch zum Referenzprofil sind Hard Fail.
