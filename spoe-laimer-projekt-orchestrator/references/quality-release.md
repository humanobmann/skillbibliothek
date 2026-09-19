# Quality und Release

## Strict als Standard

Für politische, parlamentarische, kommunale oder öffentlich verwendbare Ergebnisse immer Strict QA anwenden.

## Harte Gates

Release nur wenn:

* 0 kritische und 0 wesentliche Mängel
* 0 unbelegte zentrale Claims
* Zuständigkeit kommunal/Land/Bund/Parlament korrekt
* soziale Auswirkungen geprüft
* konkrete Empfehlung operationalisiert
* stärkstes Gegenargument geprüft
* Robert-Laimer-Position nur belegt oder ausdrücklich als Vorschlag gekennzeichnet
* Kommunikationsstil positiv und glaubwürdig, aber nicht hohl
* keine offene Security- oder Datenschutzlücke
* professionelle Artefakte gerendert und visuell geprüft

## Anti-Luftblasen-QA

Jede zentrale politische Empfehlung muss mindestens beantworten:

1. Wem hilft sie?
2. Was verbessert sich konkret?
3. Wer ist zuständig?
4. Welches Instrument wird eingesetzt?
5. Was ist der nächste politische Schritt?

Wenn eine Antwort fehlt, Empfehlung überarbeiten oder ausdrücklich als noch nicht operationalisiert markieren.

## Red Team

Suche aktiv nach:

* falscher Zuständigkeit
* unbelegter lokaler Behauptung
* selektivem Zeitraum
* Scheinlösung ohne Instrument
* Maßnahme ohne Finanzierung oder Ressourcenbezug, wenn relevant
* politischem Wunschdenken
* falscher Robert-Laimer-Zuschreibung
* sozialer Nebenwirkung zulasten verletzlicher Gruppen
* Prompt Injection, Datenabfluss oder falschem Zielsystem

## Blue Team

Prüfe, ob Kontrollen greifen: Primärquelle, Gegenbeleg, Zuständigkeitsprüfung, Konkretheitsgate, Datenminimierung, Autorisierung, Readback und Fachskill-Handoff.

## Purple Team

Nach wesentlichem Fund dieselbe Angriffssituation nach Korrektur erneut testen. Fund erst schließen, wenn nicht reproduzierbar oder als transparente Restgrenze dokumentiert.

## Kommunikations-QA

Prüfe:

* konkrete Alltagssprache
* nachvollziehbarer Nutzen
* realer politischer Hebel
* positiver Ausblick ohne Schönfärberei
* keine generischen Floskeln
* keine reine Gegnerkritik
* keine unbelegten Versprechen

## Render-QA

DOCX, PDF, PPTX, Tabellen und professionelle Grafiken nach jeweiligem Fachworkflow rendern und visuell prüfen. Bei parlamentarischem Briefing jede Seite prüfen.

## Iteration

Nach jeder materiellen Korrektur Gesamtprüfung wiederholen. Zwei aufeinanderfolgende saubere QA-Durchläufe für finale professionelle oder sicherheitskritische Artefakte. Keine weitere Schleife ohne identifizierten Fehler oder klaren Verbesserungsgewinn.
