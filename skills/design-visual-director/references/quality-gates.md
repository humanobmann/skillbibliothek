# Visual quality and evidence gates

## Required QA record
For each relevant check record requirement, evidence method, result PASS/FAIL/NOT_TESTED, severity and action. Do not mark a visually inspected item as mechanically proven.

| Gate | BLOCKER examples | Allowed evidence |
|---|---|---|
| Content | wrong dates, source text altered, omitted locked text, invented sources | literal comparison against source, visual inspection |
| Identity | wrong person, identity distortions, misattributed portrait | reference comparison by available image viewing |
| Type | unreadable essential headline, corrupted umlaut or numeric figure | image inspect plus exact text layer inspection if available |
| Layout | cut-off content or severe overlap | full-size render and small-size thumbnail |
| Image | severe anatomy, impossible objects, forged evidence | image inspection, local edit review |
| Data | invented chart value or deceptive proportion | source table, axis audit, calculations |
| Platform | hidden content behind known controls, unsupported dimensions | official channel reference or marked internal heuristic |
| Technical | corrupt file, wrong requested format, missing linked media | file open, actual dimensions and preflight where possible |
| Accessibility | unacceptable content legibility or invalid control semantics | contrast test, keyboard/screen-reader testing where relevant |

## Severity and status
BLOCKER prevents publishing. MAJOR reduces professional suitability; correct before normal delivery where feasible. MINOR is fine tuning. PLANNED is a concept only; DRAFT is produced but not fully checked; REVIEWED only after documented visual/technical evaluation; APPROVED FOR INTENDED USE requires successful relevant checks and no known blocker; BLOCKED is material known failure; UNVERIFIED is missing essential evidence. Reviewer approval by a human is distinct from technical release readiness.

## Checks by artifact
Image: check all edges, glyphs, object count, perspective, light, overlap and reference fidelity. Social: feed thumbnail + native ratio + stated safe-region heuristics. PDF: page render + programmatic metadata/preflight when host offers it; never assert PDF/X compliance by appearance. UI: responsive states, keyboard focus, contrast, semantics, long text and reduced motion where relevant. Series: validate each individual slot; NEVER substitute a contact sheet for requested separate outputs. Corrected outputs need fresh examination.

## Iteration
Fix BLOCKER, then MAJOR. Limit repeated unchanged repair attempts. Escalate to controlled layout when permitted and typography consistently fails. Do not downgrade the user's original mandatory content to make an attractive image without permission.
