#!/usr/bin/env python3
"""
scripts/validate_skills.py

Deterministischer Validator für die Agent Skills Bibliothek gemäß Open Agent Skills Standard.
Prüft:
  1. Struktur: Jedes Skill-Verzeichnis enthält SKILL.md
  2. Frontmatter: Gültiges YAML mit 'name' (^[a-z0-9-]+$, <=64 Zeichen, Verzeichnisübereinstimmung)
     und 'description' (<=1024 Zeichen, nicht-leer)
  3. Links: Alle relativen Markdown-Links zeigen auf existierende Dateien
  4. Skript-Integrität: Python-Skripte in scripts/ kompilieren fehlerfrei
"""

import os
import sys
import re
import ast
import json
import argparse

SKILLS_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "skills"))
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

NAME_PATTERN = re.compile(r"^[a-z0-9-]+$")

def strip_code_blocks(text: str) -> str:
    """Entfernt Codeblöcke und Inline-Code, um irreführende Markdown-Syntax zu ignorieren."""
    clean = re.sub(r"```[\s\S]*?```", "", text)
    clean = re.sub(r"`[^`\n]+`", "", clean)
    return clean

def parse_frontmatter(content: str):
    match = re.match(r"^---\s*\n([\s\S]*?)\n---", content)
    if not match:
        return None, "Kein gültiger YAML-Frontmatter Block (--- ... ---) am Dateianfang gefunden."
    
    yaml_text = match.group(1)
    fields = {}
    current_key = None
    multiline_val = []

    for line in yaml_text.splitlines():
        # Handle key: value
        key_match = re.match(r"^([a-zA-Z0-9_-]+):\s*(.*)$", line)
        if key_match:
            if current_key and multiline_val:
                fields[current_key] = "\n".join(multiline_val).strip()
                multiline_val = []
            current_key = key_match.group(1).strip()
            val = key_match.group(2).strip()
            if val in (">-", ">", "|", "|-"):
                multiline_val = []
            else:
                fields[current_key] = val.strip("\"'")
        elif current_key and line.startswith(("  ", "\t")):
            multiline_val.append(line.strip())
        elif current_key and not line.strip():
            multiline_val.append("")
            
    if current_key and multiline_val:
        fields[current_key] = "\n".join(multiline_val).strip()

    return fields, None

def validate_skill(skill_dir: str):
    errors = []
    warnings = []
    skill_name = os.path.basename(skill_dir)
    skill_md_path = os.path.join(skill_dir, "SKILL.md")

    if not os.path.isfile(skill_md_path):
        return {"skill": skill_name, "valid": False, "errors": ["SKILL.md fehlt"], "warnings": []}

    try:
        with open(skill_md_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    except Exception as e:
        return {"skill": skill_name, "valid": False, "errors": [f"Lesefehler: {e}"], "warnings": []}

    # 1. Frontmatter
    fields, err = parse_frontmatter(content)
    if err:
        errors.append(err)
    else:
        name = fields.get("name", "")
        desc = fields.get("description", "")

        if not name:
            errors.append("Frontmatter-Feld 'name' fehlt oder ist leer.")
        else:
            if not NAME_PATTERN.match(name):
                errors.append(f"Name '{name}' entspricht nicht der Spezifikation (nur Kleinbuchstaben, Ziffern, Bindestriche).")
            if len(name) > 64:
                errors.append(f"Name '{name}' ist länger als 64 Zeichen ({len(name)}).")
            if name != skill_name:
                warnings.append(f"Name '{name}' weicht vom Ordnernamen '{skill_name}' ab.")

        if not desc:
            errors.append("Frontmatter-Feld 'description' fehlt oder ist leer.")
        elif len(desc) > 1024:
            errors.append(f"Description überschreitet die Obergrenze von 1024 Zeichen ({len(desc)}).")

    # 2. Markdown Links in allen .md Dateien des Skills
    for root, _, files in os.walk(skill_dir):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                try:
                    with open(md_path, "r", encoding="utf-8", errors="replace") as f:
                        md_content = f.read()
                    
                    clean_md = strip_code_blocks(md_content)
                    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", clean_md)
                    for _, target in links:
                        target = target.strip()
                        if target.startswith(("http://", "https://", "mailto:", "#")):
                            continue
                        target_path = target.split("#")[0]
                        if not target_path:
                            continue
                        
                        resolved = os.path.normpath(os.path.join(root, target_path))
                        if not os.path.exists(resolved):
                            rel_md = os.path.relpath(md_path, REPO_ROOT)
                            errors.append(f"Defekter Link in {rel_md}: '{target}' zeigt auf nicht existierende Datei '{resolved}'.")
                except Exception as e:
                    errors.append(f"Fehler beim Prüfen von {file}: {e}")

    # 3. Python-Syntaxprüfungen für scripts/
    scripts_dir = os.path.join(skill_dir, "scripts")
    if os.path.isdir(scripts_dir):
        for script_file in os.listdir(scripts_dir):
            if script_file.endswith(".py"):
                py_path = os.path.join(scripts_dir, script_file)
                try:
                    with open(py_path, "r", encoding="utf-8", errors="replace") as pf:
                        py_src = pf.read()
                    ast.parse(py_src, filename=script_file)
                except SyntaxError as se:
                    errors.append(f"Python Syntaxfehler in scripts/{script_file}: {se}")

    return {
        "skill": skill_name,
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }

def main():
    parser = argparse.ArgumentParser(description="Validiert alle Skills in skills/")
    parser.add_argument("--json", action="store_true", help="Gibt das Ergebnis als JSON aus")
    parser.add_argument("--strict", action="store_true", help="Behandelt Warnungen als Fehler")
    parser.add_argument("--path", default=SKILLS_ROOT, help="Pfad zum Skills-Verzeichnis")
    args = parser.parse_args()

    skills_path = os.path.abspath(args.path)
    if not os.path.isdir(skills_path):
        print(f"Fehler: Skills-Verzeichnis '{skills_path}' nicht gefunden.", file=sys.stderr)
        sys.exit(1)

    skill_folders = [
        os.path.join(skills_path, d)
        for d in sorted(os.listdir(skills_path))
        if os.path.isdir(os.path.join(skills_path, d)) and not d.startswith(".")
    ]

    results = []
    total_errors = 0
    total_warnings = 0

    for folder in skill_folders:
        res = validate_skill(folder)
        results.append(res)
        total_errors += len(res["errors"])
        total_warnings += len(res["warnings"])

    passed = sum(1 for r in results if r["valid"])
    failed = len(results) - passed

    if args.json:
        output = {
            "total_skills": len(results),
            "passed": passed,
            "failed": failed,
            "total_errors": total_errors,
            "total_warnings": total_warnings,
            "skills": results,
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        print("=" * 60)
        print(f"SKILL VALIDATION REPORT: {len(results)} Skills geprüft")
        print("=" * 60)
        for r in results:
            if not r["valid"]:
                print(f"[FAIL] {r['skill']}:")
                for err in r["errors"]:
                    print(f"       - ERROR: {err}")
            elif r["warnings"]:
                print(f"[WARN] {r['skill']}:")
                for w in r["warnings"]:
                    print(f"       - WARN: {w}")
        
        print("-" * 60)
        print(f"Ergebnis: {passed}/{len(results)} bestanden, {failed} fehlgeschlagen, {total_warnings} Warnungen.")
        print("=" * 60)

    if failed > 0 or (args.strict and total_warnings > 0):
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
