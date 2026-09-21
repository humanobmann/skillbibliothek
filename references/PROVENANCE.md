# Provenienzregister und Lizenz-Compliance (Open Source Registry)

Dieses Dokument erfasst die Herkunft, Urheber, Lizenzen und Integrationsarten aller in diese Bibliothek übernommenen oder adaptierten Komponenten gemäß den Vorgaben aus Abschnitt 24 des Masterprompts.

---

## 1. Externe Komponenten & Architektur-Standards

| Komponente | Kanonische Quelle | Urheber / Maintainer | Lizenz | Version / Stand | Übernahme-Art | Attribution & Compliance-Status |
|---|---|---|---|---|---|---|
| **Open Agent Skills Standard** | [github.com/anthropics/skills](https://github.com/anthropics/skills) | Anthropic PBC | Apache 2.0 | v1.0 / 2026 | Spezifikation & Schema | Vollständig konform; Frontmatter-Schema (`name`, `description`, Progressive Disclosure) adaptiert. |
| **ModelScope MS-Agent** | [github.com/modelscope/ms-agent](https://github.com/modelscope/ms-agent) | Alibaba ModelScope Team | Apache 2.0 | v2.2 | Architekturmuster | Evidenz-basierte Webrecherche, strukturierte Speicherung unter `.research/evidence/` und progressive Intent-Erkennung übernommen. |
| **Claude-Skills Security Auditor** | [github.com/borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | Borghei et al. | MIT | 2025/2026 | Architektur & Heuristiken | Statische Prüfmuster für Prompt Injection und Credential Harvesting in `skill-security-auditor` überführt. |
| **Web Design Guidelines** | [github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Vercel Inc. | MIT | 2025/2026 | Regeln & Standards | Performance- und UI/UX-Checklisten als Offline-Referenz in `skills/web-design-guidelines/references/` integriert. |
| **Skills CLI Portability** | [github.com/antfu/skills-cli](https://github.com/antfu/skills-cli) | Anthony Fu | MIT | v0.4+ | Deployment-Muster | Cross-Runtime-Verlinkung und Deployment-Muster für Claude Code, Codex und Cursor adaptiert. |
| **TerminalSkills Router** | [github.com/TerminalSkills/skills](https://github.com/TerminalSkills/skills) | TerminalSkills Community | Apache 2.0 | 2025 | Router-Topologie | Intent-Map und Relegationsmuster für `skills/core-routing/` übernommen. |
| **UseOSINT Suite** | [useosint.com](https://useosint.com) | Bellingcat / OSINT Community | Open / Public Domain | 2025 | Fachmethodik | 28 OSINT- und Verifikationsskills mit ethischen Begleitregeln (`references/ETHICS.md`). |

---

## 2. Abgrenzung der Integrationsarten

1. **Spezifikation & Standard**: Übernahme der normativen Metadaten- und Frontmatter-Konventionen (z. B. Anthropic `SKILL.md`).
2. **Architekturmuster**: Konzeptionelle Neuimplementierung in Python und Markdown ohne 1:1 Code-Kopie (z. B. MS-Agent Evidenz-Store, ModelScope zweiphasige Kontextanalyse).
3. **Regel- und Checklistenübernahme**: Kuration von Best Practices unter Wahrung der MIT/Apache-2.0 Lizenzpflichten.
4. **Deterministische Eigenimplementierungen**: Alle Validierungs-, Benchmark- und Sicherheits-Skripte (`scripts/validate_skills.py`, `scripts/context_benchmark.py`, `skills/skill-security-auditor/scripts/*`) sind originäre Implementierungen für diese Bibliothek.

---

## 3. Lizenz-Compliance-Prüfung

- Alle Quell-Lizenzen (Apache 2.0, MIT) sind freie, kommerziell und privat uneingeschränkt nutzbare Open-Source-Lizenzen.
- Keine GPL- oder proprietär geschützten Komponenten ohne Weitergaberecht wurden in diese Bibliothek integriert.
- Alle Skripte enthalten standardkonforme Lizenz- und Funktions-Header.

## 4. Target-authored hardening

`code-review`, `library-skill-authoring`, `references/intent-map.md` and
`references/PROFILES.md` are original repository maintenance artifacts. The
`deep-research` evidence boundary, router transitivity rules, and auditor gates
are target rewrites of existing local material; no source tree was modified.


## 5. Social algorithm evidence layer

The `social-platform-algorithm-core`, TikTok, YouTube and LinkedIn optimizer
hardening in PR #4 is target-authored repository material. Platform facts are
grounded in publicly available first-party documentation from Meta Transparency
and Meta Newsroom, TikTok Support and TikTok Newsroom, YouTube Help, and
LinkedIn Help/Engineering. The repository records URLs, retrieval date, surface,
mechanism and claim scope; it does not copy platform source code or proprietary
ranking weights. Creator monetization documentation is explicitly separated
from recommendation-ranking evidence.


## 6. 2026 architecture expansion

The `mlops-ai-operations`, `cloud-native-security` and `low-code-no-code-engineering` skills are target-authored repository material.

Reference standards and first-party guidance used for architecture decisions:

- NIST AI Risk Management Framework and NIST AI 600-1 Generative AI Profile for AI governance.
- CNCF cloud-native survey and Kubernetes first-party Pod Security Standards / security checklist for cloud-native controls.
- SLSA and OpenSSF guidance for software supply-chain provenance and security posture.
- Microsoft Power Platform ALM and governance documentation for low-code lifecycle controls.

No external source code is copied into these skills. Examples are repository-authored and provider-neutral where practical.

## 7. 2026 SRE, FinOps and agentic-governance expansion

The `automated-sre-observability`, `finops-cloud-governance` and `agentic-ai-orchestration-governance` skills are target-authored repository material, added to extend the existing single-source `skills/<name>/SKILL.md` architecture (no structural fork or parallel tree was introduced).

Reference standards and first-party guidance used for architecture decisions:

- Google SRE workbook concepts (error budgets, symptom-based alerting, burn-rate alerting) as a publicly documented reliability-engineering baseline.
- FinOps Foundation Framework (Inform/Optimize/Operate phases and shared-responsibility principle) for cloud cost governance.
- NIST AI Risk Management Framework and OWASP guidance on LLM/agent risks (excessive agency, insecure tool use, resource exhaustion) for the agentic orchestration guardrails.

No external source code is copied into these skills. Examples, manifest schemas and validator scripts are repository-authored and provider-neutral.

## 8. 2026 evidence-based Meta Feed Strategy

`skills/social-platform-algorithm-core/references/meta-feed-strategy.md` is the canonical, regression-tested Facebook/Instagram feed-ranking source of truth for the library (target-authored repository material). `facebook-text-optimizer`, `instagram-text-optimizer` and `instagram-hashtag-research` route to it instead of holding divergent local copies; `adaptive-poster-image-series` shares its 4:5/1080x1350 feed-graphic and safe-zone standard.

The existing evidence model (`OFFICIAL`/`ACCOUNT`/`OBSERVED`/`HYPOTHESIS`) was extended, not replaced, with a `status` lifecycle (`active`/`superseded`/`deprecated`/`rejected`) on both source records and a new `claims` array in `evidence-records.json`, validated by `scripts/validate_social_evidence.py`. Thirteen previously-circulating algorithm myths (hashtag reach boosts, fixed comment/like weighting, a 4:5 ranking bonus, a blanket link penalty, an automatic image-text-ratio penalty, a general AI-image demotion, a hard first-hour rule, etc.) are recorded as `status: "rejected"` claims and are regression-gated by `tests/test_meta_feed_strategy.py`, which also greps the relevant skill directories to ensure no myth is restated as active prose outside the canonical file.

Research retrieval date: 2026-09-22, Europe/Vienna, frozen dataset (no confirmed live web access during this session). Reference standards and first-party sources used: Meta Transparency Center (Facebook/Instagram Feed, Feed Recommendations, Explore, Reels ranking explanations), Meta Newsroom (AI ranking overview, News Feed prediction, original-creator rewarding, engagement-bait policy, spam crackdown, distribution and recommendation guidelines, AI-generated-content labeling, EU political-ads policy), Instagram for Creators best-practices hub, and W3C WCAG 2.1 contrast guidance (cited as an accessibility reference only, never as a ranking factor). Each source is recorded in `evidence-records.json` with its real URL, publisher, title and retrieval date; no internal research-tool markers are stored.

The Instagram hashtag hard cap (maximum 5) was aligned across `instagram-hashtag-research` and `instagram-text-optimizer`, which previously allowed up to 8 in one skill's default range. The `adaptive-poster-image-series` feed-graphic safe margins for `feed_4x5` were raised from the prior 72/72/90/110 px (left/right/top/bottom) to the mandated 100/100/100/120 px, with an additional 40 px outer hard edge, consistently across its Markdown references and the three Python validators/self-test that encode them.
