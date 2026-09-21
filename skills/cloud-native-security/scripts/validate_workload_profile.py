#!/usr/bin/env python3
"""Validate a provider-neutral JSON security profile for a Kubernetes workload."""
import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED = {"namespace", "service_account", "run_as_non_root", "allow_privilege_escalation", "capabilities_drop", "seccomp_profile", "image_digest"}
DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")


def validate(data: dict) -> list[str]:
    errors = []
    missing = sorted(REQUIRED - data.keys())
    if missing:
        errors.append("missing fields: " + ", ".join(missing))
    if data.get("run_as_non_root") is not True:
        errors.append("run_as_non_root must be true")
    if data.get("allow_privilege_escalation") is not False:
        errors.append("allow_privilege_escalation must be false")
    if "ALL" not in data.get("capabilities_drop", []):
        errors.append("capabilities_drop must contain ALL")
    if data.get("seccomp_profile") != "RuntimeDefault":
        errors.append("seccomp_profile must be RuntimeDefault")
    if "image_digest" in data and not DIGEST_RE.fullmatch(str(data["image_digest"])):
        errors.append("image_digest must be sha256:<64 lowercase hex characters>")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("profile", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.profile.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}))
        return 2
    errors = validate(data)
    print(json.dumps({"valid": not errors, "errors": errors}, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    sys.exit(main())
