---
name: core-routing
description: Central intent router for identifying user goals and delegating execution to specialized skills with zero unnecessary context consumption.
metadata:
  canonical: true
  profile: control-plane
  provenance: target-rewrite
allowed-tools:
  - Read
  - Glob
---

# Core Routing Control Plane

## Zweck

Universeller Intent-Router. Er waehlt den spezifischsten vorhandenen Fachskill, ohne ungenutzte Instruktionen zu laden.

## Trigger

Aktivieren bei komplexen, offenen oder domaenenuebergreifenden Anforderungen sowie bei Fragen nach dem passenden Skill.

Nicht aktivieren bei direktem Aufruf eines bekannten Skills oder einer eindeutig durch einen Fachskill abgedeckten Anfrage.

## Routing Decision Logic

1. Sicherheit/Audit -> `skills/skill-security-auditor`
2. aktuelle oder mehrstufige Recherche -> `skills/deep-research`
3. Social Media:
   - plattformuebergreifender Algorithmus, Ranking, Reach, Discovery oder Search -> `skills/social-platform-algorithm-core`
   - Facebook Text -> `skills/facebook-text-optimizer`
   - Instagram Text -> `skills/instagram-text-optimizer`
   - Instagram Hashtags -> `skills/instagram-hashtag-research`
   - TikTok -> `skills/tiktok-content-optimizer`
   - YouTube/Shorts -> `skills/youtube-content-optimizer`
   - LinkedIn -> `skills/linkedin-content-optimizer`
   - Social Poster-/Bildserie -> `skills/adaptive-poster-image-series`
   Bei plattformspezifischer Algorithmusoptimierung wird der Plattformskill ausgefuehrt und social-platform-algorithm-core als gemeinsame Evidenzschicht geladen.
4. AI/ML Operations, model lifecycle oder LLMOps -> `skills/mlops-ai-operations`
5. Kubernetes, Container, GitOps oder Cloud-Native Security -> `skills/cloud-native-security`
6. Low-Code/No-Code Governance und ALM -> `skills/low-code-no-code-engineering`
7. SLOs, Error Budgets, Alerting, Observability oder Incident Response -> `skills/automated-sre-observability`
8. Cloud-Kostenguardrails, Tagging, Budget oder Commitment-Strategie -> `skills/finops-cloud-governance`
9. Multi-Agent-/autonome Agent-Orchestrierung, Tool-Scoping oder Guardrails gegen Endlosschleifen/Kontextueberlauf -> `skills/agentic-ai-orchestration-governance`
10. Frontend/Design -> `skills/web-design-guidelines`
11. Skill-Suche -> `skills/find-skills`
12. andere Fachaufgaben -> spezifischsten vorhandenen Skill aktivieren; bei echter Luecke nichts erfinden.

## Workflow

1. Primaeres Ziel und Randbedingungen extrahieren.
2. Gegen [intent-map.md](../../references/intent-map.md) abgleichen.
3. Nur die minimale Beschreibung des Zielskills laden.
4. Aliase genau einmal aufloesen; Zyklen oder unbekannte Ziele ablehnen.
5. Zielskill aktivieren und Routing beenden.

## Hard Rules

- Direkte Skill-Nennung hat Vorrang.
- Ein Plattformskill ist spezifischer als der gemeinsame Social Algorithm Core, wenn die Plattform feststeht.
- Der Core ersetzt den Plattformskill nicht; er liefert Evidenz fuer Algorithmus-, Reach- und Search-Fragen.
- Keine nicht vorhandenen Skills erfinden.
