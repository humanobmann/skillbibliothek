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
| cross-platform social algorithm, reach, discovery or ranking analysis | `social-platform-algorithm-core` | platform, surface, format, current evidence |
| political text in an abstracted Philip Kucher rhetoric profile | `philip-kucher-writing` | draft or topic, factual basis, output format |\n| Facebook post or caption optimization | `facebook-text-optimizer` | post, audience, communication goal |
| Instagram caption, Feed, Carousel or Reel text optimization | `instagram-text-optimizer` | content, format, audience |
| Instagram hashtag research | `instagram-hashtag-research` | topic, language, region, format |
| TikTok hook, script, For You or Search optimization | `tiktok-content-optimizer` | surface, video concept, audience, query intent |
| YouTube video, Shorts, title, thumbnail, Search or retention optimization | `youtube-content-optimizer` | surface, format, video concept, analytics if available |
| LinkedIn post, Feed or Suggested Posts optimization | `linkedin-content-optimizer` | surface, professional audience, post goal |
| social editorial poster or ten-image campaign series | `adaptive-poster-image-series` | theme/texts/templates, target platform, factual mode |

Routing is transitive: aliases resolve to the canonical target, and the target
must not route back to `core-routing`. If no row matches, activate the most
specific existing domain skill or report the missing capability.

For platform-specific social work, use the platform skill as execution skill
and `social-platform-algorithm-core` as the shared evidence layer when algorithm,
reach, ranking, Search, Discovery or maximal optimization is part of the task.
