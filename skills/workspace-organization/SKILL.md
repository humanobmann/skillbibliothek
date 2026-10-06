---
name: workspace-organization
description: Inventarisiere und ordne erreichbare Chats, Projekte, Dateien und Workflowdokumente mit kontrollierter Autonomie. Verwende den Skill für Workspace-Aufräumen, Chat-/Projekt-Zuordnung, Dublettenprüfung, Konsolidierung verstreuter Entscheidungen, Projektindizes sowie Reviews von GOAL.md, WORKFLOW.md, AGENTS.md und ähnlichen Arbeitsanweisungen. Nutze nur tatsächlich verfügbare Connectoren und stabile IDs, trenne private, Vereins-, Partei-, parlamentarische, Entwicklungs- und Buchkontexte, und führe nur nachweislich reversible risikoarme Ordnungsaktionen selbstständig aus.
---

# Workspace Organization

## Auftrag

Ordne erreichbare Arbeitsbestände, ohne Kontext, Rechte oder Source of Truth zu beschädigen. Dieser Skill organisiert Struktur und Metadaten; er ersetzt weder fachliche Inhaltsarbeit noch Tagespriorisierung.

Für Tagesplanung, Todo-Steuerung und gemischte Eingänge verwende `peter-schuller-arbeitssteuerung`. Für Handoffs zwischen Sitzungen verwende `work-handoff`.

## Ablauf

1. Scope und erlaubte Quellen bestimmen.
2. Pro Quelle zuerst Metadaten inventarisieren, erst danach entscheidungsrelevante Inhalte lesen.
3. Für jedes Objekt soweit verfügbar erfassen: Provider, stabile ID, Pfad oder Link, Typ, Titel, Kontext/Projekt, Eigentum, Zugriffskreis, Version, Änderungszeit und Lesestatus.
4. Status nur aus Evidenz setzen: `verified`, `partial`, `metadata_only`, `not_connected`, `blocked_by_policy`, `unsupported` oder `error`.
5. Logische Zielstruktur und Zuordnungsplan erstellen.
6. Nur eindeutig reversible, risikoarme Änderungen ausführen, wenn der Nutzer ausdrücklich organisiert oder aufgeräumt haben will.
7. Vor jedem Write den aktuellen Zustand erneut lesen; nach dem Write ID, Version, Pfad und Inhalt soweit möglich zurücklesen.
8. Irreversible, zugriffsverändernde, vertraulichkeitsrelevante oder weitreichende Änderungen als Entscheidungspunkt vorlegen.

## Kontext- und Zugriffsgrenzen

Private, Vereins-, Partei-, parlamentarische, Entwicklungs- und Buchkontexte niemals still zusammenführen. Speicherort oder Login beweist keine Absenderrolle.

Keine Inhalte, Zusammenfassungen oder Metadaten in einen breiteren Zugriffskreis verschieben. Bestehende ACLs nicht allein aus Ordnernamen ableiten.

Ein verfügbarer Connector beweist weder erfolgreiche Anmeldung noch Schreibberechtigung. Vor Schreibaktionen die konkrete Fähigkeit durch einen harmlosen Read und die tatsächliche Toolantwort belegen.

## Zuordnung und Dubletten

Automatische Verschiebung oder Umbenennung nur bei mindestens zwei voneinander unabhängigen Zuordnungssignalen, z. B. Projekt-ID plus Quellordner. Ähnlicher Titel allein genügt nicht.

Unterscheide:
- dasselbe Provider-Objekt,
- identische Dateibytes,
- unterschiedliche Versionen,
- nur semantisch ähnliche Inhalte.

Keine Dublette automatisch löschen. Identische Bytes können unterschiedliche Rechte, Referenzen oder Aufbewahrungsanforderungen haben.

Chats nicht als nativ verschmolzen darstellen. Bei verwandten Chats höchstens eine quellenverlinkte Zusammenfassung oder einen Projektindex erzeugen.

## Workflowdateien

Bei GOAL-, README-, WORKFLOW-, STATUS-, AGENTS-, CLAUDE-, SKILL- und CI-Dateien:

1. bestehende Autorität, Scope und Source of Truth bestimmen;
2. Widersprüche, Dopplungen, veraltete Anweisungen und tote Verweise markieren;
3. Bedeutung, Freigaben, offene Entscheidungen und Sicherheitsgrenzen erhalten;
4. Wiederholungen nur dann konsolidieren, wenn keine Anforderung verloren geht;
5. produktive Automation, CI oder Zieldefinition nicht als Nebenwirkung eines Aufräumlaufs verändern.

Bei Repository-Arbeit an den zuständigen Entwicklungsworkflow übergeben.

## Schreibpakete

Persistente Änderungen in kleinen, überprüfbaren Paketen ausführen. Vorherzustand und Wiederherstellungsweg festhalten, wenn das Zielsystem dies unterstützt.

Bei Timeout oder unklarem Ergebnis zuerst Zielzustand lesen statt den Write blind zu wiederholen. Bei Versionskonflikt, unerwarteter Rechteänderung oder unklarem Ziel nur den betroffenen Teil stoppen.

## Ausgabe

Berichte:

1. inventarisierter Scope und Abdeckung,
2. belegte Zuordnungen,
3. tatsächlich ausgeführte und verifizierte Änderungen,
4. ungelöste Dubletten oder Konflikte,
5. Zugriffs- und Toollücken,
6. Entscheidungen mit konkreten Optionen,
7. nächsten sicheren Fortsetzungspunkt.

Keine Vollständigkeitsquote behaupten, wenn der Gesamtumfang einer Quelle nicht zuverlässig bekannt ist.
