#!/usr/bin/env python3
"""
scripts/context_benchmark.py

Misst den Context Footprint der Agent Skills Bibliothek:
  1. Discovery Footprint (Name + Description im Open Agent Skills Format)
  2. Full-Text Aktivierungs-Footprint (vollständige SKILL.md-Inhalte)
  3. Domain-Katalog Footprints
  4. Top 10 größte Skills zur Optimierung
"""

import os
import sys
import json
import argparse
import re

SKILLS_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "skills"))

def parse_frontmatter(content: str):
    m = re.match(r"^---\s*\n([\s\S]*?)\n---", content)
    if not m:
        return {}
    lines = m.group(1).splitlines()
    res = {}
    ck = None
    mv = []
    for line in lines:
        km = re.match(r"^([a-zA-Z0-9_-]+):\s*(.*)$", line)
        if km:
            if ck and mv:
                res[ck] = "\n".join(mv).strip()
                mv = []
            ck = km.group(1).strip()
            v = km.group(2).strip()
            if v in (">-", ">", "|", "|-"):
                mv = []
            else:
                res[ck] = v.strip("\"'")
        elif ck and line.startswith(("  ", "\t")):
            mv.append(line.strip())
    if ck and mv:
        res[ck] = "\n".join(mv).strip()
    return res

def benchmark(skills_path: str):
    skills_data = []
    
    for item in sorted(os.listdir(skills_path)):
        sp = os.path.join(skills_path, item)
        if os.path.isdir(sp) and not item.startswith("."):
            s_md = os.path.join(sp, "SKILL.md")
            if os.path.isfile(s_md):
                try:
                    with open(s_md, "r", encoding="utf-8", errors="replace") as f:
                        text = f.read()
                except Exception:
                    text = ""
                
                fm = parse_frontmatter(text)
                name = fm.get("name", item)
                desc = fm.get("description", "")
                
                # Discovery footprint = name + description
                discovery_chars = len(name) + len(desc)
                full_chars = len(text)
                
                skills_data.append({
                    "skill": item,
                    "name": name,
                    "desc_chars": len(desc),
                    "discovery_chars": discovery_chars,
                    "discovery_tokens": discovery_chars // 4,
                    "full_chars": full_chars,
                    "full_tokens": full_chars // 4,
                    "line_count": len(text.splitlines())
                })
    
    total_skills = len(skills_data)
    total_discovery_chars = sum(s["discovery_chars"] for s in skills_data)
    total_discovery_tokens = total_discovery_chars // 4
    total_full_chars = sum(s["full_chars"] for s in skills_data)
    total_full_tokens = total_full_chars // 4
    
    avg_discovery_tokens = total_discovery_tokens / total_skills if total_skills else 0
    avg_full_tokens = total_full_tokens / total_skills if total_skills else 0
    
    top_largest = sorted(skills_data, key=lambda x: x["full_chars"], reverse=True)[:10]

    return {
        "total_skills": total_skills,
        "total_discovery_chars": total_discovery_chars,
        "total_discovery_tokens": total_discovery_tokens,
        "avg_discovery_tokens_per_skill": round(avg_discovery_tokens, 1),
        "total_full_chars": total_full_chars,
        "total_full_tokens": total_full_tokens,
        "avg_full_tokens_per_skill": round(avg_full_tokens, 1),
        "context_savings_via_progressive_disclosure_pct": round((1 - (total_discovery_tokens / total_full_tokens)) * 100, 2) if total_full_tokens else 0,
        "top_10_largest_skills": top_largest,
        "skills": skills_data
    }

def main():
    parser = argparse.ArgumentParser(description="Context Footprint Benchmark für Agent Skills")
    parser.add_argument("--json", action="store_true", help="JSON-Ausgabe")
    parser.add_argument("--path", default=SKILLS_ROOT, help="Skills-Verzeichnis")
    args = parser.parse_args()

    data = benchmark(args.path)

    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print("=" * 65)
        print("CONTEXT FOOTPRINT & PROGRESSIVE DISCLOSURE BENCHMARK")
        print("=" * 65)
        print(f"Gesamtanzahl Skills:             {data['total_skills']}")
        print(f"Discovery Footprint (Gesamt):    {data['total_discovery_chars']:,} Zeichen (~{data['total_discovery_tokens']:,} Tokens)")
        print(f"Discovery pro Skill (Ø):         {data['avg_discovery_tokens_per_skill']} Tokens")
        print(f"Volltext Footprint (Gesamt):     {data['total_full_chars']:,} Zeichen (~{data['total_full_tokens']:,} Tokens)")
        print(f"Aktivierter Skill Volltext (Ø):  {data['avg_full_tokens_per_skill']} Tokens")
        print(f"Kontext-Einsparung (Discovery):  {data['context_savings_via_progressive_disclosure_pct']}%")
        print("-" * 65)
        print("TOP 10 GRÖSSTE SKILLS:")
        for s in data["top_10_largest_skills"]:
            print(f"  - {s['skill']:<35} {s['full_chars']:>6} Zeichen (~{s['full_tokens']:>5} Tokens, {s['line_count']:>4} Zeilen)")
        print("=" * 65)

if __name__ == "__main__":
    main()
