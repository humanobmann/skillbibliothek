# Standards und Kontrollpunkte

## NIST AI RMF

Die Funktionen Govern, Map, Measure und Manage als Lifecycle-Checkliste verwenden. Technische Metriken ergänzen, nicht anstelle von Governance verwenden.

## Reproduzierbarkeit

* Source Commit unveränderlich referenzieren.
* Datensatz/Evaluationssatz per Digest oder versioniertem Dataset-Identifier festhalten.
* Modellartefakt per Version und Digest referenzieren.
* Training-Konfiguration und Runtime-Abhängigkeiten nachvollziehbar machen.

## Supply Chain

Build-Provenienz und signierte/verifizierbare Artefakte nach SLSA-Prinzipien anstreben. Für externe Modelle Herkunft, Lizenz, Hash, Bezugsquelle und Review-Status dokumentieren.

## Rollout

Riskante Änderungen nicht als Big-Bang ausrollen. Canary, Shadow oder Blue/Green verwenden, sofern System und Datenfluss das zulassen. Vor dem Rollout klare Stop- und Rollback-Kriterien definieren.
