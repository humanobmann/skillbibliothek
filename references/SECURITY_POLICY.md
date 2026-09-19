# Security Policy: Agent Skills Bibliothek

## 1. Verbindliche Sicherheitsarchitektur (P0)

Diese Sicherheitsrichtlinie definiert die verbindlichen Qualitäts- und Security-Gates für alle Skills dieser Bibliothek gemäß dem Open Agent Skills Standard, wissenschaftlichen Erkenntnissen (u.a. SkillJect, SkillSecurer) und Zero-Trust-Prinzipien.

Skills sind ausführbare prozedurale Handlungsanweisungen für autonome Agenten. Sie besitzen Zugriff auf System-Tools, Terminals, Dateisysteme und Netzwerkressourcen und müssen daher wie ausführbarer Code behandelt werden.

---

## 2. Bedrohungsmodell (Threat Model)

Jeder Skill wird vor Aufnahme oder Aktualisierung gegen folgende Angriffsvektoren auditiert:

### 2.1 Prompt Injection & Instruction Overrides
- **Direct Prompt Injections**: Befehle im Frontmatter oder Anweisungstext, die versuchen, übergeordnete System-Prompts zu überschreiben (z. B. `Ignore previous instructions`, `System Override`, `You are now in Developer Mode`).
- **Indirect Prompt Injections**: Instruktionen, die dem Agenten vorgeben, Webinhalte oder externe Daten ungesehen als Systembefehle auszuführen.
- **Versteckte Steuerzeichen**: Zero-Width Space (`\u200b`), Zero-Width Joiner (`\u200d`), Bidirektionale Unicode-Steuerzeichen (`\u202e` RLO etc.), die Text für Menschen unsichtbar manipulieren.
- **Payload-Hiding in HTML-Kommentaren**: Injektionen in `<!-- ... -->` Blöcken.

### 2.2 Remote Code Execution (RCE) & Gefährliche Befehle
- **Dynamische Code-Ausführung**: Verwendung von `eval()`, `exec()`, `compile()` mit unvalidierten Eingaben in Python-Helfern.
- **Unsichere Shell-Subprozesse**: `subprocess.Popen/run/call(..., shell=True)` oder `os.system()`.
- **PowerShell / Bash Exploits**: `Invoke-Expression` (`iex`), `curl ... | bash`, `Invoke-WebRequest ... | iex`.
- **Obfuszierung**: Nicht deklarierte Base64-Codierung, Hex-Encodings oder polymorphe Skripte.

### 2.3 Exfiltration & Credential Harvesting
- Zugriff auf sensitive Pfade: `~/.ssh`, `~/.aws`, `~/.config`, `%APPDATA%`, Environment-Variablen (`*_TOKEN`, `*_KEY`, `*_SECRET`).
- Ungenehmigte Netzwerk-Egress-Calls an beliebige externe C2-Server.
- Hartcodierte API-Keys, Private Keys oder Passwörter in Skill-Dateien.

### 2.4 Supply-Chain & Dependency Risks
- Unpinned Dependencies in `requirements.txt` oder Skripten.
- Nicht auditierte transitive Paketinstallationen während der Skill-Ausführung.
- Pfad-Traversal (`../..`) außerhalb des Projektkontexts.

---

## 3. Sicherheits-Ergebnis- und Gate-Modell

Jede statische und dynamische Prüfung stuft Befunde in folgende Severity-Klassen ein:

| Severity | Definition | Konsequenz |
|---|---|---|
| **CRITICAL** | Bestätigte RCE, Prompt Injection, Shell-Pipes, Credential Harvesting, Hardcoded Secrets | Sofortiger Installationsstopp (`FAIL`), Skill gesperrt |
| **HIGH** | `shell=True`, ungeschütztes `eval/exec`, versteckte Unicode-Steuerzeichen, verdeckte HTML-Instruktionen | Sofortiger Installationsstopp (`FAIL`), manuelle Freigabe erforderlich |
| **MEDIUM** | Base64-Nutzung, unvalidierte Netzwerkaufrufe, unpinned Dependencies | Warnung (`WARN`), Prüfung erforderlich |
| **LOW** | Veraltete Syntax, unvollständige Fehlerbehandlung | Dokumentation, zulässig |
| **INFO** | Strukturelle Hinweise, Best-Practice-Empfehlungen | Keine Auswirkung |

### Verdikt-Definition:
- **`PASS`**: Keine Befunde der Stufen `CRITICAL` oder `HIGH`. Skill ist installations- und ausführungsreif.
- **`WARN`**: Geringfügige oder erklärbare Befunde (z. B. legitime Dokumentationsbeispiele). Freigabe unter Vorbehalt.
- **`FAIL`**: Mindestens ein Befund der Stufe `CRITICAL` oder `HIGH`, oder der Skill kann statisch nicht analysiert werden (**Zero-Trust Fallback**).

---

## 4. Automatisierte Audit-Gates

Vor jeder Freigabe in die Registry müssen folgende Scanner erfolgreich durchlaufen:
1. `python skills/skill-security-auditor/scripts/prompt_injection_scanner.py --path <skill_folder>`
2. `python skills/skill-security-auditor/scripts/code_scanner.py --path <skill_folder> --strict`
3. `pytest tests/test_security.py`

Kein Skill mit Status `FAIL` darf in die aktive Registry übernommen werden.
