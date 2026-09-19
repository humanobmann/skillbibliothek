import re
from pathlib import Path


ROOT = Path(__file__).parents[1]
SKILLS = ROOT / "skills"
ALLOWED_PRODUCTS = {"CHAT", "CODEX"}


def extract_products(text):
    lines = text.splitlines()
    products = []

    for idx, line in enumerate(lines):
        match = re.match(r"^(\s*)products:\s*(.*)$", line)
        if not match:
            continue

        indent = len(match.group(1))
        inline = match.group(2).strip()

        if inline:
            if inline.startswith("[") and inline.endswith("]"):
                products.extend(
                    item.strip().strip("\"'")
                    for item in inline[1:-1].split(",")
                    if item.strip()
                )
            else:
                products.append(inline.strip().strip("\"'"))
            continue

        j = idx + 1
        while j < len(lines):
            item_match = re.match(r"^(\s*)-\s*(.+?)\s*$", lines[j])
            if not item_match or len(item_match.group(1)) <= indent:
                break
            products.append(item_match.group(2).strip().strip("\"'"))
            j += 1

    return products


def test_openai_product_policy_uses_only_supported_values():
    invalid = {}

    for metadata in SKILLS.glob("*/agents/openai.yaml"):
        products = extract_products(metadata.read_text(encoding="utf-8"))
        bad = [product for product in products if product not in ALLOWED_PRODUCTS]
        if bad:
            invalid[str(metadata.relative_to(ROOT))] = bad

    assert invalid == {}


def test_no_legacy_openai_product_names_remain():
    legacy = {"chatgpt", "codex", "api", "atlas"}
    hits = {}

    for metadata in SKILLS.glob("*/agents/openai.yaml"):
        products = extract_products(metadata.read_text(encoding="utf-8"))
        bad = [product for product in products if product in legacy]
        if bad:
            hits[str(metadata.relative_to(ROOT))] = bad

    assert hits == {}
