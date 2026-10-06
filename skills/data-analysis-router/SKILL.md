---
name: data-analysis-router
description: Route datenbezogene Aufgaben zur kleinsten geeigneten Analyseoberfläche und trenne Datenerhebung, Datenqualität, quantitative Analyse, Spreadsheet-Bearbeitung, KPI-Design, Reports und Dashboards sauber voneinander. Verwenden bei CSV/XLSX/TSV, Kennzahlen, Trends, KPIs, Charts, Dashboards, Reports, Marktgrößen, Datenqualität, Google Sheets oder österreichischen Open-Data-Datensätzen, wenn entschieden werden muss, welcher Datenworkflow die Aufgabe besitzt.
---

# Data Analysis Router

## Ziel

Wähle zuerst den richtigen Datenworkflow. Dupliziere keine Analyse, die ein spezialisierter Daten- oder Spreadsheet-Workflow bereits zuverlässig besitzt.

## Routing

1. **Quantitative Analyse, Kennzahlen, Trends, Treiber, KPI, Chart, Report oder Dashboard**  
   An das verfügbare Data-Analytics-Plugin übergeben. Dieses besitzt Analyse, KPI-Design, Datenqualität, Visualisierung, Reports und Dashboards.

2. **Nutzer liefert CSV/XLSX/TSV als Datenquelle**  
   Wenn das gewünschte Ergebnis Analyse, Report oder Dashboard ist: Data Analytics.  
   Wenn ausdrücklich eine bearbeitete Spreadsheet-Datei, Formeln, Tabellenstruktur oder Workbook-Ausgabe verlangt ist: den Spreadsheet-Workflow verwenden.

3. **Google Sheets als Arbeitsoberfläche**  
   Für range-genaue Lese-/Schreiboperationen den Google-Sheets-Connector verwenden. Für umfangreiche Analyse darf Data Analytics die Daten als Quelle verwenden, wenn die Quelle autoritativ und zugänglich ist.

4. **Österreichische öffentliche Daten beschaffen oder normalisieren**  
   Zuerst `austria-open-data-research` für reproduzierbare Erhebung und Provenienz. Danach Data Analytics für quantitative Auswertung, falls nötig.

5. **Datenqualität oder widersprüchliche Zahlen**  
   Grain, Zeitraum, Population, Einheit, Definition, Aktualität, Missingness, Dubletten und Join-Logik prüfen. Wenn die eigentliche Aufgabe methodische Datenqualitätsdiagnose ist, an den entsprechenden Data-Analytics-Workflow übergeben.

6. **Börsennotierte Unternehmen aus Investorensicht**  
   Wenn die Frage Bewertung, Earnings, Investmentthese oder Public-Equity-Modellierung betrifft, an den spezialisierten Public-Equity-Workflow routen statt an generische Datenanalyse.

## Quellen- und Übergaberegeln

Vor der Übergabe intern festhalten:
- autoritative Datenquelle
- betrachteter Zeitraum
- Population/Grundgesamtheit
- Grain
- Einheit/Währung
- zentrale Definitionen
- bekannte Datenlücken

Keine CSV oder Tabelle allein als autoritativ behandeln, wenn ihre Herkunft unklar ist. Keine Zahlen aus unterschiedlichen Definitionen still zusammenführen.

## Ausgabe

Bei reiner Routingfrage: empfohlener Workflow plus Begründung.  
Bei Datenauftrag: Router entscheidet intern und übergibt anschließend an den zuständigen Datenworkflow.
