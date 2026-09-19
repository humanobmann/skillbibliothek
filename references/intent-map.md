# Canonical intent map

This map is the single routing target list. Every target below is a directory
under `skills/` with a `SKILL.md`; unknown or retired targets must be reported as
a gap, never guessed.

| Intent | Canonical target | Required evidence/context |
|---|---|---|
| security audit of a skill or untrusted skill | `skill-security-auditor` | target path and scan scope |
| multi-source/current web research | `deep-research` | question, date sensitivity, source constraints |
| stress-test a plan or design | `grilling` | settled decisions and open frontier |
| find a suitable skill | `find-skills` | user goal and constraints |
| code review | `code-review` | diff or file scope, test context |
| author or maintain a library skill | `library-skill-authoring` | skill purpose, inputs, links, provenance |
| UI/accessibility/performance guidance | `web-design-guidelines` | route/component and acceptance criteria |

Routing is transitive: aliases resolve to the canonical target, and the target
must not route back to `core-routing`. If no row matches, activate the most
specific existing domain skill or report the missing capability.
