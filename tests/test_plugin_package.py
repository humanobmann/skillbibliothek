import json
import tomllib
from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_portable_plugin_manifest_is_wired_to_root_skills():
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))

    assert manifest["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    assert manifest["name"] == "skillbibliothek"
    assert manifest["version"] == "1.0.0"
    assert (ROOT / "skills").is_dir()
    assert any((ROOT / "skills").glob("*/SKILL.md"))


def test_repository_marketplace_points_to_plugin_root():
    marketplace = json.loads(
        (ROOT / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8")
    )

    assert marketplace["name"] == "skillbibliothek"
    entry = marketplace["plugins"][0]
    assert entry["name"] == "skillbibliothek"
    assert entry["source"] == {"source": "local", "path": "./"}
    assert entry["policy"]["installation"] == "AVAILABLE"
    assert entry["policy"]["authentication"] == "ON_INSTALL"
    assert entry["category"] == "Productivity"


def test_codex_project_enables_repository_plugin():
    config = tomllib.loads((ROOT / ".codex" / "config.toml").read_text(encoding="utf-8"))

    assert config["plugins"]["skillbibliothek@skillbibliothek"]["enabled"] is True
