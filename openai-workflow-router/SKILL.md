---
name: openai-workflow-router
description: Route tasks across ChatGPT Chat, Work, Codex, local projects, Skills, plugins, connectors, MCP and artifact workflows. Use whenever a request spans multiple OpenAI surfaces, asks where a task should run, needs a handoff between research, documents and code, or risks duplicate/conflicting Skills or plugins. Prefer portable Skills across surfaces, keep environment-specific capabilities only where their runtime exists, and define fallbacks when a capability is unavailable.
---

# OpenAI Workflow Router

Use this Skill as the control plane for deciding where work should happen and which capability should own it.

## Core rule

Choose the smallest capable surface and the smallest capable Skill set.

Do not force every Skill or plugin into every surface. Make portable logic available everywhere practical, and keep runtime-bound integrations only where they can actually execute.

## Surface routing

Route by task type:

- Use Chat for quick questions, decisions, short research, brainstorming, drafting, image generation and lightweight connected-app actions.
- Use Work for long-form research, books, dossiers, documents, spreadsheets, presentations, multi-file knowledge work, connected-app workflows and durable project context.
- Use Codex for repositories, local projects, terminal work, Git, PowerShell, MCP, APIs, tests, React, Next.js, deployment and technical automation.
- Treat ChatGPT Classic as compatibility fallback only. Do not start new workflows there unless a required capability exists only there.

Read `references/capability-matrix.md` when a task spans surfaces or when availability is uncertain.

## Skill routing

Apply one primary Skill whenever possible. Add secondary Skills only when they contribute a distinct stage.

Preferred composition patterns:

- Long-form content: brainstorming -> document-development -> non-fiction-revision when a substantial factual draft exists -> fact-check as a separate verification pass -> role/style overlay -> docx/pdf if files are required.
- Political work: politik-analyse -> relevant role communication Skill only when a finished political text is requested.
- Social-media text: research or politik-analyse for current/strittige claims -> role communication Skill -> exactly one platform owner (`facebook-text-optimizer` or `instagram-text-optimizer`) -> optional humanizer-de -> fact-check as the final pass whenever externally verifiable, political, legal, health, financial or safety-critical claims remain. The platform owner never publishes the text.
- Development: agents-md maintains portable repository instructions; using-superpowers handles complex implementation workflow -> framework-specific Skill -> security-gate -> verification.
- UI: choose one primary UI Skill by scope; add interaction-design, react-best-practices, shadcn-ui or seo-review only for their specialist concern.
- Austrian public data: austria-open-data-research for structured/reproducible datasets; politik-analyse for interpretation.
- Parliamentary deep research: spoe-parlamentsforensik owns forensic research; parliament-briefing-designer owns the final briefing artifact.
- Book campaign: danke-fuer-nichts-operations only when two or more campaign domains must be orchestrated; otherwise invoke the specialist Skill directly.

Avoid loading overlapping generalists together.

## Social-platform boundary

Choose a platform owner from the requested channel, not from a generic desire for reach:

- `facebook-text-optimizer` owns Facebook post or caption revision.
- `instagram-text-optimizer` owns short Feed, Carousel and Reel captions and its mandatory current hashtag research.
- Neither skill promises distribution, trends, reach or non-follower visibility. For a current platform-rule question, use official Meta sources at request time.
- A visible caption, a visual asset and a publishing action remain separate stages. Image skills create or audit the visual; Connector or publishing workflows require separate user authorization.

## OSINT safety boundary

For public-interest, political, cross-border, human-rights, corporate-accountability or other investigative reporting, invoke `journalistic-osint-governance` **before** `investigate-anything`. It owns documented public interest, necessity, proportionality, jurisdiction, source protection, data minimisation, right-of-reply and publication stop-gates.

Use `useosint` or `investigate-anything` only for a legitimate, proportionate, public-interest, self-audit, organizational-security, journalism, compliance or user-authorized research purpose. Start by recording the question, target scope, legal/ethical basis and a passive collection plan.

- Prefer public records, official registers, archived public pages and passive third-party datasets.
- Do not log into accounts, use leaked credentials, scrape private areas, scan targets directly, bypass access controls, identify uninvolved private people, build stalking dossiers or expose sensitive personal data.
- For a business, domain, own exposure or security review, use the narrowest relevant specialist skill and retain sources, dates, confidence and negative findings.
- Use `write-the-intel-brief`, `source-verification` or `fact-check` before presenting a consequential finding. Separate observed fact, inference and unresolved lead.
- Do not treat a journalism purpose, public availability, a public role, a security finding or a foreign jurisdiction as a blanket exception to privacy, data-protection, platform, computer-misuse or source-protection rules. Where the governance skill calls for editorial/legal review, return `HOLD FOR REVIEW` rather than improvising.

## Portability policy

Classify every capability as one of:

1. Portable Skill
   - Instructions, templates, standards, checklists and text workflows.
   - Keep available in ChatGPT and Codex when useful.
   - Store canonical source in Git whenever the Skill is user-maintained.

2. Surface Skill
   - Depends on a host-specific artifact system, persistent workspace, local runtime or platform behavior.
   - Install only on surfaces where it can execute correctly.

3. Connector or plugin
   - Depends on OAuth, external SaaS, MCP, desktop app, account connection or product-specific tool.
   - Do not duplicate its behavior in a Skill.
   - Keep a portable fallback instruction for export/import or manual handoff when possible.

4. Local runtime capability
   - Terminal, repo, PowerShell, local Zotero, local MCP, build/test environment.
   - Codex is primary.

## Availability rule

When the user asks to make capabilities available everywhere:

- Make all portable Skills available across ChatGPT and Codex where supported.
- Keep Work-oriented artifact Skills available in Work/ChatGPT.
- Keep local execution Skills and MCP integrations in Codex/Desktop.
- Keep connected SaaS apps in Chat/Work when their connector is available; use Codex only when code or API integration is required.
- Do not create fake parity where the platform does not provide it.
- Define a handoff path instead.

## Duplicate suppression

When equivalent Skills exist at top level and inside a plugin bundle:

- Prefer the already-installed top-level Skill if scope and freshness are equivalent.
- Prefer the plugin-bundled variant only when the workflow explicitly depends on that plugin package or it is materially newer/more specific.
- Never invoke both equivalent variants for the same stage.

Known duplicate families to treat carefully include React best practices, shadcn guidance, Superpowers workflows and broad UI/design generalists.

## UI routing

Use exactly one broad UI owner:

- ui-ux-pro-max: new interface or broad redesign.
- interface-design: product interface design/review.
- ui-design-engineering: evidence-first cleanup and hardening.
- impeccable: final visual craft pass.

Then add specialists only if needed:

- interaction-design for motion and behavior.
- shadcn-ui for shadcn mechanics.
- react-best-practices for React/Next.js performance.
- web-design-guidelines for guideline/accessibility audit.
- seo-review for SEO.

## Plugin and connector routing

Use connected apps for external state. Do not encode credentials or external state into Skills.

Recommended ownership:

- Microsoft 365, Google Workspace, Slack, HubSpot, Canva, Adobe, Miro, Make: Chat/Work for operational use.
- GitHub: Work for issue/context lookup; Codex for repository implementation.
- Figma: Work for design collaboration; Codex when implementing the design.
- PostHog: Work for product analysis; Codex for instrumentation changes.
- Stripe: Work for business operations; Codex for integration code.
- OpenAI Platform: Codex for API implementation and troubleshooting.
- Semrush: Chat/Work for external SEO and competitive research; combine with GSC for owned-site truth.
- Vercel: Codex for deployment/runtime operations and Work for operational inspection when supported.
- Zotero Desktop Skill: Codex/local runtime.

## Handoff protocol

When moving work between surfaces, preserve a compact handoff bundle:

- goal
- current state
- decisions already made
- source files or repo paths
- relevant URLs/IDs only when safe and necessary
- active Skill owner
- next action
- verification criteria

Prefer project files such as `PROJECT.md`, `AGENTS.md`, `STYLEGUIDE.md`, `DECISIONS.md`, `SOURCES.md` and repository documentation over relying on chat history alone.

## Canonical-source policy

For user-owned reusable Skills and prompts, use one canonical Git repository as source of truth when practical.

Recommended layout:

```text
ai-workflows/
  skills/
  prompts/
  standards/
  templates/
  compatibility/
```

Do not make ChatGPT, Work or Codex the only place where critical reusable project logic exists.

## Verification

Before declaring a workflow optimized, confirm:

1. Every major task class has exactly one primary surface.
2. Every broad capability has exactly one primary Skill owner.
3. Portable Skills have a canonical source and can be installed where useful.
4. Connector-bound capabilities are not duplicated as pseudo-Skills.
5. Runtime-bound capabilities remain on the correct surface.
6. Every cross-surface workflow has an explicit handoff.
7. No known duplicate Skills are invoked simultaneously.
8. Substantive software changes pass security-gate before release.
9. Classic is not used for new work unless required for compatibility.
