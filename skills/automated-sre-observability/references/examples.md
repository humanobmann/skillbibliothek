# Beispiele

## SLO-Manifest

```json
{
  "service_name": "checkout-api",
  "sli_type": "availability",
  "slo_target": 99.9,
  "measurement_window_days": 28,
  "error_budget_policy": "Feature-Release-Freeze bei Budgetverbrauch > 80% im laufenden Fenster",
  "burn_rate_alerting": [
    {"window_hours": 1, "threshold_multiplier": 14.4, "severity": "page"},
    {"window_hours": 6, "threshold_multiplier": 6, "severity": "ticket"}
  ],
  "escalation_owner": "checkout-oncall",
  "runbook_url": "https://runbooks.internal/checkout-api-availability"
}
```

## CI-Gate

```yaml
name: slo-gate
on: [pull_request]
jobs:
  validate-manifest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python skills/automated-sre-observability/scripts/validate_slo_manifest.py slo-manifest.json
```

Bei Änderungen an Burn-Rate-Schwellen zusätzlich gegen die letzten 90 Tage Incident-Historie backtesten, bevor der Alert produktiv geschaltet wird.
