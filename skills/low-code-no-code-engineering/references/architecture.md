# Low-Code Architektur und Governance

## Referenzstruktur

```text
solution/
  docs/
    architecture.md
    runbook.md
  src/
    exported-solution/
  tests/
    acceptance-cases.md
  solution-manifest.json
```

Visuelle Flows sind ein Implementierungsdetail. Fachliche Regeln, Datenverträge, Ownership und Betriebsanforderungen außerhalb proprietärer Designer dokumentieren.

## Connector Boundary

Jeden Connector wie eine externe API behandeln:

* Authentifizierung
* Berechtigungsscope
* Datenklassifikation
* Rate Limits
* Fehler-/Retry-Semantik
* Exit-Risiko

## Environment Strategy

Development, Test und Production als getrennte Vertrauenszonen führen. Service Accounts und Connections nicht zwischen Umgebungen teilen, wenn dadurch Produktionsrechte in Entwicklungsumgebungen gelangen.
