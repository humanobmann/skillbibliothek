# Protokoll für ChatGPT Bildwerkzeuge

## image_gen.text2im

Für jeden Slot einen eigenen seriellen Aufruf verwenden.

Parameter:

1. `n: 1`
2. `size`: gewünschtes Einzelbildformat
3. `transparent_background`: nur nach ausdrücklichem Auftrag
4. `is_style_transfer`: nur bei tatsächlicher Stilübertragung
5. `referenced_image_ids`: bei Bearbeitung möglichst genau die ID der aktuellen Inhaltsquelle
6. `prompt`: bei als veraltet markiertem Feld `null` lassen

## Kontrolle bei automatisch abgeleitetem Prompt

Wenn das Werkzeug den Auftrag aus dem Gespräch ableitet, unmittelbar vor jedem Aufruf eine Slotkapsel schreiben. Diese enthält nur:

1. aktuelle Slotnummer
2. aktuelle Quelle oder eine einzelne Szene
3. unveränderliche Merkmale
4. konkrete Änderung
5. Format

Nicht aufnehmen:

1. Gesamtzahl des Batches
2. andere Quellen
3. andere Briefings
4. mehrere Optionen oder Ansichten
5. eine Zusammenfassung der ganzen Serie

## Referenz-ID Regeln

### Zehn Zielbilder

Pro Aufruf genau eine Zielbild-ID verwenden.

### Wiederkehrende Person oder Produkt

Die notwendige Identitätsreferenz zusätzlich verwenden, sofern das Werkzeug mehrere Referenzen eindeutig verarbeiten kann. Keine andere Batchquelle ergänzen.

### Stilreferenzen

Den Stil bevorzugt in Textregeln übersetzen. Eine Stilreferenz nur ergänzen, wenn dadurch die Inhaltsquelle nicht mehrdeutig wird. Niemals eine Kontaktübersicht oder mehrere Stilbilder gemeinsam mit allen Zielbildern übergeben.

## Werkzeugergebnis zählen

Ein Werkzeugaufruf zählt erst nach visueller Prüfung als gültige Ausgabe. Das Vorhandensein einer Toolantwort allein genügt nicht.
