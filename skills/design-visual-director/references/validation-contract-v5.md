# Deterministic JSON production preflight

The helper ../scripts/validate_design_job.py checks job metadata and release gates. It does not access Canva, inspect a screenshot, evaluate image quality or confirm a person was preserved.

Job fields: campaign_id, project_scope, canva_account, optional template_source_account, output {type,format,width_px,height_px}, assets {logo,person}, content {factual_claims,source_refs}, qa {boolean result flags}, release {status,human_approved,automatic_publication}.

When an authorized host has Python, run:
```bash
python3 skills/design-visual-director/scripts/validate_design_job.py job.json --json
python3 -m unittest discover -s skills/design-visual-director/tests -v
```

Supported project_scope: personal, ngo, party, parliamentary. Official party and parliamentary work uses SPÖ; personal and NGO work uses Peter. The latter remain separate brand namespaces. For standalone image output use image_only; for native Canva use canva_native. A HTML/iframe mockup is never a permitted design deliverable.

Final requires documented human approval, source checks for factual material, rendered/layout/dimension checks, identity check for real people and editability verification when converting images to designs. Passing JSON checks does not prove any corresponding boolean value is true; evidence remains an independent requirement. No auto publication.
