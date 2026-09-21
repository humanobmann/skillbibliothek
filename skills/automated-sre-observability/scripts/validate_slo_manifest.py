#!/usr/bin/env python3
"""Validate a provider-neutral SLO/error-budget manifest."""
import argparse
import json
import sys
from pathlib import Path

REQUIRED = {
    "service_name",
    "sli_type",
    "slo_target",
    "measurement_window_days",
    "error_budget_policy",
    "burn_rate_alerting",
    "escalation_owner",
    "runbook_url",
}
ALLOWED_SLI_TYPES = {"availability", "latency", "error_rate", "throughput", "saturation"}


def validate(data: dict) -> list[str]:
    errors = []
    missing = sorted(REQUIRED - data.keys())
    if missing:
        errors.append("missing fields: " + ", ".join(missing))
    if "sli_type" in data and data["sli_type"] not in ALLOWED_SLI_TYPES:
        errors.append("sli_type must be one of " + ", ".join(sorted(ALLOWED_SLI_TYPES)))
    slo_target = data.get("slo_target")
    if not isinstance(slo_target, (int, float)) or isinstance(slo_target, bool) or not (0 < slo_target < 100):
        errors.append("slo_target must be a number strictly between 0 and 100 (100% is not a valid SLO)")
    window = data.get("measurement_window_days")
    if not isinstance(window, int) or isinstance(window, bool) or window <= 0:
        errors.append("measurement_window_days must be a positive integer")
    if not str(data.get("error_budget_policy", "")).strip():
        errors.append("error_budget_policy must describe a concrete, enforceable consequence")
    alerting = data.get("burn_rate_alerting")
    if not isinstance(alerting, list) or not alerting:
        errors.append("burn_rate_alerting must be a non-empty list of burn-rate windows")
    elif len(alerting) < 2:
        errors.append("burn_rate_alerting should include at least a fast and a slow burn window")
    if not str(data.get("escalation_owner", "")).strip():
        errors.append("escalation_owner must be a non-empty owner or rotation identifier")
    runbook_url = str(data.get("runbook_url", ""))
    if not runbook_url.strip():
        errors.append("runbook_url must be set; every page must link an actionable runbook")
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
