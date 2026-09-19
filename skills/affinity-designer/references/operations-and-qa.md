# Affinity operations and quality assurance

Use this reference after the integration contract is known and the target document has been analyzed.

## Change plan

For each requested outcome, identify:

- target application, document, page/artboard, layer, and object using stable identifiers when available;
- current value and requested value;
- units, anchor point, coordinate space, scaling/cropping behavior, and color representation;
- related objects or constraints that must remain unchanged;
- observable acceptance check in the final render.

Order dependent changes deliberately: document/page geometry, structural layers, placed assets, text frames/styles, colors/effects, then exports. Re-read the affected scope after each structural batch.

## Editing checks

### Text and typography

Preserve paragraph and character styles when possible. Check font availability before changing fonts. Verify language, hyphenation, ligatures, alignment, baseline, leading, tracking, frame insets, text-on-path behavior, and overset text. Inspect the rendered result rather than relying only on stored text values.

### Images and pixel content

Distinguish placed, linked, embedded, and pixel-layer content. Preserve aspect ratio unless deliberate distortion is requested. Verify crop/fit mode, transform, mask, interpolation, effective DPI, transparency, linked-resource status, and color profile. Do not silently embed, relink, rasterize, or resample.

### Layers and structure

Prefer edits to existing nodes. Preserve names, order, grouping, masks, clipping relationships, symbols, styles, visibility, locks, and blend modes unless the task requires a change. Confirm that a selector resolves to exactly the intended object before bulk mutation.

### Artboards and pages

For Designer, verify artboard size, position, naming, background, and export scope. For Publisher, verify page/spread order, facing-page behavior, master-page association, bleed, margins, linked frames, and pagination. Do not translate one model into the other unless the SDK explicitly supports it.

### Size, layout, and color

Make units explicit. Distinguish resizing a document/canvas/page from scaling content. Record anchor and whether strokes, effects, corners, and text scale. For print work, verify profile, color space, spot/global colors, overprint if exposed, bleed, trim, and PDF settings. For screen output, verify pixel dimensions, DPI metadata where relevant, RGB profile, transparency, and resampling.

## Export rules

Export into the dedicated output directory with unique filenames. Use the integration's documented preset or explicit parameters; never guess defaults when they materially affect the result.

### PNG

Verify pixel dimensions, selected page/artboard/slice, RGB/profile behavior, transparency or matte, resampling, and that no unintended background was introduced.

### JPEG/JPG

Verify pixel dimensions, quality, RGB/profile behavior, resampling, and background flattening. JPEG cannot preserve transparency; require or derive an intentional background through the documented workflow.

### PDF

Verify page/artboard range and order, trim size, bleed inclusion, crop/registration marks, color profile, font handling, rasterization/downsampling, transparency, and PDF preset/standard when requested. Do not claim print readiness without checking the requested print specification.

### Affinity document

Save to a new `.afdesign`, `.afphoto`, or `.afpub` path appropriate to the source application. Confirm that the saved document can be reopened or re-inspected and retains expected editable structure. Do not change extension as a substitute for a supported conversion.

## Visual QA loop

1. Render a baseline before mutation when supported.
2. Render every affected page, spread, or artboard after mutation; render the final exported artifact rather than only the in-memory document when possible.
3. Compare composition, geometry, hierarchy, text wrapping, typography, imagery, colors, transparency, effects, and page/artboard coverage against the request and preserved invariants.
4. Inspect edges and small type at higher zoom when output resolution matters.
5. Correct only the identified defect and rerender the affected scope.
6. Stop after two focused correction passes if the defect persists or a new design decision is required.

Record whether validation was visual, structural, filesystem-level, or unavailable. Never describe structural inspection alone as visual approval.
