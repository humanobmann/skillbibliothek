# Kalibrierungsbeispiele

Die Beispiele zeigen Struktur und Entscheidungslogik. Inhalte nicht ungeprüft auf andere Aufgaben übertragen.

## Beispiel 1: Vage Bitte in einen Standardprompt übersetzen

### Eingabe

„Analysiere meine Website maximal und sag mir, was ich verbessern muss.“

### Gute Umsetzung

```text
# Auftrag
Analysiere die bereitgestellte Website hinsichtlich Nutzerführung, Verständlichkeit, Barrierefreiheit, technischer Qualität und Conversion. Leite daraus eine priorisierte Verbesserungsliste ab.

# Eingaben
Website: [URL]
Primäres Ziel: [ZIEL, zum Beispiel Spenden, Verkauf oder Anmeldung]
Zielgruppe: [ZIELGRUPPE]

# Vorgehen
1. Prüfe Startseite, Navigation, zentrale Zielseiten und den wichtigsten Conversion-Pfad.
2. Trenne beobachtbare Befunde von Annahmen.
3. Bewerte jeden Befund nach Wirkung, Dringlichkeit und Umsetzungsaufwand.
4. Formuliere für die fünf wichtigsten Probleme konkrete Änderungen.
5. Kennzeichne Punkte, die ohne Analytics, Repositoryzugriff oder Nutzertests nicht verifiziert werden können.

# Ausgabe
Liefere:
1. eine Zusammenfassung mit den drei größten Hebeln,
2. eine Tabelle mit Befund, Evidenz, Auswirkung, Priorität und Maßnahme,
3. einen umsetzbaren 30-Tage-Plan.

# Qualitätskriterien
Keine generischen Best-Practice-Listen ohne Bezug zur untersuchten Seite. Keine erfundenen Kennzahlen. Aktuelle technische Behauptungen nur nach Prüfung der tatsächlich sichtbaren Implementierung.
```

### Warum diese Umsetzung funktioniert

„Maximal“ wurde in konkrete Prüfdimensionen, Priorisierung, Evidenz und Ergebnisse übersetzt. Fehlende Daten wurden als Variablen und Grenzen behandelt.

## Beispiel 2: Deep-Research-Masterprompt

### Eingabe

„Erstelle mir einen Deep-Research-Prompt für die beste Automationsarchitektur mit Make, Microsoft 365 und einem CRM.“

### Gute Umsetzung

```text
# Gesamtauftrag
Entwickle eine belastbare Zielarchitektur für [ORGANISATION], die wiederkehrende Verwaltungs-, Kommunikations- und CRM-Prozesse mit Make und Microsoft 365 automatisiert. Prüfe zuerst den Istzustand und begründe anschließend Systemgrenzen, Datenhoheit, Integrationen, Sicherheitskontrollen und eine realistische Einführungsreihenfolge.

# Forschungsfragen
1. Welches System ist je Datenobjekt die verbindliche Quelle der Wahrheit?
2. Welche Prozesse eignen sich für Make und welche müssen wegen Kritikalität außerhalb einer Best-Effort-Automation bleiben?
3. Wie werden Identitäten, Berechtigungen, Secrets, Fehler, Wiederanläufe und Audit-Trails behandelt?
4. Welche CRM-Option erfüllt die Anforderungen mit geringster Systemduplizierung?
5. Welche Architektur ist für drei Jahre Betrieb, Wartung und Kosten am robustesten?

# Quellenstandard
Ermittle den zum Ausführungszeitpunkt aktuellen Stand. Priorisiere offizielle Produktdokumentation, Sicherheitsdokumentation, API-Referenzen, Preis- und Limitseiten sowie anerkannte Architekturquellen. Kennzeichne Annahmen und stelle relevante Produktgrenzen oder widersprüchliche Angaben gegenüber.

# Vorgehen
1. Erfasse Ziele, Prozesse, Datenobjekte, Volumen, Rollen und vorhandene Systeme.
2. Erstelle eine Istarchitektur und einen Coverage-Audit der fehlenden Informationen.
3. Vergleiche mindestens drei tragfähige Architekturvarianten einschließlich Status quo.
4. Entwirf die empfohlene Zielarchitektur mit Datenflüssen, Fehlerpfaden, Sicherheitsmodell und Betriebsverantwortung.
5. Führe einen Red-Team-Test auf Single Points of Failure, Vendor Lock-in, Datenverlust, Dubletten und unkontrollierte Kosten durch.
6. Erstelle einen phasenweisen Umsetzungsplan mit Abnahmekriterien.

# Ergebnisse
1. Executive Summary
2. Istarchitektur und Risiken
3. Variantenvergleich mit gewichteten Kriterien
4. empfohlene Zielarchitektur
5. Daten- und Integrationsmatrix
6. Sicherheits- und Betriebsmodell
7. 90-Tage-Umsetzungsplan
8. offene Fragen und nicht verifizierbare Punkte

# Abschlussbedingung
Die Untersuchung gilt erst als abgeschlossen, wenn jede Empfehlung einer Anforderung und einer belastbaren Quelle oder klar gekennzeichneten Architekturannahme zugeordnet ist.
```

## Beispiel 3: Coding-Agent statt allgemeiner Programmierberatung

### Eingabe

„Mach einen Prompt für Codex, damit er den Login-Bug vollständig behebt.“

### Gute Umsetzung

```text
# Auftrag
Behebe den reproduzierbaren Login-Fehler im Repository `[REPOSITORY ODER PFAD]`, ohne das Authentifizierungsmodell außerhalb des nötigen Umfangs zu verändern.

# Fehlerbild
[FEHLERMELDUNG, REPRODUKTIONSSCHRITTE UND ERWARTETES VERHALTEN]

# Vorgehen
1. Lies zuerst alle einschlägigen Repositoryanweisungen und die Authentifizierungsdokumentation.
2. Reproduziere den Fehler oder dokumentiere präzise, wodurch die Reproduktion blockiert ist.
3. Bestimme die Ursache anhand konkreter Dateien, Funktionen und Laufzeitdaten.
4. Ergänze einen Test, der vor der Korrektur fehlschlägt und das erwartete Verhalten beschreibt.
5. Implementiere die kleinste tragfähige Korrektur.
6. Führe betroffene Tests, Typprüfung, Linting und Build aus.
7. Prüfe Session-Sicherheit, Fehlermeldungen und bestehende Login-Varianten auf Regressionen.

# Grenzen
Keine neuen Auth-Anbieter, keine Schemaänderung und keine Änderung öffentlicher APIs ohne nachgewiesene Notwendigkeit. Keine Secrets oder personenbezogenen Daten in Logs schreiben.

# Ergebnis
Berichte Ursache, geänderte Dateien, Testnachweise und verbleibende Risiken. Behaupte keine erfolgreiche Behebung, solange eine vorgeschriebene Prüfung fehlschlägt oder nicht ausgeführt wurde.
```

## Beispiel 4: Strenge Referenztreue bei Bildbearbeitung

### Eingabe

„Verbessere meinen Bildprompt. Mein Gesicht darf nicht verändert werden und nur der Hintergrund soll neu sein.“

### Gute Umsetzung

```text
Bearbeite ausschließlich das in dieser Unterhaltung bereitgestellte Originalfoto.

ZIEL
Ersetze nur den vorhandenen Hintergrund durch [NEUER HINTERGRUND]. Das Ergebnis muss wie eine reale Aufnahme am neuen Ort wirken.

UNVERÄNDERLICH
Verwende Kopf, Gesicht, Haare, Hautstruktur, Ausdruck, Körper, Kleidung, Haltung und Proportionen direkt aus dem Originalfoto. Diese Bereiche weder neu generieren noch rekonstruieren, retuschieren, glätten, verschönern oder stilistisch verändern.

BEARBEITUNG
1. Stelle die Person sauber frei, besonders an Haaren, Schultern und Kleidung.
2. Entferne ausschließlich [ZU ENTFERNENDE ELEMENTE].
3. Passe Perspektive, Licht, Schatten, Farbtemperatur, Körnung und Schärfe des neuen Hintergrunds an das Originalfoto an.
4. Vermeide sichtbare Freistellungsränder, künstliche Tiefenunschärfe und unnatürliche Montageeffekte.

FORMAT
[SEITENVERHÄLTNIS UND AUFLÖSUNG]

NICHT HINZUFÜGEN
Keine Logos, Organisationsnamen, Footer, zusätzlichen Texte oder nicht verlangten Objekte.
```

### Warum diese Umsetzung funktioniert

Die unveränderlichen Bildbereiche sind positiv definiert. Die zulässige Änderung ist eng abgegrenzt. Technische Anpassungen für eine glaubwürdige Montage sind ausdrücklich beschrieben.

## Beispiel 5: Vorhandenen Prompt reparieren

### Eingabe

„Optimiere: Arbeite maximal tief, aber sehr kurz. Frag mich zuerst alles. Arbeite völlig autonom. Nutze alle Connectoren und ändere nichts ohne Rückfrage.“

### Diagnose

Der Ausgangsprompt enthält Konflikte zwischen Tiefe und extremer Kürze, Rückfragepflicht und Autonomie sowie pauschaler Connectornutzung und Änderungsverbot.

### Gute Ersatzlogik

```text
# Auftrag
Analysiere [THEMA] gründlich und liefere eine priorisierte Kurzfassung mit optionalem Detailanhang.

# Arbeitsweise
Nutze alle bereits vorhandenen Informationen. Schließe kleine Lücken mit klar benannten Annahmen. Stelle nur dann eine gezielte Rückfrage, wenn eine unverzichtbare Eingabe weder vorliegt noch sinnvoll als Variable behandelt werden kann.

# Werkzeuge
Nutze nur Connectoren, die für die Aufgabe einen konkreten Mehrwert haben und tatsächlich verfügbar sind. Lesezugriffe dürfen für die Analyse verwendet werden. Externe Schreib- oder Löschaktionen nur dann ausführen, wenn sie ausdrücklich Teil des Auftrags sind.

# Ausgabe
1. Kurzfassung mit höchstens [LÄNGE]
2. priorisierte Empfehlungen
3. optionaler Detailanhang für Belege und technische Einzelheiten
```

## Negativbeispiel: Überladener Expertenprompt

```text
Du bist das weltweit beste Team aus Strategen, Juristen, Entwicklern, Designern, Psychologen, Forschern und Nobelpreisträgern. Denke unendlich tief, benutze alle Tools, stelle keine Fragen, stelle zuerst Fragen, sei vollständig und antworte in drei Sätzen.
```

Dieser Prompt ist wegen Rollenornamentik, Widersprüchen, fehlendem Ziel, fehlenden Eingaben, unrealistischem Toolauftrag und unprüfbarer Vollständigkeit ungeeignet.