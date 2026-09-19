# Craft Floor

Load immediately before implementation or final styling. These are quality defaults, not aesthetic dogma. A clear user brief may intentionally override a style warning, but never accessibility or functional correctness.

## Hierarchy

* Every viewport needs an obvious first read.
* One element should dominate each local decision region.
* Use spacing to express grouping before adding containers.
* Avoid making every heading, button, card, and badge equally loud.
* Keep secondary actions visually subordinate without making them inaccessible.

## Layout

* Align related edges deliberately.
* Use a small spacing system rather than arbitrary values everywhere.
* Avoid card nesting. Prefer section structure, dividers, whitespace, or a single surface level.
* Avoid centered composition by reflex. Choose alignment based on content and task.
* Avoid empty decorative columns and huge unused hero space unless the composition earns it.

## Typography

* Do not default to Inter merely because it is familiar.
* Use a small, deliberate type scale with clear role separation.
* Keep body text at a comfortable measure.
* Avoid all-caps paragraphs and excessive letter spacing.
* Use real font weight and line height hierarchy before relying on color alone.
* Maintain readable contrast on every surface.

## Color

* Build a semantic palette: background, surface, text, muted text, border, accent, success, warning, danger.
* Use accent color to communicate priority or state, not to decorate every component.
* Avoid purple-to-blue gradients and neon glows as generic AI decoration unless explicitly required by the brief.
* Do not put low contrast gray text on saturated backgrounds.
* Check selected, hover, focus, disabled, error, and success states.

## Components

* Prefer semantic controls over clickable `div` or `span` elements.
* Use icon buttons only when the icon is genuinely understood. Otherwise pair with text or accessible labeling.
* Avoid decorative rounded-square icon tiles above every heading.
* Avoid pill shapes for every control. Shape should signal function or system identity.
* Do not use modals for information that belongs inline.

## Motion

* Motion must explain state, continuity, causality, hierarchy, or feedback.
* Keep routine transitions short and restrained.
* Avoid `transition: all` where property-specific transitions are possible.
* Respect reduced-motion preferences for meaningful animation.
* Do not animate layout merely to make a static page feel active.

## Content and UX copy

* Buttons describe actions, not vague intent such as `Continue` when a more specific verb exists.
* Error messages state what happened and what the user can do next.
* Empty states explain why the state exists and the next useful action.
* Avoid filler copy, invented social proof, and synthetic statistics.

## Accessibility

* Preserve visible keyboard focus.
* Ensure form controls have accessible names.
* Images need appropriate alternative text or an explicit decorative treatment.
* Do not communicate state through color alone.
* Keep touch targets usable on mobile.
* Confirm logical DOM and keyboard order after visual reordering.

## AI design smell check

Reconsider the result if several of these appear together without a product-specific reason:

* Inter everywhere
* purple-blue gradients
* glass panels
* oversized generic gradient headline
* rounded cards inside rounded cards
* icon tile above every feature heading
* a three-column feature grid used regardless of content
* floating badge clutter
* excessive shadows and blur
* generic dashboard cards with no task hierarchy
* gray-on-gray information density
* decorative charts that do not answer a user question

The goal is not minimalism. The goal is intentionality.
