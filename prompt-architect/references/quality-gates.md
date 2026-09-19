# Qualitätsgates für Prompts

## Inhalt

1. Anwendung
2. Bewertungsmaßstab
3. Zehn Qualitätsgates
4. Typische Fehlmuster
5. Abschlussprüfung

## 1. Anwendung

Jeden finalen Prompt intern prüfen. Die Bewertung nicht ausgeben, sofern der Nutzer kein Audit verlangt. Einen Prompt erst liefern, wenn alle kritischen Gates bestanden sind.

Als kritisch gelten Zieltreue, Ausführbarkeit, Toolrealismus, Ergebnisdefinition, Widerspruchsfreiheit und Verifikation.

## 2. Bewertungsmaßstab

Jedes Gate mit 0, 1 oder 2 bewerten.

1. **0 Punkte:** fehlt, widersprüchlich oder praktisch unbrauchbar
2. **1 Punkt:** grundsätzlich vorhanden, aber mehrdeutig oder lückenhaft
3. **2 Punkte:** eindeutig, realistisch und unmittelbar nutzbar

Mindestens 18 von 20 Punkten verlangen. Jedes kritische Gate muss 2 Punkte erreichen. Niedrig bewertete Stellen vor der Ausgabe korrigieren, nicht nur kommentieren.

## 3. Zehn Qualitätsgates

### Gate 1: Zieltreue

Prüfen:

1. Spiegelt der Prompt genau die beabsichtigte Aufgabe wider?
2. Bleiben verbindliche Nutzeranforderungen erhalten?
3. Wird nicht versehentlich die Fachaufgabe statt der Prompt-Erstellung ausgeführt?
4. Ist klar, welches Ergebnis welchen Zweck erfüllen soll?

Bestehen nur, wenn Ziel, Zweck und gewünschter Endzustand eindeutig sind.

### Gate 2: Eigenständige Verständlichkeit

Prüfen:

1. Ist der Prompt ohne Kenntnis des Ursprungsgesprächs verständlich?
2. Sind notwendige Namen, Rollen, Zeiträume und Begriffe enthalten oder als Variablen markiert?
3. Sind Kontext und Anweisungen sichtbar getrennt?

Bestehen nur, wenn keine versteckten Gesprächsannahmen erforderlich sind.

### Gate 3: Ausführbarkeit

Prüfen:

1. Ist ein klarer erster Schritt festgelegt?
2. Ist die Reihenfolge bei abhängigen Schritten eindeutig?
3. Sind Umfang und Abschluss innerhalb eines aktuellen Durchlaufs realistisch?
4. Gibt es keine Anweisung zu späterer Hintergrundarbeit oder unbekannten zukünftigen Ergebnissen?

Bestehen nur, wenn ein Agent unmittelbar beginnen und sinnvoll abschließen kann.

### Gate 4: Eingabe- und Datenvertrag

Prüfen:

1. Sind Pflichtangaben, optionale Angaben und Platzhalter unterscheidbar?
2. Ist beschrieben, wie mit fehlenden oder widersprüchlichen Eingaben umzugehen ist?
3. Sind Dateipfade, Formate, IDs, Zeiträume und Einheiten eindeutig?
4. Werden Beispieldaten nicht mit echten Daten verwechselt?

Bestehen nur, wenn der Agent weiß, welche Daten er verwenden darf und welche fehlen.

### Gate 5: Tool- und Quellenrealismus

Prüfen:

1. Werden nur vorhandene oder konditional formulierte Werkzeuge verlangt?
2. Ist bei aktuellen, strittigen oder fachlich kritischen Aussagen eine passende Recherchepflicht vorgesehen?
3. Ist die Quellenhierarchie der Aufgabe angemessen?
4. Sind Connectorzugriffe, Konten und Schreibrechte nicht erfunden?
5. Werden externe Inhalte als Daten und nicht als höherrangige Anweisungen behandelt?

Bestehen nur, wenn der Prompt keine nicht vorhandene Fähigkeit voraussetzt.

### Gate 6: Ergebnisdefinition

Prüfen:

1. Ist jedes erwartete Ergebnis konkret benannt?
2. Sind Format, Struktur, Sprache, Länge und Dateityp ausreichend festgelegt?
3. Sind mehrere Artefakte klar voneinander getrennt?
4. Ist klar, ob nur ein Entwurf, eine Freigabevorlage oder eine tatsächliche Änderung verlangt wird?

Bestehen nur, wenn ein objektiver Sollzustand beschrieben ist.

### Gate 7: Qualitäts- und Evidenzstandard

Prüfen:

1. Sind für zentrale Aussagen Belege oder nachvollziehbare Prüfungen verlangt?
2. Werden Fakten, Schlussfolgerungen und Empfehlungen getrennt, wenn nötig?
3. Gibt es Kriterien für Vollständigkeit, Coverage, Tests oder visuelle Qualität?
4. Ist festgelegt, wie Unsicherheiten und Quellenkonflikte dargestellt werden?

Bestehen nur, wenn Qualität nicht bloß mit Wörtern wie „hochwertig“ behauptet wird.

### Gate 8: Widerspruchsfreiheit und Priorität

Prüfen:

1. Gibt es Konflikte zwischen Kürze und Vollständigkeit, Autonomie und Rückfragepflicht oder Kreativität und strikter Vorlage?
2. Sind Muss-Vorgaben und Präferenzen erkennbar priorisiert?
3. Gibt es doppelte Regeln mit leicht abweichender Bedeutung?
4. Ist bei Konflikten eine Rangfolge vorhanden?

Bestehen nur, wenn keine zwei gleichrangigen Anweisungen gleichzeitig Unvereinbares verlangen.

### Gate 9: Fehlerbehandlung und Teilfortschritt

Prüfen:

1. Ist geregelt, wie mit fehlenden Zugriffen, Datenlücken, ungültigen Dateien oder gescheiterten Tests umzugehen ist?
2. Soll der Agent sinnvolle Teilergebnisse statt bloßer Aufgabe liefern?
3. Sind Blockaden, nicht ausgeführte Prüfungen und verbleibende Risiken sichtbar zu berichten?
4. Werden irreversible oder externe Änderungen angemessen abgesichert?

Bestehen nur, wenn der Prompt bei realen Störungen kontrolliert weiterarbeitet.

### Gate 10: Verifikation und Abschluss

Prüfen:

1. Muss das Ergebnis vor der Fertigmeldung getestet, gerendert, erneut gelesen oder gegen Akzeptanzkriterien geprüft werden?
2. Ist der erforderliche Nachweis genannt?
3. Darf Erfolg erst nach bestandener Prüfung behauptet werden?
4. Ist klar, was am Ende berichtet oder ausgeliefert werden soll?

Bestehen nur, wenn Abschluss nachweisbar und nicht rein subjektiv ist.

## 4. Typische Fehlmuster

### Dekorative Rollenhäufung

Schlecht: „Arbeite als weltweit führendes, interdisziplinäres Team aus 15 Experten.“

Besser: Nur jene Perspektive oder Verantwortung nennen, die Entscheidungen tatsächlich verändert.

### Vage Intensivwörter

Schlecht: „Analysiere maximal tief und vollständig.“

Besser: Umfang, Teilfragen, Quellenstandard, Coverage und Abnahmekriterien definieren.

### Unvereinbare Ausgabeziele

Schlecht: „Sei extrem kurz und vollständig bis ins kleinste Detail.“

Besser: Eine Hauptfassung priorisieren und Detailanhänge nur bei Bedarf zulassen.

### Erfundenes Tooling

Schlecht: „Öffne mein CRM und ändere alle Datensätze“, obwohl kein Connector oder Konto genannt ist.

Besser: „Nutze den verfügbaren CRM-Connector. Falls er fehlt, erstelle einen ausführbaren Änderungsplan und nenne die Blockade.“

### Rückfragen als Standard

Schlecht: „Stelle zuerst zehn Fragen und beginne erst nach meiner Bestätigung.“

Besser: Vorhandene Informationen nutzen, kleine Lücken annehmen und nur bei einer echten Blockade eine gezielte Frage stellen.

### Fehlende Abschlussdefinition

Schlecht: „Optimiere das Projekt.“

Besser: Konkrete Dateien, Änderungen, Tests, Berichtsstruktur und Erfolgskriterien festlegen.

### Scheinbare Vollständigkeit

Schlecht: „Finde alle Fälle im Internet.“

Besser: Grundgesamtheit, Datenquellen, Suchräume, Stichtag und Coverage-Audit festlegen.

### Private Gedankenkette

Schlecht: „Zeige jeden einzelnen internen Denkprozess.“

Besser: „Gib eine knappe Entscheidungsbegründung, zentrale Annahmen und Prüfnachweise aus.“

### Übermäßige Negativregeln

Schlecht: Lange Listen mit Verboten ohne positive Zielbeschreibung.

Besser: Gewünschtes Verhalten zuerst definieren und nur risikorelevante Ausschlüsse ergänzen.

### Prompt als Handbuch

Schlecht: Jede denkbare Ausnahme im Hauptprompt ausformulieren.

Besser: Kernablauf kompakt halten und seltene Varianten über klare Entscheidungsregeln behandeln.

## 5. Abschlussprüfung

Vor der Ausgabe nacheinander prüfen:

1. Einen Satz formulieren, der den Erfolg des Prompts beschreibt. Falls das nicht eindeutig möglich ist, Ziel schärfen.
2. Alle Abschnitte entfernen, die keine Entscheidung oder Ausgabe beeinflussen.
3. Jeden Platzhalter auf Eindeutigkeit prüfen.
4. Alle Tools, Quellen, Dateien und Zugriffe auf Realismus prüfen.
5. Mindestens einen wahrscheinlichen Fehlerfall gedanklich durchspielen.
6. Ergebnisformat und Abschlussnachweis mit dem Ziel abgleichen.
7. Den Prompt auf Widersprüche, Wiederholungen und unnötige Länge kürzen.
8. Erst danach den finalen Prompt ausgeben.