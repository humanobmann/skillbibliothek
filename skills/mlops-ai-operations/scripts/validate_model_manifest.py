#!/usr/bin/env python3
"""Validate a minimal immutable model release manifest without third-party packages."""
import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED = {"model_name", "version", "source_commit", "dataset_digest", "metrics", "risk_owner", "approved_for"}
COMMIT_RE = re.compile(r"^[0-9a-f]{7,64}$")
SHA256_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
ALLOWED_ENVIRONMENTS = {"development", "staging", "production"}


def validate(data: dict) -> list[str]:
    errors = []
    missing = sorted(REQUIRED - data.keys())
    if missing:
        errors.append("missing fields: " + ", ".join(missing))
    if "source_commit" in data and not COMMIT_RE.fullmatch(str(data["source_commit"])):
        errors.append("source_commit must be a 7-64 character lowercase hexadecimal commit id")
    if "dataset_digest" in data and not SHA256_RE.fullmatch(str(data["dataset_digest"])):
        errors.append("dataset_digest must be sha256:<64 lowercase hex characters>")
    if "metrics" in data and not isinstance(data["metrics"], dict):
        errors.append("metrics must be an object")
    if "approved_for" in data and data["approved_for"] not in ALLOWED_ENVIRONMENTS:
        errors.append("approved_for must be development, staging, or production")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}))
        return 2
    errors = validate(data)
    print(json.dumps({"valid": not errors, "errors": errors}, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    sys.exit(main())
