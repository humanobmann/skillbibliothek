---
name: agentic-ai-orchestration-governance
description: Design and govern multi-agent and autonomous agent orchestration, including least-privilege tool-permission scoping, iteration and context-window budgets, loop and runaway-cost prevention, human-escalation triggers, and kill switches. Use for multi-agent systems, autonomous CLI/agent loops, tool-use governance, agent-to-agent delegation, guardrails against infinite loops or context-window overflow, agent cost caps, or agent incident response. Prefer hard iteration/token/cost ceilings, explicit least-privilege tool scopes, and mandatory human-escalation triggers over unbounded autonomous execution.
---

# Agentic AI Orchestration Governance

## Auftrag

Autonome und Multi-Agent-Systeme als produktive, aber unzuverlässige Ausführungsschicht behandeln, die harte, extern erzwungene Grenzen braucht. Kein Agent-Lauf ohne Iterations-, Kontext- und Kostenobergrenze sowie definierten Eskalationspfad starten.

## Workflow

1. Aufgabe, Autonomiegrad und Blast Radius des Agenten bestimmen.
2. Tool-Zugriff nach Least Privilege scopen; keine Wildcard-Berechtigungen.
3. Iterations-, Tool-Call- und Kontextbudget festlegen, bevor der Lauf startet.
4. Kostenobergrenze pro Lauf definieren und technisch erzwingen.
5. Abbruchkriterien definieren: Erfolg, Budgeterschöpfung, wiederholter Fehler, erkannte Schleife.
6. Kill Switch und manuelle Eingriffsmöglichkeit vor dem Start verifizieren.
7. Human-Escalation-Trigger für riskante, irreversible oder mehrdeutige Aktionen festlegen.
8. Lauf protokollieren: Entscheidungen, Tool-Aufrufe, Kontextverbrauch, Abbruchgrund.

## Guardrails gegen Endlosschleifen

* Harte Obergrenze für Iterationen/Turns pro Lauf setzen; kein „bis es fertig ist" ohne Zahl.
* Wiederholungserkennung einbauen: identische oder zyklische Tool-Aufrufe nach N Wiederholungen abbrechen, nicht endlos retryen.
* Fortschritt operational messen (z. B. Zieldistanz, Testergebnisse), nicht nur Zeit verstreichen lassen.
* Bei erkannter Schleife eskalieren statt automatisch mit veränderten Parametern erneut zu versuchen.

## Guardrails gegen Kontextüberlauf

* Kontextbudget in Tokens explizit budgetieren, mit Marge unterhalb des Modell-Limits, nicht am Limit selbst.
* Lange Werkzeugausgaben zusammenfassen oder auslagern, statt vollständig im Kontext zu akkumulieren.
* Zwischenergebnisse in externen Speicher/Dateien auslagern, wenn der Lauf mehrere Phasen umfasst.
* Kontextverbrauch pro Phase überwachen und bei Annäherung an das Budget Übergabe/Kompaktierung auslösen, nicht stillschweigend abschneiden.

## Least-Privilege Tool-Scoping

* Werkzeugzugriff pro Aufgabe explizit auflisten; keine pauschale „alle Werkzeuge"-Freigabe für autonome Läufe.
* Destruktive oder irreversible Aktionen (Löschen, Force-Push, Zahlungen, externe Kommunikation) grundsätzlich hinter menschlicher Bestätigung halten.
* Delegation zwischen Agenten mit demselben oder engerem Scope wie der delegierende Agent versehen, nie mit weiterem.

## Qualität

Vor Abschluss prüfen:

1. Iterations-, Tool-Call- und Kontextbudget sind gesetzt und technisch erzwungen.
2. Kostenobergrenze existiert und ist durchsetzbar.
3. Kill Switch ist vor dem Lauf getestet, nicht nur dokumentiert.
4. Human-Escalation-Trigger decken irreversible und mehrdeutige Aktionen ab.
5. Schleifenerkennung eskaliert statt endlos zu retryen.
6. Tool-Scope ist minimal und pro Aufgabe begründet.
7. Lauf-Protokoll erlaubt vollständige Rekonstruktion der Entscheidungen.

## Ressourcen

* Architektur und Kontrollebenen: [references/architecture.md](references/architecture.md)
* Standards und Bedrohungsmodell: [references/standards.md](references/standards.md)
* Beispiele: [references/examples.md](references/examples.md)
* Deterministische Manifestprüfung: `scripts/validate_agent_run_contract.py`
