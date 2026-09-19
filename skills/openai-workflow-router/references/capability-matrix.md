# Capability Matrix

## Surface legend

P = primary
S = secondary/useful
F = fallback only
N = generally not appropriate

| Capability | Chat | Work | Codex | Classic |
|---|---:|---:|---:|---:|
| Quick Q&A | P | S | N | F |
| Brainstorming | P | P | S | F |
| Long-form research | S | P | S | F |
| Books and dossiers | S | P | S | F |
| DOCX/PDF/Slides/Sheets artifacts | S | P | S | F |
| Connected SaaS operations | P | P | S | F |
| Local files and folders | S | P on desktop | P | F |
| Git/repositories | N | S | P | F |
| Terminal/PowerShell | N | N | P | F |
| React/Next.js implementation | N | S | P | F |
| Testing/build/deploy | N | N | P | F |
| MCP/local servers | N | N | P | F |
| Zotero Desktop | N | N | P | F |
| Image generation | P | P | N | F |

## Core Skills

### Portable across ChatGPT and Codex where supported

- brainstorming
- find-skills
- skill-creator
- politik-analyse
- peter-schuller-schreibstil
- peter-schuller-politiker-kommunikation
- peter-schuller-obmann-kommunikation
- automator
- powershell-senior-expert, primarily Codex in actual execution
- interaction-design
- interface-design
- ui-design-engineering
- ui-ux-pro-max
- impeccable
- web-design-guidelines
- react-best-practices, primarily Codex
- seo-review
- using-superpowers, primarily Codex

### Work-primary artifact and knowledge Skills

- document-development
- docx
- pdfs
- spreadsheets
- slides
- parliament-briefing-designer
- pdf-campaign-redesigner
- austria-open-data-research
- spoe-parlamentsforensik
- spoe-laimer-projekt-orchestrator
- peter-schuller-arbeitssteuerung
- danke-fuer-nichts-operations
- danke-fuer-nichts-publishing-audit
- danke-fuer-nichts-outreach
- danke-fuer-nichts-content-seo

### Runtime-specific

- Zotero plugin Skill: Codex/Desktop
- frontend-app-builder and related build-web-apps plugin Skills: Codex
- build-web-data-visualization plugin Skills: Codex
- openai-developers plugin Skills: Codex
- superpowers plugin Skills: Codex
- webmcp-site-author: Codex

## Plugin families

### Chat/Work primary

- Gmail
- Google Calendar
- Google Contacts
- Google Drive
- Microsoft Outlook Email
- Microsoft Outlook Calendar
- Microsoft SharePoint
- Microsoft Teams
- Slack
- HubSpot
- Notion
- Asana
- ClickUp
- Canva
- Adobe
- Adobe Acrobat
- Adobe Express
- Miro
- Canvs Whiteboard
- Make
- Booking.com
- Skyscanner
- trivago
- Wikiloc
- AccuWeather
- Legal Data Hunter
- Exa
- GSC Wizard

### Shared, but with different ownership by task

- GitHub: Work for context/read operations, Codex for implementation and repo writes.
- Figma: Work for design context, Codex for implementation.
- Stripe: Work for operational commerce, Codex for integration code.
- PostHog: Work for analysis, Codex for instrumentation changes.
- OpenAI Platform: Codex for API development, Chat/Work only for account-level actions when appropriate.

## Duplicate/overlap policy

### React
Use top-level `react-best-practices` by default. Use the plugin-bundled equivalent only inside a plugin workflow that explicitly depends on it.

### Superpowers
Use top-level `using-superpowers` as the router. Invoke plugin-specific Superpowers Skills only for the concrete development stage.

### shadcn
Use top-level `shadcn-ui` for user-facing shadcn work. Use plugin `shadcn` only when the build-web-apps workflow specifically requires its project tooling.

### UI generalists
Do not stack `ui-ux-pro-max`, `interface-design`, `ui-design-engineering` and `impeccable` as co-owners. Select one owner, then add specialist Skills only when needed.

## Recommended global rule

Portable instructions everywhere practical. External state through connectors. Local execution through Codex. Long-form artifact work through Work. Chat for fast interaction and decisions.
