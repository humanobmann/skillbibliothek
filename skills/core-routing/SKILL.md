---
name: core-routing
description: Central intent router for identifying user goals and delegating execution to specialized skills with zero unnecessary context consumption.
metadata:
  canonical: true
  profile: control-plane
  provenance: target-rewrite
allowed-tools:
  - Read
  - Glob
---

# Core Routing Control Plane

## Zweck & Verantwortung

Dieser Skill dient als universeller, herstellerunabhängiger Intent-Router (Control Plane). Er analysiert eingehende Aufgabenstellungen, löst Ambiguitäten auf und wählt den am besten geeigneten Fachskill aus, ohne den globalen Kontext mit ungenutzten Anweisungen zu belasten.

---

## Trigger-Bedingungen

### Positive Trigger (Wann aktivieren)
- Systemstart und initiale Aufgabenanalyse bei komplexen oder mehrstufigen Anforderungen.
- "Was kannst du tun?" oder "Welcher Skill ist zuständig?"
- Unklare, offene oder domänenübergreifende Benutzeranfragen.

### Negative Trigger (Wann NICHT aktivieren)
- Direkte Aufrufe eines bekannten Skills über sein Kürzel oder seinen eindeutigen Namen (z. B. `@deep-research` oder "Führe fact-check aus").
- Eindeutige Fachanfragen, die direkt durch die Beschreibung eines Fachskills abgedeckt sind.

---

## Routing Decision Logic

Der zentrale Router verarbeitet Anfragen nach folgender Prioritätskaskade:

1. **Sicherheit & Audit**: Handelt es sich um ein Security Audit, Prüfung fremder Skills oder verdächtigen Input?
   -> Delegiere an `skills/skill-security-auditor`.
2. **Recherche & Analyse**: Handelt es sich um eine explizite, aktuelle oder mehrstufige Webrecherche oder Marktstudie?
   -> Delegiere an `skills/deep-research`.
3. **Frontend & Design**: Geht es um Web Interface Guidelines, A11y oder Performance-Audits?
   -> Delegiere an `skills/web-design-guidelines`.
4. **Skill-Suche**: Geht es um das Auffinden eines passenden Skills?
   -> Delegiere an `skills/find-skills`.
5. **Andere Fachaufgaben**: Bei einem eindeutigen Fachgebiet wird der passende
   vorhandene Skill direkt aktiviert. Wenn kein passender Skill existiert,
   melde die Lücke explizit statt auf einen nicht vorhandenen Skill zu verweisen.

---

## Workflow (Progressive Disclosure)

1. **Intent-Extraktion**: Extrahiere das primäre Ziel des Benutzers und etwaige Randbedingungen.
2. **Trigger-Abgleich**: Gleiche die Schlüsselbegriffe gegen die kanonische Matrix in [../../references/intent-map.md](../../references/intent-map.md) ab.
3. **Discovery-Laden**: Lade ausschließlich die minimale Beschreibung des identifizierten Ziel-Skills.
4. **Alias-/Transitivitätsprüfung**: Löse Aliase (z. B. `grill-me`) genau einmal auf und lehne Zyklen oder unbekannte Ziele ab.
5. **Aktivierung**: Übergib die Kontrolle an den Ziel-Skill (`skills/<ziel-skill>/SKILL.md`) und beende das Routing.
