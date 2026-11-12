#!/usr/bin/env python3
"""Preflight a Design & Visual production job without pretending to inspect Canva."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ACCOUNTS = {"personal": "Peter", "ngo": "Peter", "party": "SPÖ", "parliamentary": "SPÖ"}
SIZES = {"feed_4_5": (1080, 1350), "story_9_16": (1080, 1920), "reel_cover_9_16": (1080, 1920)}
TYPES = {"canva_native", "image_only", "print_pdf", "image_to_design_experimental"}
STATES = {"Entwurf", "Geprüft", "Freigabe erforderlich", "Final"}
FINAL_FLAGS = ("text_exact_checked", "dimensions_checked", "brand_checked", "safe_area_checked", "render_checked")


def mapping(v: Any) -> dict[str, Any]:
    return v if isinstance(v, dict) else {}


def inspect(job: Any) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(job, dict):
        return {"pass": False, "errors": ["Job must be a JSON object"], "warnings": []}

    scope = job.get("project_scope")
    account = job.get("canva_account")
    if scope not in ACCOUNTS:
        errors.append("Unknown project_scope")
    elif account != ACCOUNTS[scope]:
        errors.append("Canva account conflicts with project_scope")
    if job.get("template_source_account") and job["template_source_account"] != account:
        errors.append("Cross-account template source is forbidden")

    out = mapping(job.get("output"))
    output_type = out.get("type")
    if output_type not in TYPES:
        errors.append("Unsupported output type; no HTML, iframe or fake Canva views")
    fmt = out.get("format")
    if fmt in SIZES:
        w, h = SIZES[fmt]
        if (out.get("width_px"), out.get("height_px")) != (w, h):
            errors.append(f"Format {fmt} requires {w} x {h} px")
    elif fmt is None:
        errors.append("output.format is required")
    width, height = out.get("width_px"), out.get("height_px")
    if type(width) is not int or type(height) is not int or width <= 0 or height <= 0:
        errors.append("Positive numeric width_px and height_px are required")

    assets = mapping(job.get("assets"))
    logo = mapping(assets.get("logo"))
    person = mapping(assets.get("person"))
    if logo and logo.get("origin") != "approved_original":
        errors.append("Logo must be an approved original")
    if person.get("real_person") and person.get("ai_replaced"):
        errors.append("Unapproved replacement of a real person is forbidden")

    release = mapping(job.get("release"))
    state = release.get("status")
    if state not in STATES:
        errors.append("Unknown release status")
    if release.get("automatic_publication") is True:
        errors.append("Automatic publication is forbidden")

    qa = mapping(job.get("qa"))
    content = mapping(job.get("content"))
    if state == "Final":
        if release.get("human_approved") is not True:
            errors.append("Final requires recorded human approval")
        for flag in FINAL_FLAGS:
            if qa.get(flag) is not True:
                errors.append(f"Final requires qa.{flag}=true")
        if person.get("real_person") and qa.get("person_identity_checked") is not True:
            errors.append("Final real-person design requires identity comparison")
        if content.get("factual_claims"):
            if not content.get("source_refs") or qa.get("sources_checked") is not True:
                errors.append("Final factual content requires sources and source check")
        if output_type == "image_to_design_experimental" and qa.get("editable_layers_checked") is not True:
            errors.append("Converted image needs verified editable layers")
    else:
        if not qa:
            warnings.append("QA not recorded; a draft must not be published")
        if output_type == "image_to_design_experimental":
            warnings.append("Converted image needs individual layer inspection")
    if not job.get("campaign_id"):
        warnings.append("No campaign_id")
    return {"pass": not errors, "errors": errors, "warnings": warnings}


def main() -> int:
    p = argparse.ArgumentParser(description="Validate a Design & Visual job")
    p.add_argument("job", type=Path)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    try:
        job = json.loads(args.job.read_text(encoding="utf-8"))
        result = inspect(job)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        result = {"pass": False, "errors": [f"Cannot read job: {exc}"], "warnings": []}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("PASS" if result["pass"] else "FAIL")
        for kind in ("errors", "warnings"):
            for message in result[kind]:
                print(f"{kind}: {message}")
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
