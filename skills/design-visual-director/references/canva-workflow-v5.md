# Native Canva Production Workflow

Canva owns the final editable design. ChatGPT handles research, art direction, structured data and checks. A native image generator, when available, produces motives and controlled photo edits. Text, original logos, facts, sources and layouts stay in Canva where feasible.

## Choose tools by objective

- Read: list_brand_kits, search_brand_templates, search_designs, get_design, get_design_pages, get_design_content, get_design_dataset and get_brand_template_dataset as actually available.
- Reuse: create_design_from_brand_template or copy_design on the correct account; originals immutable.
- Edit: start_editing_transaction, perform_editing_operations, get_design_thumbnail, commit_editing_transaction or cancel_editing_transaction. Each preview returned by the thumbnail tool must be shown; commit requires explicit user approval after preview.
- Populate: autofill_design only after checking a nonempty dataset, exactly matched field labels/types. Create a separate new design by default, never update_in_place on a master.
- Create: existing template first, then on-brand supported Canva generation; generic create_design cannot promise Brand Kit adherence unless its tool actually supports it.
- Media: upload_asset_from_url needs a real, retrievable URL or platform file reference; only use returned asset IDs. Do not invent a bridge between image generator and Canva.
- Variants: resize_design creates an independent output, followed by manual crop, text, person and safe zone review.
- Conversion: image_to_design may transform PNG, JPEG or WEBP into editable layers; this is experimental and requires an explicit inspection of every critical layer.
- Export: check exact target file type and resulting pixel size or PDF metadata; never claim 4K, 8K, bleed, CMYK or PDF/X without verifiable output.

## Production protocol

1. Determine brand, project_scope, Canva account, desired format, approved text, source evidence and protected assets.
2. Search existing designs and reusable Brand Templates only within the authorized account. Prefer verified master reuse over recreation.
3. Lock original logos, real people, source figures and all approved literal text. Do not embed them in a generative raster if native editability is required.
4. Create an independent working version. Inspect editable elements and dataset. No phantom Brand Templates or unsupported operations.
5. Produce the image motive using native ChatGPT Images if available and approved. Place into real Canva media elements with an actual upload result. Keep fonts/marks native.
6. Show a real preview after editing. Fix blocking errors, then request approval before committing transaction changes.
7. Derive each channel version as a separate Canva design. Perform per-format visual QA instead of assuming Resize is sufficient.
8. Return real edit/view links, the QA checklist, actual status and any blockers. Do not post automatically.

## Tool and provider boundaries

All methods depend on current live tool availability, current Canva plan and user permissions. Canva AI functions can spend credits. A skill cannot create missing auth, a subscription or an MCP server. Never use an HTML frame or a fabricated Canva replica if a provider call fails.

Optional Git repositories for future development: canva-sdks/canva-skills, canva-sdks/canva-developer-agent-kit, canva-sdks/canva-connect-api-starter-kit, openai/openai-node, modelcontextprotocol/typescript-sdk, lovell/sharp and mapbox/pixelmatch. Do not clone, install or run unfamiliar code automatically. Native connector actions take precedence.
