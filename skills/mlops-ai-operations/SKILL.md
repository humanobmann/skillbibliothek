---
name: mlops-ai-operations
description: Design, review, and operate production AI/ML delivery workflows across data lineage, experiment tracking, model registry, evaluation, deployment, observability, rollback, cost controls, and AI risk governance. Use for MLOps, LLMOps, model release gates, reproducibility, model cards, drift monitoring, inference operations, CI/CD for models, or productionizing Python/Jupyter AI work. Prefer explicit provenance, immutable versions, measurable quality gates, and reversible deployments.
---

# MLOps & AI Operations

## Auftrag

AI/ML-Systeme als reproduzierbare, auditierbare und rückrollbare Produktionssysteme behandeln. Forschung, Training, Evaluation und Serving klar trennen. Keine Notebook-Logik direkt zur Produktionsarchitektur erklären.

## Workflow

1. Zielsystem und Risikoklasse bestimmen: Batch, Online Inference, RAG, Agent, Training oder Fine-Tuning.
2. Eingaben und Provenienz erfassen: Code Commit, Daten-Digest, Modellbasis, Parameter, Abhängigkeiten und Evaluationssatz.
3. Release-Gates definieren: technische Metriken, Sicherheits-/Bias-Prüfung, Kosten, Latenz und fachliche Akzeptanz.
4. Artefakte unveränderlich versionieren und Registry-/Promotion-Status dokumentieren.
5. Deployment mit Canary, Shadow oder Blue/Green planen; Rollback vor Rollout definieren.
6. Produktion überwachen: Fehler, Latenz, Kosten, Drift, Datenqualität, Output-Qualität und Sicherheitsereignisse.
7. Änderungen mit nachvollziehbarer Freigabe und Evidenz abschließen.

## Clean Architecture

Trenne vier Schichten:

* **Domain**: Qualitätskriterien, Risikogrenzen, Modellvertrag.
* **Application**: Train, Evaluate, Register, Promote, Deploy, Monitor.
* **Adapters**: MLflow/Kubeflow/KServe/Cloud-Provider/Vector Store/Observability.
* **Infrastructure**: CI, Container, Kubernetes, Secrets, Storage und Networking.

Provider-spezifische Details nicht in Domain-Regeln einbauen. Für die Zielstruktur [references/architecture.md](references/architecture.md) laden.

## Mindestartefakte

Für produktive Releases mindestens erfassen:

* Modellname und unveränderliche Version
* Source-Commit
* Daten- oder Evaluations-Digest
* Metriken und Akzeptanzschwellen
* verantwortliche Person oder Rolle
* Freigabeumgebung
* Rollback-Ziel
* bekannte Einschränkungen

Das Beispielmanifest mit `scripts/validate_model_manifest.py` validieren.

## AI Governance

NIST AI RMF als Governance-Rahmen verwenden: Govern, Map, Measure, Manage. Für generative Systeme zusätzliche Risiken wie Halluzination, Prompt Injection, Datenabfluss, Missbrauch und Evaluation gegen domänenspezifische Fehlermodi berücksichtigen.

Keine einzelne Metrik als vollständigen Qualitätsnachweis behandeln. Bei menschlich relevanten Entscheidungen fachliche Review-Gates und nachvollziehbare Verantwortlichkeit vorsehen.

## Security & Supply Chain

* Modelle, Container und Datenstände mit Digests referenzieren.
* Secrets nie in Notebooks, Prompts, Beispielkonfigurationen oder Modellartefakten speichern.
* Build- und Modellprovenienz dokumentieren.
* Abhängigkeiten und Base Images versionieren und prüfen.
* Trainings- und Inferenzrollen nach Least Privilege trennen.
* Fremdmodelle und Datensätze als Supply-Chain-Inputs behandeln.

## Qualität

Vor Abschluss prüfen:

1. Reproduzierbarkeit ist möglich.
2. Daten- und Modellprovenienz sind explizit.
3. Promotion ist von Deployment getrennt.
4. Rollback ist ausführbar.
5. Produktionsmetriken decken Qualität, Zuverlässigkeit, Sicherheit und Kosten ab.
6. Provider-Lock-in ist auf Adapter beschränkt.
7. Governance und technische Gates widersprechen einander nicht.

## Ressourcen

* Architektur und Modulgrenzen: [references/architecture.md](references/architecture.md)
* Standards und Kontrollpunkte: [references/standards.md](references/standards.md)
* Code- und Manifestbeispiele: [references/examples.md](references/examples.md)
* Deterministische Manifestprüfung: `scripts/validate_model_manifest.py`
