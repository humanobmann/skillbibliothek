# Final QA Report Schema v5

```json
{
  "items": [
    {
      "slot": 1,
      "file": "01.png",
      "visual_reviewed": true,
      "review_notes": "Konkrete Beobachtung zu sichtbarem Text, Referenz-DNA, fertigem Grafikdesign, Hierarchie, Motiv, Glaubwuerdigkeit und mobiler Lesbarkeit.",
      "issues": [],
      "hard_gates": {
        "single_image": true,
        "text_exact": true,
        "facts_exact": true,
        "headline_breaks_controlled": true,
        "no_text_clipping": true,
        "no_extra_text": true,
        "mobile_readable": true,
        "contrast_safe": true,
        "safe_margins": true,
        "hierarchy_clear": true,
        "typography_professional": true,
        "composition_balanced": true,
        "image_integrity_credible": true,
        "fake_evidence_free": true,
        "visual_claim_safe": true,
        "generic_ai_look_absent": true,
        "symbolism_restrained": true,
        "no_unrequested_branding": true,
        "standalone_effective": true,
        "series_role_clear": true,
        "neighbor_distinct": true,
        "publish_ready": true,
        "full_graphic_design_present": true,
        "visible_text_present": true,
        "raw_photo_absent": true,
        "reference_design_dna_present": true
      },
      "scores": {
        "intent_match": 5,
        "hierarchy": 5,
        "typography": 5,
        "composition": 4,
        "specificity": 5,
        "credibility": 5,
        "restraint": 4,
        "mobile_readability": 5,
        "series_role": 5,
        "finish": 5
      }
    }
  ],
  "series_review_notes": "Konkrete Beobachtungen zu Rhythmus, Variation, Referenz-DNA und korrigierten Schwachstellen.",
  "series_gates": {
    "ten_individual_files": true,
    "no_collage_endproduct": true,
    "image_tool_only_confirmed": true,
    "functional_layout_variation": true,
    "render_strategy_rhythm": true,
    "accent_rhythm": true,
    "no_near_duplicates": true,
    "dramaturgy_passed": true,
    "style_consistency_passed": true,
    "no_template_monotony": true,
    "no_dark_or_color_drift": true,
    "hook_and_close_distinct": true,
    "reference_design_dna_consistent": true
  },
  "evidence_gate": true
}
```

Exakt zehn Items sind Pflicht.

Jede Enddatei muss tatsaechlich angesehen worden sein. Alle Hard Gates muessen `true` sein, `issues` leer, jeder Score 4 oder 5 und Summe mindestens 44 von 50.
