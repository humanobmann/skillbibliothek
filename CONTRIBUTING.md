# Contributing

Danke für Beiträge zur Skillbibliothek. Die Bibliothek behandelt Skills als ausführbare Agentenlogik und verlangt deshalb dieselbe Sorgfalt wie bei produktivem Code.

## Workflow

1. Issue oder klaren Problemkontext dokumentieren, wenn die Änderung nicht trivial ist.
2. Änderungen auf einem Feature-Branch durchführen.
3. Pro Skill genau einen kanonischen Ordner unter `skills/<name>/` verwenden.
4. `SKILL.md`, relative Links, Skripte und `agents/openai.yaml` validieren.
5. Neue Skills in `skills/CATALOG.md`, `references/SKILL_CATALOG.json` und bei Bedarf `references/intent-map.md` integrieren.
6. Security-Gates und Tests lokal beziehungsweise in CI ausführen.
7. Pull Request mit Motivation, Risiko, Testnachweisen und Rollback-Hinweis erstellen.

## Qualitätsanforderungen

* kleine, kohärente Änderungen bevorzugen
* keine generierten Cache-Dateien wie `__pycache__` committen
* keine Secrets, Tokens oder produktiven personenbezogenen Daten einchecken
* neue Python-Helfer ohne unnötige Drittanbieterabhängigkeiten bauen
* externe Konzepte und übernommene Komponenten in `references/PROVENANCE.md` dokumentieren
* bei sicherheitsrelevanten Änderungen Threat Model und Least Privilege explizit prüfen

## Pflichtchecks

```bash
python scripts/validate_skills.py --strict
python scripts/validate_social_evidence.py
python -m pytest -q tests
```

## Review

Mindestens ein menschlicher Review ist für sicherheitskritische, Routing-, Governance- oder Release-Änderungen empfohlen. Bei Solo-Maintenance muss der Pull Request die Review-Entscheidung und die Testevidenz nachvollziehbar dokumentieren.

## Lizenzhinweis

Das Repository enthält derzeit Provenienz- und Upstream-Lizenzinformationen, aber die Repository-weite Lizenzentscheidung muss vom Rechteinhaber eindeutig im Root dokumentiert werden. Bis dahin keine Annahme treffen, dass neue Beiträge automatisch unter MIT oder Apache-2.0 stehen.
