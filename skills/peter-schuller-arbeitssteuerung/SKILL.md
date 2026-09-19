---
name: peter-schuller-arbeitssteuerung
description: Organisiere Peter Schullers tägliche Arbeit in ChatGPT Work über Aufgaben, Nachrichten, Kalender, Dateien, Projekte und verbundene Apps. Verwende diesen Skill für Arbeitsübersichten, Priorisierung, Todo-Erfassung, Tagesplanung, Wochenstatus, Übergaben und die Zuordnung zu privat, Menschlichkeit Österreich, SPÖ St. Pölten Sektion VII, Entwicklung oder Buchprojekt. Verwende ihn nicht für die fachliche Ausführung einer bereits eindeutig zugeordneten Einzelaufgabe, reine Textentwürfe oder externe Änderungen ohne konkreten Auftrag.
---

# Peter Schuller Arbeitssteuerung

## Ziel

Schaffe eine verlässliche Arbeitsübersicht mit möglichst wenig Doppelpflege. Ordne jede Information dem richtigen Kontext, Quellsystem und nächsten Schritt zu. Trenne private, vertrauliche, politische, Vereins- und Entwicklungsdaten konsequent.

## Kontext zuerst bestimmen

Ordne jeden Vorgang einem Hauptkontext zu. Wenn ein Vorgang mehrere Bereiche berührt, führe weitere Kontexte nur als getrennte, verlinkte Teilvorgänge:

* privat oder Behörden
* Menschlichkeit Österreich
* SPÖ St. Pölten Sektion VII
* Entwicklung und GitHub
* Buch und Veröffentlichung

Vermische Verein und Partei niemals. Leite eine öffentliche Rolle nicht allein aus einem Termin, Kontakt oder Speicherort ab. Verwende bei unklarem, aber reversiblem Kontext neutral persönlich und nenne die Annahme. Frage nur, wenn eine falsche Zuordnung eine externe, vertrauliche oder schwer rückgängig zu machende Wirkung hätte.

## Quellen und Zielsysteme

Verwende nach Möglichkeit ein führendes System:

* bestätigter Organisationsspeicher für Organisationsdokumente
* GitHub Issues oder das bestätigte Repositorysystem für konkrete Codearbeit
* ein bestätigtes Team-Aufgabensystem für organisatorische Todos
* ChatGPT Library für persönliche KI-Artefakte ohne Repository oder festgelegten Organisationsspeicher

Erfinde kein Zielsystem. Prüfe die tatsächlich verfügbaren Apps und Verbindungen mit einer harmlosen Leseaktion, bevor du externe Daten verwendest oder eine Automation anlegst. Vermische SharePoint, Google Drive und Library nicht stillschweigend.

Eine Übersicht, Analyse oder Planung autorisiert keinen externen Write. Aufgaben, Termine, Nachrichten, Dateien oder Status nur bei einem konkreten Änderungsauftrag anlegen oder ändern. Bei unbekanntem Write-Status vor einem Retry zuerst den Zielzustand lesen.

## Private Kontenmatrix

Verwende für private Vorgänge folgende bestätigte Zuordnung:

* Gmail, Google Kalender und Google Drive: `pschuller.stp@gmail.com`
* Outlook: `schuller.peter@outlook.at`
* iCloud Mail: `schuller_peter@icloud.com`

Behandle Google Drive und den primären Google Kalender als privat. Lege dort keine Vereins-, Partei- oder Buchprojektinhalte ab, sofern Peter nicht für den konkreten Vorgang ausdrücklich diesen Speicher bestimmt.

Outlook und iCloud dürfen Nachrichten an Gmail weiterleiten, bleiben aber eigene Absenderidentitäten. Erkenne bei weitergeleiteten Nachrichten das ursprüngliche Empfängerkonto und antworte über dieses Konto, sofern eine bestätigte Senden-als-Konfiguration nicht ausdrücklich eine andere sichere Route erlaubt. Bei Kalendereinladungen aus einer Weiterleitung prüfe vor Annahme, für welche Adresse die Einladung bestimmt ist.

## Bestätigte Arbeitsverbindungen

Ordne die verbundenen Systeme standardmäßig so zu, bis Peter für einen konkreten Vorgang etwas anderes bestätigt:

* Menschlichkeit Österreich: Outlook Kalender, SharePoint und Teams über `peter.schuller@menschlichkeit-oesterreich.at`; Slack-Workspace, Make-Organisation, Stripe-Livekonto und PostHog-Organisation mit dem Namen `Menschlichkeit Österreich`
* Buch und Veröffentlichung: HubSpot-Portal `147248299` über `schuller.peter@outlook.at`
* Entwicklung und GitHub: GitHub-Konto `humanobmann` über `office@menschlichkeit-oesterreich.at`; der konkrete Repository-Kontext bleibt maßgeblich
* Design: Figma-Anmeldung über `pschuller.stp@gmail.com`; `Menschlichkeit` ist der Vereinsbereich, `Peter Schuller's team` der private Bereich
* privat: Gmail, Google Kalender, Google Drive und Google Kontakte über `pschuller.stp@gmail.com`; Outlook Mail über `schuller.peter@outlook.at`

Eine Anmeldung bestimmt nicht automatisch die öffentliche Absenderrolle. Prüfe bei Figma und GitHub zusätzlich Team, Datei oder Repository. Für SPÖ-Arbeit ist derzeit keine eigene bestätigte Speicher- oder Versandverbindung belegt; verwende deshalb keine Vereinsverbindung als Ersatz.

## Todo-Vertrag

Erfasse für jede Aufgabe:

* klarer Titel
* Hauptkontext
* Quelle oder Link
* konkrete nächste Aktion
* verantwortliche Person, sofern bekannt
* Fälligkeit nur, wenn belegt oder ausdrücklich festgelegt
* Status: offen, in Arbeit, blockiert oder erledigt
* Vertraulichkeit: intern, vertraulich oder öffentlich

Erzeuge keine neue Aufgabe ohne konkrete nächste Aktion. Erfinde keine Frist oder verantwortliche Person. Bilde zur Duplikaterkennung die Normalform aus Hauptkontext, Zielobjekt oder Projekt, normalisierter nächster Aktion und externer Referenz. Suche vor jeder externen Erstellung nach offenen oder laufenden Aufgaben mit derselben Normalform. Aktualisiere oder verlinke bei einem ähnlichen Treffer die bestehende Aufgabe, statt eine zweite anzulegen. Behandle denselben Vorgang aus E-Mail, Teams oder anderen Quellen als eine Aufgabe, wenn Ziel und nächste Aktion übereinstimmen.

## Standardabläufe

### Arbeitsübersicht

Fasse relevante Eingänge, Termine und Aufgaben nach Dringlichkeit zusammen. Zeige zuerst:

1. heute notwendig
2. blockiert oder fristkritisch
3. als Nächstes sinnvoll
4. kann warten

Nenne Quelle, Kontext und nächste Aktion. Sende nichts und ändere nichts extern, solange nur eine Übersicht verlangt wurde.

### Nachricht zu Aufgabe

Lies die Nachricht mit dem zuständigen E-Mail- oder Messaging-Skill. Extrahiere nur belegte Aufgaben, Zusagen, Fristen und offene Fragen. Zeige den Todo-Vorschlag vor einer externen Erstellung.

### Dokument oder Bericht

Verwende den passenden Dokument-, PDF-, Tabellen- oder Präsentationsskill für Struktur, Dateiintegrität und visuelle Prüfung. Verwende Peters Schreibstil nur für lesbaren Text. Speichere bestehende Repo-Inhalte nicht zusätzlich in der Library.

### Externe Kommunikation

Verwende den Ablauf:

1. Quelle und Kontext prüfen
2. Rolle bestimmen
3. Fakten prüfen
4. Entwurf erstellen
5. Peters Schreibstil anwenden
6. exakte Vorschau zeigen
7. Freigabe einholen, wenn erforderlich
8. Connector-Aktion ausführen
9. Ergebnis zurücklesen oder bestätigen

Verändere einen bereits freigegebenen Text nicht mehr vor dem Versand.

### Wiederkehrende oder bedingte Aufgabe

Wenn Peter etwas später, regelmäßig oder beim Eintritt einer Bedingung erhalten möchte, verwende den Automationsmechanismus. Prüfe vorher jede benötigte Quelle mit einer harmlosen Leseaktion. Lege Duplikatschutz, Bedeutungsschwelle, Datenschutzkontext und Zielkanal fest. Erzeuge keine Benachrichtigung, wenn bei einer Bedingungsprüfung nichts Relevantes passiert ist.

## Routing zu persönlichen Skills

* neutraler Text: `peter-schuller-schreibstil`
* Vereinskommunikation: `peter-schuller-obmann-kommunikation` plus Schreibstil
* Parteikommunikation: `peter-schuller-politiker-kommunikation` plus Schreibstil
* politische Analyse oder Faktencheck: `politik-analyse`, danach bei Bedarf Rollen-Skill und Schreibstil
* Prozessautomatisierung: `automator`
* PowerShell: `powershell-senior-expert`

Der Fachskill bestimmt Recherche, Tools, Dateiformat und Sicherheitsgrenzen. Der Rollenskill bestimmt Absenderrolle und Kontext. Der Schreibstil bestimmt Sprache und Endredaktion. Der Connector führt nur die ausdrücklich erlaubte externe Aktion aus.

## Priorität bei mehreren passenden Skills

Verwende die kleinste ausreichende Kombination und lade nicht mehrere allgemeine Orchestratoren für dieselbe Aufgabe.

1. `peter-schuller-arbeitssteuerung` ordnet nur gemischte Eingänge, Rollen, Systeme oder Prioritäten. Für eine bereits eindeutig zugeordnete Einzelaufgabe übernimmt sofort der Fachskill.
2. Ein ausdrücklich genannter Skill oder der engste Fachskill bestimmt die Ausführung.
3. Rollen- und Schreibstilskills ergänzen den Fachskill nur bei einem Kommunikationsauftrag.
4. Dokument-, Tabellen-, Präsentations- oder PDF-Skills bestimmen das Dateiformat und die technische Qualitätsprüfung.
5. Ein Connector führt ausschließlich die konkret erlaubte externe Aktion aus.

Für das Buchprojekt haben die vier `danke-fuer-nichts-*` Skills Vorrang vor allgemeinen Creator- oder Sales-Workflows. `creator-workbench` bleibt für allgemeine private Creator-Aufgaben zuständig. Superpowers gilt nur für komplexe Softwareentwicklung. Adaptive Orchestrierung, Codex Coordinator, parallele Agenten oder Worktrees nur verwenden, wenn Peter diese Arbeitsweise ausdrücklich verlangt oder die Aufgabe sie nach den geltenden Hostregeln erlaubt.

## Ausgabe

Liefere kurze Antworten direkt im Chat. Erstelle dauerhafte Berichte, Checklisten oder Projektübersichten nur dann als Datei, wenn der Umfang oder die spätere Nutzung das rechtfertigt. Jede dauerhafte Übersicht enthält Standdatum, Quellenstatus, offene Punkte und Verantwortlichkeit.

Beende Arbeitsübersichten mit höchstens fünf konkreten nächsten Aktionen. Vermeide parallele Masterlisten und unnötige Rückfragen.
