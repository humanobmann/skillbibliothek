# Critique and Audit

Use this playbook when the user asks to review, critique, audit, assess, or improve an existing interface.

## Keep critique and audit distinct

### Critique

Judge whether the interface communicates priority, reduces cognitive load, feels coherent, supports the user's task, and expresses an appropriate visual identity.

Review:

* first read and visual hierarchy
* information architecture
* task flow and decision clarity
* density and grouping
* typography and readability
* color and contrast as hierarchy
* consistency without monotony
* visual identity and specificity
* trust cues and content credibility
* empty, error, and first-run experience

### Audit

Look for implementation risks that can be tied to evidence.

Review:

* semantic HTML and accessible names
* keyboard and focus behavior
* contrast and non-color state cues
* reduced motion
* responsive overflow and touch targets
* content expansion and localization
* loading and layout stability
* image sizing and asset cost
* excessive client-side work
* render-heavy animation
* duplicate components and hard-coded tokens
* error, loading, empty, and permission states

## Severity model

* Critical: blocks a primary task, creates severe accessibility failure, loses data, or makes the interface unusable for a meaningful user group.
* High: materially degrades task completion, comprehension, trust, or accessibility.
* Medium: creates recurring friction, inconsistency, or maintainability risk.
* Low: craft issue with limited user impact.

## Finding format

Use this structure:

`[Severity] Finding title`

Evidence: exact screen, component, selector, or code pattern.

Impact: concrete user or product consequence.

Fix: specific corrective action.

Avoid vague findings such as `improve hierarchy` without identifying what competes, which element should lead, and what to change.

## Scoring for broad critiques

When a numeric summary is useful, score each category from 1 to 5:

1. Hierarchy
2. Clarity
3. Task efficiency
4. Visual coherence
5. Accessibility readiness
6. Responsive readiness
7. Product specificity
8. Finish quality

Do not let the average hide a critical problem. Lead with critical and high severity findings regardless of score.

## Final prioritization

End broad evaluations with three groups:

1. Fix before shipping
2. Improve next
3. Optional craft upgrades

Do not create a massive backlog unless the user explicitly asks for one.
