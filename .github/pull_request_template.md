## Ziel

<!-- Welches konkrete Problem löst dieser PR? -->

## Änderungen

<!-- Wichtigste strukturelle und fachliche Änderungen. -->

## Risiko und Rückrollbarkeit

- [ ] Trust Boundaries / Berechtigungen geprüft, falls relevant
- [ ] Keine Secrets oder produktiven personenbezogenen Daten enthalten
- [ ] Rollback oder Revert ist beschrieben
- [ ] Provenienz/Lizenzhinweise aktualisiert, falls externe Quellen übernommen wurden

## Validierung

- [ ] `python scripts/validate_skills.py --strict`
- [ ] `python scripts/validate_social_evidence.py`
- [ ] `python -m pytest -q tests`
- [ ] Neue/angepasste Skripte mit realistischem Positiv- und Negativfall getestet

## Routing / Registry

- [ ] `skills/CATALOG.md` aktualisiert, falls Skill-Bestand geändert wurde
- [ ] `references/SKILL_CATALOG.json` synchron
- [ ] `references/intent-map.md` angepasst, falls ein neuer Intent eingeführt wurde
