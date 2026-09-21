# FinOps-Architektur

## Referenzstruktur

```text
finops/
  tagging/
    required-tags-policy.yaml
  budgets/
    <workload>-budget.json
  anomaly-detection/
    rules.yaml
  reporting/
    showback/
    chargeback/
```

Tagging-Policy ist providerneutral formuliert und wird pro Cloud-Provider (z. B. über Policy-as-Code) technisch erzwungen. Budgets sind pro Workload versioniert und mit dem jeweiligen Owner verknüpft.

## FinOps-Lifecycle

Die drei FinOps-Foundation-Phasen als wiederkehrenden Zyklus behandeln, nicht als einmaliges Projekt:

1. **Inform**: Sichtbarkeit, Zuordnung, Benchmarking.
2. **Optimize**: Rightsizing, Commitment-Käufe, Architekturentscheidungen.
3. **Operate**: kontinuierliche Governance, Automatisierung, Kulturverankerung.

## Verantwortungsmodell

Kostenverantwortung liegt beim Team, das die Ressource betreibt; FinOps-Funktion liefert Sichtbarkeit, Benchmarks und Guardrails, trifft aber keine technischen Entscheidungen allein. Finance liefert Budgetrahmen und Unit-Economics-Ziele.
