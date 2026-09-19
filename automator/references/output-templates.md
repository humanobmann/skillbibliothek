# Ausgabeformate

## Konkreter Prozess

Verwende dieses Format, wenn der Nutzer einen Prozess, Ist-Ablauf oder eine Ineffizienz beschreibt.

```markdown
## Vorgeschlagene Automatisierungslösungen

1. **[Loesungsname]**

   **Setup Schritt fuer Schritt**
   1. ...
   2. ...
   3. ...

   **Genutzte Tools/Connectoren**
   - [Tool]: [lesend/schreibend] - [Zweck]

   **Warum das Zeit spart**
   - ...

2. **[Loesungsname]**

   **Setup Schritt fuer Schritt**
   1. ...
   2. ...
   3. ...

   **Genutzte Tools/Connectoren**
   - [Tool]: [lesend/schreibend] - [Zweck]

   **Warum das Zeit spart**
   - ...

## Prozessverschlankung

- ...
- ...

## Naechste konkrete Umsetzung

1. ...
2. ...
3. ...
```

## Bereich ohne konkreten Prozess

Wenn der Nutzer nur einen Bereich oder Geschaeftstyp nennt und eine Prozessliste will, ausschliesslich diese Tabelle verwenden:

```markdown
| Prozess zur Automatisierung | Empfohlenes Tool / Methode |
|---|---|
| ... | ... |
| ... | ... |
```

Keine Einleitung und keine Erklaerung, wenn der Nutzer explizit Tabellenformat verlangt.

## Custom-GPT- oder Agentenkonzept

```markdown
## Agent-/GPT-Konzept: [Name]

**Zweck:** ...
**Geeignet als:** Custom GPT / Workflow-Agent / Kombination
**Trigger:** ...
**Eingaben:** ...
**Connectoren lesend:** ...
**Connectoren schreibend:** ...

**Ablauf**
1. ...
2. ...
3. ...

**Menschliche Freigabe**
- ...

**Outputs**
- ...

**Risiken und Schutzregeln**
- ...

**Kleinste erste Version**
1. ...
2. ...
3. ...
```

## Schnelle Automationsdiagnose

Wenn der Nutzer wenig Kontext liefert, liefere eine verwertbare erste Diagnose:

```markdown
## Wahrscheinlich bester Hebel

[Ein konkreter Hebel]

## Annahmen

- ...

## Sofort umsetzbar

1. ...
2. ...
3. ...

## Danach automatisieren

- ...
```
