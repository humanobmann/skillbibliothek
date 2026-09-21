#!/usr/bin/env python3
"""Validate a platform-neutral low-code solution governance manifest."""
import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED = {"solution_name", "solution_version", "business_owner", "technical_owner", "data_classification", "connectors", "dlp_reviewed", "environment_strategy", "source_control_path"}
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
REQUIRED_ENVS = {"development", "test", "production"}


def validate(data: dict) -> list[str]:
    errors = []
    missing = sorted(REQUIRED - data.keys())
    if missing:
        errors.append("missing fields: " + ", ".join(missing))
    if "solution_version" in data and not SEMVER_RE.fullmatch(str(data["solution_version"])):
        errors.append("solution_version must use MAJOR.MINOR.PATCH")
    if "connectors" in data and (not isinstance(data["connectors"], list) or not data["connectors"]):
        errors.append("connectors must be a non-empty list")
    if data.get("dlp_reviewed") is not True:
        errors.append("dlp_reviewed must be true before production promotion")
    if "environment_strategy" in data:
        envs = set(data["environment_strategy"]) if isinstance(data["environment_strategy"], list) else set()
        if not REQUIRED_ENVS.issubset(envs):
            errors.append("environment_strategy must include development, test, and production")
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
