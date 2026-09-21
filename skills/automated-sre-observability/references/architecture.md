# SRE-Architektur

## Referenzstruktur

```text
reliability/
  slo/
    service-catalog.yaml
    slo-definitions.yaml
  alerting/
    burn-rate-rules.yaml
    escalation-policy.yaml
  runbooks/
    <alert-id>.md
  postmortems/
    <incident-id>.md
```

SLO-Definitionen sind von Alerting-Regeln getrennt; Alerting-Regeln generieren sich aus SLOs, nicht umgekehrt. Runbooks sind eigenständige, versionierte Artefakte, die von Alerts verlinkt, aber nicht in Alert-Text dupliziert werden.

## Signalmodell

Vier Signalklassen konsistent für jeden Service erfassen:

1. **Verfügbarkeit**: erfolgreiche vs. fehlgeschlagene Anfragen aus Nutzersicht.
2. **Latenz**: Perzentile (p50/p95/p99), nicht nur Mittelwert.
3. **Sättigung**: Auslastung begrenzter Ressourcen vor Erschöpfung.
4. **Fehlerbudget-Verbrauch**: kumulierter Burn über das Messfenster, mit schnellem und langsamem Alarmfenster.

## Eskalations-State-Machine

`detected -> acknowledged -> mitigated -> resolved -> postmortem-complete`

`mitigated` ist ein technischer Zustand (Nutzerauswirkung beendet), `resolved` ein fachlicher (Ursache behoben). Beides nicht vermischen, sonst verschleiert die Metrik echte Restrisiken.
