# Canonical intent map

This map is the single routing target list. Every target below is a directory
under `skills/` with a `SKILL.md`; unknown or retired targets must be reported as
a gap, never guessed.

| Intent | Canonical target | Required evidence/context |
|---|---|---|
| data, metrics, KPI, spreadsheet analysis, report or dashboard routing | `data-analysis-router` | source, grain, period, population, requested output |
| Austrian or EU law, case law, legal citation or procedure routing | `legal-at-eu-router` | jurisdiction, legal issue, document basis, current-law cutoff |
| security audit of a skill or untrusted skill | `skill-security-auditor` | target path and scan scope |
| multi-source/current web research | `deep-research` | question, date sensitivity, source constraints |
| stress-test a plan or design | `grilling` | settled decisions and open frontier |
| find a suitable skill | `find-skills` | user goal and constraints |
| code review | `code-review` | diff or file scope, test context |
| technical implementation specification before coding | `implementation-specification` | project evidence, approved scope, interfaces, tests and constraints |
| read-only specification readiness audit | `specification-readiness-audit` | specification suite, source authority, implementation target |
| controlled multi-document implementation documentation suite | `implementation-documentation-suite` | multiple authoritative sources/domains, precedence, specialist ownership |
| author or maintain a library skill | `library-skill-authoring` | skill purpose, inputs, links, provenance |
| consolidate, migrate, version or remove plugins and skills | `plugin-portfolio-control` | plugin inventory, backend IDs, releases, sources, authorization |
| extract decisions, tasks, owners and deadlines from material | `action-register` | source material, project context, authority boundary |
| transfer work between chats, sessions, agents or people | `work-handoff` | current state, source of truth, verified completion, next action |
| build SOP, runbook, playbook or operational checklist | `operating-procedure-builder` | real process evidence, roles, systems, exception paths |
| UI/accessibility/performance guidance | `web-design-guidelines` | route/component and acceptance criteria |
| cross-platform social algorithm, reach, discovery or ranking analysis | `social-platform-algorithm-core` | platform, surface, format, current evidence |
| design a reusable multi-platform social content operating system | `social-content-engine` | communication goal, platforms, resources, governance and metrics |
| MLOps, LLMOps, model lifecycle, model release or AI operations | `mlops-ai-operations` | workload type, data/model provenance, release criteria |
| Kubernetes, container, GitOps or cloud-native security review | `cloud-native-security` | workload/cluster scope, identities, manifests, trust boundaries |
| low-code/no-code governance, ALM or enterprise automation engineering | `low-code-no-code-engineering` | platform, connectors, data classification, environment strategy |
| SRE, SLO/error-budget design, alerting, on-call escalation or incident response | `automated-sre-observability` | service, SLI type, target, current alerting/runbook state |
| FinOps, cloud budget guardrails, cost tagging, anomaly detection or commitment strategy | `finops-cloud-governance` | workload, cost center, current budget/tagging state |
| multi-agent or autonomous agent orchestration, tool-scope governance, loop/context-overflow guardrails | `agentic-ai-orchestration-governance` | agent task, autonomy level, tool access needed |
| quick natural German rewrite without a full audit | `humanizer-de-natural` | source text, locked facts, intended register |
| personal text in Peter Schuller's voice or final voice pass | `peter-schuller-schreibstil` | draft, role, factual boundary, intended register |
| political text in an abstracted Philip Kucher rhetoric profile | `philip-kucher-writing` | draft or topic, factual basis, output format |
| Robert Laimer weekly dossier, source bundle, QA or editorial weekly plan | `weekly-dossier` | current week, source bundle, current official sources, Make pipeline state |
| Facebook post or caption optimization | `facebook-text-optimizer` | post, audience, communication goal |
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
