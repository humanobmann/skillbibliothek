# Trigger und Routing

## Positive Trigger

1. Recherchiere steigende kommunale Gebühren in St. Pölten, prüfe soziale Auswirkungen und entwickle konkrete Gemeinderatsmaßnahmen.
2. Prüfe eine aktuelle Bundesheer-Beschaffung, entwickle parlamentarische Fragen für Robert Laimer und erstelle ein Briefing.
3. Analysiere Lehrstellenentwicklung im Wahlkreis und entwickle kommunale plus bundespolitische Hebel.
4. Recherchiere Leistbarkeit von Kinderbetreuung und formuliere konkrete sozialdemokratische Maßnahmen für St. Pölten.
5. Prüfe Wohnkosten, kommunale Einflussmöglichkeiten und entwickle eine politisch verwendbare Linie.
6. Recherchiere Neutralitäts- und Sicherheitsdebatte, prüfe Gegenargumente und bereite parlamentarische Ansatzpunkte vor.
7. Führe Statistik, kommunale Dokumente und parlamentarische Quellen zu einem Dossier mit konkreten Handlungsschritten zusammen.
8. Entwickle aus einer politischen Analyse ein 3- bis 5-seitiges parlamentarisches Briefing mit strenger Quellen- und Render-QA.
9. Prüfe eine behauptete Einsparung der Stadt und zeige, wer sozial davon profitiert oder belastet wird.
10. Erstelle einen Maßnahmenplan für bessere Öffi-Erreichbarkeit mit kommunaler Zuständigkeit, Zielgruppen und politischem Hebel.
11. Analysiere Pflegeversorgung im Wahlkreis und trenne Gemeinde-, Landes- und Bundeszuständigkeit.
12. Erstelle aus belegten Fakten eine positive, konkrete sozialdemokratische Kommunikationslinie für ein lokales Thema.

## Negative Trigger

1. Formuliere diesen Satz besser.
2. Schreib eine kurze Facebook-Antwort.
3. Wie hoch ist die Inflation heute?
4. Fasse dieses PDF zusammen.
5. Erstelle nur eine Tabelle aus diesen Zahlen.
6. Erstelle nur ein Bild.
7. Prüfe nur dieses PowerShell-Skript.
8. Analysiere nur diese einzelne politische Aussage ohne Folgeworkflow.
9. Erstelle aus fertigem Inhalt nur ein PDF.
10. Suche nur eine Mail in Outlook.
11. Erstelle nur ein Board aus einer fertigen Liste.
12. Korrigiere Rechtschreibung in diesem Text.

## Grenzfälle

| Fall | Primär | Unterstützung | Orchestrator |
|---|---|---|---|
| einzelne politische Faktenprüfung | `politik-analyse` | Web | NEIN |
| Faktenprüfung + kommunale Maßnahmen + Kommunikationslinie | Orchestrator | Politik + Stil | JA |
| parlamentarisches PDF aus fertigem Dossier | `parliament-briefing-designer` | PDF | NEIN |
| Dossier erst recherchieren + parlamentarisches PDF | Orchestrator | Politik + Briefing | JA |
| reine lokale Presseaussendung aus fertigen Fakten | Schreib-/Politikstil | ggf. Stil | NEIN |
| lokale Presseaussendung mit fehlenden Fakten und Maßnahmenentwicklung | Orchestrator | Recherche + Politik + Stil | JA |
| Board aus fertigem Maßnahmenplan | verfügbares Board-Werkzeug | keiner | NEIN |
| Maßnahmen entwickeln + Board-Roadmap | Orchestrator | Brainstorming + verfügbares Board-Werkzeug | JA |
| einzelne Tabelle analysieren | verfügbarer Tabellen-Skill | keiner | NEIN |
| Tabelle + politische Verteilungsanalyse + Briefing | Orchestrator | Tabelle + Politik + Briefing | JA |
| Robert-Laimer-Kommentar aus belegtem Faktenset | Schreibstil/Politikkommunikation | Stil | NEIN |
| Robert-Laimer-Dossier mit Recherche, Fragen und Visualisierung | Orchestrator | Politik + Briefing + Visual | JA |

## Fehltrigger

Wenn nach Aktivierung sichtbar wird, dass nur ein Fachworkflow erforderlich ist, sofort delegieren und Orchestrierung beenden.
