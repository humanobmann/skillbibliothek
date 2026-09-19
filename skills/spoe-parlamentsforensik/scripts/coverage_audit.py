#!/usr/bin/env python3
import argparse
import json
import sys
from collections import deque
from pathlib import Path


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def find_count_rows(obj):
    queue = deque([obj])
    while queue:
        current = queue.popleft()
        if isinstance(current, dict):
            if "count" in current and isinstance(current.get("rows"), list):
                return current.get("count"), current["rows"]
            queue.extend(current.values())
        elif isinstance(current, list):
            queue.extend(current)
    raise ValueError("no object containing both count and rows was found")


def row_key(row, key_indexes, key_fields):
    if key_indexes:
        if not isinstance(row, list):
            raise ValueError("--key-index requires list rows")
        try:
            selected = [row[i] for i in key_indexes]
        except IndexError as exc:
            raise ValueError(f"row is too short for key index: {exc}")
        return json.dumps(selected, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    if key_fields:
        if not isinstance(row, dict):
            raise ValueError("--key-field requires object rows")
        selected = [row.get(field) for field in key_fields]
        return json.dumps(selected, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def summarize(path, key_indexes, key_fields):
    count, rows = find_count_rows(load_json(path))
    keys = [row_key(row, key_indexes, key_fields) for row in rows]
    return {
        "path": str(path),
        "api_count": count,
        "rows": len(rows),
        "unique": len(set(keys)),
        "duplicates": len(rows) - len(set(keys)),
        "keys": set(keys),
    }


def main():
    parser = argparse.ArgumentParser(description="Audit count/rows and independent partition coverage for Parliament API responses.")
    parser.add_argument("--base", required=True)
    parser.add_argument("--partition", action="append", default=[])
    parser.add_argument("--key-index", action="append", type=int, default=[])
    parser.add_argument("--key-field", action="append", default=[])
    parser.add_argument("--output")
    args = parser.parse_args()

    if args.key_index and args.key_field:
        raise SystemExit("use either --key-index or --key-field, not both")

    try:
        base = summarize(args.base, args.key_index, args.key_field)
        parts = [summarize(p, args.key_index, args.key_field) for p in args.partition]
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)

    base_count_matches_rows = isinstance(base["api_count"], int) and base["api_count"] == base["rows"]
    base_rows_are_unique = base["rows"] == base["unique"]

    union = set()
    child_count_sum = 0
    child_counts_numeric = True
    part_output = []
    for part in parts:
        union.update(part["keys"])
        if isinstance(part["api_count"], int):
            child_count_sum += part["api_count"]
        else:
            child_counts_numeric = False
        part_output.append({k: v for k, v in part.items() if k != "keys"})

    if parts:
        base_equals_partition_union = base["keys"] == union
        child_counts_match_parent = (
            child_counts_numeric
            and isinstance(base["api_count"], int)
            and child_count_sum == base["api_count"]
        )
        status = "PASS" if (
            base_count_matches_rows
            and base_rows_are_unique
            and base_equals_partition_union
            and child_counts_match_parent
        ) else "FAIL"
    else:
        base_equals_partition_union = None
        child_counts_match_parent = None
        status = "PASS" if base_count_matches_rows and base_rows_are_unique else "FAIL"

    result = {
        "status": status,
        "base": {k: v for k, v in base.items() if k != "keys"},
        "partitions": part_output,
        "checks": {
            "base_count_matches_rows": base_count_matches_rows,
            "base_rows_are_unique": base_rows_are_unique,
            "base_equals_partition_union": base_equals_partition_union,
            "child_counts_match_parent": child_counts_match_parent,
        },
        "partition_union_unique": len(union) if parts else None,
        "child_count_sum": child_count_sum if parts and child_counts_numeric else None,
    }

    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    print(text, end="")
    raise SystemExit(0 if status == "PASS" else 2)


if __name__ == "__main__":
    main()
