# Plugin-Masterplan

Stand: 2026-10-06

## Zielbild

Die private Skillbibliothek wird als **eine kanonische GitHub-Quelle** gepflegt und in **elf thematische Workspace-Plugins** gebaut. Externe Provider-Plugins und Connectoren bleiben getrennt, wenn sie eigene Daten, Aktionen oder spezialisierte Engines bereitstellen.

Aktueller verifizierter Zustand:

- 122 kanonische Skills
- 11 private Workspace-Bundles
- jeder kanonische Skill genau einem Bundle zugeordnet
- keine fehlenden oder doppelt gebündelten Skills
- alle elf Workspace-Plugins entsprechen den in `scripts/build_plugin_bundles.py` definierten Versionen
- Workspace-Plugins bleiben `PRIVATE`

## Die elf privaten Kernplugins

| Bundle | Rolle | Skills | Version |
|---|---|---:|---:|
| Research & Verification | Recherche, Faktenprüfung, Quellen-, Daten- und Rechtsrouting | 10 | 1.0.2 |
| OSINT & Investigations | OSINT, Forensik, Firmen-, Personen-, Domain- und Medienrecherche | 28 | 1.0.0 |
| Social Content | Plattformcontent, Algorithmen, Humanisierung, Schreibprofile, Content-System | 12 | 1.0.2 |
| Design & Visual | Designrouting, Editorialgrafik, Affinity, PDF-Redesign, visuelle QA | 6 | 1.0.1 |
| Software Development | Entwicklung, GitHub, CI, Browsertests, UI Engineering, technische Spezifikationen | 23 | 1.0.1 |
| Security & Platform | Security, SRE, MLOps, FinOps, Cloud- und Agent-Governance | 11 | 1.0.0 |
| Politik Österreich | Politikanalyse, Parlament, Framing, Briefings, Laimer-Projekt und Wochendossier | 7 | 1.0.2 |
| Publishing & Writing | Dokumententwicklung, Sachbuch, SEO und PDF-Publishing | 5 | 1.0.0 |
| Automation & Workflows | Automationen, Arbeitssteuerung, Workspace-Organisation, Plugin-Kontrolle, Handoffs, SOPs | 15 | 1.0.3 |
| Danke für nichts | Projektplugin für das Buchprojekt | 4 | 1.0.0 |
| Vereinskommunikation | Vereinsrolle Menschlichkeit Österreich | 1 | 1.0.0 |

Die kanonische Bundle-Definition liegt in `scripts/build_plugin_bundles.py`. Diese Tabelle ist Dokumentation; bei Abweichung gilt der validierte Build als technische Quelle.

## Router statt weiterer Mega-Plugins

Neue Fachbereiche werden nur dann als eigenes privates Plugin angelegt, wenn ein echter separater Ausführungsbereich entsteht. Reines Routing bleibt in vorhandenen Kernplugins.

Aktuelle Router:

- `research-source-router`: wählt die passende Evidenzquelle.
- `data-analysis-router`: trennt Data Analytics, Spreadsheet-Arbeit, Google Sheets und Open-Data-Erhebung.
- `legal-at-eu-router`: trennt österreichisches/EU-Recht, Judikatur, parlamentarische Materialien und politische Bewertung.
- `design-workflow-router`: wählt den passenden visuellen Produktionsweg.
- `plugin-portfolio-control`: steuert Konsolidierung, Migration, Versionierung und Entfernung.
- `workspace-organization`: organisiert Chats, Projekte, Dateien, Dubletten und Workflowdokumente.
- `core-routing`: hält die bibliotheksweite Intent-Zuordnung.

## Externe Spezialisten bleiben extern

Ein Provider-Plugin soll **nicht** in ein privates Bundle kopiert werden, wenn sein eigentlicher Wert im Connector, in proprietären Daten oder in einer spezialisierten Laufzeit liegt.

Beispiele:

- **Legal Data Hunter**: spezialisierte Rechtsrecherche und verifizierte Rechtsfundstellen.
- **GitHub**: Repository-, PR-, Actions- und Source-Control-Zugriff.
- **Google Drive / Sheets**: verbundene Dokument- und Tabellenquelle sowie präzise Schreibaktionen.
- **Vercel**: provider-spezifische Deployments, Logs und Plattformfunktionen.
- weitere verbundene CRM-, Messaging-, Analytics- oder Designprovider bleiben getrennt, solange sie echte externe Fähigkeiten liefern.

Die private Bibliothek darf solche Provider **routen**, aber nicht deren Connectorfunktion imitieren.

### Data Analytics

Der `data-analysis-router` darf Data-Analytics-Workflows verwenden, wenn diese in der aktuellen Hostoberfläche tatsächlich verfügbar sind. Sichtbare Data-Analytics-Skills allein beweisen keine installierte App. Fehlt die Laufzeit, wird auf vorhandene Spreadsheet-, Google-Sheets-, Open-Data- oder andere belegte Datenpfade ausgewichen.

## Sichtbarer Skill ist nicht gleich installierte App

Ein URI wie `skills://plugins/<paket>/<skill>` beweist nur, dass der Host den Skill zur Discovery bereitstellt. Daraus darf **nicht** geschlossen werden, dass:

- das Paket als App installiert ist,
- es eine löschbare Workspace-Plugin-ID besitzt,
- der sichtbare Paketname dem User-facing Plugin-Namen entspricht,
- ein Uninstall mit dem Paketnamen zulässig ist.

Für Installationsstatus gilt Plugin Management. Für eigene private Workspace-Plugins gilt zusätzlich Plugin Creator mit der exakten Backend-ID und aktuellen Release-ID.

## Bereits konsolidierte Standalones

| Ehemaliger Bereich | Ziel |
|---|---|
| monolithische Skillbibliothek | elf thematische Kernbundles |
| Peter-Schuller-Schreibstil Standalone | Social Content |
| Humanizer DE Natural Standalone | Social Content |
| Laimer-Wochendossier Standalone | Politik Österreich |
| Argos-Kernfunktionen | Social, Development und Automation |
| Workspace Organizer Logik | Automation / `workspace-organization` |
| Research Plugin Methodik | keine Kopie: bestehende Research-, Verification-, Handoff- und Specification-Skills besitzen die Funktion bereits |

### Claus Argos

`claus-argos-skill-os` kann weiterhin als sichtbares Skillpaket erscheinen. Plugin Management meldet diesen Namen jedoch als **nicht installiert** und es liegt keine verifizierte Backend-ID eines löschbaren Workspace-Plugins vor.

Folge: nicht raten und nicht löschen. Die relevanten Funktionen sind bereits kanonisch migriert; der sichtbare Rest wird als Host-/Discovery-Artefakt behandelt, bis eine eindeutige App-Identität vorliegt.

## Null-Verlust-Gate vor jeder Entfernung

Ein Plugin darf erst entfernt werden, wenn alle Punkte erfüllt sind:

1. exakte zu entfernende Plugin-Identität ist belegt;
2. Ersatzskill oder Ersatzworkflow existiert;
3. funktionale Abdeckung wurde geprüft;
4. References, Scripts, Assets und Agent-Metadaten wurden berücksichtigt;
5. Zielplugin ist installiert;
6. Zielrelease wurde zurückgelesen und der Ersatz darin verifiziert;
7. reproduzierbare GitHub-Quelle oder historischer Release existiert;
8. die Entfernung ist vom Nutzer autorisiert.

Bei `not_installed`, unklarer ID, Scope-Konflikt oder fehlender Schreibberechtigung: **keinen Ersatzwert raten und nicht löschen**.

## Release-Prozess

Für Änderungen an privaten Kernplugins gilt:

1. Änderung zuerst in `humanobmann/skillbibliothek`.
2. Eigener Branch.
3. Skill-, Routing- und Katalogdaten synchron ändern.
4. Bundle-Version nur für betroffene Plugins erhöhen.
5. `Skill library validation` erfolgreich ausführen.
6. `Build Plugin Bundles` erfolgreich ausführen.
7. Pull Request erst danach mergen.
8. Das CI-Artefakt des betroffenen Bundles verwenden.
9. Vor Update die aktuelle Workspace-Release-ID lesen.
10. Plugin mit `expected_release_id` geschützt aktualisieren.
11. Version und geänderte Skilldateien aus dem installierten Release zurücklesen.
12. Erst danach einen ersetzten Standalone-Kandidaten entfernen.

## Wartungsregeln

- Ein Skill hat genau einen kanonischen Ordner im Repository.
- Ein kanonischer Skill gehört genau zu einem privaten Bundle.
- Gleiche Aufgabe nicht unter mehreren Namen duplizieren.
- Router klein halten; Fachlogik im engsten zuständigen Skill belassen.
- Provider-Connectoren nicht nachbauen.
- Bundle-Displayname, internen Paketnamen und Backend-ID gedanklich getrennt halten.
- Backend-IDs und Workspace-IDs nicht als öffentliche Architekturkonstante dokumentieren; sie werden zur Laufzeit verifiziert.
- Neue Skills nur aufnehmen, wenn sie eine echte wiederverwendbare Aufgabe oder klare Routinglücke schließen.
- Öffentliche/global sichtbare Skills nicht allein wegen Discovery-Überlappung deinstallieren.

## Definition of Done

Der Pluginbestand gilt als konsistent, wenn:

- Katalog, Repository-Tree und README dieselbe Skillanzahl ausweisen;
- die Bundle-Union exakt der kanonischen Skillmenge entspricht;
- kein Skill fehlt oder in mehreren Bundles liegt;
- jedes private Workspace-Plugin die erwartete Version trägt;
- alle Kernplugins privat im vorgesehenen Workspace liegen;
- ersetzte Standalones nur nach dem Null-Verlust-Gate entfernt wurden;
- verbleibende externe Plugins einen belegten Provider- oder Spezialnutzen besitzen.
