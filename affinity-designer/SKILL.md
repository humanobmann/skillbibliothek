---
name: affinity-designer
description: Safely inspect, edit, and export Affinity Designer, Photo, and Publisher documents on Windows through a local Affinity MCP/SDK integration. Use for the active Affinity document or named .afdesign, .afphoto, and .afpub files; when the integration is unavailable, diagnose the missing capability and provide a clear non-executed fallback.
---

# Affinity Designer

Work through the locally available Affinity MCP/SDK integration without assuming its server name, tool names, schemas, or capabilities. Preserve the source document and existing editable structure while producing a visually verified working copy and requested exports.

## Start with the integration contract

Before inspecting or changing a document:

1. Read the connected MCP server's preamble, capability description, and safety guidance in full.
2. Read the relevant SDK documentation or MCP resources for document discovery, inspection, mutation, saving, rendering, and export. Load only the sections needed for the request.
3. Inspect the exact schemas of every tool intended for use. Treat listed tools and resources as the only supported API; never invent a method, parameter, menu action, response field, or success state.
4. Establish whether the integration actually supports Affinity Designer, Photo, Publisher, the active document, direct file opening, and the requested export format. A connected server is not proof of a capability.

Read [references/mcp-sdk-discovery.md](references/mcp-sdk-discovery.md) whenever discovering or troubleshooting the integration.

If the integration, preamble, or required capability is unavailable, do not simulate edits or claim completion. State precisely what is missing and give the fallback in **Fallback** below.

## Separate analysis from mutation

### Analysis phase

Resolve the target unambiguously: the active document or one explicit `.afdesign`, `.afphoto`, or `.afpub` path. For an active document, record the application, document name, saved/unsaved state, and backing path if exposed. For a file target, confirm that it exists and that its extension matches the requested Affinity application.

Inspect before editing, using only documented read operations. Capture what the integration exposes about:

- document type, dimensions, DPI, color space/profile, bleed, margins, spreads, artboards, or pages;
- layer hierarchy, names, visibility, locking, grouping, masks, adjustments, and effects;
- text frames, text content, styles, fonts, overflow, alignment, tracking, leading, and typography;
- placed or embedded images, links, crop/fit state, effective resolution, and missing assets;
- fills, strokes, swatches, gradients, opacity, blend modes, and reusable styles;
- export presets, slices, linked resources, unsupported objects, and warnings.

Render a baseline preview when supported. Summarize the intended changes, affected objects/pages, invariants to preserve, outputs, and validation criteria before mutation. Ask only when the target, desired result, or a consequential design choice remains genuinely ambiguous.

### Mutation phase

Treat every source as an original unless the user explicitly identifies it as a disposable working copy. Never save changes over the original.

- For a named file, create a unique working copy before opening it for mutation. Prefer `scripts/New-AffinityWorkingCopy.ps1` when local file access is available.
- For an active saved document, use a documented **Save As**, **Save a Copy**, or duplicate-document capability to create a distinct Affinity working file before the first mutation.
- For an active unsaved document, first save a distinct working document through a documented capability. If that is unavailable, stop before mutation and request that the user save or duplicate it manually.
- For large, multi-page, structural, destructive, or hard-to-reverse edits, create an additional checkpoint copy before the change set.
- Never flatten, rasterize, merge, detach, replace, or delete editable structure unless required by the request and supported by the documented workflow. Prefer targeted edits to existing objects and preserve layer names, hierarchy, IDs, styles, masks, links, artboards, and pages where possible.
- Unlock or reveal an object only when needed, restore its prior state when practical, and do not silently substitute missing fonts, profiles, or linked assets.

Execute changes in small coherent batches. After each structural batch, re-inspect the affected objects so a partial or misdirected mutation is caught early.

## Supported task families

Use the documented capabilities of Affinity Designer, Affinity Photo, or Affinity Publisher as appropriate:

- edit text content, styles, font choices, size, leading, tracking, alignment, frames, and overflow;
- place, replace, crop, fit, resize, mask, and reposition images while maintaining intended aspect ratio and sufficient output resolution;
- create, rename, reorder, group, hide, lock, duplicate, or remove layers without collapsing unrelated structure;
- create or edit artboards in Designer and pages/master-page relationships in Publisher when supported;
- change canvas, document, artboard, page, bleed, margin, DPI, or output dimensions with explicit units and scaling behavior;
- adjust layout, grids, guides, alignment, spacing, typography, fills, strokes, swatches, gradients, opacity, blend modes, and color profiles;
- save an editable Affinity working file and export PNG, JPEG/JPG, or PDF according to the user's requested dimensions, pages/artboards, quality, color handling, bleed, and transparency.

Do not force a cross-application operation when the connected SDK documents it as unsupported. Preserve `.afdesign`, `.afphoto`, or `.afpub` according to the source application unless the user explicitly requests a supported conversion.

Read [references/operations-and-qa.md](references/operations-and-qa.md) for edit planning, format-specific export checks, and the visual QA loop.

## Safe outputs

Use absolute Windows paths. Default to a new sibling workspace or a user-provided output directory; never default to the source filename. Sanitize derived names, preserve the correct extension, and add a timestamp or explicit version suffix. Refuse a resolved output path that equals the original path.

Before every save or export, check whether the destination already exists. Create a new versioned filename instead of overwriting unless the user explicitly selected an expendable generated output in the current task. Keep editable Affinity output separate from rendered exports.

After a tool reports success, verify the output through readback where possible: file existence, nonzero size, format, dimensions/page count, and a fresh render from the saved/exported artifact. A tool acknowledgement alone is not visual verification.

## Render, inspect, correct

After production, render every affected artboard, page, spread, or export at useful inspection resolution. Compare against the baseline and requested outcome. Check for clipping, overflow, missing fonts/assets, accidental movement, changed stacking, pixelation, halos, transparency errors, color shifts, bleed/trim mistakes, blank or duplicated pages, and inconsistent spacing.

Correct identified defects with focused changes, then render the affected output again. Limit autonomous correction to two focused passes; if a defect persists or the fix would require a new design decision, preserve the last safe working copy and report the unresolved issue instead of making broad speculative changes.

Finish with a concise record of:

- analyzed source and application;
- working-copy path and whether a checkpoint was created;
- material changes made;
- editable Affinity output and rendered export paths;
- inspections actually performed and their result;
- warnings, unsupported features, substitutions, or unverified items.

## Fallback

When Affinity MCP/SDK access is missing or insufficient, do not use UI automation, filesystem binary rewriting, or another editor as an implicit substitute. Explain which integration or capability is absent. Ask the user to enable/connect the local Affinity MCP integration and expose its preamble plus relevant SDK resources, or to perform the narrowly specified manual Affinity step (for example, save a copy) and then retry. You may still provide a non-executed edit/export checklist, clearly labeled as instructions rather than completed work.
