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
