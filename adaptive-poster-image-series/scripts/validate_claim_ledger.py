#!/usr/bin/env python3
"""Validate claim-ledger.json for factual poster production."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from quality_contract import CLAIM_STATUSES, CLAIM_TYPES, HARD_CLAIM_TYPES, HARD_SOURCE_TIERS, RISK_LEVELS, SOURCE_TIERS, norm

ID_RE = re.compile(r"^[A-Z][A-Z0-9_-]{0,31}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def fail(message: str) -> None:
    raise ValueError(message)


def validate(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    if not norm(data.get("series_id")):
        fail("series_id is required")
    if data.get("locale") != "de-AT":
        fail("locale must be 'de-AT'")
    claims = data.get("claims")
    if not isinstance(claims, list) or not claims:
        fail("claims must be a non-empty array")

    by_id: dict[str, dict[str, Any]] = {}
    for idx, item in enumerate(claims, start=1):
        if not isinstance(item, dict):
            fail(f"claim {idx}: object required")
        cid = norm(item.get("id"))
        if not ID_RE.match(cid):
            fail(f"claim {idx}: invalid id {cid!r}")
        if cid in by_id:
            fail(f"claim {idx}: duplicate id {cid!r}")
        ctype = norm(item.get("type")).lower()
        status = norm(item.get("status")).lower()
        if ctype not in CLAIM_TYPES:
            fail(f"claim {cid}: invalid type {ctype!r}")
        if status not in CLAIM_STATUSES:
            fail(f"claim {cid}: invalid status {status!r}")
        approved = norm(item.get("approved_text"))
        if not approved:
            fail(f"claim {cid}: approved_text required")
        risk = norm(item.get("risk")).lower()
        if risk not in RISK_LEVELS:
            fail(f"claim {cid}: risk must be one of {sorted(RISK_LEVELS)}")

        if ctype in HARD_CLAIM_TYPES:
            if status != "verified":
                fail(f"claim {cid}: hard claim requires status=verified")
            tier = norm(item.get("source_tier")).upper()
            if tier not in HARD_SOURCE_TIERS:
                fail(f"claim {cid}: hard claim requires source_tier A or B")
            if not norm(item.get("source_note")):
                fail(f"claim {cid}: hard claim requires source_note")
            if not norm(item.get("poster_source")):
                fail(f"claim {cid}: hard claim requires poster_source")
            retrieved = norm(item.get("retrieved_at"))
            if retrieved and not DATE_RE.match(retrieved):
                fail(f"claim {cid}: retrieved_at must be YYYY-MM-DD")
        else:
            tier = norm(item.get("source_tier")).upper()
            if tier and tier not in SOURCE_TIERS:
                fail(f"claim {cid}: invalid source_tier {tier!r}")

        if ctype == "political_opinion" and status not in {"opinion", "verified"}:
            fail(f"claim {cid}: political_opinion requires status opinion or verified")
        if ctype == "question" and status not in {"open_question", "verified"}:
            fail(f"claim {cid}: question requires status open_question or verified")
        if ctype == "unverified" and status != "unverified":
            fail(f"claim {cid}: type unverified requires status unverified")
        if ctype == "blocked" and status != "blocked":
            fail(f"claim {cid}: type blocked requires status blocked")

        by_id[cid] = item
    return by_id


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate claim ledger")
    p.add_argument("ledger", type=Path)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        data = json.loads(args.ledger.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            fail("ledger root must be an object")
        claims = validate(data)
        print(f"PASS: claim ledger contains {len(claims)} structurally valid claims.")
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
