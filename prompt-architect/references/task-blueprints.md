# Aufgaben-Blueprints

## Inhalt

1. Recherche und Deep Research
2. Faktencheck
3. Coding und Agentenaufträge
4. Automationen und Integrationen
5. Connector- und App-Aktionen
6. Schreiben, Überarbeiten und Kommunikation
7. Dokumente, Tabellen, Präsentationen und PDFs
8. Bilder und visuelle Gestaltung
9. Analyse, Entscheidung und Planung
10. Wiederverwendbare Meta-Prompts

Diese Blueprints nur laden, wenn der jeweilige Aufgabentyp vorliegt. Pflichtfelder übernehmen, aber keine unnötigen Abschnitte in den finalen Prompt kopieren.

## 1. Recherche und Deep Research

### Pflichtfelder

- Präzise Forschungsfrage und unterstützte Entscheidung
- Zeitlicher, geografischer und sachlicher Umfang
- Begriffe, Ein- und Ausschlüsse sowie gewünschte Vergleichsgruppen
- Stichtag oder Aktualitätsanforderung
- Quellenhierarchie und Mindestqualität
- Vorgehen für Suche, Querverifikation und Widersprüche
- Gewünschte Daten, Tabellen, Zitate oder Primärquellen
- Ausgabeformat, Länge und Zielgruppe
- Grenzen, Unsicherheiten und offene Punkte

### Sinnvolle Ablaufstruktur

1. Forschungsfrage in überprüfbare Teilfragen zerlegen.
2. Zuerst Primärquellen, offizielle Daten, Originaldokumente oder Fachliteratur suchen.
3. Sekundärquellen zur Einordnung und zur Entdeckung weiterer Primärquellen nutzen.
4. Zentrale Behauptungen mindestens durch eine belastbare Quelle stützen; besonders strittige oder folgenreiche Aussagen gegenprüfen.
5. Veröffentlichungsdatum und Ereignisdatum unterscheiden.
6. Abweichende Angaben erklären, statt willkürlich eine Zahl auszuwählen.
7. Fakten, Schlussfolgerungen und Empfehlungen sichtbar trennen.
8. Recherchelücken und nicht verifizierbare Punkte ausdrücklich nennen.

### Ergänzungen für Vollerhebungen

- Grundgesamtheit und Datenquelle definieren.
- Vollständigkeit anhand erwarteter und gefundener Datensätze prüfen.
- Duplikate, Ausfälle und zeitabhängige Zuordnungen behandeln.
- Reproduzierbare Suchparameter, Filter, Abfragen und Stichtage dokumentieren.

## 2. Faktencheck

### Pflichtfelder

- Zu prüfender Text oder klar abgegrenzte Behauptungen
- Prüfzeitpunkt und relevante Rechts-, Daten- oder Wissenslage
- Bewertungsmaßstab, beispielsweise richtig, überwiegend richtig, unbelegt, irreführend oder falsch
- Primärquellenpflicht für zentrale Aussagen
- Korrekturvorschlag für fehlerhafte oder missverständliche Stellen
- Trennung zwischen Tatsachenbehauptung, Wertung und Prognose

### Sinnvolle Ablaufstruktur

1. Atomare überprüfbare Behauptungen extrahieren.
2. Behauptungen nach Tragweite und Fehlerrisiko priorisieren.
3. Jede Behauptung mit der stärksten verfügbaren Quelle prüfen.
4. Quellenqualität, Datum und Kontext berücksichtigen.
5. Urteil mit kurzer Begründung und Beleg ausgeben.
6. Fehlende Evidenz nicht als Widerlegung darstellen.
7. Einen korrigierten Text nur aus bestätigten oder klar gekennzeichneten Aussagen formulieren.

## 3. Coding und Agentenaufträge

### Pflichtfelder

- Repository, Arbeitsverzeichnis oder Projektkontext
- Konkretes gewünschtes Verhalten oder zu behebender Fehler
- Bestehende Architektur, Konventionen und relevante Anweisungsdateien
- Zulässiger Änderungsumfang und ausgeschlossene Bereiche
- Laufzeit, Sprache, Framework und unterstützte Versionen
- Tests, Linting, Typprüfung, Build und Sicherheitsprüfungen
- Akzeptanzkriterien und erwartete Nachweise
- Umgang mit fehlenden Zugangsdaten oder externen Diensten

### Sinnvolle Ablaufstruktur

1. Repositoryregeln und vorhandene Dokumentation lesen.
2. Istzustand und wahrscheinlichste Ursache mit konkreten Dateien oder Symbolen belegen.
3. Den kleinsten tragfähigen Änderungsplan festlegen.
4. Bei Features und Fehlerbehebungen zuerst relevante Tests ergänzen oder festlegen.
5. Implementieren, ohne unbeauftragte Architekturwechsel vorzunehmen.
6. Betroffene Tests, Typprüfung, Linting und Build ausführen.
7. Sicherheits- und Regressionsrisiken prüfen.
8. Geänderte Dateien, Nachweise, verbleibende Risiken und blockierte Prüfungen berichten.

### Zusätzliche Regeln

- Keine erfolgreiche Fertigstellung behaupten, wenn definierte Prüfungen nicht ausgeführt oder nicht bestanden wurden.
- Keine Secrets, Tokens oder produktiven Zugangsdaten in Code oder Logs schreiben.
- Bestehende APIs und Abwärtskompatibilität nur nach ausdrücklicher Freigabe brechen.
- Bei unklarem Bug zuerst reproduzieren oder die fehlende Reproduktionsmöglichkeit dokumentieren.

## 4. Automationen und Integrationen

### Pflichtfelder

- Geschäftsziel und verantwortlicher Prozess
- Auslöser, Frequenz und erwartetes Volumen
- Quell- und Zielsysteme sowie System of Record
- Datenobjekte, Pflichtfelder, IDs und Mappingregeln
- Authentifizierung und Secret-Verwaltung
- Idempotenz, Duplikatschutz und Wiederanlauf
- Fehlerklassen, Wiederholungen, Quarantäne oder Dead-Letter-Pfad
- Beobachtbarkeit, Alarmierung und Audit-Trail
- Datenschutz, Aufbewahrung und Löschung
- Testfälle, Rollback und Betriebsübergabe

### Sinnvolle Ablaufstruktur

1. Zielprozess und Verantwortungsgrenzen modellieren.
2. Source of Truth je Datenobjekt festlegen.
3. Trigger, Ereignisse und Datenvertrag definieren.
4. Happy Path und Fehlerpfade getrennt entwerfen.
5. Idempotenzschlüssel und Zustandsmodell festlegen.
6. Retries nur für vorübergehende Fehler verwenden.
7. Secrets außerhalb des Workflows verwalten.
8. Testdaten, Staging, Monitoring und manuelle Wiederaufnahme planen.
9. Erst danach konkrete Szenarien, Nodes oder Module umsetzen.

### Architekturwarnungen

- Kein zweites CRM, Task-System oder Schattenregister ohne begründete Notwendigkeit einführen.
- Kritische Zahlungs-, Rechts- oder Buchhaltungsprozesse nicht ausschließlich auf unkontrollierte Best-Effort-Automationen stützen.
- Synchronisationen nicht ohne Konfliktregel und Eigentümerschaft für Felder entwerfen.

## 5. Connector- und App-Aktionen

### Pflichtfelder

- Gewünschte Lese- oder Schreibaktion
- Konto, Organisation, Workspace oder Rolle
- Eindeutige Zielobjekte wie Empfänger, Kalender, Datei, Projekt oder Datensatz
- Freigabegrenze und mögliche Außenwirkung
- Kriterien für Suche und Identitätsauflösung
- Duplikat- und Kollisionsschutz
- Ergebnisbestätigung mit IDs, Zeitstempel oder Änderungsübersicht

### Sinnvolle Ablaufstruktur

1. Vorhandene Objekte lesen oder suchen, bevor neue erstellt werden.
2. Namen, E-Mail-Adressen, IDs und Zielcontainer auflösen.
3. Schreibaktion mit den tatsächlich verfügbaren Connectorfunktionen ausführen.
4. Bei mehreren möglichen Zielen die sicherste begründete Auswahl treffen oder klar benannte Platzhalter verwenden.
5. Keine Mutation aus einer bloßen Analyseabsicht ableiten.
6. Nach dem Schreiben das Ergebnis erneut lesen oder anhand der Rückgabe verifizieren.
7. Genau berichten, was geändert, erstellt, gesendet oder nicht ausgeführt wurde.

## 6. Schreiben, Überarbeiten und Kommunikation

### Pflichtfelder

- Zweck, Zielgruppe und gewünschte Wirkung
- Absenderrolle und organisatorischer Kontext
- Kernaussage und verpflichtende Fakten
- Ton, Länge, Kanal und gewünschte Handlungsaufforderung
- Tabus, rechtliche Risiken und zu vermeidende Behauptungen
- Gewünschtes Ausgabeformat

### Sinnvolle Ablaufstruktur

1. Aussageziel und Adressat bestimmen.
2. Fakten, Bewertung und Formulierung trennen, wenn das Thema strittig oder politisch ist.
3. Nur bestätigte Tatsachen verwenden; fehlende Zitate, Erlebnisse oder Zahlen nicht erfinden.
4. Mit der stärksten Aussage beginnen.
5. Wiederholungen, Floskeln und abstrakte Sprache entfernen.
6. Für den Kanal passende Länge, Lesbarkeit und Handlungsaufforderung herstellen.
7. Standardmäßig den fertigen Text liefern, nicht zuerst eine Schreibberatung.

### Überarbeitung vorhandener Texte

- Aussage und Stimme erhalten, sofern keine Neupositionierung verlangt wird.
- Unklare Bezüge, logische Sprünge und unbelegte Behauptungen korrigieren.
- Kürzungen nicht auf Kosten zentraler Bedeutung vornehmen.
- Bei heiklen Aussagen eine belastbare, weniger angreifbare Formulierung wählen.

## 7. Dokumente, Tabellen, Präsentationen und PDFs

### Pflichtfelder

- Ausgangsdatei oder Rohinhalt
- Zielformat und gewünschter Dateiname
- Zielgruppe und Verwendungszweck
- Inhaltliche Struktur und Pflichtbestandteile
- Gestaltungs-, Marken- und Barrierefreiheitsregeln
- Anforderungen an Formeln, Tabellen, Diagramme, Quellen oder Anhänge
- Render-, Funktions- und Vollständigkeitsprüfung
- Gewünschter Auslieferungsort

### Sinnvolle Ablaufstruktur

1. Ausgangsdateien und relevante Dateiinhalte vollständig prüfen.
2. Das passende Autorenformat wählen und unnötige Konvertierungen vermeiden.
3. Inhalt und Layout getrennt strukturieren.
4. Datei programmgesteuert oder mit dem vorgesehenen Werkzeug erstellen.
5. Das Ergebnis rendern oder öffnen und visuell prüfen.
6. Formeln, Links, Seitenumbrüche, Überläufe und Dateiintegrität testen.
7. Erst die verifizierte Datei ausliefern.

## 8. Bilder und visuelle Gestaltung

### Pflichtfelder

- Bildtyp, Zweck und Ausgabekanal
- Motiv, Personen, Objekte und Handlung
- Komposition, Perspektive, Licht und Hintergrund
- Seitenverhältnis und Auflösung
- Stil, Materialität und Farbwirkung
- Exakte Textelemente und typografische Priorität
- Referenzbilder und unveränderliche Merkmale
- Ausdrücklich unerwünschte Veränderungen

### Für Bildbearbeitung

- Nur ein tatsächlich bereitgestelltes Zielbild bearbeiten.
- Identität, Gesicht, Körper, Produktform oder andere geschützte Referenzmerkmale nur im verlangten Umfang verändern.
- Zu entfernende und zu erhaltende Elemente getrennt benennen.
- Perspektive, Licht, Schatten, Körnung und Schärfe an das Ausgangsbild anpassen.
- Keine nicht verlangten Logos, Marken, Organisationsnamen oder Footer ergänzen.

### Für Bildserien

- Konsistente Identität, Kleidung, Farbwelt und Stilregeln festlegen.
- Gewünschte Unterschiede pro Bild definieren, beispielsweise Pose, Ausschnitt, Handlung oder Kamerawinkel.
- Collagen und Mehrfachpanels ausdrücklich ausschließen, wenn Einzelbilder verlangt sind.

## 9. Analyse, Entscheidung und Planung

### Pflichtfelder

- Entscheidungsfrage und Entscheidungshorizont
- Ziele, Muss-Kriterien und Gewichtung
- Verfügbare Optionen oder Suchraum
- Datenbasis und Unsicherheiten
- Risiken, Kosten, Abhängigkeiten und Reversibilität
- Erwartete Empfehlung und nächste Schritte

### Sinnvolle Ablaufstruktur

1. Problem und Zielzustand präzisieren.
2. Kriterien definieren und Muss-Kriterien von Optimierungskriterien trennen.
3. Realistische Optionen einschließlich Status quo vergleichen.
4. Annahmen und Unsicherheiten sichtbar machen.
5. Eine klare Empfehlung mit Begründung und Gegenargumenten geben.
6. Sofortige nächste Schritte, Entscheidungspunkte und Risiken priorisieren.

## 10. Wiederverwendbare Meta-Prompts

### Pflichtfelder

- Klarer Anwendungsbereich und Auslöser
- Eingabeschema mit Pflicht- und Optionalfeldern
- Unveränderliche Regeln und anpassbare Parameter
- Entscheidungslogik für unterschiedliche Aufgabentypen
- Ausgabeschema und Standardmodus
- Verhalten bei fehlenden oder widersprüchlichen Eingaben
- Ein bis drei realistische Beispiele
- Selbstprüfung vor der Ausgabe

### Konstruktionsprinzipien

- Den Meta-Prompt als kleinen Compiler entwerfen: Eingaben normalisieren, Modus wählen, Ergebnis erzeugen, prüfen und erst dann ausgeben.
- Eingaben und Anweisungen klar trennen.
- Standardwerte definieren, damit der Meta-Prompt ohne lange Rückfragen nutzbar bleibt.
- Erweiterungspunkte benennen, ohne den Kern mit seltenen Sonderfällen zu überladen.
- Ein unverwechselbares Ausgabeformat verlangen, damit nachgelagerte Automationen das Ergebnis verarbeiten können.