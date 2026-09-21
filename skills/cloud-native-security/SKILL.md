---
name: cloud-native-security
description: Design and review security controls for Kubernetes, containers, GitOps, CI/CD and cloud-native workloads. Use for Pod Security Standards, least-privilege RBAC, workload identity, admission controls, image provenance, secrets handling, runtime hardening, network isolation, supply-chain controls, multi-tenant clusters, or cloud-native threat modeling. Prefer secure defaults, immutable artifacts, explicit trust boundaries, policy-as-code, and controls that can be verified in CI before deployment.
---

# Cloud-Native Security

## Auftrag

Cloud-native Systeme entlang der gesamten Software Supply Chain absichern: Source, Build, Registry, Deploy, Runtime und Observability. Kubernetes-Sicherheit nicht auf Container-Scanning reduzieren.

## Workflow

1. Trust Boundaries und Assets erfassen.
2. Identitäten und Berechtigungen nach Least Privilege prüfen.
3. Workload-Härtung gegen Kubernetes Pod Security Standards prüfen.
4. Netzwerk- und Egress-Grenzen definieren.
5. Images und Build-Provenienz verifizieren.
6. Secrets, Workload Identity und Schlüsselrotation prüfen.
7. Admission-/Policy-as-Code Gates definieren.
8. Runtime-Detektion, Audit Logs und Incident-Pfade festlegen.

## Baseline

Für normale Applikationsworkloads `restricted` als Zielniveau anstreben. Abweichungen explizit begründen und auf den kleinsten Scope beschränken.

Mindestens prüfen:

* `runAsNonRoot: true`
* `allowPrivilegeEscalation: false`
* Capabilities `ALL` droppen und nur begründet ergänzen
* `seccompProfile.type: RuntimeDefault`
* read-only root filesystem, wenn workload-kompatibel
* keine Host Namespaces/hostPath ohne dokumentierte Notwendigkeit
* Ressourcenlimits und ServiceAccount explizit
* Images per Digest für kritische Deployments

## Supply Chain

Artefakte unveränderlich adressieren. Build-Provenienz und Herkunft dokumentieren. CI/CD Credentials kurzlebig und minimal berechtigen. Keine Secrets in Git, Images oder CI Logs.

## Netzwerk

Default-Deny als Zielbild verwenden. Ingress und Egress auf benötigte Flows begrenzen. DNS, Control Plane und Observability-Flows bewusst berücksichtigen, statt Regeln nur aus Applikationsports abzuleiten.

## Policy-as-Code

Policy-Gates müssen deterministisch und reviewbar sein. Admission-Regeln versionieren, testen und zuerst im Audit/Warn-Modus beobachten, wenn ein harter Cutover Produktionsrisiken erzeugt.

## Qualität

Vor Abschluss prüfen:

1. Jede privilegierte Ausnahme hat Owner und Begründung.
2. Identität ist stärker als langlebige statische Credentials.
3. Build- und Runtime-Vertrauen sind getrennt.
4. Netzwerkregeln berücksichtigen Egress.
5. Logs reichen für Incident Reconstruction.
6. Rollback und Break-Glass sind dokumentiert, nicht dauerhaft offen.

## Ressourcen

* Architektur und Control Plane: [references/architecture.md](references/architecture.md)
* Kubernetes-Härtung: [references/kubernetes-baseline.md](references/kubernetes-baseline.md)
* Sichere Manifestbeispiele: [references/examples.md](references/examples.md)
* Workload-Profilprüfung: `scripts/validate_workload_profile.py`
