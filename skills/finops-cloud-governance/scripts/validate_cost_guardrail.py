#!/usr/bin/env python3
"""Validate a provider-neutral cloud cost guardrail manifest."""
import argparse
import json
import sys
from pathlib import Path

REQUIRED = {
    "cost_center",
    "workload_name",
    "monthly_budget_usd",
    "alert_thresholds_pct",
    "required_tags",
    "owner",
    "commitment_strategy",
    "anomaly_detection",
}
ALLOWED_COMMITMENT = {"on-demand", "reserved", "savings-plan", "spot-mixed"}
BASELINE_TAGS = {"cost-center", "owner", "environment"}


def validate(data: dict) -> list[str]:
    errors = []
    missing = sorted(REQUIRED - data.keys())
    if missing:
        errors.append("missing fields: " + ", ".join(missing))
    budget = data.get("monthly_budget_usd")
    if not isinstance(budget, (int, float)) or isinstance(budget, bool) or budget <= 0:
        errors.append("monthly_budget_usd must be a positive number")
    thresholds = data.get("alert_thresholds_pct")
    if not isinstance(thresholds, list) or not thresholds:
        errors.append("alert_thresholds_pct must be a non-empty list of percentages")
    else:
        if sorted(thresholds) != list(thresholds):
            errors.append("alert_thresholds_pct must be listed in ascending order")
        if max(thresholds) < 100:
            errors.append("alert_thresholds_pct must include a hard-limit threshold of at least 100")
    tags = data.get("required_tags")
    if not isinstance(tags, list) or not BASELINE_TAGS.issubset(set(tags)):
        errors.append("required_tags must include at least: " + ", ".join(sorted(BASELINE_TAGS)))
    if data.get("commitment_strategy") not in ALLOWED_COMMITMENT:
        errors.append("commitment_strategy must be one of " + ", ".join(sorted(ALLOWED_COMMITMENT)))
    if data.get("anomaly_detection") is not True:
        errors.append("anomaly_detection must be true")
    if not str(data.get("owner", "")).strip():
        errors.append("owner must be a non-empty accountable owner")
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
