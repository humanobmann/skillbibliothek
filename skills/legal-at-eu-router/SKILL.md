---
name: legal-at-eu-router
description: Route österreichische und europäische Rechtsfragen zur passenden Primärquelle oder Legal-Research-Engine und trenne Gesetzesstand, Judikatur, parlamentarische Entstehungsgeschichte, Verfahrensunterlagen und politische Bewertung. Verwenden bei österreichischem oder EU-Recht, RIS, EUR-Lex, CURIA, ECLI, CELEX, Gerichtsentscheidungen, Gesetzesmaterialien, Verfahren, Rechtsmemo, Rechtsvergleich oder rechtlich relevanten politischen Vorhaben.
---

# Legal AT/EU Router

## Ziel

Erst Rechtsquelle und Jurisdiktion bestimmen, dann analysieren. Politische Bewertung und rechtliche Aussage nicht vermischen.

## Routing

1. **Aktueller österreichischer Gesetzesstand**  
   Offizielle österreichische Primärquellen priorisieren, insbesondere RIS und zuständige Behörden. Geltungsstand, Fassung und Inkrafttreten prüfen.

2. **Österreichische oder EU-Judikatur, ECLI, CELEX, konkrete Rechtszitate**  
   Den verfügbaren Legal-Research-Connector verwenden, wenn er die Referenz verifizieren und einen echten Quellenlink liefern kann. Keine URL und keine Fundstelle raten.

3. **EU-Recht oder grenzüberschreitende Rechtsfrage**  
   Legal Data Hunter bzw. offizielle EU-Primärquellen verwenden. Rechtsakt, Artikel, konsolidierte Fassung, zuständige Gerichtsbarkeit und relevante Judikatur getrennt prüfen.

4. **Parlamentarische Entstehung, Materialien oder politische Gesetzgebung**  
   Offizielle Parlamentsquellen und `spoe-parlamentsforensik` verwenden. Gesetzesmaterialien und politische Positionen sind keine Ersatzquelle für den geltenden Normtext.

5. **Nutzer stellt eigene Verfahrens- oder Gerichtsunterlagen bereit**  
   Zuerst die bereitgestellten Dateien als Primärbasis lesen. Externe Rechtsrecherche nur ergänzend verwenden und klar von dokumentenbasierten Aussagen trennen.

6. **Politische Folgen oder Kommunikationsstrategie eines Rechtsvorhabens**  
   Zuerst Rechtslage verifizieren. Danach geprüften Rechtsfaktenblock an `politik-analyse` übergeben.

## Zitierregeln

- Jede konkrete Rechtsbehauptung braucht eine verifizierbare Quelle.
- Offizielle Primärquellen vor Sekundärkommentaren.
- Keine erfundenen URLs, Aktenzeichen, ECLI-, CELEX- oder Artikelreferenzen.
- Bei widersprüchlichen Fassungen Datum, Jurisdiktion und Geltungsstand offenlegen.
- Nicht zugängliche oder nicht verifizierte Fundstellen als solche kennzeichnen.

## Verfahrensgrenze

Der Skill strukturiert Rechtsrecherche und Quellenlage. Er behauptet keine anwaltliche Vertretung und trifft keine prozessuale Entscheidung anstelle des Nutzers oder seiner Rechtsvertretung.

## Ausgabe

Bei Routingfrage:
1. Jurisdiktion
2. maßgebliche Quellenklasse
3. empfohlener Rechercheworkflow
4. nötige Verifikationsschritte

Bei Rechtsauftrag: Router übergibt an die zuständige Rechtsrecherche und hält Rechtslage, Dokumenteninhalt, Unsicherheit und politische Bewertung getrennt.
