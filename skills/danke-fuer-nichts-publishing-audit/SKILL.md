---
name: danke-fuer-nichts-publishing-audit
description: Prüfe Editionen, Buchdaten, Druckdateien, Presseunterlagen und öffentliche Handelslistungen für „Danke für nichts“. Verwende den Skill für Canonical Book Data, tredition- und KDP-Abgrenzung, formatbezogene ISBN, Preise, Seiten, Beschnitt, Farbstatus, Händlerlinks, Listung, Bestellbarkeit, Lagerstatus, Lieferzeit, Rabatt, Remission und Buchhandelsfreigabe. Verwende ihn nicht für Outreach-Versand, allgemeine Contentplanung oder unbestätigte Änderungen bei Publishern und Händlern.
---

# Danke für nichts Publishing Audit

## Grundsatz

Edition, Format, Datei und Handelsstatus nie vermischen. Jede Aussage braucht einen eindeutigen Geltungsbereich und eine sachlich führende Quelle.

`gelistet`, `bestellbar`, `auf Bestellung produziert`, `lieferbar`, `lagernd`, `im Regal` und `Sortimentszusage` sind verschiedene Zustände. Die Evidenzregeln stehen in `references/evidence-model.md`.

## Auditvertrag

Vor Beginn festhalten:

* Stichtag und Zielmarkt
* zu prüfende Editionen und Formate
* bekannte Identifikatoren
* bereitgestellte Dateien und fehlende Dateien
* Publisher-, Händler- und Kommunikationsquellen
* gewünschte Aktion: Audit, lokale Korrektur, Publisheränderung oder Veröffentlichung

Eine Analyse autorisiert keine Änderung bei tredition, Amazon, Händler, CMS oder Dateiablage.

## Canonical Book Data

Pro Edition und Format einen eigenen Datensatz führen:

| Gruppe | Pflichtfelder |
|---|---|
| Identität | Titel, Untertitel, Autor, Sprache, Auflage, Ausgabebezeichnung |
| Veröffentlichung | Publisher oder Eigenverlag, Distribution, Veröffentlichungsdatum, Status |
| Produkt | Bindung, Trimformat, Beschnitt, Papier, Farbstatus, Seiten im PDF, Produktionsseiten |
| Identifikatoren | ISBN je Format, ASIN falls relevant, interne Projekt-ID |
| Handel | Preis je Markt, Steuerkontext, Produktlink, Katalog, Bestellbarkeit, Lagerstatus, Lieferzeit |
| Konditionen | Rabatt, Remission, Mindestmenge, Rezensionsexemplare, Autorenpreis |
| Assets | Innen-PDF, Cover, EPUB, Leseprobe, Pressemappe, Landingpage, Versionsdatum, Prüfsumme |
| Rechte | Text, Cover, Autorenfoto, Grafiken, Zitate und Downloadfreigabe |

Alte KDP- und neue tredition-Ausgabe als getrennte Editionszeilen führen. Softcover und Hardcover als getrennte Formatzeilen führen. Ein formatbezogener Beleg darf nicht auf das andere Format übertragen werden.

## Quellenhierarchie je Claim

* aktuelle Publisherquelle führt ihren öffentlichen Produktstatus, Preis und die von ihr ausgelieferten Metadaten
* konkrete Händlerseite führt ausschließlich die Darstellung dieses Händlers
* direkte aktuelle Publisherkommunikation oder Vertrag führt nicht öffentliche Konditionen
* finale Produktionsdatei führt tatsächlichen Inhalt, PDF-Seitenzahl, eingebettete ISBN und technische Ausführung
* Freigabedokument führt Medienkontakt und Rechte
* Mailantwort führt nur die konkrete Zusage des Absenders

Widersprüche nicht durch pauschale Rangfolge verstecken. Edition, Format, Definition, Quelle, Quelldatum und Prüfdatum vergleichen.

## Evidenzstatus

* `BESTÄTIGT`: für den exakt benannten Claim durch führende Quelle belegt
* `TEILBESTÄTIGT`: nur für ein Format, eine Plattform oder eine Stichprobe belegt
* `OFFEN`: nicht belegt
* `WIDERSPRÜCHLICH`: belastbare Quellen weichen ab
* `VERALTET`: gehört zu früherer Edition oder früherem Stand
* `NICHT VERWENDEN`: darf nicht in aktiver Kommunikation erscheinen

Keine Händler- oder Distributionsvollständigkeit behaupten, wenn Suchindex, Login, Bot-Schutz oder Stichprobe den Zugriff begrenzen.

## Workflow

1. Editionen und Formate inventarisieren.
2. Identifikatoren normalisieren und Prüfziffern plausibilisieren.
3. Dateien mit Größe, Änderungsstand und SHA-256 registrieren.
4. Produktionsdateien technisch und visuell prüfen.
5. Eingebettete Buchdaten per Textauszug oder OCR mit Canonical Book Data vergleichen.
6. Pressemappe und Landingpage gegen genau diese Editionen prüfen.
7. Publisher- und Händlerquellen je ISBN abfragen.
8. Handelszustand pro Plattform klassifizieren.
9. nicht öffentliche Konditionen aus aktueller Kommunikation erfassen.
10. Widerspruchsmatrix, Dateiregister und Freigabestatus erstellen.

## Druckdatei-Audit

Für jede Innen- und Coverdatei prüfen:

* Dateityp, Größe, Prüfsumme, Seitenzahl und PDF-Version
* MediaBox, Trimformat und Beschnitt je Seite
* Hoch- und Querformat, Rotation und unerwartete Seitengrößen
* Text-PDF oder gerasterte Seiten
* Bildauflösung, Farbräume, Kompression und auffällige Ausreißer
* Schriften und Einbettung, soweit Textobjekte vorhanden sind
* Titelblatt, Impressum, ISBN, Copyright, Publisher- und Kontaktdaten
* Inhaltsverzeichnis, Seitenfolge, Vakatseiten und Schlussseiten
* Abbildungen, Kästen, Tabellen, Beschnitt, Bundsteg und Lesbarkeit

`scripts/audit_pdf_package.py` für die technische Basis verwenden. Danach visuell:

1. Kontaktübersicht aller Seiten rendern.
2. Titelseiten, Impressum, Inhaltsverzeichnis, erste Textseiten, Seiten mit hoher Bilddichte, Teilanfänge und Schlussseiten hochauflösend prüfen.
3. auffällige Seiten einzeln prüfen.
4. Bei gerastertem PDF OCR nur als Hilfsmittel verwenden. Visuelle Prüfung bleibt erforderlich.

PDF-Seitenzahl, römisch oder arabisch gedruckte Seitenzahl und vom Publisher ausgewiesene Produktionsseiten getrennt dokumentieren.

Eine monochrome Innen-PDF belegt keine teilweise farbige Hardcover-Innenseite. Dafür die konkrete Hardcover-Datei oder Publisherkonfiguration verlangen.

## Pressemappe

Seite für Seite prüfen:

* Titel, Untertitel, Auflage, Jahr und Seiten
* ISBN und Formatzuordnung
* Preis, Link und Bestellformulierung
* Publisher-, Eigenverlags- und Distributionsformulierung
* Autorenkontakt statt allgemeiner Publisher-Supportadresse
* Bildnachweis und eindeutig geklärte Nutzungsrechte
* Coverzuordnung, Farbbehauptungen und Ausgabendifferenz
* aktuelle Tatsachenbehauptungen und Quellenstand
* klickbare Links, Dateiname, PDF-Metadaten, Barrierearmut und Layout

`Nutzungsrechte bitte abstimmen` ist kein freigegebener Bildnachweis. Eine Pressemappe mit offenem Rechtehinweis ist nicht versandbereit.

Live verlinkte Pressemappe und bereitgestellte Datei per Name, Datum, Seitenzahl, Größe und Prüfsumme vergleichen. Bei Abweichung beide Fassungen getrennt führen.

## Händler- und Distributionsaudit

Pro ISBN und Plattform erfassen:

| Feld | Beispielstatus |
|---|---|
| Produktseite | gefunden oder nicht gefunden |
| Katalogstatus | gelistet oder nicht feststellbar |
| Bestellbarkeit | bestellbar, nicht bestellbar, unklar |
| Produktion | POD, Lagerware, unbekannt |
| Lagerstatus | lagernd, nicht lagernd, nicht ausgewiesen |
| Lieferzeit | wörtlicher Händlerhinweis plus Prüfdatum |
| Sortimentsstatus | Webshop, Bestellservice, Filiale, Regalplatz oder keine Zusage |

Eine positive Händlerantwort ist Evidenz für diesen Händler. Zwei Händlerbeispiele sind keine Bestätigung aller Barsortimente. Allgemeine Publisheraussagen zum Vertriebsnetz sind keine titelbezogene Bestätigung.

Exakte ISBN-Suche ohne Treffer bedeutet `öffentlich nicht gefunden`, nicht automatisch `nicht lieferbar`. Technischer Bot-Schutz bedeutet `nicht prüfbar`, nicht `Seite defekt`.

## Buchhandelsschwelle

Buchhandels-Outreach erst als `BEREIT` markieren, wenn mindestens bestätigt sind:

* ISBN und Format
* Preis im Zielmarkt
* Veröffentlichungsstatus
* konkreter Bestellweg
* formatbezogene Produktions- und Lieferlogik
* belastbare Formulierung zu Distribution
* Rabatt und Remission, falls sie im Pitch behauptet werden
* aktuelle Autorenkontaktadresse

Offene Konditionen dürfen als offene Frage an den Publisher geführt werden. Sie dürfen nicht erfunden oder aus allgemeinen Hilfeseiten übernommen werden.

## Datei- und Freigabestatus

* `CURRENT`: inhaltlich und technisch bestätigt
* `UPDATE ERFORDERLICH`: richtige Edition, aber korrigierbarer Fehler
* `ARCHIV`: historisch, nicht operativ
* `NICHT VERWENDEN`: riskant oder editionsfalsch

Originaldateien nicht überschreiben. Korrigierte Fassung mit Datum und Versionshinweis erstellen. Öffentliche Links erst nach bestandener Prüfung umstellen.

## Autonomie und Abschluss

Lesen, Recherche, Dateiprüfung, technische Skripte und Berichte autonom durchführen. Publisher-, Händler-, Metadaten-, Datei- oder Liveänderungen nur bei konkretem Auftrag und nach Zielverifikation ausführen.

Ergebnis liefern als:

1. Canonical Book Data je Edition und Format
2. technische Dateiprüfung
3. Widerspruchsmatrix
4. Dateiregister
5. Händlerstatus mit Prüfgrenzen
6. P0- und P1-Fehler
7. Freigabeempfehlung mit Stichtag

Vollständig nur melden, wenn alle benannten Editionen, Formate und Quellenklassen abgedeckt oder ausdrücklich als Lücke ausgewiesen sind.
