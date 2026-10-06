---
name: research-source-router
description: Route komplexe Recherchefragen zur kleinsten geeigneten Evidenzquelle und kombiniere nur bei Bedarf Web, wissenschaftliche Literatur, Rechtsquellen, öffentliche Daten, verbundene Dateien und Spezialdatenbanken. Verwenden vor Deep Research, wenn mehrere Recherchewerkzeuge verfügbar sind oder unnötige Parallelsuchen vermieden werden sollen. Nicht als Ersatz für die eigentliche fachliche Recherche verwenden.
---

# Research Source Router

## Ziel

Wähle zuerst die Quelle, dann recherchiere. Vermeide fünf parallele Systeme ohne klaren Zusatznutzen.

## Routing

1. **Aktuelle allgemeine Fakten, Nachrichten, Unternehmen, Produkte, Regeln**  
   Aktuelle Webrecherche und Primärquellen verwenden.

2. **Peer-reviewed Literatur und Paper Discovery**  
   Verfügbare wissenschaftliche Such- oder Literaturconnectoren verwenden. Für medizinische Literatur bevorzugt offizielle biomedizinische Datenbanken.

3. **Recht und Rechtsprechung**  
   Verfügbare juristische Primärquellen oder Legal-Research-Connectoren verwenden. Gesetz, Judikatur und Sekundärkommentar trennen.

4. **Österreichische öffentliche Daten**  
   `austria-open-data-research`, amtliche Statistik, Parlament, Behörden und andere Primärquellen priorisieren.

5. **Gesundheits-, Arzneimittel- oder Versorgungsdaten**  
   Nur die passende offizielle Spezialquelle verwenden, wenn sie für die konkrete Frage zuständig ist.

6. **Nutzer- oder Organisationsdaten**  
   Zuerst die freigegebene Datei oder den verbundenen Dienst verwenden, wenn die Antwort davon abhängt. Nicht durch Websuche ersetzen.

7. **Breite, strittige oder folgenreiche Fragen**  
   Danach `deep-research` für Mehrquellen-Synthese und `source-verification` für kritische Evidenzprüfung verwenden.

## Auswahlregel

Für jede Quelle intern festhalten:
- welche Teilfrage sie beantwortet
- warum sie gegenüber Alternativen bevorzugt wird
- Aktualität/Cutoff
- Primär- oder Sekundärstatus
- bekannte Lücke

Ein zweites System nur hinzufügen, wenn es eine andere Evidenzklasse, Gegenprüfung oder fehlende Abdeckung liefert.

## Ausgabe

Bei reiner Routingfrage: Quellenplan und Reihenfolge.  
Bei Research-Auftrag: Router entscheidet intern und übergibt anschließend an den passenden Recherche-Skill.
