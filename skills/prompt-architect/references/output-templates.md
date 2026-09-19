# Promptvorlagen

## Inhalt

1. Kompaktprompt
2. Standardprompt
3. Masterprompt
4. Wiederverwendbarer Meta-Prompt
5. Prompt-Audit und Reparatur
6. Modulare Ergänzungen

Vorlagen nicht mechanisch vollständig ausfüllen. Nur Abschnitte übernehmen, die für den konkreten Auftrag eine Funktion haben.

## 1. Kompaktprompt

```text
AUFTRAG
[Konkrete Handlung in einem Satz.]

KONTEXT
[Minimal nötige Ausgangslage und verfügbare Eingaben.]

ANFORDERUNGEN
1. [Verbindliche Anforderung]
2. [Verbindliche Anforderung]
3. [Stil, Länge oder Ausschluss]

AUSGABE
[Liefere das Ergebnis in genau diesem Format.]
```

Geeignet für einzelne Texte, kurze Analysen, einfache Umformulierungen, kleine Bildaufträge und klar begrenzte Entscheidungen.

## 2. Standardprompt

```text
# Auftrag
[Was soll konkret getan werden?]

# Ziel
[Welcher überprüfbare Endzustand soll erreicht werden und wofür?]

# Ausgangslage und Eingaben
[Relevanter Kontext, vorhandene Inhalte, Dateien, Links, Variablen oder Daten.]

# Verbindliche Anforderungen
1. [Muss-Anforderung]
2. [Muss-Anforderung]
3. [Tonalität, Format, Zielgruppe oder technische Grenze]

# Umfang
Einbeziehen:
1. [In Scope]
2. [In Scope]

Nicht einbeziehen:
1. [Out of Scope]

# Vorgehen
1. [Erster überprüfbarer Schritt]
2. [Weitere Schritte in sinnvoller Reihenfolge]
3. [Prüfung vor der Ausgabe]

# Werkzeuge und Quellen
[Nur tatsächlich verfügbare oder konditional formulierte Werkzeuge nennen. Quellenstandard und Aktualität festlegen.]

# Ergebnis
[Liefere genau benannte Ergebnisse oder Artefakte mit Struktur, Sprache, Länge und Dateiformat.]

# Qualitätsprüfung
[Akzeptanzkriterien, Tests, Quellenprüfung, visuelle Kontrolle oder andere Nachweise.]

# Umgang mit Lücken
[Annahmen, Platzhalter, Teilergebnisse und Blockaden regeln.]
```

Geeignet als Standard für die meisten anspruchsvolleren Einzelaufträge.

## 3. Masterprompt

```text
# Rolle und Verantwortung
[Nur eine funktionale Rolle mit Entscheidungsverantwortung und Qualitätsmaßstab definieren.]

# Gesamtauftrag
[Den vollständigen Auftrag mit klarem Endzustand formulieren.]

# Geschäftliches oder fachliches Ziel
[Entscheidung, Wirkung, Zielgruppe und Erfolgskriterium.]

# Ausgangslage
[Gesicherter Kontext. Vermutungen als solche kennzeichnen.]

# Quellen der Wahrheit und Prioritäten
1. [Höchste Priorität oder maßgebliche Quelle]
2. [Weitere Quelle oder Regel]
3. [Konfliktregel]

# Eingaben
Pflicht:
1. [Eingabe oder Variable]

Optional:
1. [Eingabe oder Variable]

# Umfang und Grenzen
Einbeziehen:
1. [Bereich]

Ausschließen:
1. [Bereich]

# Arbeitsphasen

## Phase 1: Bestandsaufnahme
1. [Lesen, suchen, inventarisieren oder reproduzieren]
2. [Lücken und Risiken identifizieren]
3. [Zwischenergebnis]

## Phase 2: Analyse oder Entwurf
1. [Teilfragen, Architektur, Optionen oder Lösung]
2. [Abhängigkeiten und Gegenargumente]
3. [Zwischenergebnis]

## Phase 3: Umsetzung
1. [Konkrete Änderungen, Erstellung oder Ausarbeitung]
2. [Änderungsgrenzen und Freigaben]
3. [Zwischenergebnis]

## Phase 4: Verifikation
1. [Tests, Querverifikation, Rendering oder Coverage-Audit]
2. [Fehlerkorrektur]
3. [Abschlussnachweis]

# Werkzeuge, Connectoren und Quellen
1. [Tatsächlich verfügbare Werkzeuge und wofür sie eingesetzt werden]
2. [Recherchepflicht, Quellenhierarchie und Stichtag]
3. [Verhalten bei fehlendem Zugriff]

# Qualitätsregeln
1. [Evidenzstandard]
2. [Sicherheits-, Datenschutz- oder Rollenregel]
3. [Stil- und Konsistenzregel]
4. [Keine Fertigmeldung vor bestandener Prüfung]

# Ergebnisse
1. [Ergebnis oder Artefakt mit Format]
2. [Ergebnis oder Artefakt mit Format]
3. [Abschlussbericht mit Nachweisen, Risiken und offenen Punkten]

# Fehler- und Konfliktbehandlung
1. Kleine Lücken mit klar benannten Annahmen schließen.
2. Bei blockierten Zugriffen alle ohne diesen Zugriff möglichen Teile erledigen.
3. Widersprüchliche Quellen gegenüberstellen und begründet gewichten.
4. Nicht ausgeführte Prüfungen und verbleibende Risiken ausdrücklich nennen.

# Abschlussbedingung
Der Auftrag gilt erst als abgeschlossen, wenn [messbare Abnahmekriterien] erfüllt und [Nachweise] ausgegeben wurden.
```

Geeignet für Deep Research, komplexe Agentenaufträge, Architektur, Automationen, mehrere Systeme oder hohe fachliche Risiken.

## 4. Wiederverwendbarer Meta-Prompt

```text
# Funktion
Du wandelst die übergebenen Eingaben in [ZIELERGEBNIS] um.

# Gültiger Anwendungsbereich
Verwende diesen Ablauf für [AUFGABENTYPEN]. Verwende ihn nicht für [AUSSCHLÜSSE].

# Eingabeschema
Pflichtfelder:
1. `ziel`: [Beschreibung]
2. `kontext`: [Beschreibung]
3. `ausgabe`: [Beschreibung]

Optionale Felder:
1. `zielsystem`: [Standardwert]
2. `werkzeuge`: [Standardwert]
3. `stil`: [Standardwert]
4. `grenzen`: [Standardwert]

# Verarbeitung
1. Eingaben validieren und normalisieren.
2. Fehlende optionale Felder mit den angegebenen Standardwerten ergänzen.
3. Widersprüche nach [RANGFOLGE] lösen.
4. Den passenden Modus aus [MODI] wählen.
5. Das Ergebnis nach [AUSGABESCHEMA] erzeugen.
6. Das Ergebnis gegen [QUALITÄTSKRITERIEN] prüfen und vor der Ausgabe korrigieren.

# Verhalten bei Lücken
Nur dann nachfragen, wenn ein Pflichtfeld weder vorhanden noch sinnvoll als Variable darstellbar ist. Andernfalls eine transparente Annahme oder einen eindeutigen Platzhalter verwenden.

# Ausgabeschema
[Striktes, maschinenlesbares oder menschlich lesbares Schema.]

# Beispiele
[Eins bis drei kurze Eingabe-Ausgabe-Paare.]
```

Geeignet für wiederkehrende Promptgeneratoren, Systemprompts, Skilllogik und automatisierte Verarbeitung.

## 5. Prompt-Audit und Reparatur

```text
# Auftrag
Prüfe den folgenden Prompt auf Zieltreue, Eigenständigkeit, Ausführbarkeit, Toolrealismus, Ergebnisdefinition, Evidenzstandard, Widersprüche, Fehlerbehandlung und Verifikation. Erhalte die beabsichtigte Aufgabe, entferne Wiederholungen und ersetze vage Intensivwörter durch überprüfbare Kriterien.

# Ausgangsprompt
[ORIGINALPROMPT]

# Verbindliche Zielsetzung
[Was unverändert erreicht werden muss.]

# Vorgehen
1. Harte Anforderungen, Präferenzen, Kontext und Beispiele trennen.
2. Konflikte, Lücken, unrealistische Fähigkeiten und unnötige Vorgaben identifizieren.
3. Den Prompt vollständig neu ordnen und präzisieren.
4. Den Ersatzprompt gegen die genannten Qualitätskriterien prüfen.

# Ausgabe
Gib zuerst den vollständigen, direkt kopierbaren Ersatzprompt in einem `text`-Codeblock aus. Ergänze nur auf ausdrücklichen Wunsch eine knappe Änderungsübersicht oder Bewertung.
```

## 6. Modulare Ergänzungen

### Recherchemodul

```text
Ermittle den zum Ausführungszeitpunkt aktuellen Stand. Priorisiere Primärquellen und offizielle Daten. Unterscheide Veröffentlichungsdatum und Ereignisdatum. Belege zentrale Tatsachenbehauptungen, stelle widersprüchliche Angaben gegenüber und kennzeichne Schlussfolgerungen als solche.
```

### Connector-Schreibmodul

```text
Lies oder suche das Zielobjekt vor jeder Änderung. Löse Namen und IDs eindeutig auf, verhindere Duplikate und führe nur die ausdrücklich verlangte Mutation aus. Verifiziere das Ergebnis anhand der Connector-Rückgabe oder durch erneutes Lesen und berichte die konkrete Änderung mit relevanter ID.
```

### Coding-Verifikationsmodul

```text
Lies zuerst die Repositoryanweisungen und den betroffenen Code. Implementiere nur den nötigen Umfang. Führe die relevanten Tests, Typprüfung, Linting und den Build aus. Behaupte keine erfolgreiche Fertigstellung, wenn eine vorgeschriebene Prüfung nicht ausgeführt oder nicht bestanden wurde.
```

### Artefakt-Prüfmodul

```text
Erstelle das Artefakt im verlangten Format, öffne oder rendere das Ergebnis und prüfe Layout, Überläufe, Seitenumbrüche, Formeln, Links und Dateiintegrität. Liefere ausschließlich die verifizierte Enddatei aus.
```

### Bildreferenzmodul

```text
Verwende ausschließlich das tatsächlich bereitgestellte Referenzbild als Bearbeitungsgrundlage. Erhalte alle als unveränderlich bezeichneten Identitäts-, Produkt- oder Gestaltungsmerkmale. Ändere nur die ausdrücklich benannten Elemente und gleiche Licht, Perspektive, Schatten, Schärfe und Textur realistisch an.
```