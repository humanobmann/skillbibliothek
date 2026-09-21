---
name: finops-cloud-governance
description: Design and operate FinOps cloud cost governance across budgets, cost-allocation tagging, anomaly alerting, unit economics, showback/chargeback, and commitment or reserved-capacity strategy. Use for cloud cost governance, budget guardrails, tagging policy, cost-anomaly detection, rightsizing, FinOps maturity, showback, chargeback, or reservation/savings-plan planning. Prefer mandatory cost-allocation tags, automated budget guardrails, and unit-economics metrics over static spend dashboards.
---

# FinOps & Cloud Cost Governance

## Auftrag

Cloud-Kosten als geteilte Verantwortung zwischen Engineering, Finance und Business behandeln. Kostenkontrolle darf Reliability und Delivery-Geschwindigkeit nicht blind unterordnen; Trade-offs werden explizit gemacht, nicht stillschweigend getroffen.

## Workflow

1. Workload, Cost Center und Business Owner bestimmen.
2. Pflicht-Tags für Kostenzuordnung definieren (Cost Center, Owner, Environment, Service).
3. Budget je Workload/Team festlegen, inklusive Warn- und Hartgrenzen.
4. Anomalieerkennung für ungewöhnliche Ausgabenmuster aktivieren.
5. Commitment-Strategie prüfen: On-Demand, Reserved, Savings Plan oder Spot-Mischung passend zur Lastform wählen.
6. Unit-Economics-Metrik definieren (Kosten pro Transaktion, Nutzer oder Anfrage).
7. Showback/Chargeback-Reporting an die verantwortlichen Teams etablieren.
8. Rightsizing- und Lifecycle-Reviews regelmäßig wiederholen, nicht einmalig.

## Kostenzuordnung

* Pflicht-Tags technisch erzwingen (Policy-as-Code), nicht nur dokumentieren.
* Ungetaggte oder falsch getaggte Ressourcen als Governance-Lücke behandeln, nicht ignorieren.
* Shared Costs (z. B. Plattform, Netzwerk) nach nachvollziehbarem Schlüssel verteilen, nicht pauschal einer Einheit zuweisen.

## Budget-Guardrails

* Warnschwellen (z. B. 50/80 %) von Hartgrenzen unterscheiden.
* Automatisierte Reaktion bei Hartgrenzen definieren: Benachrichtigung, Freeze oder Genehmigungspflicht, je nach Risikoklasse.
* Budgetverantwortung an denselben Owner koppeln, der auch die technische Entscheidung trifft.

## Commitment- und Rightsizing-Strategie

* Commitment-Grad an Lastvorhersagbarkeit koppeln: stabile Baseline in Reserved/Savings Plan, volatile Spitzen in On-Demand oder Spot.
* Ungenutzte oder überdimensionierte Ressourcen regelmäßig identifizieren und mit Owner klären, bevor automatisiert eingegriffen wird.
* Kostenoptimierung nie ohne Blick auf SLOs und Kapazitätsreserven durchführen.

## Qualität

Vor Abschluss prüfen:

1. Jede Ressource ist eindeutig einem Cost Center und Owner zuordenbar.
2. Budget-Guardrails haben eine definierte, automatisierte Konsequenz.
3. Anomalieerkennung ist aktiv und hat einen Eskalationspfad.
4. Commitment-Strategie passt zur tatsächlichen Lastform.
5. Unit-Economics-Metrik ist mit dem Business nachvollziehbar verknüpft.
6. Kostenmaßnahmen widersprechen keiner bestehenden SLO- oder Kapazitätsvorgabe.

## Ressourcen

* Architektur und Kostenmodell: [references/architecture.md](references/architecture.md)
* Standards und Reifegrad: [references/standards.md](references/standards.md)
* Beispiele: [references/examples.md](references/examples.md)
* Deterministische Manifestprüfung: `scripts/validate_cost_guardrail.py`
