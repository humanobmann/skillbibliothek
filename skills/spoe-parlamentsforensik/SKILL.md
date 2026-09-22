---
name: spoe-parlamentsforensik
description: Forensische Deep-Research-Pipeline für das österreichische Parlament mit reproduzierbarer Vollerhebung, Open-Data-API-Abfragen, Coverage-Audit, zeitabhängiger Personen- und Parteiauflösung, Antrags- und Protokollforensik, Widerspruchs- und Positionshistorie sowie Blue-, Red- und Purple-Team-Prüfung. Verwenden bei Parlamentsforensik, Antragsforensik, Widerspruchsanalysen, Promise- und Vote-Tracking, SPÖ-Symmetrietests, Partei- oder Akteursdossiers, regionaler Evidenzanalyse, parlamentarischen Handlungsvorschlägen und strategischer SPÖ-Analyse auf Basis öffentlicher aggregierter Daten. Nicht für einfache politische Faktenfragen, reine Textformulierung oder individualisierte psychografische Wählerprofilierung verwenden.
---

# SPÖ Parlamentsforensik

## Ziel

Ein auditierbares Parliamentary Evidence and Strategy System aufbauen. Erst Quellen und Coverage sichern, danach politische Findings ableiten. Politische Nützlichkeit niemals über Quellenqualität stellen.

## Leitprinzip

Immer in dieser Richtung arbeiten:

`Quelle -> Fundstelle -> Kontext -> Normalisierung -> Vergleich -> Gegenbeleg -> externe Verifikation -> Red Team -> SPÖ Symmetrie -> Purple Team -> Strategie`

Nie umgekehrt von einer gewünschten politischen Erzählung zu passenden Fundstellen suchen.

## Modus bestimmen

Vor Beginn intern einen Modus wählen:

1. `TARGETED`: einzelne Person, Aussage, Antrag, Widerspruch oder Sachfrage.
2. `SCOPED`: Thema, Partei, Zeitraum, Region oder Gesetzgebungsperiode.
3. `FULL_CORPUS`: möglichst vollständige Parlamentsforensik über alle maschinenlesbar verfügbaren Pflichtquellen.

Bei `FULL_CORPUS` keine Toplisten oder strategischen Angriffe vor bestandenem Corpus Gate erzeugen.

## Verbindliche Ressourcen

Je nach Schritt direkt laden:

* `references/api-endpoints.md` für Endpoint-, Filter- und Datensatzlogik.
* `references/api_registry.json` für maschinenlesbare Query-Vorlagen.
* `references/coverage-and-ingestion.md` für Vollerhebung, Segmentierung, Hashing und Resume.
* `references/data-model.md` für IDs, Provenance, Timeline und Graphbeziehungen.
* `references/analysis-engine.md` für Blue, Blind, Red, SPÖ-Symmetrie und Purple.
* `references/output-contracts.md` für Findings, Dossiers und Strategieoutputs.
* `references/licensing.md` vor Download, Speicherung oder Ausgabe eingeschränkter Inhalte.
* `references/masterprompt-source.md` nur bei umfassenden Projektläufen oder wenn eine Detailregel aus dem ursprünglichen Masterprompt benötigt wird.

## Phase 0: Aktuelle Dokumentation prüfen

Vor jeder größeren oder aktuellen Erhebung:

1. Offizielle Open-Data-Übersicht des Parlaments prüfen.
2. Dokumentationsseite jedes benötigten Datensatzes prüfen.
3. `references/api_registry.json` gegen die aktuelle Dokumentation abgleichen.
4. Abweichungen als `DOC_DRIFT` protokollieren.
5. Aktuelle Gesetzgebungsperiode nicht aus dem Skill ableiten, sondern live bestimmen.
6. VTS-Filter des Auftraggebers nur als `AUXILIARY_DISCOVERY` behandeln, bis er live gegen dokumentierte Quellen geprüft wurde.

Bei Widerspruch zwischen Skill und offizieller aktueller Dokumentation gilt die aktuelle offizielle Dokumentation.

## Phase 1: Preflight und Query Plan

Für jeden Research Run festlegen:

```text
RUN_ID
MODE
SCOPE
CHAMBER
GP_OR_DATE_RANGE
REQUIRED_LAYERS
OPTIONAL_LAYERS
CURRENT_DOC_CHECKED_AT
REGISTRY_VERSION
RUNTIME_VERIFIED
```

Wenn Codeausführung verfügbar ist, zuerst ausführen:

```bash
python scripts/validate_registry.py references/api_registry.json
python scripts/parliament_api.py plan --registry references/api_registry.json --gp <GP>
```

Bei fehlendem Netzwerk nicht vortäuschen, dass API-Requests ausgeführt wurden. Status auf `VERIFIED_DOC_NOT_RUNTIME` setzen.

## Phase 2: Korpus erheben

Für Vollerhebungen partei- und themenneutral beginnen. `FRAK_CODE`, `THEMEN`, Person, Schlagwort und EuroVoc sind Kontroll- oder Analysefilter, keine primären Vollerhebungsfilter.

Kanonische Batch-Einheit:

`Quellenklasse x Gremium x Gesetzgebungsperiode oder disjunkter Zeitraum`

Pflichtlayer für das Masterprompt-System:

1. Anträge NR und BR
2. Regierungsvorlagen
3. Ausschussberichte NR und BR
4. Beschlüsse ab dokumentiertem Verfügbarkeitsbeginn
5. schriftliche Anfragen NR und BR inklusive Antwortverknüpfung aus der Verfahrensgeschichte
6. stenographische Protokolle NR und BR
7. Plenarsitzungen NR und BR
8. Parlamentarier:innen und zeitabhängige Mandate
9. Ausschüsse
10. Ausschussmitgliedschaften
11. Parlamentskorrespondenz
12. bei Bedarf Termine, Bürgerinitiativen, Petitionen, Beteiligungen und EU-Verhandlungsgegenstände

Zusätzlich externe Primärquellen nach Sachbedarf verknüpfen: RIS/BGBl, Budgetdienst, Rechnungshof, Statistik Austria, OeNB, Ministerien, Behörden, EU/Eurostat, veröffentlichte Gerichtsentscheidungen und Bundesregierungstimeline.

## Phase 3: Zweistufiger Download

Bei Verhandlungsgegenständen:

1. Index/Filter-API abrufen.
2. Relative Geschichtsseiten-URL kanonisieren.
3. `?json=TRUE` laden.
4. Detail-JSON unverändert speichern und hashen.
5. Dokumentlinks nach Lizenz und Zweck verarbeiten.
6. `status`, `progress/phase` oder `stages`, `documents`, `names`, `vote`, `topics`, `headwords`, `eurovoc`, `correspondence`, `reference` normalisieren.

Keine politische Bewertung allein aus der Ergebnisliste durchführen.

## Phase 4: Coverage beweisen

`showAll=true` niemals als alleinigen Vollständigkeitsbeweis akzeptieren.

Für jeden Batch mindestens prüfen:

```text
API_COUNT
ROWS_RECEIVED
UNIQUE_CANONICAL_OBJECTS
DUPLICATES
DETAIL_SUCCESS
DETAIL_FAILED
```

Freigabe nur, wenn Count- und Identitätsprüfung passen oder eine dokumentierte vollständige Pagination vorliegt.

Danach mindestens eine unabhängige Partition vergleichen. Für Datensatz 101 bevorzugt:

1. Basisscan nach GP und Gremium.
2. Union aller beobachteten `DOKTYP`-Partitionen.
3. Union disjunkter Zeitfenster.

Wenn Sets abweichen: `COVERAGE_CONFLICT`.

Bei Trunkierung oder Konflikt adaptiv segmentieren:

`GP -> Jahr -> Halbjahr -> Quartal -> Monat -> Tag`

Kindfenster müssen disjunkt sein. Die Summe der Counts muss mit dem Elternfenster vereinbar sein. Sonst `SEGMENTATION_INCONSISTENCY`.

Für mechanische Prüfung verwenden:

```bash
python scripts/coverage_audit.py --base <base.json> --partition <part1.json> --partition <part2.json>
```

## Phase 5: Historische Protokolle korrekt behandeln

XX bis XXV:

`Steno Index -> vollständiges HTML -> Tagesordnung -> Sprecherwechsel -> Redeabschnitte -> Zwischenrufe/Beifall/Ordnungsrufe getrennt`

Ab XXVI:

`Steno Index + Plenarsitzungs-JSON + Einzelrede-HTML + vollständiges Steno-HTML`

Einzelrede und Gesamtprotokoll gegenseitig validieren. Parserunsicherheit speichern. OCR nur verwenden, wenn kein besserer maschinenlesbarer Text verfügbar ist.

## Phase 6: Temporal Identity

Personen primär über PAD/amtliche IDs auflösen, nicht nur über Namen.

Für jedes Ereignis zum Ereignisdatum bestimmen:

```text
Person
Partei oder Klub
Funktion
Mandat
Regierungs- oder Oppositionsrolle
Wahlkreis/Bundesland soweit relevant
Ausschussfunktion soweit relevant
```

Heutige Parteizugehörigkeit nie rückwirkend verwenden.

## Phase 7: Normalisierung

Vier Schichten strikt trennen:

`RAW -> NORMALIZED -> DERIVED -> ANALYSIS`

RAW niemals überschreiben. Jede abgeleitete Aussage benötigt Provenance.

Nicht gefunden bedeutet nur `NO_MATCH_IN_SEARCHED_CORPUS`, niemals automatisch `DOES_NOT_EXIST`.

## Phase 8: Analyseobjekte erzeugen

Aus freigegebenem Korpus extrahieren:

* Aussagen und prüfbare Claims
* Versprechen
* Forderungen und Ablehnungen
* Zahlenbehauptungen
* Anträge und Motion DNA
* Abstimmungen soweit dokumentiert
* Beschlüsse und Umsetzung
* Rede-gegen-Antrag
* Antrag-gegen-Antrag
* Motion Lineage
* Vote Flip Kandidaten
* Regierung-Opposition-Flips
* Talk-Action-Gaps
* Policy Persistence
* Kontroversen-Kandidaten
* regionale Sachbezüge

Semantische Ähnlichkeit erzeugt nur einen Kandidaten, keinen politischen Befund.

## Phase 9: Blue, Blind, Red, Symmetry, Purple

Jedes strategisch relevante Finding durchläuft strikt:

1. `BLUE`: stärkste Evidenz für den Kandidaten aufbauen.
2. `BLIND`: wenn sinnvoll Namen und Parteien entfernen und nur Gegenstand, Zeitpunkt und Handlung vergleichen.
3. `RED`: Kontext, Vergleichbarkeit, Rechtslage, Finanzierung, Zuständigkeit, Gegenbelege und alternative Erklärung aktiv suchen.
4. `SPÖ_SYMMETRY`: materiell vergleichbaren SPÖ-Fall suchen und Gegenangriffsrisiko bewerten.
5. `EXTERNAL_CHECK`: amtliche externe Fakten und heutigen Status prüfen.
6. `PURPLE`: endgültig einstufen und strategische Bedeutung ableiten.

Details und Einstufungen in `references/analysis-engine.md` verwenden.

Wenn ein Finding anschließend als Frame-, Narrativ-, Gegenframing- oder Prebunking-Analyse genutzt werden soll, erst nach Purple-Freigabe an `framing-analysis` übergeben. Parlamentarische Evidenz bleibt dabei die Faktenbasis; `framing-analysis` ergänzt Kommunikationsarchitektur, ersetzt aber weder Coverage-, Symmetrie- noch Rechtsprüfung.

## Phase 10: Kontroversen und Rechtsrisiko

Strikt unterscheiden:

`Behauptung -> Vorwurf -> Hinweis/Verdachtslage -> Ermittlung -> Anklage -> Verurteilung -> gerichtlich festgestellter Sachverhalt`

Politische Verantwortung und rechtliche Verantwortung trennen. Ermittlung ist keine Schuld. Ein Positionswechsel ist kein Skandal. Ein Widerspruch ist kein Skandal.

Bei schweren Vorwürfen mindestens Originalquelle, Stellungnahme der betroffenen Seite, zuständige Behörde oder Gericht soweit relevant, aktuellen Verfahrensstatus, Red Team und Purple Team prüfen.

## Phase 11: Strategie ableiten

Erst nach Purple-Freigabe strategisch arbeiten.

Zulässig sind insbesondere:

* bundesweite, Landes-, Wahlkreis-, Bezirks- und Gemeindeanalyse
* Politikfelder
* öffentlich definierte gesellschaftliche Gruppen
* aggregierte Wahlergebnisse, Umfragen und sozioökonomische Daten
* öffentliche regionale Daten
* parlamentarische Aktivität und Medien-/Themenentwicklung

Keine individualisierte psychologische Profilierung einzelner Bürger:innen. Keine politische Ansprache auf Basis privater oder sensibler personenbezogener Daten.

Strategisch priorisieren nach Evidenz, Aktualität, Sachrelevanz, sozialer Wirkung, Verantwortlichkeit, regionaler Bedeutung und Gegenangriffsrisiko. Nicht auf maximale Anzahl von Angriffspunkten optimieren.

## Phase 12: Parlamentarische Handlungsoptionen

Bei belastbaren offenen Sachfragen prüfen:

1. Wurde bereits eine gleichartige Anfrage oder Initiative gestellt?
2. Ist die Antwort noch aktuell?
3. Wer ist zuständig?
4. Welches Instrument erzeugt Informationsgewinn, Kontrolle, Gesetzesänderung, Budgetwirkung, Umsetzungsdruck, Transparenz oder regionale Problemlösung?

Nur dann schriftliche Anfrage, mündliche Anfrage, Entschließungsantrag, Abänderungsantrag, Ausschussfrage, Budgetfrage, Rechnungshofbezug oder Gesetzesinitiative empfehlen.

## Freigabestatus

Für Korpus:

`VERIFIED_DOC_NOT_RUNTIME`, `PARTIAL`, `FAILED_COVERAGE`, `COMPLETE`

Für Findings:

`VERIFIED_STRONG`, `VERIFIED`, `CONTEXT_REQUIRED`, `OPEN`, `WEAK`, `REJECTED`

Top Findings benötigen grundsätzlich Primärquellenqualität E3 oder höher und Confidence A oder B.

## Harte Stopregeln

Keine strategische Freigabe bei:

* Coverage-Konflikt
* nicht nachvollziehbarer Query- oder Quellenherkunft
* ungeklärter zeitlicher Identität
* angenommener statt dokumentierter Abstimmung
* fehlendem Kontext eines starken Zitats
* ungeklärtem Quellenkonflikt
* laufendem Verfahren mit überzogener Tatsachenbehauptung
* Lizenzproblem
* erheblichem SPÖ-Gegenfall ohne Bewertung
* aktueller Lage ungeprüft

## Standardausgabe

Bei Forschungsruns zuerst Status und Coverage liefern. Danach je nach Auftrag die passenden Outputs aus `references/output-contracts.md` erzeugen.

Jedes Top Finding muss mindestens enthalten:

```text
Finding ID
Kernbefund
Quelle A und B
Kontext
Vergleichbarkeit
Gegenbelege
aktuelle Lage
Blue Urteil
Red Urteil
SPÖ Symmetry
Purple Urteil
Evidence Grade
Confidence
Counterattack Risk
Legal Risk
sichere Formulierung
nicht zulässige Übertreibung
```

Wenn Vollerhebung technisch nicht vollständig möglich ist, exakt benennen, was fehlt. Niemals behaupten, alle Protokolle oder alle Anträge analysiert zu haben, wenn dies nicht nachgewiesen ist.
