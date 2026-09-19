---
name: danke-fuer-nichts-content-seo
description: Prüfe und optimiere Landingpage, Content, Conversion und organische Auffindbarkeit für die private Autorenkampagne „Danke für nichts“. Verwende den Skill für Live- und CMS-Audits, mobile Darstellung, CTA-Hierarchie, Pressebereich, SEO-Metadaten, Book-Strukturdaten, Alt-Texte, interne Links, Consent, UTM-Tracking, Contentcluster und handlungsrelevante KPIs. Verwende ihn nicht für Publishing-Fakten ohne Contentbezug, Outreach-Versand oder ungeprüfte öffentliche Änderungen.
---

# Danke für nichts Content und SEO

## Ziel und Aktionsgrenze

Vor jeder Optimierung festlegen:

* primäre Zielgruppe: Leserschaft, Presse, Buchhandel, Veranstalter oder Partner
* primäre Conversion und höchstens zwei Sekundärpfade
* konkrete Seite, Sprache und Zielmarkt
* aktuelle Buchdatenquelle
* erlaubte Aktion: Audit, lokaler Entwurf, CMS-Entwurf oder Veröffentlichung
* Ausgangszustand und Erfolgskriterium

Eine Analyse oder ein Änderungsauftrag autorisiert keine Veröffentlichung. Liveänderung erst nach Vorschau und ausdrücklicher Freigabe.

## Rollen- und Datenregel

Die Seite ist Teil der privaten Autorenkampagne. Keine Vereins-, SPÖ- oder Organisationskonten, Marken, Verteiler oder Einwilligungen still übernehmen.

Publisher- und formatbezogene Buchdaten ausschließlich aus `danke-fuer-nichts-publishing-audit` beziehen. `gelistet`, `bestellbar`, `lagernd` und `im Sortiment` nicht gleichsetzen.

## CTA-Hierarchie

| Zielgruppe | Primärziel | mögliche Sekundärziele |
|---|---|---|
| Leserschaft | konkrete Ausgabe oder Bezugsquellen wählen | Leseprobe, Autorenkontakt |
| Presse | aktuelle Presseunterlagen | Interview oder Rezensionsexemplar anfragen |
| Buchhandel | verifizierte ISBN- und Bestellinformationen | Lesung oder Gespräch anfragen |
| Veranstalter | Gesprächsformat anfragen | Buchprofil, Autorenprofil |
| gemischt | Buch und Bezugsquellen | klar getrennte Presse- und Veranstalterpfade |

Nicht mehrere gleich starke Primärbuttons im Hero verwenden. Formatkarten brauchen je Format sichtbaren Preis, ISBN, Unterschied und eigenen klaren CTA. Ein generischer Händlerbutton darf die Formatwahl nicht ersetzen.

## Live- und CMS-Audit

Immer beide Zustände unterscheiden:

1. aktuelle CMS-Fassung mit Modul- und Linkwerten
2. veröffentlichte Seite in frischer, nicht eingeloggter Sitzung

Abdeckung dokumentieren. Browser- oder Bot-Sperre als `nicht prüfbar` führen.

Prüffelder:

* URL, Seitentitel, Meta-Description, Canonical, Sprache
* Open Graph, Social Preview und Vorschaubild
* genau eine H1 und logische Überschriftenfolge
* Hero, Nutzenversprechen und sichtbare Ausgabeinformation
* Preise, ISBN, Kaufwege und Linkziele
* Presse-PDF, Dateistand, Kontakt und Rechte
* Autorenfoto, Ladeverhalten, Alt-Text und Bildrechte
* Desktop, Mobil und mindestens ein schmales Zwischenergebnis
* Kartenabstände, Preiszeilen, Buttonflächen und Zeilenumbrüche
* Formulare, Double Opt-in und Bestätigungspfad
* Cookiebanner mit Einstellungen, Akzeptieren und Ablehnen
* Impressum, Datenschutz, Footer und doppelte Rechtelinks
* Analytics, Ereignisse und UTM-Weitergabe
* Ladezeit, visuelle Stabilität und auffällige Blocker

Mobile Qualität nicht aus Desktopdarstellung oder CSS allein ableiten. Tatsächliche Viewports prüfen und Screenshots dokumentieren.

`scripts/audit_landing_snapshot.py` für gespeicherte HTML-Snapshots verwenden. Das Skript ersetzt keine visuelle oder interaktive Prüfung.

## Informationsarchitektur

Empfohlene Reihenfolge für eine gemischte Buchseite:

1. Hero mit Titel, Nutzen und Primär-CTA
2. knappes Buchversprechen und Methode
3. Themen und Zielgruppe
4. Formatwahl mit Softcover und Hardcover
5. Kaufweg über tredition oder bestätigten Buchhandel
6. Leseprobe, wenn aktuell und freigegeben
7. Presse- und Veranstalterpfad
8. Autor mit geklärtem Bildnachweis
9. Kontakt
10. einmaliger Footer mit Rechtelinks

Große dekorative Leerflächen oder überdimensionierte Überschriften nur verwenden, wenn sie Mobilansicht und Conversion nicht beeinträchtigen.

## SEO-Basis

1. Suchintention aus Titel, Autor, Sozialstaat, Österreich und konkreten Buchthemen ableiten.
2. Seitentitel und H1 unterschiedlich, aber konsistent formulieren.
3. Meta-Description als überprüfbares Nutzenversprechen schreiben.
4. eine kanonische URL verwenden.
5. interne Links zu Autor, Presse, Leseprobe und relevanten Analysen schaffen.
6. Bilder beschreibend benennen und mit sinnvollem Alt-Text versehen.
7. indexierbare Textinhalte statt rein grafischer Aussagen verwenden.
8. Indexierung und Snippet live prüfen, wenn eine aktuelle Bewertung verlangt ist.

Keywordvolumen oder Ranking nicht ohne aktuelle Daten behaupten. Empfehlungen mit relevantem Zeitbezug oder Plattformregeln aktuell recherchieren.

## Strukturierte Daten

Pro aktivem Buchformat `Book`-Daten aus der bestätigten Edition ableiten. Mindestens:

* `name`
* `author`
* `isbn`
* `bookEdition`
* `bookFormat`
* `inLanguage`
* `numberOfPages`
* `url`
* `image`
* `publisher`, wenn bibliografisch bestätigt

Preis- oder Verfügbarkeitsdaten nur ergänzen, wenn das verwendete Schema und die konkrete Handelsquelle sie tragen. JSON-LD syntaktisch validieren und mit sichtbarem Seiteninhalt abgleichen. Kein erfundener Rating- oder Reviewwert.

## Content-System

Ein Kernthema pro Woche reicht. Daraus nur Formate ableiten, die einen eigenen Nutzen haben:

* eine quellenbasierte Hauptanalyse
* ein kurzer visueller oder textlicher Auszug
* ein Gesprächs-, Newsletter- oder Medienwinkel

Redaktionelle Standardstruktur:

`Frage → Primärquelle → Kontext → stärkstes Gegenargument → Bewertung → Buchbezug → nächste Handlung`

Fakt, Interpretation und politische Position sichtbar trennen. Zeitbezogene Statistiken vor Veröffentlichung neu prüfen. Keine täglichen Serien oder kanalübergreifende Vervielfachung ohne Kapazität und Messsignal.

## Presse- und Downloadbereich

Nur aktuelle, freigegebene und editionsrichtige Dateien verlinken. Vor Release prüfen:

* Dateiname, Datum, Seitenzahl und Prüfsumme
* korrekter privater Medienkontakt
* Cover- und Formatzuordnung
* geklärter Bildnachweis und Nutzungsrechte
* klickbare Links und barrierearme Lesbarkeit

Ein offener Rechtehinweis macht die Datei nicht versandbereit. Eine Dateibezeichnung wie `CURRENT` ist kein Qualitätsbeleg.

## Formulare und Consent

Newsletter erst aktivieren, wenn Zweck, Frequenz, Rechtsgrundlage, Datenschutzhinweis, Double Opt-in, Abmeldung und Einwilligungsnachweis vollständig funktionieren.

Cookieprüfung in frischer Sitzung:

1. nur notwendige Cookies
2. Ablehnen oder nur notwendige
3. Einstellungen
4. Akzeptieren
5. Verhalten nach erneuter Auswahl

Nicht notwendiges Tracking darf vor Zustimmung nicht ausgelöst werden. Technische und rechtliche Prüfung getrennt dokumentieren.

## Tracking und KPIs

UTM-Schema:

* `utm_source`: konkrete Quelle
* `utm_medium`: Kanalart
* `utm_campaign`: stabile Kampagnenkennung
* `utm_content`: konkretes Asset oder CTA

Händlerklicks auf der eigenen Seite messen. Externe Händler müssen UTM-Parameter nicht bewahren.

Priorisierte Kennzahlen:

* eindeutige Landingpagebesuche
* Klickrate zur Ausgabe oder zum Händler
* Presse- und Veranstaltungsanfragen
* bestätigte Newsletteranmeldungen, falls aktiviert
* organische Suchzugriffe und indexierte Seiten
* technische Fehler

Antworten, Interviews, Rezensionen und Veranstaltungen aus dem Outreach-Ledger ergänzen. Likes und Impressionen nur im Kontext auswerten.

## Releaseworkflow

1. Baseline und Screenshot sichern.
2. CMS-Entwurf oder lokale Fassung erstellen.
3. Buchdaten und Assets gegen Publishing-Audit prüfen.
4. Desktop, Mobil, Links, Downloads, Consent und strukturierte Daten testen.
5. vollständige Änderungsvorschau zeigen.
6. ausdrückliche Veröffentlichungsfreigabe einholen.
7. veröffentlichen.
8. Live-Readback in frischer Sitzung durchführen.
9. Fehler bei kritischem Gate zurückrollen oder sofort korrigieren.
10. Änderungslog und Messbaseline aktualisieren.

Die vollständige Prüfliste steht in `references/release-checklist.md`.

## Autonomie und Definition of Done

Lesen, Audit, Entwürfe, Metadatenvorschläge, JSON-LD-Entwurf und Redaktionsplanung autonom durchführen. Öffentliche Änderung, Formularänderung, Trackinginstallation oder Veröffentlichung nur bei konkretem Auftrag und nach Vorschau.

Eine Seite ist `BEREIT`, wenn:

1. Buchdaten und Dateien bestätigt sind
2. Zielgruppe und CTA eindeutig sind
3. Mobil- und Desktopprüfung bestanden sind
4. Bilder, Links und Downloads funktionieren
5. genau ein Footer und konsistente Rechtelinks vorliegen
6. Consent und Formulare erwartungsgemäß arbeiten
7. Metadaten und strukturierte Daten valide sind
8. Erfolgsmessung und Ausgangswert dokumentiert sind

Bei fehlendem Zugriff eine umsetzbare Änderungsliste liefern und Umsetzung nicht behaupten.
