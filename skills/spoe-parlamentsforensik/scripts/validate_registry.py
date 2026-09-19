#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

ALLOWED_STATUS = {"VERIFIED_DOC", "DOC_DRIFT", "RUNTIME_VERIFIED"}
EXPECTED_DATASETS = {f"OD{i:02d}" for i in range(1, 26)}


def fail(errors):
    for err in errors:
        print(f"ERROR: {err}", file=sys.stderr)
    raise SystemExit(1)


def main():
    parser = argparse.ArgumentParser(description="Validate the parliamentary API registry.")
    parser.add_argument("registry", type=Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.registry.read_text(encoding="utf-8"))
    except Exception as exc:
        fail([f"cannot read registry: {exc}"])

    errors = []
    for key in ("version", "verified_doc_date", "base_url", "datasets"):
        if key not in data:
            errors.append(f"missing top-level key: {key}")

    if not isinstance(data.get("datasets"), list) or not data.get("datasets"):
        errors.append("datasets must be a non-empty list")

    base_url = data.get("base_url", "")
    if not isinstance(base_url, str) or not base_url.startswith("https://www.parlament.gv.at"):
        errors.append("base_url must use the official parlament.gv.at HTTPS host")

    seen = set()
    prefixes = set()
    for idx, item in enumerate(data.get("datasets", []), start=1):
        where = f"datasets[{idx}]"
        if not isinstance(item, dict):
            errors.append(f"{where} is not an object")
            continue
        for key in ("id", "name", "method", "endpoint", "body_template", "docs_url", "status"):
            if key not in item:
                errors.append(f"{where} missing {key}")
        ident = item.get("id")
        if ident in seen:
            errors.append(f"duplicate id: {ident}")
        seen.add(ident)
        if isinstance(ident, str):
            match = re.match(r"^(OD\d{2})_", ident)
            if match:
                prefixes.add(match.group(1))
            else:
                errors.append(f"invalid dataset id prefix: {ident}")
        if item.get("method") != "POST":
            errors.append(f"{ident}: only POST is supported by this registry")
        endpoint = item.get("endpoint", "")
        if not isinstance(endpoint, str) or not endpoint.startswith("/Filter/"):
            errors.append(f"{ident}: endpoint must be a relative /Filter/ path")
        if not isinstance(item.get("body_template"), dict):
            errors.append(f"{ident}: body_template must be an object")
        docs_url = item.get("docs_url", "")
        if not isinstance(docs_url, str) or not docs_url.startswith("https://www.parlament.gv.at/"):
            errors.append(f"{ident}: docs_url must point to official Parliament documentation")
        if item.get("status") not in ALLOWED_STATUS:
            errors.append(f"{ident}: unsupported status {item.get('status')!r}")

    missing = sorted(EXPECTED_DATASETS - prefixes)
    extra = sorted(prefixes - EXPECTED_DATASETS)
    if missing:
        errors.append("missing documented dataset groups: " + ", ".join(missing))
    if extra:
        errors.append("unexpected dataset groups: " + ", ".join(extra))

    aux_ids = set()
    for idx, item in enumerate(data.get("auxiliary_queries", []), start=1):
        where = f"auxiliary_queries[{idx}]"
        if not isinstance(item, dict):
            errors.append(f"{where} is not an object")
            continue
        ident = item.get("id")
        if not ident:
            errors.append(f"{where} missing id")
        elif ident in seen or ident in aux_ids:
            errors.append(f"duplicate auxiliary id: {ident}")
        aux_ids.add(ident)
        if item.get("status") == "RUNTIME_VERIFIED" and not data.get("runtime_verified"):
            errors.append(f"{ident}: runtime verified item conflicts with registry runtime_verified=false")

    rules = data.get("coverage_rules", {})
    if not rules.get("show_all_is_not_proof"):
        errors.append("coverage_rules.show_all_is_not_proof must be true")
    if not rules.get("require_independent_partition_for_full_corpus"):
        errors.append("full-corpus runs must require an independent coverage partition")

    if errors:
        fail(errors)

    print(
        f"OK: registry {data['version']} contains {len(data['datasets'])} query templates "
        f"covering all 25 documented dataset groups; runtime_verified={bool(data.get('runtime_verified'))}"
    )


if __name__ == "__main__":
    main()
