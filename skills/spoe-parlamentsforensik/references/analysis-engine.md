# Analysis Engine

## Inhaltsübersicht

1. Evidenzpipeline
2. Blue Team
3. Blind Review
4. Red Team
5. SPÖ Symmetry
6. Purple Team
7. Vergleichbarkeit
8. Claim- und Zahlenprüfung
9. Motion Intelligence
10. Kontroversen
11. Strategische Priorisierung

## 1. Evidenzpipeline

Jeder Kandidat durchläuft:

```text
HYPOTHESIS
-> BLUE EVIDENCE PACK
-> BLIND REVIEW bei hoher Relevanz
-> RED CHALLENGE PACK
-> SPÖ SYMMETRY
-> EXTERNAL FACT CHECK
-> CURRENT STATUS CHECK
-> PURPLE DECISION
```

Hypothese und Finding niemals vermischen.

## 2. Blue Team

Blue sucht vollständig nach:

* Aussagen, Forderungen, Versprechen und Ablehnungen
* Anträgen, Abstimmungen und Beschlüssen
* Positionsänderungen und Widerspruchskandidaten
* Budget-, Kosten- und Zahlenbehauptungen
* Verantwortungszuweisungen
* parlamentarischen Erfolgen und ungelösten Sachproblemen
* regional relevanten Vorgängen
* robusten SPÖ-Initiativen und untergenutzten Leistungen
* belastbaren Schwachstellen anderer Parteien

Blue baut den stärksten Evidence Pack, entscheidet aber nicht final.

## 3. Blind Review

Bei besonders wichtigen Widerspruchskandidaten zunächst Partei- und Akteursnamen entfernen. Nur Gegenstand, Instrument, Zeitpunkt, Rechtslage, Finanzierung und Handlung vergleichen. Erst nach Bewertung der materiellen Vergleichbarkeit Namen wieder einblenden.

## 4. Red Team

Red muss aktiv versuchen, den Blue-Befund zu zerstören. Mindestens prüfen:

1. Original korrekt zitiert?
2. Kontext vollständig?
3. tatsächlich derselbe Gegenstand?
4. zeitlich vergleichbar?
5. Rechtslage geändert?
6. wirtschaftliche oder gesellschaftliche Lage geändert?
7. Krise oder neue wissenschaftliche Erkenntnisse?
8. neue EU-Vorgaben?
9. damalige Funktion anders?
10. Regierung oder Opposition?
11. persönliche Aussage oder offizielle Parteilinie?
12. Antrag technisch, finanziell oder im Umfang anders?
13. Teil eines Gesamtpakets?
14. Änderungsanträge?
15. offizielle Erklärung des Positionswechsels?
16. Gegenbelege?
17. strukturell vergleichbarer SPÖ-Fall?
18. könnte ein Faktencheck den Kern widerlegen?
19. könnte ein Interviewer den Vergleich leicht zerlegen?
20. rechtliches oder unnötiges Reputationsrisiko?
21. Korrelation mit Kausalität verwechselt?
22. Nichtbehandlung als Ablehnung missverstanden?
23. fehlende Evidenz als Beweis verwendet?
24. Koalitionsentscheidung einer Einzelperson zugeschrieben?
25. heutiges Wissen rückwirkend angewendet?

Red darf Findings vollständig verwerfen.

## 5. SPÖ Symmetry

Für jedes Finding gegen eine andere Partei materiell vergleichbare SPÖ-Fälle suchen.

Bewertung:

```text
GREEN   robust
YELLOW  mit Kontext belastbar
ORANGE  erhebliches Gegenangriffsrisiko
RED     strategisch nicht belastbar
```

Der Test erzwingt keine künstliche Gleichheit. Ist Evidenz asymmetrisch, die Asymmetrie zeigen.

## 6. Purple Team

Purple erhält Evidence Pack, Challenge Pack, Originalquellen, Gegenquellen, Timeline, SPÖ-Symmetry, Rechts-/Budgetprüfung und aktuellen Status.

Status:

```text
VERIFIED_STRONG
VERIFIED
CONTEXT_REQUIRED
OPEN
WEAK
REJECTED
```

`VERIFIED_STRONG` nur, wenn Originalquelle, Kontext, zeitliche Identität, hohe Vergleichbarkeit, relevante Volltexte, Abstimmung soweit relevant, Gegenbelege, Red Team, SPÖ-Symmetry, aktueller Status und korrekte rechtliche Sprache bestanden sind.

## 7. Vergleichbarkeit

Vor einem Widerspruch 0 bis 5 bewerten:

* gleicher Gegenstand
* gleiche Ebene und Rechtsmaterie
* vergleichbarer Umfang und Ziel
* vergleichbares Instrument
* vergleichbare Finanzierung
* vergleichbarer Zeitkontext
* vergleichbare Verantwortlichkeit
* vergleichbare Informationslage

Unter 4 keinen starken Widerspruch freigeben.

## 8. Claim- und Zahlenprüfung

Claim-Typen:

```text
FAKT
PROGNOSE
VERSPRECHEN
FORDERUNG
GRUNDSATZPOSITION
ABLEHNUNG
RECHTFERTIGUNG
FINANZIERUNGSARGUMENT
KOSTENBEHAUPTUNG
KAUSALBEHAUPTUNG
VERANTWORTUNGSZUWEISUNG
WERTURTEIL
ANGRIFF
KOALITIONSPOSITION
PERSOENLICHE_POSITION
PARTEIPOSITION
KOMPROMISSPOSITION
REGIONALE_FORDERUNG
RECHTLICHE_BEHAUPTUNG
```

Prüfergebnisse:

```text
KORREKT
WEITGEHEND_KORREKT
TEILWEISE_KORREKT
IRREFUEHREND
VERALTET
FALSCH
UNBELEGT
NICHT_PRUEFBAR
```

Bei Zahlen Definition, Bezugsgröße, Zeitraum, geografische Ebene, Preisbasis, Brutto/Netto und Quelle prüfen.

## 9. Motion Intelligence

Für relevante Anträge erfassen:

* Kernforderung
* Gesetzestext und Begründung
* Finanzierung und Kostenbehauptung
* Kompetenz und Adressat
* Zielgruppe
* gewünschtes Inkrafttreten
* Ausschuss- und Plenarverlauf
* Abstimmungen
* Beschluss/Gesetz/Umsetzung
* verwandte frühere und spätere Anträge

Analysen:

```text
SPEECH_MOTION_CONSISTENCY 0..5
MOTION_SIMILARITY_SCORE 0..100
POLICY_PERSISTENCE 0..5
TALK_ACTION_GAP
VOTE_FLIP V1..V5
GOV_OPPOSITION_CONSISTENCY
```

Similarity und Anomalien sind Leads, keine Findings.

## 10. Kontroversen

Strikt zwischen politischer Kontroverse, Vorwurf, Verdachtslage, Ermittlungsverfahren, Anklage, Verurteilung und gerichtlich festgestelltem Sachverhalt unterscheiden.

Bei schweren Fällen mindestens Originalquelle im Parlament, Stellungnahme der betroffenen Seite, zuständige Behörde, Rechnungshof soweit relevant, Justiz/Gericht soweit relevant, aktuellen Status und hochwertige aktuelle journalistische Verifikation prüfen.

## 11. Strategische Priorisierung

Erst nach Purple bewerten:

```text
PRIORITAET_1  hohe Relevanz, starke Evidenz, aktuell, geringe Gegenangriffsgefahr
PRIORITAET_2  relevant und belastbar, aber erklärungsbedürftig
PRIORITAET_3  interessant, kontextabhängig
WATCHLIST      noch nicht ausreichend belegt
DO_NOT_USE     schwach, widerlegt oder strategisch riskant
```

Zusätzlich bewerten: Evidence, Source Quality, Comparability, Contradiction Strength, Voting Evidence, Current Relevance, Policy Relevance, Social Relevance, Regional Relevance, Context Dependence, Counterattack Risk, Legal Risk, SPÖ Symmetry Risk. Keine scheinwissenschaftliche Gesamtnote aus bloßer Multiplikation bilden.
