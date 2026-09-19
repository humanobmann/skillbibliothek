# Metadata

Use for page metadata, social previews, indexing controls, manifests, icons, and structured data.

## Workflow

1. Find missing, conflicting, or duplicated metadata.
2. Fix correctness and indexing errors first.
3. Keep title, description, canonical URL, and social URL aligned.
4. Validate social preview behavior against a publicly reachable URL when possible.
5. Keep code changes scoped to metadata.

## Correctness

- Define each metadata concern in one authoritative place per page.
- Avoid duplicate title, description, canonical, or robots directives.
- Keep dynamic metadata deterministic and sanitize user-provided strings.
- Provide safe defaults for routable pages.

## Title and description

- Every page needs a meaningful title.
- Use a consistent title convention across the product.
- Avoid keyword stuffing.
- Searchable or shareable pages should normally have a useful plain-text description.

## Canonical and indexing

- Canonical URLs must point to the preferred public URL.
- Use `noindex` intentionally for private, duplicate, preview, or staging content.
- Keep robots directives aligned with actual publication intent.
- Handle pagination and alternate routes deliberately.

## Social cards

- Set Open Graph title, description, image, and URL for shareable pages.
- Use absolute URLs for social images.
- Keep `og:url` aligned with canonical.
- Choose the correct Open Graph type.
- Use an appropriate Twitter/X card type, commonly a large-image summary for content pages.

## Icons and manifests

- Provide a broadly compatible favicon.
- Add Apple touch icons and a manifest when the product needs them.
- Keep icon paths stable and cacheable.
- Set browser theme color intentionally.

## Structured data

- Add JSON-LD only when it corresponds to real rendered content.
- Never invent ratings, reviews, prices, authorship, organization details, or other structured-data facts.
- Validate emitted JSON-LD syntax and page consistency.
