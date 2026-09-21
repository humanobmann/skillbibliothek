# Agent-Orchestrierungsarchitektur

## Referenzstruktur

```text
agent-runs/
  contracts/
    <run-id>-contract.json
  policies/
    tool-scopes.yaml
    escalation-triggers.yaml
  logs/
    <run-id>/
      decisions.jsonl
      tool-calls.jsonl
      context-usage.jsonl
```

Der Run-Contract wird vor Laufbeginn erzeugt und ist unveränderlich; Änderungen an Budgets erfordern einen neuen Lauf, nicht eine stille Anpassung während der Ausführung.

## Kontrollebenen

Drei Ebenen getrennt durchsetzen:

1. **Orchestrator-Ebene**: erzwingt Iterations-, Tool-Call- und Kontextbudget technisch, unabhängig vom Modellverhalten.
2. **Policy-Ebene**: definiert Tool-Scopes und Eskalationstrigger; wird vom Orchestrator gelesen, nicht vom Agenten selbst verändert.
3. **Beobachtungsebene**: protokolliert jede Entscheidung, jeden Tool-Aufruf und den Kontextverbrauch für Rekonstruktion und Audit.

Der Agent selbst darf seine eigenen Budgets, Scopes oder den Kill Switch nicht verändern können; diese Kontrolle liegt außerhalb seines Einflussbereichs.

## Multi-Agent-Delegation

Bei Delegation an Sub-Agenten gilt: Sub-Agent erbt höchstens den Scope des delegierenden Agenten, nie mehr. Jede Delegationsebene reduziert oder erhält den Scope, erweitert ihn nie. Zirkuläre Delegation (Agent A delegiert an B, B an A) wird erkannt und abgelehnt.
