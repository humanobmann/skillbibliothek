# API Endpoints und Query Strategie

Stand der Dokumentationsprüfung: 24. August 2026

## Inhaltsübersicht

1. Kanonische Regeln
2. Alle 25 Open-Data-Datensätze
3. Masterprompt-Pflichtlayer
4. Datensatz 101
5. Protokolle und Sitzungen
6. Personen und Ausschüsse
7. Parlamentskorrespondenz und Termine
8. EU-Datensätze
9. Detailseiten
10. VTS Auxiliary
11. Live-Verifikation

## 1. Kanonische Regeln

Die maschinenlesbare Registry liegt in `api_registry.json`.

Basisdomain:

```text
https://www.parlament.gv.at
```

Bei Widerspruch gilt die jeweils aktuelle offizielle Datensatzdokumentation. Varianten wie `?js=eval?showAll=true` in einzelnen Dokumentationszeilen nicht blind kopieren. Produktiv nur einen live verifizierten Querystring verwenden.

Die aktuelle Gesetzgebungsperiode immer live bestimmen.

## 2. Alle 25 Open-Data-Datensätze

Die offizielle Übersicht nennt derzeit 25 Datensätze. Der Skill führt alle 25 in der Registry, einige mit mehreren Query-Templates für NR/BR oder Untertypen:

1. Anträge
2. Ausschussberichte
3. Beschlüsse
4. Gesetzesanträge des Bundesrats
5. Regierungsvorlagen
6. Aktuelle Beteiligungen
7. Bürgerinitiativen
8. Petitionen
9. Stenographische Protokolle NR/BR
10. Plenarsitzungen NR/BR
11. Parlamentarier:innen seit 1918
12. Aktuelle Abgeordnete zum NR
13. Aktuelle Mitglieder des BR
14. Parlamentskorrespondenz
15. Termine
16. Ausschüsse
17. Ausschussmitgliedschaften
18. Schriftliche Anfragen NR
19. Schriftliche Anfragen BR
20. Stellungnahmen des EU-Hauptausschusses
21. Mitteilungen des EU-Unterausschusses
22. Stellungnahmen des Ständigen Unterausschusses des Hauptausschusses EU
23. Begründete Stellungnahmen des EU-Ausschusses BR
24. Mitteilungen des EU-Ausschusses BR
25. Stellungnahmen des EU-Ausschusses BR

## 3. Masterprompt-Pflichtlayer

### Datensatz 101

Kanonischer Basisendpoint:

```text
POST /Filter/api/filter/data/101?js=eval&showAll=true
```

Wichtige VHG-Werte:

```text
ANTR       Anträge
RV         Regierungsvorlagen
AUB        Ausschussberichte NR
AUB-BR     Ausschussberichte BR
BNR        Beschlüsse
GABR       Gesetzesanträge BR
GABR13     Gesetzesanträge eines Drittels des BR
BI         Bürgerinitiativen
PET        Petitionen
J_JPR_M    Schriftliche Anfragen NR
J_JPR_M-BR Schriftliche Anfragen BR
EU         EU betreffende Vorlagen/Beschlüsse
```

Nicht mit Partei oder Thema als Primärfilter voll erheben. Erst Grundkorpus laden, dann `DOKTYP`, Datum, Partei, Person oder Thema als Kontroll-/Analysepartition verwenden.

### Anträge

```json
{"NRBR":["NR"],"GP_CODE":["<GP>"],"VHG":["ANTR"]}
```

```json
{"NRBR":["BR"],"GP_CODE":["<GP>"],"VHG":["ANTR"]}
```

Bekannte NR-Antragsarten umfassen `A`, `A(E)`, `AA`, `AEA`, `AMIN`, `ARH2`, `AVB`, `BUA`, `UEA`, `URH2`. BR-Typen nicht ausschließlich aus einer statischen Liste ableiten, sondern aus dem Korpus beobachten.

### Regierungsvorlagen

```json
{"NRBR":["NR"],"GP_CODE":["<GP>"],"VHG":["RV"]}
```

### Ausschussberichte

```json
{"NRBR":["NR"],"GP_CODE":["<GP>"],"VHG":["AUB"]}
```

```json
{"NRBR":["BR"],"GP_CODE":["<GP>"],"VHG":["AUB-BR"]}
```

### Beschlüsse

```json
{"NRBR":["NR"],"GP_CODE":["<GP>"],"VHG":["BNR"]}
```

```json
{"NRBR":["BR"],"GP_CODE":["<GP>"],"VHG":["BNR"]}
```

Dokumentierte DOKTYP: `BNR`, `BS`, `BSE`, `BSESM`, `BS-BR`. Eigenständiger Beschlussdatensatz ab XXII. GP. XX und XXI nicht als Nichtvorhandensein behandeln, sondern historisch rekonstruieren.

### Gesetzesanträge des BR

Die offizielle Dokumentation verwendet trotz BR-Ursprung `NRBR=["NR"]`:

```json
{"NRBR":["NR"],"GP_CODE":["<GP>"],"VHG":["GABR"]}
```

Ab XXV zusätzlich:

```json
{"NRBR":["NR"],"GP_CODE":["<GP>"],"VHG":["GABR13"]}
```

Diesen kontraintuitiven Filter vor Massenerhebung live prüfen.

### Schriftliche Anfragen NR

```json
{"NRBR":["NR"],"GP_CODE":["<GP>"],"VHG":["J_JPR_M"],"DOKTYP":["J"]}
```

Präsidium:

```json
{"NRBR":["NR"],"GP_CODE":["<GP>"],"VHG":["J_JPR_M"],"DOKTYP":["JPR"]}
```

Die schriftliche Beantwortung aus der Detailseite/Verfahrensgeschichte verknüpfen. Nicht aus separatem Datensatz erfinden.

### Schriftliche Anfragen BR

```json
{"NRBR":["BR"],"GP_CODE":["<GP>"],"VHG":["J_JPR_M-BR"],"VHG2":["JMIN-BR"]}
```

Präsidium:

```json
{"NRBR":["BR"],"GP_CODE":["<GP>"],"VHG":["J_JPR_M-BR"],"VHG2":["JPRPR-BR"]}
```

Die Dokumentation enthält in einer Beispielabfrage `JMIN` ohne Suffix, während Dimensionsbeschreibung und Ergebnis `JMIN-BR` zeigen. Deshalb `JMIN-BR` kanonisch halten und live verifizieren.

## 4. Protokolle und Sitzungen

### Stenographische Protokolle

```text
POST /Filter/api/filter/data/211?js=eval&showAll=true
```

Nationalrat:

```json
{"NBVS":["NRSITZ"],"GP_CODE":["<GP>"]}
```

Bundesrat:

```json
{"NBVS":["BRSITZ"],"GP_CODE":["<GP>"]}
```

Datumsfilter in `yyyy-mm-dd`.

### Plenarsitzungen

```text
POST /Filter/api/json/post?jsMode=EVAL&FBEZ=WFP_007&listeId=11070&showAll=true
```

NR:

```json
{"NRBRBV":["NR"],"GP":["<GP>"]}
```

BR zeitbasiert. Den konkreten Zeitraum aus dem Filterexport übernehmen.

Die Dokumentation nennt im Hauptendpoint `listeId=11070`, in einem Beispiel `listeId=undefined`. Vor Vollerhebung live testen und den erfolgreichen Wert im Run Manifest speichern.

## 5. Personen und Ausschüsse

### Parlamentarier:innen seit 1918

```text
POST /Filter/api/filter/data/409?1=1&showAll=true&export=true
```

Beispiel:

```json
{"ATTR_JSON.mandate_detail.gremium_name":["Nationalrat","Bundesrat"]}
```

Für Temporal Identity bevorzugt diesen historischen Datensatz plus Personendetailseite nutzen.

### Aktuelle Abgeordnete NR

```text
POST /Filter/api/json/post?jsMode=EVAL&FBEZ=WFW_002&listeId=10002&showAll=true
```

### Aktuelle Mitglieder BR

```text
POST /Filter/api/json/post?jsMode=EVAL&FBEZ=WFW_005&listeId=10005&showAll=true
```

### Ausschüsse

```text
POST /Filter/api/json/post?jsMode=EVAL&FBEZ=WFP_009&listeId=undefined&showAll=true
```

NR:

```json
{"NRBR":["NR"],"GP":["<GP>"],"UA":["J"]}
```

BR aktiv:

```json
{"NRBR":["BR"],"R_AKTAUF":["AKT"]}
```

BR aufgelöst:

```json
{"NRBR":["BR"],"R_AKTAUF":["AUF"]}
```

### Ausschussmitgliedschaften

```text
POST /Filter/api/filter/data/250?js=eval&showAll=true&export=true
```

```json
{"PAD_INTERN":["<PAD>"]}
```

## 6. Parlamentskorrespondenz und Termine

### Parlamentskorrespondenz

```text
POST /Filter/api/filter/data/110?js=eval&showAll=true
```

Dimensionen: `STW`, `SACHB`, `THEMEN`, `JAHR`. Für Vollerhebung jahrweise partitionieren.

### Termine

```text
POST /Filter/api/filter/data/600?js=eval&showAll=true
```

Dimensionen: `GREMIUM`, `TERMINART`, `ORT`, `THEMEN`, `DATERANGE`, `FORMAT`.

## 7. Aktuelle Beteiligungen

```text
POST /Filter/api/filter/data/143?js=eval&showAll=true
```

Pflichtfilter `AKTIV=["J"]`.

## 8. EU-Datensätze über Datensatz 101

Gemeinsam:

```text
VHG=["EU"]
```

VHG2:

```text
S       Stellungnahmen EU-Hauptausschuss
MTEU    Mitteilungen EU-Unterausschuss
SEU     Stellungnahmen Ständiger UA des Hauptausschusses EU
SB-BR   Begründete Stellungnahmen EU-Ausschuss BR
MT-BR   Mitteilungen EU-Ausschuss BR
S-BR    Stellungnahmen EU-Ausschuss BR
```

## 9. Detailseiten

Für jede relative Ergebnis-URL:

```text
https://www.parlament.gv.at + <relative_url> + ?json=TRUE
```

Detailseiten sind die zentrale Quelle für Verfahrensstufen, Dokumente, Personen, Reden, Abstimmungen, Bezüge und Korrespondenz. Indexdaten allein nicht als vollständige Sachanalyse verwenden.

## 10. VTS Auxiliary

Vom Auftraggeber bereitgestellt:

```text
POST /Filter/api/filterform/vts/data?FBEZ=VTS_01&showAll=true&export=true
```

```json
{"searchType":["all"],"searchScope":["all"],"category":["Protokolle"]}
```

Nur als Discovery-/Crosscheck-Quelle verwenden. Nie die dokumentierten Open-Data-Datensätze ersetzen lassen.

## 11. Live-Verifikation

Vor Massenerhebung besonders testen:

1. `showAll=true` auf große Batches
2. Plenarsitzungen `listeId=11070` gegen `undefined`
3. GABR/GABR13 mit `NRBR=NR`
4. BR-Anfragen `JMIN-BR` gegen das abweichende Dokumentationsbeispiel
5. BR-Plenarsitzungs-Zeitraumformat
6. tatsächliche Response-Header und Row-Positionen
7. aktuelle GP und neue Dokumenttypen
8. neue oder geänderte Lizenzhinweise
