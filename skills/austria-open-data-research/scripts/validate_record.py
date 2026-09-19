#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

REQUIRED_DATASET_FIELDS = [
    "dataset_id",
    "title",
    "publisher",
    "retrieved_at",
    "primary_source",
    "distributions",
    "provenance",
]

REQUIRED_DISTRIBUTION_FIELDS = ["url"]


def validate_dataset(record):
    errors = []
    for field in REQUIRED_DATASET_FIELDS:
        if field not in record:
            errors.append(f"missing dataset field: {field}")

    distributions = record.get("distributions", [])
    if not isinstance(distributions, list):
        errors.append("distributions must be a list")
    else:
        for idx, distribution in enumerate(distributions):
            if not isinstance(distribution, dict):
                errors.append(f"distribution {idx} must be an object")
                continue
            for field in REQUIRED_DISTRIBUTION_FIELDS:
                if not distribution.get(field):
                    errors.append(f"distribution {idx} missing field: {field}")

    provenance = record.get("provenance")
    if provenance is not None and not isinstance(provenance, dict):
        errors.append("provenance must be an object")

    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate canonical Austria Open Data dataset JSON.")
    parser.add_argument("json_file", type=Path)
    args = parser.parse_args()

    try:
        payload = json.loads(args.json_file.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"invalid JSON: {exc}", file=sys.stderr)
        return 2

    records = payload if isinstance(payload, list) else [payload]
    all_errors = []

    for idx, record in enumerate(records):
        if not isinstance(record, dict):
            all_errors.append(f"record {idx} must be an object")
            continue
        for error in validate_dataset(record):
            all_errors.append(f"record {idx}: {error}")

    if all_errors:
        for error in all_errors:
            print(error, file=sys.stderr)
        return 1

    print(f"valid: {len(records)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
