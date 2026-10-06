---
name: weekly-dossier
description: Erstelle, aktualisiere, verifiziere oder prüfe das interne Robert-Laimer-Wochendossier, sein Quellenbundle, die Qualitätsgates, den PDF-fertigen Dossierkörper oder den getrennten redaktionellen Wochenplan. Verwende den Skill auch zur Diagnose der bestehenden Make-Wochendossier-Pipeline vor der Produktion. Aktuelle Aussagen müssen aus frischen, nachvollziehbaren Quellen stammen.
---

# Robert Laimer Wochendossier

## Zweck

Erstelle ein aktuelles, quellennachvollziehbares internes Wochendossier für Robert Laimer und auf Wunsch einen getrennten redaktionellen Wochenplan. Verwende die bestehende Make-Quellenarchitektur dort, wo sie gesund ist, übernimm aber keine defekten Referenzen, veralteten URLs oder unbelegten Release-Behauptungen.

Fakten, Analyse, offene Fragen und Textentwürfe müssen unterscheidbar bleiben. Keine individualisierte politische Überzeugungsoptimierung und keine Ableitung politischer Präferenzen aus personenbezogenen Daten.

## Standardpfad

1. Make-Umgebung prüfen, bevor ihre Daten als gesund angenommen werden.
2. Szenarien über Namen finden, nicht über dauerhaft angenommene IDs.
3. Weekly Source Bundle, Dossier-Generation und Montagszustellung prüfen.
4. Ein gesundes Wochenbundle als eine Quellenebene verwenden.
5. Zeitkritische Primärquellen unabhängig aktualisieren.
6. Dossier aus verifizierten Eingaben erstellen.
7. Deterministische Qualitätsgates ausführen.
8. Wochenplan nur aus dem verifizierten Dossier ableiten.
9. Dateien nur auf Wunsch erzeugen; niemals ohne ausdrücklichen Auftrag senden oder veröffentlichen.

Für Architektur und bekannte Defekte `references/make-pipeline.md` laden. Vor dem Drafting `references/quality-gates.md` laden. Für die Dokumentstruktur `references/output-contract.md` verwenden.

## Quellenhierarchie

1. offizielle Primärquellen: Parlament, Ministerien, Bundesheer/BMLV, AMS, Land Niederösterreich, Gemeinden, Statistikstellen und Rechtsquellen
2. andere belastbare Primärquellen
3. seriöse Sekundärquellen für Kontext und Discovery
4. Discovery-only-Medienfunde nur als Leads

Bekannte Evidenzsemantik erhalten: E2 = Discovery-only, E3 = sekundär, E5 = offiziell/primär. E4 nicht erraten, sondern Metadaten prüfen.

## Pflicht-Livechecks

### Arbeitsmarkt Niederösterreich
Keine hart codierte Monats-URL verwenden. Die neueste offizielle AMS-NÖ-Monatsveröffentlichung finden und Publikationsdatum, Referenzmonat, Abrufdatum und exakte Quelle dokumentieren.

### Parlament und Landesverteidigung
Aktuelle offizielle Ausschuss- und Parlamentsseiten verwenden. Verfahrensstand, Rollen, Fristen, Anträge, Abstimmungen und Mehrheiten aus aktuellen offiziellen Quellen prüfen.

### Wahlkreis
Das 82-Gemeinden-Register nur als geografisches Register behandeln, nicht als Beweis aktueller Wochenabdeckung. St. Pölten Stadt, St. Pölten Land, Lilienfeld/Traisen/Gölsental und Tulln/Tullnerfeld unterscheiden.

## Dossierregeln

Wöchentlich insbesondere prüfen:

* Landesverteidigung und Bundesheer
* Neutralitäts- und Sicherheitspolitik, wenn aktuell relevant
* parlamentarische Arbeit und Kontrolle
* soziale und wirtschaftliche Auswirkungen
* aktuelle Wahlkreisthemen
* Auswirkungen auf Arbeitnehmer, Familien, Pensionisten, Pendler und Menschen mit niedrigen oder mittleren Einkommen, sofern belegt
* korrekte Zuständigkeit von Gemeinde, Land, Bund und Parlament

Positionen Robert Laimers nur dann attribuieren, wenn sie dokumentiert sind. Andernfalls als offene Frage, mögliche parlamentarische Option oder Entwurfsidee kennzeichnen.

Jede zentrale Zahl, Frist, Rechtsbehauptung, Personenrolle, Verfahrenslage und aktuelle Tatsachenbehauptung braucht eine nachvollziehbare Quelle.

## Qualitätsgates

Alle Gates aus `references/quality-gates.md` ausführen. Kein PASS für nicht ausgeführte Prüfungen. AI-Review allein ist keine Freigabe.

## Redaktionsplan

Nur aus dem verifizierten Dossier generieren. Montag bis Sonntag der aktuellen Woche verwenden. Maximal fünf Hauptthemen und drei Reservethemen. Status jedes Hauptthemas: `ZUR_PRUEFUNG`.

## Dateiproduktion und Distribution

PDF/DOCX nur auf ausdrücklichen Wunsch erzeugen und gerendertes Ergebnis prüfen. Dossier und Wochenplan getrennt halten, sofern nicht anders verlangt.

SharePoint nur bei vorhandenem Zugriff und ausdrücklichem Speicherauftrag verwenden. E-Mail, Veröffentlichung oder externe Distribution niemals ohne ausdrücklichen aktuellen Auftrag auslösen.
