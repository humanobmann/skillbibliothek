# Guided design briefing decision tree

## Recognition
IF explicitly asked to create immediately AND goal/medium/content known THEN EXPRESS, 0 questions.
ELSE IF explicitly asked for a virtual interview/selection or is unsure about artistic choices THEN GEFUEHRT.
ELSE IF the task involves actual commercial printer specs, native editable source or contractual mandatory text THEN EXPERTE only if user wants an in-depth interview; otherwise GEFUEHRT focused on real blockers.

## Per-turn procedure
1. Parse all known details from current conversation and uploaded files.
2. Present a progress cue only when helpful (e.g. 'Schritt 2 von etwa 4'). No fake exact step count for adaptive branching.
3. Ask exactly one high-impact unknown, with up to 4 answer options and 'Auto'. Offer short free text.
4. On choice, append it to brief state, restate only ambiguous binding, choose next unknown. Never restart from Step 1.
5. On ZURUECK, revise prior editable selection without deleting locked content.
6. On AUTO, decide only a nonfactual creative field and record chosen assumption.
7. On FERTIG, skip optional prompts and produce finished brief plus executable next step.

## Branches
- User supplied portrait and layout: do NOT ask them to upload a photo or select reference role again; ask if the portrait is an IDENTITY lock only when truly ambiguous.
- User says 'keine Fotos': never suggest human portrait directions. Offer typography/symbol/conceptual illustration.
- User says 'keine KI-Artefakte': prioritize controlled typeset, reliable object rendering and manual QA; no absolute zero-artifact guarantee.
- User says 'nur planen': produce a professional plan and do not create media files.
- User says 'erstelle': after any real blocker, create with tools; no invented final image link.
- User gives exact long text: do not shorten without permission; warn about probable mobile fit and offer multi-slide design as optional direction, never replace user input silently.
- Political/NGO context uncertain: leave neutral and no unsolicited branding.

## Handoff
Carry factual locks, reference role map, design direction, medium and output into `design-visual-director` as one brief. Proposals must never be misrepresented as verified output.
