# Custom-GPT- und Workflow-Agenten-Konzepte

Nutze diese Anleitung, wenn der Nutzer optionale Custom GPTs, spezialisierte Agenten oder mehrstufige Workflow-Agenten fuer Menschlichkeit Oesterreich plant.

## Grundsatz

Nicht jeder Prozess braucht einen eigenen Agenten. Ein Agent lohnt sich, wenn mindestens drei Punkte zutreffen:

- Der Prozess kommt regelmaessig vor.
- Mehrere Quellen muessen gelesen werden.
- Es gibt ein klares Standardergebnis.
- Es gibt wiederkehrende Entscheidungen oder Klassifikationen.
- Menschliche Freigabe soll nur am Ende erfolgen.
- Fehler kosten Zeit, Geld, Vertrauen oder Datenschutzrisiko.

## Standardstruktur fuer ein Agentenkonzept

1. **Name und Zweck**
2. **Ausloeser**: manuell, Zeitplan, Webhook, E-Mail, Formular, GitHub, CRM, Zahlung, Kalender
3. **Eingaben**: Quellen, Felder, Dateien, Nachrichten
4. **Connectoren**: lesend und schreibend getrennt
5. **Verarbeitungsschritte**
6. **Menschliche Freigabe**
7. **Ausgaben**: Entwurf, Task, Dokument, Nachricht, CRM-Update, Issue, Report
8. **Fehlerpfade**
9. **Datenschutz/Risiko**
10. **Minimum Viable Agent**: kleinste sinnvolle erste Version

## Agenten, die fuer Menschlichkeit Oesterreich naheliegen

### 1. Spenden-Assistenz-Agent

**Zweck:** Spenden- oder Zahlungsereignisse pruefen, CRM-Abgleich vorbereiten, Dankeskommunikation entwerfen, Fehlerlisten erzeugen.

**Trigger:** Stripe-Zahlung, Formular, CiviCRM-Event oder manuelle Pruefung.

**Eingaben:** Zahlung, Kontakt, Spendenzweck, receipt_eligible, vorhandene CRM-Daten.

**Output:** Pruefprotokoll, Dankesmail-Entwurf, CiviCRM-Update-Vorschlag, Fehlerliste.

**Freigabe:** Menschliche Freigabe vor Versand und vor CRM-Schreibaktion, sofern produktiv.

### 2. Freiwilligen-Onboarding-Agent

**Zweck:** Anfragen von Freiwilligen automatisch sortieren, Erstantwort entwerfen, Interessen erfassen, Kennenlerntermin vorschlagen.

**Trigger:** E-Mail, Formular, Social-Media-Anfrage.

**Output:** Antwortentwurf, Kalendertermin, Kontakt-/CRM-Eintrag-Vorschlag, passende Aufgabenliste.

### 3. Presse- und Partnerkommunikations-Agent

**Zweck:** Partner- und Presseanfragen vorbereiten, passende Unterlagen finden, Antwortentwuerfe erstellen, Follow-ups setzen.

**Trigger:** E-Mail oder manuelle Anfrage.

**Output:** Antwortentwurf, Unterlagenpaket, Wiedervorlage, Partnernotiz.

### 4. Kampagnen-Recycling-Agent

**Zweck:** Aus einem Kerntext mehrere Formate erzeugen: Facebook, Instagram, WhatsApp, Newsletter, Flyer, Kurzstatement.

**Trigger:** Freigegebener Kampagnentext oder Briefing.

**Output:** Variantenpaket mit Kanal, Tonalitaet, Laenge, CTA und Freigabestatus.

### 5. Sitzungs- und Beschluss-Agent

**Zweck:** Protokolle, Beschluesse, Aufgaben und Fristen aus Notizen oder Transkripten erzeugen.

**Trigger:** Meetingnotiz, Audio-Transkript, Dokument.

**Output:** Protokoll, Beschlussliste, Aufgaben, Kalender-/Asana-/GitHub-Eintraege.

### 6. GitHub-/n8n-Technik-Agent

**Zweck:** technische Projektstaende pruefen, Issues formulieren, Smoke-Test-Ergebnisse zusammenfassen, Dokumentation aktualisieren.

**Trigger:** manuelle Anfrage, GitHub Issue, Testlog.

**Output:** Issue, PR-Plan, Testcheckliste, Dokumentationsupdate.

## Custom GPT vs Workflow-Agent

**Custom GPT verwenden, wenn:**
- Der Nutzer interaktiv arbeitet.
- Viel Text, Beratung, Analyse oder Entwurf gebraucht wird.
- Menschliche Entscheidung im Chat bleibt.

**Workflow-Agent verwenden, wenn:**
- Ein Trigger automatisch startet.
- Immer aehnliche Felder verarbeitet werden.
- Output maschinenlesbar sein soll.
- n8n, Make, Zapier oder eigene API die Schritte ausfuehren soll.

**Kombination verwenden, wenn:**
- Custom GPT plant, prueft und freigibt.
- Workflow-Agent fuehrt nach Freigabe aus.

## Minimaler Umsetzungsplan fuer jeden Agenten

1. Einen einzigen Trigger waehlen.
2. Ein einziges Standardergebnis definieren.
3. Nur lesenden Zugriff in Version 1 nutzen.
4. Entwurf statt produktiver Schreibaktion erzeugen.
5. Drei echte Beispiele testen.
6. Erst danach Schreibrechte oder automatische Ausfuehrung aktivieren.

## Beispiel-Ausgabe fuer Agentenkonzept

```markdown
## Agent: [Name]

**Zweck:** ...
**Trigger:** ...
**Eingaben:** ...
**Connectoren lesend:** ...
**Connectoren schreibend:** ...
**Ablauf:**
1. ...
2. ...
3. ...

**Menschliche Freigabe:** ...
**Output:** ...
**Fehlerpfade:** ...
**Datenschutz/Risiko:** ...
**Kleinste erste Version:** ...
```
