# PDF-Rebuild-Workflow

## 1. Input sichern

- Source-PDF, Zusatzquellen, Designvorgaben und Zielstatus identifizieren.
- Bei bestehenden PDFs zuerst rendern; Screenshots sind fuer Layout verbindlicher als extrahierter Text.
- Text, Tabellen, Bilder und Seitengeometrie extrahieren. OCR nur wenn noetig.

## 2. Seiteninventar

Erstelle eine Tabelle fuer die interne Planung:

| Seite | Zweck | Kernaussage | Evidenzstatus | Designproblem | Aktion |
|---:|---|---|---|---|---|

Aktionen: `halten`, `kuerzen`, `splitten`, `zusammenlegen`, `neu bauen`, `streichen`, `intern`, `sperren`.

## 3. Redesign-Entscheidung

- Textlastiges Langdossier: HTML/CSS oder DOCX -> PDF.
- Slide-/kampagnenartige Layouts: PPTX/HTML -> PDF.
- Programmgenerierte Infografikseiten: HTML/CSS/SVG -> PDF.
- PDF direkt bearbeiten nur fuer kleine Reparaturen; fuer echte Optimierung neu aufbauen.

## 4. HTML/CSS-PDF-Standard

- Nutze `assets/dossier-template.html` und `assets/dossier-styles.css`.
- Jede Seite ist ein `<section class="page ...">`.
- Datentragende Elemente immer mit `<figcaption>` oder `.source-line`.
- Tabellen in `.table-wrap`; Werte mit `.num`; Quellen mit `.src`.
- Callouts mit `.callout.fact`, `.callout.risk`, `.callout.check`, `.quote`.
- Keine Inline-Hex-Werte ausser wenn ein neuer Token dokumentiert wird.

## 5. PDF erzeugen

Optionales Script:

```bash
python scripts/render_html_to_pdf.py input.html output.pdf
```

Das Script nutzt Playwright oder WeasyPrint, wenn verfuegbar. Wenn beides fehlt, den passenden Host-PDF/Slides/DOCX-Workflow verwenden und danach PDF exportieren.

## 6. Visuell verifizieren

- Re-render der Ausgabe-PDF.
- Mindestens Titelseite, dichteste Textseite, groesste Tabelle, wichtigste Grafik, Quellenanhang pruefen.
- Korrigieren: Clipping, Ueberlauf, fehlende Quellen, Kontrast, unklare Lesereihenfolge, falsche Statusfarben, zerrissene Komponenten.
- Bei Vorher/Nachher-Vergleich optional Render-Diff erzeugen.

## 7. Deliverable-Namen

- Optimierte PDF: sprechender deutscher Dateiname, keine `final_final`-Logik.
- Bei Arbeitsfassungen: `_v01`, `_v02`, Datum oder Status.
- Keine `PDFUA`, `druckfertig` oder `barrierefrei` im Namen, wenn nicht geprueft.
