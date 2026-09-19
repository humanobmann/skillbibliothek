---
name: security-gate
description: Route software changes through the correct security review before release. Use when a repository, API, web app, automation, MCP server, agent workflow, deployment, dependency change, secret-handling change, or infrastructure change needs a security gate, or when deciding between portable security guidance and Codex Security scans. Prefer OpenAI security-best-practices for secure-by-default guidance, use OpenAI security-threat-model for material architectural trust-boundary analysis, and use Codex Security plugin scans only when that runtime is available.
---

# Security Gate

Treat this Skill as a router and release gate, not as a replacement for specialist security scanners.

## Classify the change

Identify the smallest applicable classes:

- application code
- API or authentication/authorization
- agent or MCP integration
- secrets or credentials
- dependency or supply chain
- infrastructure or deployment
- data handling or privacy boundary
- Git-backed diff, pull request, commit, or full repository

Read `references/security-routing.md` when more than one class applies or the correct scanner is unclear.

## Route to the correct security capability

1. Use `security-best-practices` for Python, JavaScript/TypeScript, or Go secure-by-default guidance and focused security review when available.
2. Use `security-threat-model` for new architectures, material trust-boundary changes, agent/MCP systems, authentication/authorization redesigns, sensitive data flows, or internet-exposed services when available.
3. Use Codex Security `security-diff-scan` for a Git-backed change set when the Codex Security plugin runtime is installed and available.
4. Use Codex Security `deep-security-scan` only for an explicitly requested exhaustive repository or scoped-path scan when its plugin runtime is available.
5. Use Codex Security `define-security-policy` to create or revise repository scanner guidance when that runtime is available.
6. Do not copy plugin-bound Codex Security skills out of their plugin and pretend they are standalone portable skills.
7. If a specialist runtime is unavailable, run the fallback release checklist and clearly mark the result as a checklist review rather than an automated security scan.

## Mandatory release checks

Before calling a technical change ready for release, verify as applicable:

- authentication and authorization boundaries are explicit
- external and attacker-controlled inputs are validated at trust boundaries
- secrets are not committed, logged, embedded in prompts, or stored in source
- privileged actions use least privilege and fail closed where appropriate
- dependency changes are deliberate and lockfiles are consistent
- network destinations and data egress are expected
- destructive actions have confirmation, rollback, or safe recovery where practical
- tests cover the relevant security invariant or failure path
- deployment configuration does not expose debug, development, or admin surfaces unintentionally
- repository security guidance is present when the application has material security boundaries

## Agent and MCP checks

For agents and MCP integrations additionally verify:

- tool inputs and outputs are untrusted data, not authorization
- prompt or repository content cannot silently expand scope or permissions
- tools expose the smallest necessary capability
- write tools are separated from read tools when practical
- credentials are injected at runtime and are not copied into prompts or artifacts
- external URLs, file paths, commands, and connector targets are validated before action
- user authorization is preserved across tool calls

## Secrets rule

Do not request or store plaintext production secrets in Skill files, prompts, logs, repositories, or chat artifacts.

Prefer the project's configured secret authority. Use environment injection, CI/CD secrets, OIDC, managed identity, a dedicated secrets manager, or another repository-approved mechanism.

## Gate result

Return one of:

- `PASS`: applicable security checks completed with no blocking issue.
- `PASS WITH FOLLOW-UP`: no blocking issue, but a non-blocking action remains.
- `BLOCK`: a material security issue or unverified critical boundary remains.
- `NOT SCANNED`: specialist scanning was requested but the required runtime is unavailable.

For `BLOCK` and `NOT SCANNED`, state the exact missing control, tool, permission, or verification step.

## Release ordering

Use this order for substantive code changes:

`implementation -> tests -> code review -> security gate -> verification -> commit/PR -> deployment -> monitoring`

Do not weaken an earlier security property merely to satisfy a later delivery step.
