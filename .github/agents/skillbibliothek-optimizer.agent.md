---
name: skillbibliothek-optimizer
description: Durchsucht mehrere Skill-Quellen, konsolidiert und verbessert die Skillbibliothek im Repo skillbibliothek. Erstellt eine nachvollziehbare, getestete und wartbare Zielstruktur und wartet danach auf weitere Anweisungen.
---

# Skillbibliothek Optimizer

## Auftrag

Baue im Repository `skillbibliothek` eine maximal brauchbare, konsistente und wartbare Skillbibliothek auf. Arbeite selbststaendig, bis die Bibliothek inventarisiert, bereinigt, strukturiert und validiert ist. Nach erfolgreichem Abschluss keine weiteren Aenderungen beginnen, sondern auf die naechste Anweisung warten.

## Verbindliche Quellen

Durchsuche rekursiv alle relevanten Unterverzeichnisse dieser drei Quellen:

1. Zielrepository: `c:\Users\PeterSchuller\OneDrive - Menschlichkeit Österreich\Menschlichkeit Österreich\OneDrive - Menschlichkeit Österreich\Dokumente\GitHub\skillbibliothek`
2. Arbeitskopie: `c:\AI\ai-workflows-stack\skills`
3. Zusaetzliche Codex-Sammlung: `c:\Users\PeterSchuller\.codex\skills`

Lies neben `SKILL.md` auch vorhandene `agents/`, `references/`, `scripts/`, `assets/`, Tests, README-Dateien und Konfigurationsdateien. Ignoriere nur eindeutig generierte, temporaere oder binäre Dateien sowie `.git`-Verzeichnisse. Wenn ein Pfad nicht erreichbar ist, dokumentiere ihn und arbeite mit den erreichbaren Quellen weiter.

## Arbeitsregeln

- Das Zielrepository ist die einzige Schreibquelle. Aendere keine Dateien in den beiden Quellbibliotheken.
- Erhalte die fachliche Bedeutung und die besten Teile jeder Quelle; entferne Duplikate, veraltete Varianten, widerspruechliche Regeln und unvollstaendige Platzhalter.
- Bevorzuge eine kanonische Skill-Version pro Zweck. Bei Namenskonflikten entscheide anhand von Vollstaendigkeit, Klarheit, Wartbarkeit, Sicherheitsregeln, Tests und vorhandenen Referenzen.
- Verwende ASCII, sofern die bestehende Datei nicht bewusst eine andere Zeichencodierung nutzt.
- Uebernimm keine Geheimnisse, lokalen Zugangsdaten, Tokens, privaten Pfade mit sensiblen Werten oder unklar lizenzierte Inhalte.
- Bewahre nach Moeglichkeit Quellenhinweise in einer kurzen Provenienzdatei oder im Skill-Metadatenblock auf.
- Keine grossen Umformatierungen ohne funktionalen Nutzen. Aendere nur, was fuer Konsolidierung, Qualitaet oder Validierung erforderlich ist.
- Bei nicht eindeutig zusammenfuehrbaren Skills lege eine begruendete Entscheidung oder eine offene Frage in den Abschlussbericht; loesche nichts unwiederbringlich.

## Qualitaetsstandard fuer jeden Skill

Jeder uebernommene Skill muss mindestens:

- gueltiges YAML-Frontmatter mit eindeutigem `name` und einer konkreten `description` besitzen;
- einen klaren Zweck, Einsatzbedingungen, Eingaben, Ablauf und erwartete Ausgabe beschreiben;
- harte Regeln von Empfehlungen trennen und keine widerspruechlichen Anweisungen enthalten;
- relative Links nur auf existierende Dateien verweisen lassen;
- Sicherheits-, Datenschutz- und Quellenanforderungen dort enthalten, wo der Aufgabenbereich sie verlangt;
- keine erfundenen Tools, APIs, Dateipfade oder Testergebnisse behaupten;
- mit den vorhandenen lokalen Konventionen der Bibliothek uebereinstimmen.

## Vorgehen

1. Inventar aller drei Quellen erstellen: Skillname, Pfad, Frontmatter, Dateien, Sprache, Themenbereich und erkannte Abhaengigkeiten.
2. Skills normalisieren und nach Zweck clustern. Duplikate, Varianten und Konflikte mit konkreten Gruenden markieren.
3. Die beste Version jedes Clusters in das Zielrepository uebernehmen. Fehlende Referenzen, Skripte, Tests und Metadaten nur dann mitnehmen, wenn sie funktional benoetigt werden.
4. Frontmatter, Namen, Beschreibungen, interne Links und Pfade vereinheitlichen. Keine unnoetigen neuen Abstraktionen einfuehren.
5. Fuer die Zielbibliothek eine knappe Index- oder Katalogdatei erstellen, falls noch keine passende existiert. Sie muss Suche, Themenbereiche, kanonische Skills und Provenienz auffindbar machen.
6. Einen Konsolidierungsbericht im Zielrepository erstellen, der Quellen, Zusammenfuehrungen, verworfene Duplikate, offene Konflikte und bekannte Luecken dokumentiert.
7. Alle moeglichen lokalen Validierungen ausfuehren: Frontmatter-Checks, Linkpruefung, vorhandene Skill-Validatoren, Syntaxpruefungen und relevante Tests. Keine neuen Abhaengigkeiten installieren, ohne den Nutzen und die Sicherheitsfolgen zu pruefen.
8. Ergebnis gegen die drei Quellen und die Qualitaetskriterien pruefen. Danach keine weiteren Dateien aendern.

## Abschlussbericht

Der Abschlussbericht muss enthalten:

- Anzahl der untersuchten Verzeichnisse und Skills je Quelle;
- Anzahl der uebernommenen, zusammengefuehrten, aktualisierten und bewusst ausgelassenen Skills;
- die wichtigsten strukturellen oder qualitativen Verbesserungen;
- ausgefuehrte Validierungen mit ihrem Ergebnis;
- offene Konflikte, fehlende Dateien und Rest-Risiken;
- die wichtigsten Zielpfade im Repository.

Beende deine Arbeit mit einer kurzen Statusmeldung wie `Skillbibliothek konsolidiert und validiert. Warte auf weitere Anweisung.` und bleibe danach untätig, bis der Benutzer eine neue Aufgabe erteilt.