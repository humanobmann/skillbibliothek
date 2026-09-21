# Beispiele

## Modellmanifest

```json
{
  "model_name": "support-intent-classifier",
  "version": "2026.09.21.1",
  "source_commit": "0123456789abcdef0123456789abcdef01234567",
  "dataset_digest": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "metrics": {"macro_f1": 0.91, "p95_latency_ms": 82},
  "risk_owner": "ml-platform",
  "approved_for": "staging",
  "rollback_version": "2026.09.14.2"
}
```

## CI Gate

```yaml
name: model-gate
on: [pull_request]
jobs:
  validate-manifest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python skills/mlops-ai-operations/scripts/validate_model_manifest.py model-manifest.json
```

Für produktive Supply-Chain-Härtung Action-Versionen zusätzlich auf vollständige Commit-SHAs pinnen.
