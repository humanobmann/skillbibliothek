#!/usr/bin/env python3
"""ChatGPT-native UI UX Pro Max search and design-system generator.

Standard-library only. No network calls. The compact catalog is intentionally
curated for routing and synthesis; ChatGPT supplies project-specific judgment.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = ROOT / "references" / "catalog.json"


def load_catalog() -> dict[str, Any]:
    with CATALOG_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9+#.]+", text.lower()))


def score(query: str, item: dict[str, Any]) -> float:
    q = tokens(query)
    searchable = " ".join(str(v) for k, v in item.items() if k not in {"hex", "tokens"})
    s = tokens(searchable)
    overlap = len(q & s)
    exact = 0
    hay = searchable.lower()
    for term in sorted(q, key=len, reverse=True):
        if len(term) >= 4 and term in hay:
            exact += 0.4
    return overlap + exact


def search_items(query: str, items: list[dict[str, Any]], n: int = 3) -> list[dict[str, Any]]:
    ranked = sorted(((score(query, item), item) for item in items), key=lambda x: x[0], reverse=True)
    positive = [item for sc, item in ranked if sc > 0]
    return positive[:n] if positive else [item for _, item in ranked[:n]]


def choose_profile(query: str, catalog: dict[str, Any]) -> dict[str, Any]:
    return search_items(query, catalog["products"], 1)[0]


def by_id(items: list[dict[str, Any]], item_id: str) -> dict[str, Any]:
    for item in items:
        if item.get("id") == item_id:
            return item
    raise KeyError(item_id)


def dial_variance(style: dict[str, Any], variance: int | None, catalog: dict[str, Any]) -> dict[str, Any]:
    if variance is None:
        return style
    preferred = ["minimal", "fluent", "material"] if variance <= 3 else ["bento", "editorial", "neo-brutal"] if variance >= 8 else []
    if not preferred:
        return style
    for pref in preferred:
        matches = [x for x in catalog["styles"] if pref in x["id"]]
        if matches:
            return matches[0]
    return style


def spacing_for_density(density: int | None) -> dict[str, str]:
    if density is None or 4 <= density <= 7:
        return {"xs": "4px", "sm": "8px", "md": "16px", "lg": "24px", "xl": "40px", "2xl": "64px"}
    if density <= 3:
        return {"xs": "8px", "sm": "16px", "md": "24px", "lg": "40px", "xl": "64px", "2xl": "96px"}
    return {"xs": "4px", "sm": "8px", "md": "12px", "lg": "16px", "xl": "24px", "2xl": "32px"}


def motion_for_level(level: int | None) -> dict[str, str]:
    if level is None or 4 <= level <= 7:
        return {"tier": "standard", "micro": "120-180ms", "transition": "180-280ms", "rule": "Prefer opacity and transform. Respect reduced motion."}
    if level <= 3:
        return {"tier": "subtle", "micro": "100-150ms", "transition": "150-220ms", "rule": "Use only state feedback and essential spatial continuity."}
    return {"tier": "expressive", "micro": "120-180ms", "transition": "220-420ms", "rule": "Use staged motion sparingly, avoid blocking interactions, provide reduced-motion fallback."}


def generate_design_system(query: str, project: str | None, variance: int | None, motion: int | None, density: int | None) -> dict[str, Any]:
    c = load_catalog()
    profile = choose_profile(query, c)
    style = by_id(c["styles"], profile["style"])
    style = dial_variance(style, variance, c)
    palette = by_id(c["palettes"], profile["palette"])
    typography = by_id(c["typography"], profile["typography"])
    pattern = by_id(c["patterns"], profile["pattern"])
    checks = c["quality_gates"]
    return {
        "project": project or "Untitled UI",
        "query": query,
        "profile": profile["name"],
        "pattern": pattern,
        "style": style,
        "palette": palette,
        "typography": typography,
        "spacing": spacing_for_density(density),
        "motion": motion_for_level(motion),
        "anti_patterns": profile["avoid"],
        "implementation_priorities": profile["priorities"],
        "quality_gates": checks,
        "dials": {"variance": variance, "motion": motion, "density": density},
        "provenance": "ChatGPT-native adaptation of nextlevelbuilder/ui-ux-pro-max-skill under MIT license; compact offline catalog.",
    }


def to_markdown(ds: dict[str, Any]) -> str:
    p = ds["palette"]["tokens"]
    out = [
        f"# {ds['project']} Design System",
        "",
        f"**Profile:** {ds['profile']}",
        f"**Pattern:** {ds['pattern']['name']}",
        f"**Style:** {ds['style']['name']}",
        f"**Typography:** {ds['typography']['heading']} / {ds['typography']['body']}",
        "",
        "## Structure",
        ds["pattern"]["structure"],
        "",
        "## Visual direction",
        ds["style"]["guidance"],
        "",
        "## Color tokens",
    ]
    for k, v in p.items():
        out.append(f"- `{k}`: `{v}`")
    out += ["", "## Typography", f"- Heading: {ds['typography']['heading']}", f"- Body: {ds['typography']['body']}", f"- Guidance: {ds['typography']['guidance']}", "", "## Spacing"]
    for k, v in ds["spacing"].items():
        out.append(f"- `{k}`: `{v}`")
    out += ["", "## Motion", f"- Tier: {ds['motion']['tier']}", f"- Micro: {ds['motion']['micro']}", f"- Transition: {ds['motion']['transition']}", f"- Rule: {ds['motion']['rule']}", "", "## Implementation priorities"]
    out += [f"- {x}" for x in ds["implementation_priorities"]]
    out += ["", "## Avoid"] + [f"- {x}" for x in ds["anti_patterns"]]
    out += ["", "## Quality gates"] + [f"- {x}" for x in ds["quality_gates"]]
    return "\n".join(out) + "\n"


def persist(ds: dict[str, Any], output_dir: str, page: str | None, force: bool) -> list[str]:
    root = Path(output_dir).resolve()
    slug = re.sub(r"[^a-z0-9]+", "-", ds["project"].lower()).strip("-") or "project"
    target = root / "design-system" / slug
    pages = target / "pages"
    pages.mkdir(parents=True, exist_ok=True)
    created: list[str] = []
    master = target / "MASTER.md"
    if force or not master.exists():
        master.write_text(to_markdown(ds), encoding="utf-8")
        created.append(str(master))
    if page:
        page_slug = re.sub(r"[^a-z0-9]+", "-", page.lower()).strip("-") or "page"
        pf = pages / f"{page_slug}.md"
        if force or not pf.exists():
            pf.write_text(
                f"# {page} overrides\n\nUse `{master.name}` as the base design system.\n\n## Page-specific deviations\n\nDocument only intentional deviations here.\n",
                encoding="utf-8",
            )
            created.append(str(pf))
    return created


def domain_search(query: str, domain: str, n: int) -> dict[str, Any]:
    c = load_catalog()
    mapping = {
        "product": "products", "style": "styles", "color": "palettes", "typography": "typography",
        "landing": "patterns", "chart": "charts", "ux": "ux", "stack": "stacks"
    }
    key = mapping[domain]
    return {"domain": domain, "query": query, "results": search_items(query, c[key], n)}


def main() -> None:
    ap = argparse.ArgumentParser(description="UI UX Pro Max compact offline search")
    ap.add_argument("query")
    ap.add_argument("--design-system", action="store_true")
    ap.add_argument("--domain", choices=["product", "style", "color", "typography", "landing", "chart", "ux", "stack"])
    ap.add_argument("--stack", dest="stack_name")
    ap.add_argument("--max-results", "-n", type=int, default=3)
    ap.add_argument("--project-name", "-p")
    ap.add_argument("--variance", type=int, choices=range(1, 11))
    ap.add_argument("--motion", type=int, choices=range(1, 11))
    ap.add_argument("--density", type=int, choices=range(1, 11))
    ap.add_argument("--persist", action="store_true")
    ap.add_argument("--page")
    ap.add_argument("--output-dir")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.design_system:
        ds = generate_design_system(args.query, args.project_name, args.variance, args.motion, args.density)
        if args.persist:
            if not args.output_dir:
                ap.error("--persist requires explicit --output-dir")
            ds["persisted_files"] = persist(ds, args.output_dir, args.page, args.force)
        print(json.dumps(ds, ensure_ascii=False, indent=2) if args.json else to_markdown(ds))
        return

    if args.stack_name:
        c = load_catalog()
        exact = [item for item in c["stacks"] if item.get("id") == args.stack_name.lower()]
        if exact:
            result = {"domain": "stack", "stack": args.stack_name.lower(), "query": args.query, "results": exact}
        else:
            query = f"{args.stack_name} {args.query}"
            result = domain_search(query, "stack", args.max_results)
            result["stack"] = args.stack_name
    else:
        result = domain_search(args.query, args.domain or "ux", args.max_results)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
