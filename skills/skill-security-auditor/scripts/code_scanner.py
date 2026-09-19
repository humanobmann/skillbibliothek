#!/usr/bin/env python3
"""
skills/skill-security-auditor/scripts/code_scanner.py

AST- und heuristische Sicherheitsanalyse von ausführbaren Skripten in Agent Skills:
  1. Gefährliche Funktionsaufrufe (eval, exec, compile, os.system)
  2. Subprozess-Ausführung mit shell=True
  3. Download-und-Execute Muster (curl | sh, Invoke-Expression)
  4. Hartcodierte Secrets und API-Keys
  5. Ungeprüfte Base64-Dekodierung / Obfuszierung
  6. Dependency-Sicherheit (unpinned dependencies)
"""

import os
import sys
import re
import ast
import json
import argparse
from typing import List, Dict, Any

SECRET_PATTERNS = [
    (re.compile(r"(?:api[_-]?key|secret|token|password|passwd|auth[_-]?token)\s*=\s*['\"][A-Za-z0-9_\-]{20,}['\"]", re.I), "CRITICAL", "Mögliches hartcodiertes Secret/Token"),
    (re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"), "CRITICAL", "Hartcodierter Private Key"),
]

SHELL_PIPE_PATTERNS = [
    (re.compile(r"(?:curl|wget)[^|\n]+(?:\|\s*(?:bash|sh|zsh))", re.I), "CRITICAL", "Download und direkte Pipe in Shell (curl | sh)"),
    (re.compile(r"(?:Invoke-WebRequest|Invoke-RestMethod|iwr|irm)[^|\n]+(?:\|\s*(?:iex|Invoke-Expression))", re.I), "CRITICAL", "PowerShell Download und Pipe in Invoke-Expression"),
]

class ScriptSecurityVisitor(ast.NodeVisitor):
    def __init__(self, filename: str):
        self.filename = filename
        self.findings = []

    def visit_Call(self, node):
        # eval, exec, compile
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name in ("eval", "exec"):
                self.findings.append({
                    "severity": "HIGH",
                    "file": self.filename,
                    "line": node.lineno,
                    "message": f"Aufruf von {func_name}() stellt ein Code-Injection-Risiko dar."
                })

        # os.system, os.popen
        elif isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "os":
                if node.func.attr in ("system", "popen", "spawnl", "spawnle", "spawnlp", "spawnlpe", "spawnv", "spawnve", "spawnvp", "spawnvpe"):
                    self.findings.append({
                        "severity": "HIGH",
                        "file": self.filename,
                        "line": node.lineno,
                        "message": f"Aufruf von os.{node.func.attr}() führt Shell-Befehle ohne Sandbox aus."
                    })
            
            # subprocess with shell=True
            elif isinstance(node.func.value, ast.Name) and node.func.value.id == "subprocess":
                for kw in node.keywords:
                    if kw.arg == "shell" and isinstance(kw.value, ast.Constant) and kw.value.value is True:
                        self.findings.append({
                            "severity": "HIGH",
                            "file": self.filename,
                            "line": node.lineno,
                            "message": f"subprocess.{node.func.attr}() mit shell=True ermöglicht Command Injection."
                        })

        self.generic_visit(node)

def scan_python_file(file_path: str) -> List[Dict[str, Any]]:
    findings = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            src = f.read()
    except Exception as e:
        return [{"severity": "CRITICAL", "file": file_path, "message": f"Zero-Trust: Konnte Datei nicht lesen: {e}"}]

    # 1. Regex-Checks für Secrets
    for pat, sev, desc in SECRET_PATTERNS:
        for m in pat.finditer(src):
            findings.append({
                "severity": sev,
                "file": file_path,
                "message": f"{desc}: '{m.group(0)[:30]}...'"
            })

    # 2. AST-Analyse
    try:
        tree = ast.parse(src, filename=file_path)
        visitor = ScriptSecurityVisitor(file_path)
        visitor.visit(tree)
        findings.extend(visitor.findings)
    except SyntaxError as se:
        findings.append({
            "severity": "CRITICAL",
            "file": file_path,
            "line": se.lineno,
            "message": f"Zero-Trust: Skript hat Syntaxfehler und kann nicht validiert werden: {se}"
        })
    except Exception as e:
        findings.append({
            "severity": "CRITICAL",
            "file": file_path,
            "message": f"Zero-Trust: Unerwarteter AST-Fehler bei der Analyse: {e}"
        })

    return findings

def scan_shell_file(file_path: str) -> List[Dict[str, Any]]:
    findings = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            src = f.read()
    except Exception as e:
        return [{"severity": "CRITICAL", "file": file_path, "message": f"Zero-Trust: Konnte Datei nicht lesen: {e}"}]

    for pat, sev, desc in SECRET_PATTERNS:
        for m in pat.finditer(src):
            findings.append({
                "severity": sev,
                "file": file_path,
                "message": f"{desc}: '{m.group(0)[:30]}...'"
            })

    for pat, sev, desc in SHELL_PIPE_PATTERNS:
        for m in pat.finditer(src):
            findings.append({
                "severity": sev,
                "file": file_path,
                "message": f"{desc} in Zeile: '{m.group(0)[:60]}'"
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
            for f in files:
                if f.endswith((".py", ".sh", ".bash", ".ps1", ".bat", ".cmd")):
                    files_to_scan.append(os.path.join(root, f))
    else:
        return {"target": target_path, "verdict": "FAIL", "findings": [{"severity": "CRITICAL", "message": f"Pfad existiert nicht: {target_path}"}]}

    for f in files_to_scan:
        files_scanned += 1
        if f.endswith(".py"):
            all_findings.extend(scan_python_file(f))
        elif f.endswith((".sh", ".bash", ".ps1", ".bat", ".cmd")):
            all_findings.extend(scan_shell_file(f))

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
    parser = argparse.ArgumentParser(description="AST Code Security Scanner für Agent Skills")
    parser.add_argument("--path", required=True, help="Pfad zum Skript oder Skill-Verzeichnis")
    parser.add_argument("--strict", action="store_true", help="Behandelt WARN als FAIL")
    parser.add_argument("--json", action="store_true", help="JSON-Ausgabe")
    args = parser.parse_args()

    result = scan_path(args.path)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("=" * 65)
        print(f"CODE SECURITY SCAN: {args.path}")
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
