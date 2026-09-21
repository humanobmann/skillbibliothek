# Beispiele

## Agent-Run-Contract

```json
{
  "agent_name": "pr-triage-agent",
  "max_iterations": 40,
  "max_tool_calls": 120,
  "context_budget_tokens": 150000,
  "tool_scope": ["github.read_pr", "github.comment", "ci.read_logs"],
  "kill_switch": true,
  "human_escalation_trigger": "vor jedem Force-Push, Merge oder externen Kommentar an Dritte",
  "cost_ceiling_usd": 5.0
}
```

## CI-Gate

```yaml
name: agent-run-contract-gate
on: [pull_request]
jobs:
  validate-contract:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python skills/agentic-ai-orchestration-governance/scripts/validate_agent_run_contract.py run-contract.json
```

Für Multi-Agent-Delegation je Sub-Agent einen eigenen Contract mit gleichem oder engerem `tool_scope` und eigenem, aus dem übergeordneten Budget abgeleitetem Kostenanteil erzeugen.
