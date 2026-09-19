# Security Routing Matrix

## Preferred capability by task

| Task | Preferred capability | Fallback if unavailable |
| --- | --- | --- |
| Secure-by-default Python/JS/TS/Go guidance | OpenAI `security-best-practices` | Manual checklist in this Skill |
| Threat model for architecture, agents/MCP, auth, sensitive data flows or trust-boundary changes | OpenAI `security-threat-model` | Minimal threat-model questions in this Skill |
| Security review of PR/commit/branch/working tree | Codex Security `security-diff-scan` | Diff review plus `security-best-practices` |
| Exhaustive repository security scan | Codex Security `deep-security-scan` | Scoped manual review; report `NOT SCANNED` for exhaustive scan request |
| Repository security policy/scanner guidance | Codex Security `define-security-policy` | Draft `SECURITY.md` from system boundary and invariants |
| Fix a validated finding | Codex Security `fix-finding` when available, then tests | Minimal repository-native fix plus targeted tests |
| Secrets | Repository-approved secrets manager/CI secret store | Stop if secure injection is unavailable |
| Dependency risk | Native package audit/advisory tooling plus lockfile review | Manual dependency/source/version review |
| IaC/deployment | Provider-native validation plus review | Manual least-privilege and exposure checklist |

## Boundaries

Codex Security plugin skills rely on plugin-provided scripts, references, state directories, and runtime behavior. Do not extract them into a generic Skill bundle.

A portable Skill can define routing and fallback checks, but it cannot claim the coverage of a dedicated scanner.

## Minimal threat model questions

1. What asset or operation matters?
2. Who is trusted to perform it?
3. Which input can an attacker control?
4. Where is the authorization decision made?
5. What must always remain true?
6. What is the realistic impact if that property fails?
