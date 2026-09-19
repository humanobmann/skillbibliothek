#!/usr/bin/env python3
from __future__ import annotations

import math
import re
from typing import Any

CLAIM_TYPES = {
    "fact", "auditor_finding", "attributed_statement", "quote",
    "political_opinion", "question", "call_to_action", "unverified", "blocked",
}
HARD_CLAIM_TYPES = {"fact", "auditor_finding", "attributed_statement", "quote"}
VISIBLE_CONTENT_TYPES = CLAIM_TYPES - {"unverified", "blocked"}
CLAIM_STATUSES = {"verified", "opinion", "open_question", "unverified", "blocked"}
SOURCE_TIERS = {"A", "B", "C", "D"}
HARD_SOURCE_TIERS = {"A", "B"}
RISK_LEVELS = {"low", "medium", "high"}

INPUT_MODES = {"theme", "ten_texts", "ten_templates"}
BRANDING_MODES = {"none", "user_provided"}
AUSTRIA_STRATEGIES = {"contextual_not_symbolic", "not_applicable", "explicit_symbolic"}
REFERENCE_STRATEGIES = {"principles_not_copy"}
DESIGN_SYSTEMS = {"civic_editorial_red_ivory"}
DESIGN_VARIANTS = {
    "hero_type_photo", "oversize_keyword_photo", "type_graphic_photo",
    "number_led_poster", "typographic_signal", "quiet_close_poster",
}
SLOT_ROLES = {
    "hook", "context", "fact", "evidence", "finding", "contrast",
    "explanation", "question", "demand", "close",
}
RENDER_STRATEGIES = {
    "photo_editorial", "typographic_editorial", "diagrammatic_editorial",
    "abstract_editorial", "provided_image_edit", "template_edit",
}
MOTIF_TYPES = {"people", "object", "architecture", "environment", "source", "type", "data", "abstract"}
NEGATIVE_SPACE = {
    "upper-left", "upper-right", "lower-left", "lower-right", "top", "bottom",
    "left", "right", "center-top", "center-bottom", "none",
}
LAYOUT_FAMILIES = {
    "editorial-split", "photo-negative-space", "editorial-card", "signal-field",
    "number-led", "source-led", "question-led", "comparison-led", "timeline-led", "quiet-close",
    "anchored-hero-top", "anchored-wave-frame", "anchored-footer-curve",
}
ACCENT_STRENGTHS = {"quiet", "medium", "strong"}
DENSITIES = {"low", "medium", "high"}

END_GATES = {
    "single_image", "text_exact", "facts_exact", "headline_breaks_controlled",
    "no_text_clipping", "no_extra_text", "mobile_readable", "contrast_safe",
    "safe_margins", "hierarchy_clear", "typography_professional",
    "composition_balanced", "image_integrity_credible", "fake_evidence_free",
    "visual_claim_safe", "generic_ai_look_absent", "symbolism_restrained",
    "no_unrequested_branding", "standalone_effective", "series_role_clear",
    "neighbor_distinct", "publish_ready", "full_graphic_design_present",
    "visible_text_present", "raw_photo_absent", "reference_design_dna_present",
}
SCORE_KEYS = {
    "intent_match", "hierarchy", "typography", "composition", "specificity",
    "credibility", "restraint", "mobile_readability", "series_role", "finish",
}
SERIES_GATES = {
    "ten_individual_files", "no_collage_endproduct", "image_tool_only_confirmed",
    "functional_layout_variation", "render_strategy_rhythm", "accent_rhythm",
    "no_near_duplicates", "dramaturgy_passed", "style_consistency_passed",
    "no_template_monotony", "no_dark_or_color_drift", "hook_and_close_distinct",
    "reference_design_dna_consistent",
}

NUMBER_RE = re.compile(r"(?<![A-Za-z])\d[\d\s.,%]*")


def strict_bool(value: Any, field: str) -> bool:
    if type(value) is not bool:
        raise ValueError(f"{field} must be a JSON boolean")
    return value


def strict_int(value: Any, field: str, minimum: int | None = None) -> int:
    if type(value) is not int:
        raise ValueError(f"{field} must be a JSON integer")
    if minimum is not None and value < minimum:
        raise ValueError(f"{field} must be >= {minimum}")
    return value


def finite_float(value: Any, field: str, minimum: float | None = None, maximum: float | None = None) -> float:
    try:
        out = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be numeric") from exc
    if not math.isfinite(out):
        raise ValueError(f"{field} must be finite")
    if minimum is not None and out < minimum:
        raise ValueError(f"{field} must be >= {minimum}")
    if maximum is not None and out > maximum:
        raise ValueError(f"{field} must be <= {maximum}")
    return out


def norm(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip())


def norm_lower(value: Any) -> str:
    return norm(value).lower()


def normalize_number_token(value: str) -> str:
    token = re.sub(r"\s+", "", value.strip()).replace("%", "")
    if "," in token and "." in token:
        if token.rfind(",") > token.rfind("."):
            token = token.replace(".", "").replace(",", ".")
        else:
            token = token.replace(",", "")
    elif "," in token:
        parts = token.split(",")
        if len(parts) == 2 and 1 <= len(parts[1]) <= 2:
            token = parts[0].replace(".", "") + "." + parts[1]
        else:
            token = token.replace(",", "")
    elif "." in token:
        parts = token.split(".")
        if not (len(parts) == 2 and 1 <= len(parts[1]) <= 2):
            token = token.replace(".", "")
    return token.strip(".,")


def numeric_tokens(text: str) -> set[str]:
    out: set[str] = set()
    for match in NUMBER_RE.finditer(text or ""):
        token = normalize_number_token(match.group(0))
        if token:
            out.add(token)
    return out
