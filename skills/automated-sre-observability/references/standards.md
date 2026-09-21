# Standards und Kontrollpunkte

## Google SRE-Praxis (öffentlich dokumentiert)

Error Budgets als gemeinsame Steuergröße zwischen Feature-Velocity und Reliability-Arbeit verwenden. Symptom-basiertes statt ursachen-basiertes Alerting als Standardmuster übernehmen.

## Burn-Rate-Alerting

* Kurzfristiges Fenster (z. B. 1h) für schnelle, kritische Budgetverbrennung.
* Langfristiges Fenster (z. B. 6h/3d) für schleichende, weniger dringliche Verstöße.
* Schweregrad und Eskalationsstufe an die Kombination aus Burn-Rate und Fenster koppeln, nicht an einen einzelnen Schwellwert.

## Postmortem-Kultur

Blameless: Ursachenkette und System-/Prozessfaktoren analysieren, keine individuelle Schuldzuweisung. Follow-up-Actions mit Owner, Termin und Nachverfolgung versehen; ohne Nachverfolgung verliert der Postmortem seinen Wert.

## Beobachtbarkeit als Code

Dashboards, Alert-Regeln und SLO-Definitionen versioniert und reviewbar halten. Änderungen an Alarmschwellen wie Code-Änderungen behandeln: Review, Test gegen historische Daten, Rollback-Pfad.
