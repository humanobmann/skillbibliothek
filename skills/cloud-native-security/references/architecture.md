# Cloud-Native Security Architektur

## Kontrollschichten

```text
Source -> CI Build -> Artifact Registry -> Admission -> Kubernetes Runtime -> Telemetry/Response
```

Jede Schicht erzeugt eigene Evidenz. Ein erfolgreicher Image-Scan ersetzt weder Admission noch Runtime-Schutz.

## Trust Boundaries

Mindestens unterscheiden:

* Entwickleridentität und Source Repository
* CI Runner und Build Credentials
* Registry und Signatur/Provenienz
* Cluster Control Plane
* Namespace/Workload Identity
* externe APIs und Datenbanken

## Clean Architecture für Policies

Policy-Intent als Domain-Regel beschreiben, Engine-spezifische Umsetzung als Adapter halten. So bleiben Anforderungen wie "keine privilegierten Container" unabhängig davon, ob Kyverno, Gatekeeper oder native Admission Controls verwendet werden.
