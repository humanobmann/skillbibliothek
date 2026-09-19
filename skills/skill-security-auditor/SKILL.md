---
name: skill-security-auditor
description: Security audit and vulnerability scanning for AI agent skills before installation or activation. Detects prompt injection, zero-width unicode attacks, dangerous code execution (eval, exec, shell=True), credential harvesting, and supply chain risks.
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
---

# Skill Security Auditor

## Zweck & Verantwortung

Der `skill-security-auditor` fungiert als das primäre Sicherheitsgate (P0) für alle Agent Skills. Er analysiert neu installierte, fremde oder geänderte Skills vor ihrer Aktivierung auf bösartige Muster, Prompt Injections, versteckte Payloads und gefährliche Code-Ausführungen.

---

## Trigger-Bedingungen

### Positive Trigger (Wann aktivieren)
- "Prüfe diesen Skill auf Sicherheitsrisiken."
- "Führe einen Security Audit für den Ordner ./skills/<name> aus."
- "Scan skill before install."
- "Ist dieser SKILL.md sicher?"
- Vor jeder Neuaufnahme eines externen Skills in die Registry.

### Negative Trigger (Wann NICHT aktivieren)
- Standardmäßige Review-Anfragen von Anwendungs- oder Projekt-Code (dafür `code-review-excellence` nutzen).
- Reine Code-Linter-Aufrufe ohne Sicherheitskontext.
- Normale Git-Status- oder Commit-Fragen.

---

## Workflow Execution Plan

1. **Statische Struktur-Analyse**:
   Scanne das Zielverzeichnis nach unerwarteten ausführbaren Dateien, Binärdateien (.exe, .dll, .so) oder versteckten Dateien.

2. **Prompt Injection & Payload Scanning**:
   Führe den Prompt-Injection-Scanner aus:
   ```bash
   python skills/skill-security-auditor/scripts/prompt_injection_scanner.py --path <target_dir>
   ```
   Prüft auf:
   - Zero-Width & BiDi Unicode-Steuerzeichen (`\u200b`, `\u202e`)
   - Bösartige / verdeckte HTML-Kommentare
   - System Override Direktiven (`ignore previous instructions`, `jailbreak`)

3. **AST Code Risk Scanning**:
   Führe den AST-Code-Scanner für alle Skripte (.py, .sh, .ps1) aus:
   ```bash
   python skills/skill-security-auditor/scripts/code_scanner.py --path <target_dir> --strict
   ```
   Prüft auf:
   - `eval()`, `exec()`, `compile()`
   - `subprocess` mit `shell=True`
   - `os.system()` und ungeschützte Shell-Aufrufe
   - Download-and-pipe Muster (`curl | sh`, `iwr | iex`)
   - Hartcodierte Secrets und API-Tokens

4. **Vergabe des Sicherheits-Verdikts**:
   - `PASS`: Keine Befunde der Stufen `CRITICAL` oder `HIGH`. Skill darf registriert/genutzt werden.
   - `WARN`: Geringfügige, dokumentierte Befunde.
   - `FAIL`: Mindestens ein Befund der Stufe `CRITICAL` oder `HIGH`. **Installationsstopp**.

---

## Qualitätsgates & Fallbacks

- **Strict Mode Gate**: Jedes Vorkommen von `HIGH` oder `CRITICAL` Severity führt automatisch zum Verdikt `FAIL`.
- **Zero-Trust Fallback**: Kann ein Skript nicht statisch analysiert werden (z. B. Syntaxfehler oder Binärformat), gilt das Zero-Trust-Prinzip (`FAIL`). Keine automatische Aktivierung eines `FAIL`-Kandidaten.
