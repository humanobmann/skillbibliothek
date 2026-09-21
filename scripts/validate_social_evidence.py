#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ALLOWED_MECHANISMS = {
    "RANKING",
    "SEARCH",
    "RECOMMENDATION_ELIGIBILITY",
    "POLICY",
    "MONETIZATION",
}
ALLOWED_VOLATILITY = {"high", "medium", "low"}
ALLOWED_PLATFORMS = {"facebook", "instagram", "tiktok", "youtube", "linkedin"}
ALLOWED_EVIDENCE_LEVELS = {"OFFICIAL", "ACCOUNT", "OBSERVED", "HYPOTHESIS"}
ALLOWED_STATUS = {"active", "superseded", "deprecated", "rejected"}
INACTIVE_STATUS = {"deprecated", "rejected"}
REQUIRED_FIELDS = {
    "source_id",
    "platform",
    "surface",
    "mechanism",
    "publisher",
    "title",
    "url",
    "retrieved",
    "claim_scope",
    "volatility",
    "status",
}
REQUIRED_CLAIM_FIELDS = {
    "claim",
    "evidence_level",
    "mechanism",
    "source_id",
    "surface",
    "observed_at",
    "limitation",
    "status",
}


def _nonempty_string(value: Any, field: str, source_id: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{source_id}: {field} must be a non-empty string")
    return value.strip()


def _valid_iso_date(value: str, field: str, source_id: str) -> None:
    try:
        dt.date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{source_id}: {field} must be YYYY-MM-DD") from exc


def validate_document(document: dict[str, Any]) -> None:
    if not isinstance(document, dict):
        raise ValueError("root must be an object")
    if document.get("schema_version") != 1:
        raise ValueError("schema_version must be 1")

    allowed = document.get("allowed_mechanisms")
    if not isinstance(allowed, list) or set(allowed) != ALLOWED_MECHANISMS:
        raise ValueError("allowed_mechanisms must exactly match the canonical mechanism set")

    retrieved = _nonempty_string(document.get("retrieved"), "retrieved", "root")
    _valid_iso_date(retrieved, "retrieved", "root")

    records = document.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("records must be a non-empty list")

    seen: set[str] = set()
    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"record {index}: object required")

        missing = REQUIRED_FIELDS - set(record)
        if missing:
            raise ValueError(f"record {index}: missing fields: {', '.join(sorted(missing))}")

        source_id = _nonempty_string(record.get("source_id"), "source_id", f"record {index}")
        if source_id in seen:
            raise ValueError(f"{source_id}: duplicate source_id")
        seen.add(source_id)

        platform = _nonempty_string(record.get("platform"), "platform", source_id)
        if platform not in ALLOWED_PLATFORMS:
            raise ValueError(f"{source_id}: unsupported platform {platform}")

        _nonempty_string(record.get("surface"), "surface", source_id)
        mechanism = _nonempty_string(record.get("mechanism"), "mechanism", source_id)
        if mechanism not in ALLOWED_MECHANISMS:
            raise ValueError(f"{source_id}: invalid mechanism {mechanism}")
        if "/" in mechanism:
            raise ValueError(f"{source_id}: combined mechanism values are forbidden")

        _nonempty_string(record.get("publisher"), "publisher", source_id)
        _nonempty_string(record.get("title"), "title", source_id)

        url = _nonempty_string(record.get("url"), "url", source_id)
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc:
            raise ValueError(f"{source_id}: url must be an absolute https URL")

        record_date = _nonempty_string(record.get("retrieved"), "retrieved", source_id)
        _valid_iso_date(record_date, "retrieved", source_id)

        scope = record.get("claim_scope")
        if not isinstance(scope, list) or not scope:
            raise ValueError(f"{source_id}: claim_scope must be a non-empty list")
        if any(not isinstance(item, str) or not item.strip() for item in scope):
            raise ValueError(f"{source_id}: claim_scope entries must be non-empty strings")

        volatility = _nonempty_string(record.get("volatility"), "volatility", source_id)
        if volatility not in ALLOWED_VOLATILITY:
            raise ValueError(f"{source_id}: volatility must be high, medium or low")

        status = _nonempty_string(record.get("status"), "status", source_id)
        if status not in ALLOWED_STATUS:
            raise ValueError(f"{source_id}: status must be one of {sorted(ALLOWED_STATUS)}")

    record_status_by_id = {r["source_id"]: r["status"] for r in records}

    claims = document.get("claims", [])
    if not isinstance(claims, list):
        raise ValueError("claims must be a list when present")

    seen_claims: set[str] = set()
    for index, claim in enumerate(claims, start=1):
        if not isinstance(claim, dict):
            raise ValueError(f"claim {index}: object required")

        missing = REQUIRED_CLAIM_FIELDS - set(claim)
        if missing:
            raise ValueError(f"claim {index}: missing fields: {', '.join(sorted(missing))}")

        claim_text = _nonempty_string(claim.get("claim"), "claim", f"claim {index}")
        if claim_text in seen_claims:
            raise ValueError(f"claim {index}: duplicate claim text")
        seen_claims.add(claim_text)

        evidence_level = _nonempty_string(claim.get("evidence_level"), "evidence_level", claim_text)
        if evidence_level not in ALLOWED_EVIDENCE_LEVELS:
            raise ValueError(f"{claim_text}: evidence_level must be one of {sorted(ALLOWED_EVIDENCE_LEVELS)}")

        mechanism = _nonempty_string(claim.get("mechanism"), "mechanism", claim_text)
        if mechanism not in ALLOWED_MECHANISMS:
            raise ValueError(f"{claim_text}: invalid mechanism {mechanism}")
        if "/" in mechanism:
            raise ValueError(f"{claim_text}: combined mechanism values are forbidden")

        claim_source_id = _nonempty_string(claim.get("source_id"), "source_id", claim_text)
        if claim_source_id not in record_status_by_id:
            raise ValueError(f"{claim_text}: source_id {claim_source_id} has no matching source record")

        _nonempty_string(claim.get("surface"), "surface", claim_text)

        observed_at = _nonempty_string(claim.get("observed_at"), "observed_at", claim_text)
        _valid_iso_date(observed_at, "observed_at", claim_text)

        _nonempty_string(claim.get("limitation"), "limitation", claim_text)

        claim_status = _nonempty_string(claim.get("status"), "status", claim_text)
        if claim_status not in ALLOWED_STATUS:
            raise ValueError(f"{claim_text}: status must be one of {sorted(ALLOWED_STATUS)}")

        if claim_status not in INACTIVE_STATUS and record_status_by_id[claim_source_id] in INACTIVE_STATUS:
            raise ValueError(
                f"{claim_text}: an active/superseded claim must not cite a deprecated/rejected source ({claim_source_id})"
            )

        if mechanism == "MONETIZATION" and claim_status not in INACTIVE_STATUS:
            scope_terms = {"ranking", "recommendation", "reach", "distribution"}
            if any(term in claim_text.lower() for term in scope_terms):
                raise ValueError(f"{claim_text}: a ranking/reach claim must not be derived from MONETIZATION-only evidence")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate structured social-platform evidence records")
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=Path("skills/social-platform-algorithm-core/references/evidence-records.json"),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        document = json.loads(args.path.read_text(encoding="utf-8"))
        validate_document(document)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 1
    print("PASS: social-platform evidence records satisfy the canonical schema.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
