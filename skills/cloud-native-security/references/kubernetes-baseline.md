# Kubernetes Baseline

## Pod Security Standards

* Privileged: nur für explizit vertrauenswürdige Infrastrukturfälle.
* Baseline: verhindert bekannte Privilege-Escalation-Klassen bei breiter Kompatibilität.
* Restricted: bevorzugtes Ziel für gewöhnliche Applikationsworkloads.

Namespaces ohne bewusste Policy-Zuordnung als Sicherheitslücke behandeln.

## RBAC

Rollen auf benötigte Ressourcen, Verben und Namespaces beschränken. `cluster-admin`, Wildcards und unnötige Secret-Leserechte vermeiden.

## Workload Identity

Cloud- und Serviceidentitäten an Workloads binden. Langlebige Cloud-Keys in Kubernetes Secrets vermeiden, wenn föderierte Workload Identity verfügbar ist.
