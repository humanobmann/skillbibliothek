# System- und Rollenkarte

## Zweck

Diese Referenz schützt die private Autorenkampagne vor Rollenvermischung. Konten und Fähigkeiten können sich ändern. Deshalb vor jedem Write den Livezustand prüfen.

## Zulässiger Kampagnenkern

| System | Rolle | Regel |
|---|---|---|
| HubSpot des privaten Autors | CRM, Landingpage, Aufgaben und zulässige Einzelaktionen | vor Write Eigentümer, Objektfähigkeit und Freigabe prüfen |
| `schuller.peter@outlook.at` | private Antworten und streng begrenzte Einzelkommunikation | Absender, Reply-to, Format und Versandumfang vor jedem Versand prüfen |
| ChatGPT Library | kanonische Berichte und freigegebene Arbeitsdateien | private Buchdateien versioniert halten |

## Ausgeschlossen ohne neuen ausdrücklichen Auftrag

| System oder Identität | Grund |
|---|---|
| Google Drive des SPÖ-Kontexts | Parteikonto, nicht Teil der privaten Autorenkampagne |
| SharePoint und Teams von Menschlichkeit Österreich | Organisationskonto, nicht Teil der privaten Autorenkampagne |
| Partei-, Vereins- oder NGO-Verteiler | keine stillschweigende Zweckübernahme |
| private Kontakte ohne dokumentierten Buchbezug | keine stillschweigende Zweckübernahme |

Canva oder andere Kreativsysteme nur verwenden, wenn das konkrete Konto und die Assetrechte als privat oder ausdrücklich freigegeben bestätigt sind.

## Führende Quellen

| Gegenstand | Führende Quelle |
|---|---|
| tatsächlicher Inhalt und Seitenstand | finale Produktionsdatei der konkreten Edition |
| ISBN, Preis und öffentlicher Produktstatus | aktuelle Publisher- oder Händlerquelle je Plattform |
| nicht öffentliche Konditionen | aktuelle direkte Publisherkommunikation oder Vertrag |
| Kontaktstatus | HubSpot plus Abgleich mit Mailthread |
| Versand, Antwort, Bounce | Originalmail und Zustelldiagnose |
| Landingpage-Inhalt | veröffentlichte Seite plus aktuelle CMS-Fassung |
| Bild- und Nutzungsrechte | Rechtefreigabe, nicht Dateiname oder Bildunterschrift |

## Write-Klassen

* `READ`: lesen, suchen, analysieren
* `DRAFT`: lokale, nicht veröffentlichte Fassung erzeugen
* `INTERNAL_WRITE`: CRM, Datei oder Aufgabe intern ändern
* `EXTERNAL_WRITE`: senden, veröffentlichen, teilen, einladen oder verbindlich zusagen

Eine höhere Klasse niemals aus einer niedrigeren ableiten. Der Auftrag muss die konkrete Klasse abdecken.
