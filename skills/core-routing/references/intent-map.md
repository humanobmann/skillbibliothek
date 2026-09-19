# Intent Mapping & Routing Matrix

Diese Matrix definiert die deterministische Zuordnung von Benutzer-Intents zu spezialisierten Fachskills der Bibliothek.

---

## 1. Primäre Intent-Tabelle

| Domäne / Intent | Typische Signalbegriffe (Trigger) | Zielskill | Nicht aktivieren bei (Negativ-Trigger) | Delegation / Anschluss-Skill |
|---|---|---|---|---|
| **Security Audit** | "prüfe skill auf sicherheit", "scan skill", "security audit", "ist skill sicher" | `skills/skill-security-auditor` | Standard Anwendungs-Code Review | Bei reinem Code-Stil an `code-review-excellence` |
| **Mehrstufige Recherche** | "deep research", "recherchiere tiefgehend", "umfassender marktbericht", "evidenz sammeln" | `skills/deep-research` | Einfache Faktenfragen (Wetter, Definitionen) | Nach Recherche an `fact-check` oder Text-Skills |
| **Code Review & QA** | "review PR", "prüfe code-änderungen", "code review", "analysiere diff" | `skills/code-review-excellence` | Vollständiger Security Penetration Test | Bei schweren Schwachstellen an `skill-security-auditor` |
| **Skill-Erstellung** | "erstelle skill", "neuer agent skill", "validiere skill", "baue skill" | `skills/skill-creator` | Normale Anwendung existierender Skills | Nach Erstellung an `skill-security-auditor` |
| **Git Commit & Release** | "erstelle commit", "conventional commit", "write release notes", "git commit" | `skills/git-commit-pro` | Reine Statusabfragen (`git status`, `git branch`) | - |
| **Subagent Task Offloading** | "delegiere aufgabe", "günstig ausführen", "offload task", "qwen delegator" | `skills/qwen-task-delegator` | Komplexe Architektur-Entscheidungen | Nach Vorbereitung an Zielruntime |
| **Web Design & UX Guidelines**| "prüfe accessibility", "web design guidelines", "ui audit", "a11y review" | `skills/web-design-guidelines` | Reines Backend-Refactoring | Bei Designsystem-Umbau an `ui-ux-pro-max` / `shadcn-ui` |
| **UI/UX Entwurf & Redesign** | "neue benutzeroberfläche", "redesign ui", "ui-ux-pro-max" | `skills/ui-ux-pro-max` | Kleinere CSS-Tweaks oder A11y-Audits | An `interaction-design` für Animationen |
| **OSINT & Firmenrecherche** | "wer besitzt diese firma", "wirtschaftliche eigentümer", "ubo recherche" | `skills/who-really-owns-it` | Technische Domain/DNS-Recherche | An `who-owns-this-domain` für DNS/WHOIS |
| **Domain & DNS Ermittlung** | "whois lookup", "wer registrierte domain", "nameserver analyse" | `skills/who-owns-this-domain` | Firmenbuch- und Gesellschaftersuche | An `who-really-owns-it` für Unternehmensregister |
| **Faktencheck & Verifikation** | "prüfe fakt", "stimmt diese aussage", "quellenverifikation", "fact check" | `skills/fact-check` | Generative Textentwürfe ohne Prüfbedarf | Vor Veröffentlichung an `source-verification` |
| **Österreich Public Data** | "open data österreich", "data.gv.at", "parlamentsdaten wien" | `skills/austria-open-data-research` | Allgemeine weltweite Recherchen | An `politik-analyse` für Interpretation |

---

## 2. Relegations- und Konfliktregeln

1. **Code Review vs. Security Audit**:
   - `code-review-excellence` bewertet funktionale Korrektheit, Architektur, Wartbarkeit, Typisierung und Stil.
   - `skill-security-auditor` prüft bösartige Injection-Vektoren, RCE und Supply-Chain-Risiken.
   - **Regel**: Ein Code Review löst keinen automatischen Deep Security Audit aus, es sei denn, verdächtige Muster werden im Diff explizit identifiziert.

2. **Deep Research vs. Einfache Faktenabfrage**:
   - `deep-research` wird **nicht** für einfache Einzelfragen ("Wie hoch ist der Mount Everest?") geladen.
   - **Regel**: Nur bei mehrdimensionalen, komplexen oder verifikationsbedürftigen Themen aktivieren.

3. **Domain Ownership vs. Corporate Ownership**:
   - `who-owns-this-domain` besitzt DNS, IP, RDAP, WHOIS.
   - `who-really-owns-it` besitzt Handelsregister, Gesellschafter, Beneficial Ownership.
