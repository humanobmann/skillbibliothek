---
name: design-workflow-router
description: Route visuelle Aufgaben zum passenden Designworkflow für Bildgenerierung, Editorialgrafik, Affinity, Figma, PDF-Redesign, Präsentationen oder templatebasierte Designwerkzeuge. Verwenden, wenn das gewünschte Ergebnis klar visuell ist, aber Werkzeug, Produktionsweg oder Dateiformat noch gewählt werden muss. Keine Gestaltung simulieren, wenn das benötigte Werkzeug nicht verfügbar ist.
---

# Design Workflow Router

## Routing

- **Neues Bild oder Bildbearbeitung**: natives Bildgenerierungswerkzeug verwenden.
- **Politische/Editorial-Socialgrafik oder Bildserie**: `adaptive-poster-image-series` oder `ten-separate-images`.
- **Vorhandene Affinity-Datei**: `affinity-designer`.
- **Kampagnen-PDF redesignen**: `pdf-campaign-redesigner`.
- **Produkt-/UI-Design oder Figma-Arbeit**: verfügbare Figma-/Product-Design-Workflows verwenden.
- **Präsentation**: aktiven Präsentations-/Slides-Workflow verwenden.
- **Templatebasiertes Canva/Adobe-Design**: nur verwenden, wenn Nutzer dies auswählt oder ein vorhandenes Template/Cloud-Asset dort weiterbearbeitet werden soll.
- **Layout-/Craft-Review**: `impeccable`.

## Entscheidungsfaktoren

1. gewünschtes Endartefakt
2. vorhandene Quelldatei und deren Eigentümerformat
3. Editierbarkeit versus finales Bild
4. benötigte visuelle Präzision
5. Plattformformat und Safe Zones
6. Nutzerwunsch nach einem bestimmten Tool
7. Rechte und vorhandene Assets

Bestehende Quelldateien möglichst im nativen System weiterbearbeiten. Keine Konvertierung nur aus Bequemlichkeit.

## Handoff

Der Router wählt genau einen primären Produktionsworkflow. Zusätzliche Tools nur für klar getrennte Schritte wie Bildgenerierung, Layout, Preflight oder Export einsetzen.
