# Beispiele

## Cost-Guardrail-Manifest

```json
{
  "cost_center": "platform-payments",
  "workload_name": "checkout-api",
  "monthly_budget_usd": 12000,
  "alert_thresholds_pct": [50, 80, 100],
  "required_tags": ["cost-center", "owner", "environment", "service"],
  "owner": "payments-platform-team",
  "commitment_strategy": "savings-plan",
  "anomaly_detection": true
}
```

## CI-Gate

```yaml
name: cost-guardrail-gate
on: [pull_request]
jobs:
  validate-manifest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python skills/finops-cloud-governance/scripts/validate_cost_guardrail.py cost-manifest.json
```

Budgets pro Environment (development/test/production) getrennt führen, damit Nicht-Produktionskosten Produktionsbudgets nicht verwässern.
