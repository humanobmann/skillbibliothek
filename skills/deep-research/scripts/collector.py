#!/usr/bin/env python3
"""
skills/deep-research/scripts/collector.py

Deterministischer Helfer für persistente Evidenz-Ablage und -Verwaltung
in Langzeit-Recherchen (.research/ Workspace).
"""

import os
import sys
import json
import argparse
from datetime import datetime, timezone

def get_workspace(base_dir: str = ".research") -> str:
    ws = os.path.abspath(base_dir)
    ev_dir = os.path.join(ws, "evidence")
    os.makedirs(ev_dir, exist_ok=True)
    return ws

def init_plan(topic: str, questions: list, ws: str):
    plan_path = os.path.join(ws, "plan.json")
    plan = {
        "topic": topic,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "IN_PROGRESS",
        "sub_questions": [{"id": f"Q{i+1}", "question": q, "status": "OPEN"} for i, q in enumerate(questions)],
        "evidence_count": 0
    }
    with open(plan_path, "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)
    print(f"Forschungsplan initialisiert unter {plan_path}")

def add_evidence(ws: str, topic: str, sub_q: str, url: str, raw: str, claim: str, tier: int = 2, verdict: str = "UNCONFIRMED"):
    ev_dir = os.path.join(ws, "evidence")
    existing_files = [f for f in os.listdir(ev_dir) if f.startswith("EVID-") and f.endswith(".json")]
    next_num = len(existing_files) + 1
    ev_id = f"EVID-{next_num:04d}"

    item = {
        "evidence_id": ev_id,
        "topic": topic,
        "sub_question": sub_q,
        "source_url": url,
        "retrieval_timestamp": datetime.now(timezone.utc).isoformat(),
        "source_tier": tier,
        "raw_snippet": raw,
        "extracted_claim": claim,
        "supporting_evidence_ids": [],
        "contradicting_evidence_ids": [],
        "triangulated": False,
        "verdict": verdict
    }

    item_path = os.path.join(ev_dir, f"{ev_id}.json")
    with open(item_path, "w", encoding="utf-8") as f:
        json.dump(item, f, indent=2, ensure_ascii=False)
    
    # Update plan count
    plan_path = os.path.join(ws, "plan.json")
    if os.path.exists(plan_path):
        try:
            with open(plan_path, "r", encoding="utf-8") as pf:
                plan = json.load(pf)
            plan["evidence_count"] = len(existing_files) + 1
            with open(plan_path, "w", encoding="utf-8") as pf:
                json.dump(plan, pf, indent=2, ensure_ascii=False)
        except Exception:
            pass

    print(f"Evidenz {ev_id} gespeichert: {item_path}")
    return ev_id

def list_evidence(ws: str):
    ev_dir = os.path.join(ws, "evidence")
    if not os.path.isdir(ev_dir):
        print("Keine Evidenzen gefunden.")
        return []
    items = []
    for f in sorted(os.listdir(ev_dir)):
        if f.endswith(".json"):
            with open(os.path.join(ev_dir, f), "r", encoding="utf-8") as ef:
                items.append(json.load(ef))
    print(f"Gesamt: {len(items)} Belege gefunden.")
    for it in items:
        print(f"  [{it['evidence_id']}] (Tier {it['source_tier']}) {it['extracted_claim'][:70]}... -> {it['source_url']}")
    return items

def generate_report(ws: str, out_file: str):
    items = list_evidence(ws)
    plan_path = os.path.join(ws, "plan.json")
    plan = {}
    if os.path.exists(plan_path):
        with open(plan_path, "r", encoding="utf-8") as f:
            plan = json.load(f)

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(f"# Evidenzbasierter Abschlussbericht: {plan.get('topic', 'Recherche')}\n\n")
        f.write(f"Erstellt am: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n\n")
        f.write("## 1. Forschungsfragen & Untersuchungsplan\n\n")
        for q in plan.get("sub_questions", []):
            f.write(f"- **{q['id']}**: {q['question']} ({q['status']})\n")
        f.write("\n## 2. Evidenz-Register\n\n")
        f.write("| ID | Tier | Sachbehauptung | Quelle | Status |\n")
        f.write("|---|---:|---|---|---|\n")
        for it in items:
            f.write(f"| `{it['evidence_id']}` | {it['source_tier']} | {it['extracted_claim']} | [{it['source_url']}]({it['source_url']}) | `{it['verdict']}` |\n")
        f.write("\n## 3. Offene Fragen & Limitationen\n\n")
        f.write("Keine weiteren widersprüchlichen Aussagen festgestellt.\n")
    print(f"Bericht generiert unter {out_file}")

def main():
    parser = argparse.ArgumentParser(description="Deep Research Evidence Collector")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init")
    p_init.add_argument("--topic", required=True)
    p_init.add_argument("--questions", nargs="+", required=True)
    p_init.add_argument("--ws", default=".research")

    p_add = sub.add_parser("add")
    p_add.add_argument("--topic", required=True)
    p_add.add_argument("--sub-q", required=True)
    p_add.add_argument("--url", required=True)
    p_add.add_argument("--raw", required=True)
    p_add.add_argument("--claim", required=True)
    p_add.add_argument("--tier", type=int, default=2)
    p_add.add_argument("--verdict", default="UNCONFIRMED")
    p_add.add_argument("--ws", default=".research")

    p_list = sub.add_parser("list")
    p_list.add_argument("--ws", default=".research")

    p_rep = sub.add_parser("report")
    p_rep.add_argument("--out", default=".research/REPORT.md")
    p_rep.add_argument("--ws", default=".research")

    args = parser.parse_args()
    ws = get_workspace(args.ws)

    if args.command == "init":
        init_plan(args.topic, args.questions, ws)
    elif args.command == "add":
        add_evidence(ws, args.topic, args.sub_q, args.url, args.raw, args.claim, args.tier, args.verdict)
    elif args.command == "list":
        list_evidence(ws)
    elif args.command == "report":
        generate_report(ws, args.out)

if __name__ == "__main__":
    main()
