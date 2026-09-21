---
name: automated-sre-observability
description: Design and operate automated Site Reliability Engineering workflows across SLIs/SLOs, error budgets, symptom-based alerting, on-call escalation, incident response, and observability-as-code (metrics, logs, traces). Use for SRE, observability, incident management, alert-fatigue reduction, error-budget policy, paging, escalation runbooks, blameless postmortems, or reliability reviews. Prefer symptom-based alerts, actionable pages, explicit escalation paths, and measurable error-budget policies over ad hoc dashboards.
---

# Automated SRE & Observability

## Auftrag

Zuverlässigkeit als messbares, budgetiertes Produktmerkmal behandeln statt als Bauchgefühl. Jede Seite muss handlungsfähig sein; jedes SLO muss eine Konsequenz haben.

## Workflow

1. Service, Nutzerreise und kritischen Pfad bestimmen.
2. SLIs aus Nutzerperspektive definieren: Verfügbarkeit, Latenz, Fehlerquote, Durchsatz oder Sättigung.
3. SLO-Ziel und Messfenster festlegen; Error Budget daraus ableiten.
4. Error-Budget-Policy definieren: was passiert bei Budgetverbrauch (Release-Freeze, Priorisierung von Reliability-Arbeit).
5. Alerting auf Symptome und Burn-Rate ausrichten, nicht auf jede Ursache einzeln.
6. Eskalationspfad, Bereitschaft und Runbooks pro Alert hinterlegen.
7. Vorfälle mit klarer Schweregrad-Klassifikation und Kommunikationsplan bearbeiten.
8. Nach Abschluss blameless Postmortem mit Follow-up-Actions durchführen.

## SLI/SLO-Baseline

* SLIs aus Nutzersicht formulieren, nicht aus Infrastruktursicht.
* SLO strikt unter 100 % ansetzen; 100 % ist kein realistisches oder sinnvolles Ziel.
* Error Budget als gemeinsame Ressource zwischen Feature-Arbeit und Reliability-Arbeit behandeln.
* Mehrere Burn-Rate-Fenster (schnell/langsam) statt eines einzelnen statischen Schwellwerts verwenden.
* SLOs regelmäßig gegen tatsächliches Nutzerverhalten und Vorfallhistorie überprüfen.

## Alerting & Eskalation

* Nur auf Symptome mit Nutzerauswirkung Seiten auslösen; Ursachenanalyse erfolgt im Runbook, nicht im Alert-Titel.
* Jeder Page-Alert braucht: Schweregrad, Eskalationsziel, verlinktes Runbook, erwartete Reaktionszeit.
* Alert-Müdigkeit aktiv reduzieren: stumme/duplizierte Alerts konsolidieren, Schwellwerte datengetrieben kalibrieren.
* Eskalationsstufen und Ausweichpfade explizit dokumentieren, keine impliziten Annahmen über Erreichbarkeit.

## Incident Response

* Schweregrade und Kommunikationskadenz vor dem Vorfall festlegen, nicht während.
* Incident Commander und Kommunikationsrolle trennen, wenn Umfang das rechtfertigt.
* Timeline, getroffene Maßnahmen und Wirkung fortlaufend dokumentieren.
* Nach Abschluss: blameless Postmortem, Ursachenkette statt Schuldzuweisung, verbindliche Follow-up-Actions mit Owner und Termin.

## Qualität

Vor Abschluss prüfen:

1. SLO ist aus Nutzersicht formuliert und messbar.
2. Error-Budget-Policy hat eine konkrete, durchsetzbare Konsequenz.
3. Jeder Page-Alert ist handlungsfähig und verlinkt ein Runbook.
4. Eskalationspfad deckt Abwesenheit und Zeitzonen ab.
5. Postmortems sind blameless und erzeugen nachverfolgte Follow-ups.
6. Beobachtbarkeit deckt Metriken, Logs und Traces konsistent ab.

## Ressourcen

* Architektur und Signalmodell: [references/architecture.md](references/architecture.md)
* Standards und Kontrollpunkte: [references/standards.md](references/standards.md)
* Beispiele: [references/examples.md](references/examples.md)
* Deterministische Manifestprüfung: `scripts/validate_slo_manifest.py`
