---
name: low-code-no-code-engineering
description: Design, review, govern, and release low-code/no-code solutions as maintainable software products rather than unmanaged app artifacts. Use for Power Platform, Power Apps, Power Automate, Copilot Studio, Make, n8n, Zapier, Airtable-style automations, citizen-development governance, DLP, connector reviews, environment strategy, ALM, source control, testing, observability, solution ownership, or migration from prototypes to enterprise-managed workflows.
---

# Low-Code / No-Code Engineering

## Auftrag

Low-Code-Systeme nach denselben Grundprinzipien wie Software behandeln: versionierbar, testbar, verantwortet, beobachtbar und rückrollbar. Geschwindigkeit darf Governance nicht ersetzen.

## Workflow

1. Use Case, Datenklassifikation und Business Owner bestimmen.
2. Plattform und Connectoren inventarisieren.
3. Umgebungsstrategie definieren: Development, Test, Production.
4. DLP- und Identitätsgrenzen prüfen.
5. Lösung paketieren und in Source Control überführen.
6. Tests und Freigabegates definieren.
7. Deployment und Rollback automatisieren.
8. Betrieb mit Ownership, Monitoring, Kosten und Lifecycle-Policy absichern.

## Architektur

Business-Regeln von Plattform-Aktionen trennen:

* **Domain**: Prozessregeln und Datenvertrag.
* **Application**: Workflow-Orchestrierung und Use Cases.
* **Connectors**: SaaS-, Datenbank- und API-Integrationen.
* **Platform**: Power Platform, Make, n8n, Zapier oder andere Runtime.

Kritische Logik nicht ausschließlich in undokumentierten visuellen Flows verstecken. Entscheidungen, Eingaben, Outputs und Fehlerpfade dokumentieren.

## Governance

Mindestens erfassen:

* Business Owner und technischer Owner
* Datenklassifikation
* verwendete Connectoren und Berechtigungen
* DLP-Review
* Umgebungs- und Deploymentstrategie
* Source-Control-Pfad
* Version
* Support- und Decommission-Plan

## ALM

Development, Test und Production trennen. Änderungen als versionierte Lösung/Export behandeln. Manuelle Produktionsänderungen vermeiden. Secrets und Umgebungswerte nicht in Flow-Definitionen einbetten.

## Qualitätsgate

Vor Produktion prüfen:

1. Ownership ist eindeutig.
2. DLP und Connector-Risiko sind geprüft.
3. Source Control enthält die kanonische Lösung oder exportierbare Definition.
4. Fehlerpfade und Retry-Verhalten sind definiert.
5. Testdaten sind von Produktionsdaten getrennt.
6. Deployment ist reproduzierbar.
7. Monitoring und Runbook existieren.
8. Exit-/Migrationspfad ist dokumentiert.

## Ressourcen

* Architektur und Governance: [references/architecture.md](references/architecture.md)
* ALM-Checkliste: [references/alm-checklist.md](references/alm-checklist.md)
* Beispiele: [references/examples.md](references/examples.md)
* Manifestprüfung: `scripts/validate_solution_manifest.py`
