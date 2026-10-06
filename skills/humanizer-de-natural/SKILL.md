---
name: humanizer-de-natural
description: Redigiert bestehenden deutschen Text schnell und schonend so, dass er natürlicher, persönlicher und weniger schablonenhaft wirkt. Verwenden bei Anfragen wie humanisieren, natürlicher schreiben, ChatGPT-Stil reduzieren, KI-Tells entfernen oder Text weniger glatt machen, wenn kein umfangreicher Audit mit Linter- und Evidenzworkflow erforderlich ist. Bewahrt Fakten, Bedeutung, Namen, Zahlen, Zitate und Haltung.
---

# Humanizer DE Natural

## Auftrag

Redigiere vorhandenen deutschen Text auf natürliche Sprachwirkung. Entferne wiederkehrende LLM-Muster, ohne Inhalt, Faktenlage oder Autorposition zu verfälschen.

Für längere, stark KI-typische oder stilistisch schwierige Texte zuerst `references/anti-ai-patterns.md` laden.

Wenn der Nutzer ausdrücklich einen detaillierten Audit, Musterdiagnose, Linter, Claim-Ledger, Registermessung oder dateibasierten Prüfworkflow verlangt, stattdessen den umfangreichen `humanizer-de` verwenden.

## Arbeitsablauf

1. Zweck, Zielgruppe, Register und vorhandene Stimme bestimmen.
2. Namen, Zahlen, Daten, Zitate, Quellen, Rechtsbegriffe, Kernthesen und ausdrückliche Einschränkungen sperren.
3. Auf schablonenhafte Muster prüfen.
4. Rhythmus, Absatzbau, Wortwahl und Übergänge nur dort redigieren, wo es nötig ist.
5. Endfassung mit dem Ausgangstext vergleichen und keine neue Tatsachenbehauptung hinzufügen.
6. Standardmäßig nur die überarbeitete Fassung ausgeben.

## Redaktionsregeln

- kurze, mittlere und längere Sätze organisch mischen
- Serien aus Ein-Satz-Absätzen vermeiden
- zusammengehörige Gedanken verbinden statt jeden Halbsatz zur Pointe zu machen
- perfekte Einleitung-Problem-Lösung-Fazit-Schemata nicht automatisch erzwingen
- `nicht X, sondern Y`, Frage-plus-Sofortantwort, Dreiergruppen und Parallelismen nur verwenden, wenn sie inhaltlich tragen
- Hochglanzfloskeln und künstliche Authentizitätsmarker reduzieren
- konkrete Informationen aus dem Ausgangstext bevorzugen
- keine Erlebnisse, Gefühle, Erinnerungen oder Beobachtungen erfinden
- keine Tippfehler oder Grammatikfehler als Tarnung einbauen
- Dialekt und Umgangssprache nicht künstlich übertreiben

## Fakten- und Bedeutungsgrenze

Humanisierung ist Redaktion, keine inhaltliche Erweiterung. Verändere keine Zahlen, Verantwortungszuschreibungen, Rechtsfolgen, medizinischen Aussagen, Quellen oder politischen Tatsachen.

Bei politischen oder strittigen Inhalten nur Stil, Lesbarkeit und Natürlichkeit bearbeiten. Keine neue politische Überzeugungsstrategie, Zielgruppensegmentierung oder unbelegte Motivunterstellung hinzufügen.

## Qualitätsgate

Vor Ausgabe prüfen:

1. Klingt der Text wie zusammenhängende menschliche Prosa statt wie eine Reihe optimierter Mini-Pointen?
2. Schwanken Satz- und Absatzlängen natürlich?
3. Sind mechanische Rhetorik und Hochglanzfloskeln reduziert?
4. Ist die Stimme des Ausgangstextes erhalten?
5. Sind Fakten, Zahlen und Einschränkungen unverändert?
6. Wurde nichts Persönliches erfunden?
7. Wird keine Umgehung von KI-Detektoren versprochen?
