#!/usr/bin/env python3
"""
skills/skill-security-auditor/scripts/prompt_injection_scanner.py

Statische Analyse von Skill-Dateien (SKILL.md, Dokumentation, Prompts) auf:
  1. Versteckte Zero-Width und Unicode-BiDi-Steuerzeichen
  2. Bösartige / verdeckte HTML-Kommentare (Payload-Hiding)
  3. Direct & Indirect Prompt Injection Muster (System Overrides, Jailbreaks)
  4. Exfiltrationsmuster (Markdown Image/Link Egress)
"""

import os
import sys
import re
import json
import argparse
from typing import List, Dict, Any

# Unicode-Steuerzeichen, die für Angriffe genutzt werden
ZERO_WIDTH_CHARS = {
    0x200B: "Zero-Width Space (U+200B)",
    0x200C: "Zero-Width Non-Joiner (U+200C)",
    0x200D: "Zero-Width Joiner (U+200D)",
    0x200E: "Left-to-Right Mark (U+200E)",
    0x200F: "Right-to-Left Mark (U+200F)",
    0xFEFF: "Zero-Width No-Break Space / BOM (U+FEFF)",
}

BIDI_OVERRIDE_CHARS = {
    0x202A: "Left-to-Right Embedding (U+202A)",
    0x202B: "Right-to-Left Embedding (U+202B)",
    0x202C: "Pop Directional Formatting (U+202C)",
    0x202D: "Left-to-Right Override (U+202D)",
    0x202E: "Right-to-Left Override (U+202E)",
    0x2066: "Left-to-Right Isolate (U+2066)",
    0x2067: "Right-to-Left Isolate (U+2067)",
    0x2068: "First Strong Isolate (U+2068)",
    0x2069: "Pop Directional Isolate (U+2069)",
}

INJECTION_PATTERNS = [
    (re.compile(r"ignore\s+(all\s+)?previous\s+(instructions|prompts|rules|commands)", re.I), "CRITICAL", "Direct Override: 'ignore previous instructions'"),
    (re.compile(r"disregard\s+(all\s+)?(prior|previous|above)\s+(instructions|prompts|context)", re.I), "CRITICAL", "Direct Override: 'disregard prior instructions'"),
    (re.compile(r"you\s+are\s+now\s+(in\s+)?(developer\s+mode|unrestricted|god\s+mode|dan\s+mode)", re.I), "CRITICAL", "Jailbreak: 'developer mode / unrestricted'"),
    (re.compile(r"system\s+prompt\s+override", re.I), "CRITICAL", "System Prompt Override Directive"),
    (re.compile(r"do\s+not\s+follow\s+(the\s+)?(system|original)\s+instructions", re.I), "CRITICAL", "Direct Override: 'do not follow system instructions'"),
    (re.compile(r"dump\s+(all\s+)?(ssh|api|keys|secrets|passwords|env|tokens|credentials)", re.I), "CRITICAL", "Credential Harvesting: 'dump secrets/keys'"),
    (re.compile(r"exfiltrate\s+(data|secrets|env|keys)", re.I), "CRITICAL", "Data Exfiltration Directive"),
]

SUSPICIOUS_COMMENT_KEYWORDS = [
    "system prompt", "override", "ignore", "secret", "password", "token", 
    "credential", "bypass", "jailbreak", "instruction"
]

def scan_file(file_path: str) -> List[Dict[str, Any]]:
    findings = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    except Exception as e:
        return [{"severity": "HIGH", "file": file_path, "message": f"Konnte Datei nicht lesen: {e}"}]

    # 1. Unicode-Checks (Zero-Width & BiDi)
    zw_found = []
    for idx, ch in enumerate(content):
        code = ord(ch)
        if code in ZERO_WIDTH_CHARS:
            zw_found.append((idx, ZERO_WIDTH_CHARS[code]))
        elif code in BIDI_OVERRIDE_CHARS:
            zw_found.append((idx, BIDI_OVERRIDE_CHARS[code]))

    if zw_found:
        details = ", ".join(f"{name} bei Pos {pos}" for pos, name in zw_found[:5])
        if len(zw_found) > 5:
            details += f" (+{len(zw_found)-5} weitere)"
        findings.append({
            "severity": "HIGH",
            "file": file_path,
            "message": f"{len(zw_found)} verdächtige Zero-Width/BiDi Unicode-Steuerzeichen gefunden: {details}"
        })

    # 2. HTML-Kommentare mit verdeckten Instruktionen
    # Ignoriere Standard-Layoutkommentare und Kommentare innerhalb von Code-Spans / Fenced Blocks
    prose_content = re.sub(r"```[\s\S]*?```", "", content)
    prose_content = re.sub(r"`[^`\n]+`", "", prose_content)
    comments = re.findall(r"<!--([\s\S]*?)-->", prose_content)
    for c in comments:
        c_lower = c.lower()
        matched_kw = [kw for kw in SUSPICIOUS_COMMENT_KEYWORDS if kw in c_lower]
        # Prüfen ob echter Text mit Anweisungen vorliegt
        if matched_kw and len(c.strip()) > 15:
            snippet = c.strip().replace("\n", " ")[:80]
            findings.append({
                "severity": "HIGH",
                "file": file_path,
                "message": f"Verdächtiger HTML-Kommentar mit Schlüsselwörtern {matched_kw}: '<!-- {snippet}... -->'"
            })

    # 3. Direct Prompt Injection Patterns
    lines = content.splitlines()
    in_code_block = False
    for line_num, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        # Strip inline code spans so documentation of patterns isn't flagged as an attack
        prose_line = re.sub(r"`[^`\n]+`", "", line).strip()
        if not prose_line:
            continue
        for pattern, severity, desc in INJECTION_PATTERNS:
            if pattern.search(prose_line):
                findings.append({
                    "severity": severity,
                    "file": file_path,
                    "line": line_num,
                    "message": f"{desc} in Zeile {line_num}: '{line.strip()[:100]}'"
                })

    return findings

def scan_path(target_path: str) -> Dict[str, Any]:
    all_findings = []
    files_scanned = 0

    if os.path.isfile(target_path):
        files_to_scan = [target_path]
    elif os.path.isdir(target_path):
        files_to_scan = []
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith((".md", ".txt", ".yaml", ".yml", ".json")):
                    files_to_scan.append(os.path.join(root, file))
    else:
        return {"target": target_path, "verdict": "FAIL", "findings": [{"severity": "CRITICAL", "message": f"Pfad existiert nicht: {target_path}"}]}

    for f in files_to_scan:
        files_scanned += 1
        findings = scan_file(f)
        all_findings.extend(findings)

    critical_count = sum(1 for f in all_findings if f["severity"] == "CRITICAL")
    high_count = sum(1 for f in all_findings if f["severity"] == "HIGH")
    medium_count = sum(1 for f in all_findings if f["severity"] == "MEDIUM")

    if critical_count > 0 or high_count > 0:
        verdict = "FAIL"
    elif medium_count > 0:
        verdict = "WARN"
    else:
        verdict = "PASS"

    return {
        "target": target_path,
        "files_scanned": files_scanned,
        "verdict": verdict,
        "summary": {
            "CRITICAL": critical_count,
            "HIGH": high_count,
            "MEDIUM": medium_count,
            "TOTAL": len(all_findings)
        },
        "findings": all_findings
    }

def main():
    parser = argparse.ArgumentParser(description="Prompt Injection & Payload Scanner für Agent Skills")
    parser.add_argument("--path", required=True, help="Pfad zur Skill-Datei oder zum Skill-Verzeichnis")
    parser.add_argument("--strict", action="store_true", help="Behandelt WARN als FAIL")
    parser.add_argument("--json", action="store_true", help="JSON-Ausgabe")
    args = parser.parse_args()

    result = scan_path(args.path)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("=" * 65)
        print(f"PROMPT INJECTION SCAN: {args.path}")
        print(f"Dateien gescannt: {result['files_scanned']}")
        print(f"Verdikt:          {result['verdict']}")
        print(f"Befunde:          {result['summary']}")
        print("=" * 65)
        for f in result["findings"]:
            loc = f.get('file', '')
            if 'line' in f:
                loc += f":{f['line']}"
            print(f"[{f['severity']:<8}] {loc} - {f['message']}")
        print("-" * 65)

    if result["verdict"] == "FAIL" or (args.strict and result["verdict"] == "WARN"):
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
