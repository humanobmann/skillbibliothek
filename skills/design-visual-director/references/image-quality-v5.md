# Image to Canva Handoff, QA and Identity

## Visual generation

Choose a single visual premise, a realistic focal point, camera/light logic and negative space for Canva copy. Provide reference roles: IDENTITY, STYLE, LAYOUT, CONTENT, ENVIRONMENT, OBJECT and LIGHT. Keep official names, quotations, chart values and logo assets out of generated pixels when exact reproduction or subsequent editability matters.

For real portraits define what must change and what must remain. A prompt cannot guarantee identical non-target pixels; when such a guarantee is requested, use a real region mask/composite method and inspect the result, or report a limitation. No unauthorized person replacement, face/body changes or forged evidence.

## Template-based output

Image motive -> real Canva image asset -> verified independent editable Canva text, logo, source and CTA elements -> platform-specific preview -> QA -> human approval -> real export. For an image_to_design experiment, verify every converted text, image and logo layer; do not assume a screenshot became editable just because conversion succeeded.

## Evidence gates

| Gate | BLOCKER example | Evidence |
| --- | --- | --- |
| Facts and locked copy | invented figure, wrong date, omitted required text | literal/source comparison and rendered proof |
| Branding/account | NGO logo on party post, wrong Canva account | active account and original logo reference |
| Identity | real person replaced or facial landmarks altered | original/reference comparison |
| Typography | misspelled glyphs, unreadable mobile copy | native text layers plus visual preview |
| Layout/platform | clipped CTA, controls cover face | rendered feed/story preview and current safe zone |
| Technical | wrong pixel ratio, corrupt or flattened required layers | file dimensions, Canva layer inspection |
| Print | no verified printer specs, ineffective image ppi | PDF print preflight and effective ppi |
| Rights | unapproved photo use | asset provenance record |
| Approval | final without review | recorded human approval |

Use PASS, FAIL, NOT_TESTED. No numerical quality score overrides a BLOCKER. A Sharp/Pixelmatch pixel difference can flag image changes but cannot establish legal rights, identity preservation or source correctness.

## Release states

Entwurf -> Geprüft -> Freigabe erforderlich -> Final.
Final requires the actual editor review, relevant checks and documented human approval. Technical success, finished generation, passed JSON preflight and completed upload are not equivalent to human publishing permission. Never publish automatically.
