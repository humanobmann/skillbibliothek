#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
BUILD_ROOT = REPO_ROOT / ".build" / "plugin-bundles"
DIST_ROOT = REPO_ROOT / "dist"

AUTHOR = {
    "name": "Peter Schuller",
    "url": "https://github.com/humanobmann",
}
HOMEPAGE = "https://github.com/humanobmann/skillbibliothek"
SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"

BUNDLES = {
    "skillbibliothek-research": {
        "display_name": "Research & Verification",
        "short_description": "Recherche und Faktenprüfung",
        "description": "Gebündelte Skills für Deep Research, Faktenprüfung, Quellenverifikation, österreichische Open Data Recherche, Webarchive, Bildherkunft und Intelligence Briefs.",
        "keywords": ["research", "verification", "fact-check", "sources", "open-data"],
        "prompts": [
            "Recherchiere dieses Thema gründlich und verifiziere die zentralen Aussagen.",
            "Prüfe diese Behauptung und dokumentiere belastbare Quellen und Unsicherheiten.",
        ],
        "skills": [
            "deep-research",
            "fact-check",
            "source-verification",
            "austria-open-data-research",
            "read-deleted-pages",
            "find-the-original-image",
            "write-the-intel-brief",
        ],
    },
    "skillbibliothek-osint": {
        "display_name": "OSINT & Investigations",
        "short_description": "OSINT und Forensik",
        "description": "Gebündelte Skills für rechtmäßige OSINT Recherche, Personen und Firmen, Domains und Infrastruktur, Bild und Geo Verifikation, Netzwerke, öffentliche Leaks, Metadaten, Krypto und investigative Dokumentation.",
        "keywords": ["osint", "investigation", "forensics", "verification", "due-diligence"],
        "prompts": [
            "Starte eine quellenbasierte OSINT Untersuchung zu diesem Ziel.",
            "Ordne diese Hinweise, verifiziere sie und erstelle einen nachvollziehbaren Ermittlungsweg.",
        ],
        "skills": [
            "useosint",
            "investigate-anything",
            "osint-investigator",
            "journalistic-osint-governance",
            "investigate-without-getting-made",
            "find-anyone",
            "dig-through-data-brokers",
            "find-exposed-servers",
            "find-hidden-subdomains",
            "find-leaks-in-the-wild",
            "google-like-a-spy",
            "graph-the-network",
            "hunt-a-handle",
            "where-was-this-taken",
            "geolocate-from-pixels",
            "is-this-photo-real",
            "who-owns-this-domain",
            "recon-a-domain-passively",
            "who-really-owns-it",
            "x-ray-a-company",
            "what-an-email-reveals",
            "whose-number-is-this",
            "what-leaked-about-you",
            "follow-the-crypto",
            "track-planes-and-ships",
            "pattern-of-life-from-socials",
            "secrets-in-file-metadata",
            "secrets-in-git-history",
        ],
    },
    "skillbibliothek-social": {
        "display_name": "Social Content",
        "short_description": "Social Content optimieren",
        "description": "Gebündelte Skills für Facebook, Instagram, LinkedIn, TikTok und YouTube Content, Plattformlogik, Hashtag Recherche, natürliches Deutsch, schnelle Humanisierung und wiederverwendbare Schreibprofile.",
        "keywords": ["social-media", "content", "facebook", "instagram", "tiktok", "youtube"],
        "prompts": [
            "Optimiere diesen Social Media Inhalt für die passende Plattform.",
            "Überarbeite diesen Text natürlich, glaubwürdig und plattformgerecht.",
        ],
        "skills": [
            "facebook-text-optimizer",
            "instagram-text-optimizer",
            "instagram-hashtag-research",
            "linkedin-content-optimizer",
            "tiktok-content-optimizer",
            "youtube-content-optimizer",
            "social-platform-algorithm-core",
            "humanizer-de",
            "humanizer-de-natural",
            "peter-schuller-schreibstil",
            "philip-kucher-writing",
        ],
    },
    "skillbibliothek-design": {
        "display_name": "Design & Visual",
        "short_description": "Design und Bildproduktion",
        "description": "Gebündelte Skills für Editorial Design, Poster und Bildserien, Affinity Workflows, Kampagnen PDF Redesign und visuelle Qualitätskontrolle.",
        "keywords": ["design", "visual", "poster", "affinity", "image", "editorial"],
        "prompts": [
            "Entwickle für diese Aufgabe eine hochwertige visuelle Richtung und Produktion.",
            "Prüfe dieses Design streng auf Hierarchie, Lesbarkeit und handwerkliche Qualität.",
        ],
        "skills": [
            "adaptive-poster-image-series",
            "ten-separate-images",
            "affinity-designer",
            "pdf-campaign-redesigner",
            "impeccable",
        ],
    },
    "skillbibliothek-development": {
        "display_name": "Software Development",
        "short_description": "Software und GitHub",
        "description": "Gebündelte Skills für Softwareentwicklung, GitHub Workflows, Code Review, CI, Browser Tests, PowerShell, React, shadcn, UI Engineering und Codex Projektsteuerung.",
        "keywords": ["development", "github", "code-review", "react", "playwright", "powershell"],
        "prompts": [
            "Analysiere diese Entwicklungsaufgabe und führe den passendsten Workflow aus.",
            "Prüfe diesen Code oder Pull Request und leite die nächsten technischen Schritte ab.",
        ],
        "skills": [
            "using-superpowers",
            "brainstorming",
            "code-review",
            "gh-address-comments",
            "gh-fix-ci",
            "yeet",
            "agents-md",
            "migrate-to-codex",
            "cli-creator",
            "playwright",
            "playwright-interactive",
            "powershell-senior-expert",
            "react-best-practices",
            "shadcn-ui",
            "interface-design",
            "interaction-design",
            "ui-design-engineering",
            "ui-ux-pro-max",
            "web-design-guidelines",
            "screenshot",
        ],
    },
    "skillbibliothek-security": {
        "display_name": "Security & Platform",
        "short_description": "Security und Plattform",
        "description": "Gebündelte Skills für Security Reviews, Threat Modeling, Ownership, Cloud Native Security, SRE, MLOps, FinOps, Low Code Governance und sichere Agenten Orchestrierung.",
        "keywords": ["security", "sre", "mlops", "finops", "cloud", "governance"],
        "prompts": [
            "Prüfe dieses System oder Repository auf Sicherheits und Betriebsrisiken.",
            "Entwickle belastbare Guardrails für diese Plattform oder Automatisierung.",
        ],
        "skills": [
            "security-best-practices",
            "security-gate",
            "security-ownership-map",
            "security-threat-model",
            "skill-security-auditor",
            "cloud-native-security",
            "automated-sre-observability",
            "mlops-ai-operations",
            "finops-cloud-governance",
            "low-code-no-code-engineering",
            "agentic-ai-orchestration-governance",
        ],
    },
    "skillbibliothek-politik-at": {
        "display_name": "Politik Österreich",
        "short_description": "Politik und Parlament AT",
        "description": "Gebündelte Skills für österreichische Politikanalyse, Framing Analyse, Parlamentsforensik, parlamentarische Briefings, das Robert-Laimer-Wochendossier sowie klar zugeordnete politische Projekt und Kommunikationsworkflows.",
        "keywords": ["politik", "austria", "parlament", "framing", "briefing"],
        "prompts": [
            "Analysiere dieses politische Thema faktenbasiert und mit belastbaren Quellen.",
            "Erstelle aus diesen Unterlagen ein nachvollziehbares parlamentarisches Briefing.",
        ],
        "skills": [
            "politik-analyse",
            "framing-analysis",
            "spoe-parlamentsforensik",
            "parliament-briefing-designer",
            "peter-schuller-politiker-kommunikation",
            "spoe-laimer-projekt-orchestrator",
            "weekly-dossier",
        ],
    },
    "skillbibliothek-publishing": {
        "display_name": "Publishing & Writing",
        "short_description": "Schreiben und Publishing",
        "description": "Gebündelte Skills für umfangreiche Dokumententwicklung, Sachbuchrevision, Manifest 2.0, SEO Reviews und PDF Produktionsworkflows.",
        "keywords": ["writing", "publishing", "non-fiction", "documents", "seo", "pdf"],
        "prompts": [
            "Entwickle oder überarbeite dieses längere Dokument strukturiert und publikationsreif.",
            "Prüfe dieses Manuskript auf Argumentation, Evidenz, Struktur und Verständlichkeit.",
        ],
        "skills": [
            "document-development",
            "non-fiction-revision",
            "manifest-2-0-author",
            "seo-review",
            "pdf",
        ],
    },
    "skillbibliothek-automation": {
        "display_name": "Automation & Workflows",
        "short_description": "Automation und Workflows",
        "description": "Gebündelte Skills für Automatisierung, Workflow Routing, Zieldefinition, Prompt Architektur, Arbeitssteuerung, Skill Discovery und Skill Authoring sowie systematisches Stress Testing von Plänen.",
        "keywords": ["automation", "workflow", "prompts", "skills", "routing", "planning"],
        "prompts": [
            "Plane und automatisiere diesen wiederkehrenden Arbeitsablauf.",
            "Wähle für diese Aufgabe den kleinsten passenden Workflow und führe ihn strukturiert aus.",
        ],
        "skills": [
            "automator",
            "openai-workflow-router",
            "define-goal",
            "prompt-architect",
            "peter-schuller-arbeitssteuerung",
            "core-routing",
            "find-skills",
            "library-skill-authoring",
            "grill-me",
            "grilling",
        ],
    },
    "skillbibliothek-danke-fuer-nichts": {
        "display_name": "Danke für nichts",
        "short_description": "Buchprojekt Danke für nichts",
        "description": "Projektplugin für die private Autorenkampagne Danke für nichts mit Publishing Audit, Outreach, Content und SEO sowie projektübergreifender Operations Orchestrierung.",
        "keywords": ["book", "publishing", "outreach", "seo", "campaign"],
        "prompts": [
            "Arbeite am Projekt Danke für nichts und wähle den passenden Projektworkflow.",
            "Prüfe den nächsten sinnvollen Schritt für Publishing, Outreach oder Content.",
        ],
        "skills": [
            "danke-fuer-nichts-content-seo",
            "danke-fuer-nichts-operations",
            "danke-fuer-nichts-outreach",
            "danke-fuer-nichts-publishing-audit",
        ],
    },
    "skillbibliothek-verein": {
        "display_name": "Vereinskommunikation",
        "short_description": "Vereinskommunikation",
        "description": "Schlankes, strikt vom Parteikontext getrenntes Plugin für öffentliche Vereinskommunikation in der Rolle als Obmann oder Vertreter von Menschlichkeit Österreich.",
        "keywords": ["verein", "ngo", "communication", "austria"],
        "prompts": [
            "Formuliere diese Vereinskommunikation seriös, solidarisch und vertrauensbildend.",
        ],
        "skills": [
            "peter-schuller-obmann-kommunikation",
        ],
    },
}


def discover_source_skills() -> set[str]:
    return {
        path.name
        for path in SKILLS_ROOT.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }


def validate_bundle_definition() -> None:
    source = discover_source_skills()
    assigned: list[str] = []
    for bundle in BUNDLES.values():
        assigned.extend(bundle["skills"])

    duplicates = sorted({name for name in assigned if assigned.count(name) > 1})
    assigned_set = set(assigned)
    missing = sorted(source - assigned_set)
    unknown = sorted(assigned_set - source)

    if duplicates or missing or unknown:
        raise SystemExit(
            "Bundle definition invalid:\n"
            f"duplicates={duplicates}\n"
            f"missing={missing}\n"
            f"unknown={unknown}"
        )

    if len(assigned) != len(source):
        raise SystemExit(
            f"Expected exactly one assignment per skill: source={len(source)} assigned={len(assigned)}"
        )


def copy_skill(skill_name: str, target: Path) -> None:
    source = SKILLS_ROOT / skill_name
    if not (source / "SKILL.md").is_file():
        raise SystemExit(f"Missing SKILL.md for {skill_name}")

    def ignore(path: str, names: list[str]) -> set[str]:
        ignored: set[str] = set()
        for name in names:
            if name == "__pycache__" or name == ".DS_Store" or name.endswith(".pyc"):
                ignored.add(name)
        return ignored

    shutil.copytree(source, target, ignore=ignore)


def plugin_manifest(slug: str, cfg: dict) -> dict:
    short_description = cfg["short_description"]
    if len(short_description) > 30:
        raise SystemExit(
            f"shortDescription for {slug} is {len(short_description)} characters; maximum is 30"
        )

    return {
        "$schema": SCHEMA,
        "name": slug,
        "version": "1.0.0",
        "description": cfg["description"],
        "author": AUTHOR,
        "homepage": HOMEPAGE,
        "repository": HOMEPAGE,
        "keywords": cfg["keywords"],
        "extensions": {
            "com.openai": {
                "interface": {
                    "displayName": cfg["display_name"],
                    "shortDescription": short_description,
                    "longDescription": cfg["description"],
                    "developerName": "Peter Schuller",
                    "category": "Productivity",
                    "capabilities": ["Read", "Write"],
                    "websiteURL": HOMEPAGE,
                    "defaultPrompt": cfg["prompts"],
                }
            }
        },
    }


def validate_skill_frontmatter(skill_dir: Path) -> None:
    content = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    match = re.search(r"(?m)^name:\s*([^\n]+?)\s*$", content)
    if not match:
        raise SystemExit(f"Missing frontmatter name in {skill_dir / 'SKILL.md'}")
    declared = match.group(1).strip().strip('"').strip("'")
    if declared != skill_dir.name:
        raise SystemExit(
            f"Skill name mismatch: folder={skill_dir.name!r} frontmatter={declared!r}"
        )


def build_bundle(slug: str, cfg: dict) -> dict:
    plugin_root = BUILD_ROOT / slug
    if plugin_root.exists():
        shutil.rmtree(plugin_root)
    (plugin_root / "skills").mkdir(parents=True)

    for skill_name in cfg["skills"]:
        target = plugin_root / "skills" / skill_name
        copy_skill(skill_name, target)
        validate_skill_frontmatter(target)

    manifest = plugin_manifest(slug, cfg)
    (plugin_root / "plugin.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    archive_path = DIST_ROOT / f"{slug}.zip"
    if archive_path.exists():
        archive_path.unlink()

    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(plugin_root.rglob("*")):
            if path.is_file():
                arcname = Path(slug) / path.relative_to(plugin_root)
                zf.write(path, arcname.as_posix())

    return {
        "name": slug,
        "display_name": cfg["display_name"],
        "skills": len(cfg["skills"]),
        "archive": archive_path.name,
        "archive_bytes": archive_path.stat().st_size,
    }


def main() -> int:
    validate_bundle_definition()

    if BUILD_ROOT.exists():
        shutil.rmtree(BUILD_ROOT)
    BUILD_ROOT.mkdir(parents=True)
    DIST_ROOT.mkdir(parents=True, exist_ok=True)

    for old in DIST_ROOT.glob("skillbibliothek-*.zip"):
        old.unlink()

    built = [build_bundle(slug, cfg) for slug, cfg in BUNDLES.items()]
    report = {
        "source_skill_count": len(discover_source_skills()),
        "bundle_count": len(built),
        "bundles": built,
    }
    (DIST_ROOT / "plugin-bundles-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
