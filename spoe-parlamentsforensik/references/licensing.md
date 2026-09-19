# License and Content Handling

Stand: 2026-08-24

## Grundsatz

Technische Abrufbarkeit und freie Weiterverwendung sind nicht identisch.

## Open Data Metadaten

Die offizielle Open Data Übersicht weist aktuell 25 Datensätze aus. Ergebnislisten und API Daten stehen grundsätzlich unter CC BY 4.0, soweit die jeweilige Datensatzbeschreibung keine Einschränkung für konkrete Inhalte nennt.

## Schriftliche Anfragen

Besonders restriktiv behandeln:

* API und Ergebnislisten: Open Data
* Geschichtsseiten: laut Dokumentation nutzbar
* Titel: von freier Weiterverwendung ausgenommen
* Kurzbeschreibung: ausgenommen
* Dokumente: ausgenommen
* Volltexte: ausgenommen

Folge für das System:

Der Researchprozess darf diese Inhalte zur Prüfung nur im zulässigen Rahmen behandeln. Exporte, Dossiers und maschinenlesbare Weitergabe dürfen ausgeschlossene Inhalte nicht automatisch replizieren.

## Regierungsvorlagen und Gesetzesanträge BR

Stellungnahmen in Geschichtsseiten sind laut Datensatzbeschreibungen nicht Teil der freien Open Data Weiterverwendung. Diese Bereiche werden separat gekennzeichnet.

## Protokolle

Stenographische Protokolle von NR und BR sind laut Dokumentation freie Werke. Andere verlinkte Inhalte werden nicht automatisch gleich behandelt.

## Personen

Bei Personenseiten sind nur bestimmte Teile frei nutzbar. Kontakt, Medien und weitere ausdrücklich ausgenommene Bereiche werden nicht in den Analysebestand übernommen, sofern sie nicht aus anderem rechtlich zulässigem Grund erforderlich sind.

## Speicherung

Jedes Dokument erhält:

```text
license_status
reuse_allowed
restricted_fields
source_terms_url
checked_at
```

Mögliche Werte:

```text
CC_BY_4_0
FREE_WORK
PUBLIC_NOT_OPEN_DATA
RESTRICTED_REUSE
UNKNOWN_NEEDS_REVIEW
```

Bei `UNKNOWN_NEEDS_REVIEW` keine externe Ausgabe des Inhalts.

## Skill-Regel für Weitergabe

In internen Analyseartefakten nur so viel Quellinhalt replizieren, wie für Prüfung und Nachvollziehbarkeit erforderlich ist. Inhalte, die laut Datensatzbeschreibung ausdrücklich nicht zur freien Weiterverwendung freigegeben sind, nicht automatisch in exportierbare Register, Trainingskorpora oder veröffentlichungsfertige Dossiers kopieren. Stattdessen Metadaten, Fundstelle, Hash, Prüfstatus und zulässige Paraphrase verwenden.
