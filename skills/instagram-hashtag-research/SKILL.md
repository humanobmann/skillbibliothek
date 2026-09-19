---
name: instagram-hashtag-research
description: Recherchiert und bewertet aktuelle Instagram-Hashtags ohne MCP-Server, Docker oder lokale Serverinstallation. Verwenden bei Anfragen nach Instagram-Hashtags, Hashtag-Recherche, Hashtag-Auswahl, Social-SEO-Tags, regionalen oder thematischen Tags sowie zur belegbaren Hashtag-Prüfung für Feed, Carousel oder Reel. Arbeitet mit verfügbarer Browser- oder Web-Recherche, optional mit einer normalen eingeloggten Instagram-Sitzung, trennt Kandidaten von verifizierter Evidenz, erfindet keine Reichweiten-, Trend- oder Volumenwerte und liefert standardmäßig 3 bis 8 belastbare Hashtags mit Prüfdatum, Quellenbasis, Evidenzstatus und relevanten Ausschlüssen.
---

# Instagram Hashtag Research

## Ziel

Eine kleine, aktuelle und nachvollziehbar geprüfte Hashtag-Auswahl liefern. Hashtags als semantische Kontext- und Discovery-Signale behandeln, nicht als primaeren Reichweitenhebel. Nicht aus vermeintlichen Algorithmus-Tricks, generischen Generatorlisten oder erfundenen Kennzahlen ableiten.

Keine MCP-Server, Docker-Container oder lokalen Dienste voraussetzen. Keine Installation externer Scraper verlangen.

## Eingabe bestimmen

Aus Thema, Caption oder Postentwurf mindestens ableiten:

1. Kernthema und Unterthemen.
2. Sprache.
3. Land, Region oder Ort, wenn relevant.
4. Format: Feed, Carousel oder Reel, falls bekannt.
5. Organisation, Kampagne, Ereignis oder Eigenname, falls vorhanden.
6. Kommunikationszweck: informieren, dokumentieren, erklären, mobilisieren oder Community-Kontext.

Fehlende unwesentliche Angaben nicht nachfragen. Mit der plausibelsten Annahme arbeiten und sie nur nennen, wenn sie die Auswahl beeinflusst.

## Recherchemodus

Die beste verfügbare Quelle verwenden, in dieser Reihenfolge:

1. Direkte öffentliche Instagram-Suche oder öffentlich sichtbare Instagram-Seiten im verfügbaren Browser.
2. Eine vorhandene normale eingeloggte Instagram-Sitzung, wenn sie ohne zusätzliche Infrastruktur verfügbar ist.
3. Aktuelle Websuche nach Instagram-Verwendungen, Hashtag-Seiten, Posts, Reels oder Accounts.
4. Meta-Dokumentation für Plattformregeln und API-Grenzen.
5. Drittanbieter-Hashtag- oder Social-Analytics-Seiten nur ergänzend und immer mit Quelle und Datum.

Nie behaupten, Instagram direkt geprüft zu haben, wenn nur Websuchtreffer verfügbar waren.

Bei Webrecherche Suchabfragen variieren, zum Beispiel:

- `site:instagram.com #<hashtag>`
- `site:instagram.com/reel <thema> <ort>`
- `site:instagram.com/p <thema> <hashtag>`
- `Instagram <thema> <ort> hashtag`

## Workflow

### 1. Kandidaten bilden

20 bis 40 plausible Kandidaten aus folgenden Gruppen erzeugen:

- Kernthema.
- Unterthema oder konkreter Sachbegriff.
- Ort oder Region.
- Ereignis oder Anlass.
- Organisation oder etablierter Kampagnenbegriff, sofern tatsächlich passend.
- Synonyme und gebräuchliche Sprachvarianten.

Kandidaten sind noch keine Empfehlung.

### 2. Grob filtern

Offensichtlich ausscheiden:

- semantisch unpassende Tags,
- generische Engagement-Tags,
- Spam- oder Bot-Tags,
- falsche Ortsbezüge,
- mehrdeutige Tags mit hohem Fehlinterpretationsrisiko,
- unbestätigte Kampagnenbegriffe,
- Tags, die nur wegen vermeintlicher Reichweite vorgeschlagen würden.

Auf etwa 8 bis 15 Kandidaten reduzieren.

### 3. Aktuell prüfen

Für die verbliebenen Kandidaten aktuelle öffentliche Evidenz sammeln. Pro Kandidat nach Möglichkeit mindestens zwei unabhängige aktuelle Signale prüfen, zum Beispiel:

- sichtbare aktuelle Posts oder Reels,
- aktuelle Suchtreffer mit Instagram-Bezug,
- erkennbare wiederholte Verwendung durch unterschiedliche Accounts,
- klare thematische Passung der sichtbaren Beiträge,
- klarer regionaler oder sprachlicher Bezug.

Für die stärksten 5 bis 10 Kandidaten nach Möglichkeit mehrere sichtbare Verwendungen prüfen. Keine Vollständigkeit behaupten.

### 4. Messwerte nur bei echter Beobachtung verwenden

Sichtbare Kennzahlen dürfen nur genannt werden, wenn sie tatsächlich erhoben wurden.

- Postzahl, Viewzahl, Likes, Kommentare oder Followerzahlen niemals schätzen.
- Bei Stichproben die Stichprobengröße nennen.
- Einen Median sichtbarer Interaktionen nur bilden, wenn mindestens fünf ausreichend vergleichbare Posts vorliegen.
- Likes oder Views verschiedener Accounts nicht als alleinige Hashtag-Qualität interpretieren.
- Verdeckte oder nicht sichtbare Metriken als `nicht öffentlich verifizierbar` kennzeichnen.

### 5. Evidenzbasiert bewerten

Die Bewertungslogik aus [references/scoring.md](references/scoring.md) verwenden.

Keine Scheingenauigkeit erzeugen. Ein numerischer Score ist nur ein internes Ordnungswerkzeug für tatsächlich beobachtete Signale. Die finale Empfehlung über Evidenz und Passung erklären.

### 6. Auswahl bilden

Standardmäßig 3 bis 8 Tags auswählen. Weniger ausgeben, wenn weniger belastbar sind.

Eine sinnvolle Mischung bevorzugen aus:

- einem breiteren Themenanker,
- einem oder mehreren präzisen Fachtags,
- einem Orts- oder Regionstag, falls relevant,
- einem Ereignis-, Organisations- oder Kampagnentag nur bei belegter Passung.

Keine Kategorie künstlich füllen. Semantische Praezision ist wichtiger als Menge oder vermeintliche Groesse eines Tags.

## Quellen- und Evidenzregeln

[references/research-method.md](references/research-method.md) für Quellenqualität, Stichproben und Unsicherheiten verwenden.

Jede Recherche muss enthalten:

- Prüfdatum,
- verwendete Suchbasis,
- welche Tags direkt oder indirekt verifiziert wurden,
- relevante Einschränkungen.

Keine Aussage wie `trending`, `viral`, `reichweitenstark`, `hohes Volumen`, `geringe Konkurrenz` oder `performt gut` ohne aktuelle belastbare Messgrundlage.

Drittanbieterwerte nie als offizielle Instagram-Daten darstellen.

## Politische und gesellschaftliche Inhalte

Bei politischen, wahlbezogenen oder gesellschaftlich strittigen Themen neutral recherchieren.

- Hashtags nach sachlicher Themenpassung und belegbarer Verwendung auswählen.
- Keine Hashtags nach vermuteter Überzeugungswirkung, Zielgruppen-Manipulierbarkeit oder politischer Mobilisierungseffizienz bewerten.
- Keine persönliche politische Präferenz ableiten.
- Kontroverse oder mehrdeutige Tags mit Kontext- oder Vereinnahmungsrisiko sichtbar kennzeichnen.

## Zusammenspiel mit Instagram-Text-Optimierung

Wenn zusätzlich ein Instagram-Text-Optimierer aktiv ist, diese Recherche als Hashtag-Schritt verwenden. Die ausgewählten Tags und den Evidenzstatus an die Caption-Ausgabe übergeben. Keine zweite, widersprüchliche Hashtag-Logik parallel anwenden.

## Ausgabe

Das Ausgabeformat aus [references/output-patterns.md](references/output-patterns.md) verwenden.

Standardmäßig kompakt ausgeben:

1. **Empfohlene Hashtags:** 3 bis 8 Tags in einer kopierbaren Zeile.
2. **Warum diese:** je Tag kurze sachliche Begründung und Evidenzstatus.
3. **Ausgeschlossen:** höchstens fünf relevante Kandidaten mit Grund.
4. **Recherche:** Prüfdatum, Suchbasis, Stichprobe und wichtigste Einschränkung.

Wenn der Nutzer nur `Hashtags` verlangt, zuerst die kopierbare Hashtag-Zeile liefern und danach eine sehr kurze Evidenznotiz.

## Qualitätsgates

Vor Abschluss prüfen:

- Jeder empfohlene Tag passt konkret zum Post.
- Jeder empfohlene Tag hat aktuelle Evidenz oder ist klar nur semantisch bestätigt.
- Keine erfundenen Kennzahlen oder Trendbehauptungen.
- Keine generischen Reichweiten-Tags als Füllmaterial.
- Orts- und Sprachbezug stimmen.
- Mehrdeutige oder problematische Tags wurden geprüft oder ausgeschlossen.
- Ausgabe nennt Prüfdatum und tatsächliche Suchbasis.
- Bei unzureichender Live-Evidenz wird die Unsicherheit offen genannt und die Auswahl entsprechend kleiner.
