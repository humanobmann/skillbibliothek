#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

PLACEHOLDER_RE = re.compile(r"<[^>]+>")


def load_registry(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def replace_value(value, ctx):
    if isinstance(value, dict):
        return {k: replace_value(v, ctx) for k, v in value.items()}
    if isinstance(value, list):
        if value == ["<DATE_RANGE>"]:
            if ctx.get("date_start") and ctx.get("date_end"):
                return [ctx["date_start"], ctx["date_end"]]
            return value
        if value == ["<YYYY-MM-DD>", "<YYYY-MM-DD>"]:
            if ctx.get("date_start") and ctx.get("date_end"):
                return [ctx["date_start"], ctx["date_end"]]
            return value
        return [replace_value(v, ctx) for v in value]
    if not isinstance(value, str):
        return value
    mapping = {
        "<GP>": ctx.get("gp"),
        "<YEAR>": ctx.get("year"),
        "<PAD>": ctx.get("pad"),
    }
    if value in mapping and mapping[value] is not None:
        return mapping[value]
    return value


def unresolved(obj):
    found = []
    if isinstance(obj, dict):
        for value in obj.values():
            found.extend(unresolved(value))
    elif isinstance(obj, list):
        for value in obj:
            found.extend(unresolved(value))
    elif isinstance(obj, str):
        found.extend(PLACEHOLDER_RE.findall(obj))
    return sorted(set(found))


def select_datasets(registry, ids=None, required_only=False):
    items = registry.get("datasets", [])
    if ids:
        wanted = set(ids)
        items = [x for x in items if x.get("id") in wanted]
        missing = wanted - {x.get("id") for x in items}
        if missing:
            raise SystemExit("Unknown registry id(s): " + ", ".join(sorted(missing)))
    if required_only:
        items = [x for x in items if x.get("required_for_masterprompt")]
    return items


def build_plan(registry, args):
    ctx = {
        "gp": args.gp,
        "year": args.year,
        "pad": args.pad,
        "date_start": args.date_start,
        "date_end": args.date_end,
    }
    plan = []
    for item in select_datasets(registry, getattr(args, "id", None), getattr(args, "required_only", False)):
        body = replace_value(item.get("body_template", {}), ctx)
        plan.append(
            {
                "id": item["id"],
                "name": item["name"],
                "method": item["method"],
                "url": registry["base_url"].rstrip("/") + item["endpoint"],
                "body": body,
                "unresolved": unresolved(body),
                "status": item.get("status"),
                "available": item.get("available"),
            }
        )
    return plan


def post_json(url, body, timeout, retries):
    payload = json.dumps(body, ensure_ascii=False).encode("utf-8")
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "OpenAI-Parliamentary-Research-Skill/1.0",
    }
    last_error = None
    for attempt in range(retries + 1):
        request = urllib.request.Request(url, data=payload, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read(), dict(response.headers), getattr(response, "status", 200)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            last_error = exc
            if attempt >= retries:
                break
            time.sleep(min(2 ** attempt, 8))
    raise RuntimeError(f"request failed after {retries + 1} attempt(s): {last_error}")


def get_bytes(url, timeout, retries):
    headers = {
        "Accept": "application/json, text/html, */*",
        "User-Agent": "OpenAI-Parliamentary-Research-Skill/1.0",
    }
    last_error = None
    for attempt in range(retries + 1):
        request = urllib.request.Request(url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read(), dict(response.headers), getattr(response, "status", 200)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            last_error = exc
            if attempt >= retries:
                break
            time.sleep(min(2 ** attempt, 8))
    raise RuntimeError(f"request failed after {retries + 1} attempt(s): {last_error}")


def safe_name(text):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", text).strip("_") or "response"


def write_result(out_dir, stem, raw, meta):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    raw_path = out_dir / f"{safe_name(stem)}.raw"
    raw_path.write_bytes(raw)
    sha = hashlib.sha256(raw).hexdigest()
    meta["sha256"] = sha
    meta["bytes"] = len(raw)
    meta_path = out_dir / f"{safe_name(stem)}.manifest.json"
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(str(raw_path))
    print(str(meta_path))


def add_context_args(parser):
    parser.add_argument("--gp")
    parser.add_argument("--year")
    parser.add_argument("--pad")
    parser.add_argument("--date-start")
    parser.add_argument("--date-end")


def cmd_plan(args):
    registry = load_registry(args.registry)
    plan = build_plan(registry, args)
    print(json.dumps(plan, ensure_ascii=False, indent=2))


def cmd_fetch(args):
    registry = load_registry(args.registry)
    plan = build_plan(registry, args)
    if len(plan) != 1:
        raise SystemExit("fetch requires exactly one --id")
    item = plan[0]
    if item["unresolved"]:
        raise SystemExit("unresolved placeholders: " + ", ".join(item["unresolved"]))
    if args.dry_run:
        print(json.dumps(item, ensure_ascii=False, indent=2))
        return
    raw, headers, status = post_json(item["url"], item["body"], args.timeout, args.retries)
    meta = {
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "registry_version": registry.get("version"),
        "registry_id": item["id"],
        "method": "POST",
        "url": item["url"],
        "body": item["body"],
        "http_status": status,
        "content_type": headers.get("Content-Type"),
    }
    write_result(args.out_dir, item["id"], raw, meta)


def cmd_detail(args):
    registry = load_registry(args.registry)
    relative = args.relative_url
    if not relative.startswith("/"):
        raise SystemExit("--relative-url must start with /")
    separator = "&" if "?" in relative else "?"
    url = registry["base_url"].rstrip("/") + relative + separator + "json=TRUE"
    if args.dry_run:
        print(json.dumps({"method": "GET", "url": url}, indent=2))
        return
    raw, headers, status = get_bytes(url, args.timeout, args.retries)
    meta = {
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "registry_version": registry.get("version"),
        "method": "GET",
        "url": url,
        "http_status": status,
        "content_type": headers.get("Content-Type"),
    }
    write_result(args.out_dir, "detail_" + safe_name(relative), raw, meta)


def main():
    parser = argparse.ArgumentParser(description="Plan and execute Austrian Parliament API requests from the skill registry.")
    sub = parser.add_subparsers(dest="command", required=True)

    plan = sub.add_parser("plan", help="Render registry templates without sending requests.")
    plan.add_argument("--registry", required=True)
    plan.add_argument("--id", action="append")
    plan.add_argument("--required-only", action="store_true")
    add_context_args(plan)
    plan.set_defaults(func=cmd_plan)

    fetch = sub.add_parser("fetch", help="Fetch one registry query and save immutable raw bytes plus manifest.")
    fetch.add_argument("--registry", required=True)
    fetch.add_argument("--id", action="append", required=True)
    fetch.add_argument("--required-only", action="store_true")
    add_context_args(fetch)
    fetch.add_argument("--out-dir", required=True)
    fetch.add_argument("--timeout", type=int, default=30)
    fetch.add_argument("--retries", type=int, default=2)
    fetch.add_argument("--dry-run", action="store_true")
    fetch.set_defaults(func=cmd_fetch)

    detail = sub.add_parser("detail", help="Fetch a ?json=TRUE detail page for a relative Parliament history URL.")
    detail.add_argument("--registry", required=True)
    detail.add_argument("--relative-url", required=True)
    detail.add_argument("--out-dir", required=True)
    detail.add_argument("--timeout", type=int, default=30)
    detail.add_argument("--retries", type=int, default=2)
    detail.add_argument("--dry-run", action="store_true")
    detail.set_defaults(func=cmd_detail)

    args = parser.parse_args()
    try:
        args.func(args)
    except KeyboardInterrupt:
        raise SystemExit(130)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
