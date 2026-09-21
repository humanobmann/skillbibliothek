# MLOps Architektur

## Referenzstruktur

```text
ml-system/
  domain/
    contracts.py
    quality_gates.py
  application/
    train.py
    evaluate.py
    promote.py
    deploy.py
  adapters/
    registry/
    serving/
    observability/
  infrastructure/
    ci/
    containers/
    kubernetes/
  model-manifest.json
```

Die Domain-Schicht kennt keine Cloud-SDKs. Application-Use-Cases sprechen nur über Ports/Interfaces mit Registry, Storage und Serving. Adapter implementieren diese Ports. Infrastruktur enthält austauschbare Deploymentspezifika.

## Release-State-Machine

`candidate -> evaluated -> approved -> staged -> production -> retired`

Jeder Übergang benötigt Evidenz. `approved` ist eine fachliche Entscheidung, `production` ein technischer Zustand. Beides nicht vermischen.

## Observability

Vier Signalgruppen getrennt erfassen:

1. System: Availability, Errors, Saturation, Latency.
2. Modell: Quality, Drift, calibration or task-specific metrics.
3. Daten: schema, null rate, range, freshness, distribution shifts.
4. Business/Risk: cost per request, human escalation, safety events, policy violations.
