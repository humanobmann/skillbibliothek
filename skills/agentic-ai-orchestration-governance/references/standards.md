# Standards und Bedrohungsmodell

## Bezugsrahmen

An NIST AI RMF (Govern, Map, Measure, Manage) sowie OWASP-Leitlinien zu LLM-/Agenten-Risiken (u. a. übermäßige Handlungsfähigkeit, unsichere Werkzeugnutzung, Ressourcenerschöpfung) anlehnen. Kein einzelnes technisches Limit als vollständige Absicherung behandeln.

## Bedrohungsmodell (Auszug)

* **Runaway Loop**: Agent wiederholt Aktionen ohne Fortschritt und verbraucht Zeit/Kosten/Kontext unbegrenzt. Gegenmaßnahme: Iterationslimit plus Wiederholungserkennung.
* **Context Overflow**: akkumulierte Werkzeugausgaben verdrängen kritische frühere Instruktionen oder überschreiten das Modell-Limit. Gegenmaßnahme: Kontextbudget mit Marge, Auslagerung, Kompaktierung.
* **Scope Creep**: Agent oder delegierter Sub-Agent nutzt Werkzeuge außerhalb des ursprünglich vorgesehenen Zwecks. Gegenmaßnahme: explizites, minimales Tool-Scoping pro Lauf.
* **Kostenexplosion**: unbegrenzte Modell-/Tool-Aufrufe erzeugen unkontrollierte Kosten. Gegenmaßnahme: harte Kostenobergrenze pro Lauf, technisch erzwungen.
* **Irreversible Aktion ohne Freigabe**: Agent führt destruktive oder extern sichtbare Aktion ohne menschliche Bestätigung aus. Gegenmaßnahme: verbindliche Human-Escalation-Trigger für definierte Aktionsklassen.

## Kill-Switch-Anforderungen

Ein Kill Switch muss außerhalb des Agentenprozesses auslösbar sein, sofort laufende Tool-Aufrufe stoppen (nicht nur neue verhindern) und vor Produktivbetrieb getestet sein. Ein rein dokumentierter, nie ausgelöster Kill Switch gilt als nicht vorhanden.
