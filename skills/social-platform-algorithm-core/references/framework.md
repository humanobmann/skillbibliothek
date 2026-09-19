# Social Algorithm Framework

Pruefstand: 2026-09-19.

## 1. Platform -> Surface -> Objective -> Signal

Nie von einem plattformweiten Einheitsalgorithmus ausgehen.

| Platform | Surface | Objective | typische belegbare Signaldimensionen |
|---|---|---|---|
| Facebook | Feed / Feed Recommendations | persoenliche Relevanz und Wert | Viewing, Interaktion, Beziehung, Interessenpassung |
| Instagram | Feed / Explore / Reels | Relevanz, Discovery, Konsum | Viewing, Watch, Saves, Shares, Interaktion, negative Feedbacksignale |
| TikTok | For You | personalisierte Empfehlung | Watch/Skip, Full Watch, Likes, Shares, Comments, Content Information |
| TikTok | Search | Query-Relevanz | Query Match, Search-/Watch-Verhalten, Hashtags, Sounds |
| YouTube | Home / Suggested | Auswahl und Zufriedenheit | Appeal, Engagement, Satisfaction, Personalisierung |
| YouTube | Search | Query-Relevanz und Performance | Metadaten-/Inhaltsmatch plus Nutzerreaktion |
| YouTube | Shorts | Auswahl, Konsum, Zufriedenheit | Chose-to-view, AVD, APV, Likes, Surveys |
| LinkedIn | Feed / Suggested Posts | professionelle Relevanz und Nutzwert | Kontext, Netzwerk, long dwell, skip, aktive Interaktion |

Eine Regel darf nur dann von einer Surface auf eine andere uebertragen werden, wenn OFFICIAL- oder ACCOUNT-Evidenz dies stuetzt. Sonst HYPOTHESIS.

## 2. Evidence Records

Jede volatile Plattformquelle soll enthalten:

    source_id
    platform
    surface
    mechanism: RANKING | SEARCH | RECOMMENDATION_ELIGIBILITY | POLICY | MONETIZATION
    publisher
    title
    url
    retrieved
    claim_scope
    volatility: high | medium | low

Jeder Algorithmusclaim soll enthalten:

    claim
    evidence_level: OFFICIAL | ACCOUNT | OBSERVED | HYPOTHESIS
    mechanism
    source_id
    surface
    observed_at
    limitation

Freshness Gate: bei zeitkritischen Aufgaben offizielle Quelle erneut pruefen. Aktuelle Surface-Dokumentation hat Vorrang vor aelteren allgemeinen oder Engineering-Quellen.

## 3. Originality Taxonomy

- ORIGINAL_CREATED: vom Account selbst erstellt.
- ORIGINAL_TRANSFORMATIVE: Drittmaterial mit substanziell neuer Analyse, Information, Erklaerung, Storyline oder kreativer Bearbeitung.
- LICENSED_REUSE: rechtlich erlaubte Wiederverwendung; algorithmische Originalitaet separat pruefen.
- COMMENTARY_REUSE: Drittmaterial mit Kommentar; nur bei substanziell eigenem Mehrwert als transformativ behandeln.
- LOW_VALUE_REUSE: minimale Edits ohne neuen Informationswert.
- DUPLICATE: identische oder nahezu identische Wiederveroeffentlichung.
- CROSS_PLATFORM_REUPLOAD: Inhalt von anderer Plattform; Rechte, Wasserzeichen und Plattformregeln separat pruefen.

Rechtliche Nutzbarkeit und algorithmische Originalitaet sind getrennte Fragen.

## 4. Social Search

Search Intent -> Primary Entity -> Primary Query -> Semantic Variants -> Content Match -> User Response

Workflow:

1. Suchintention bestimmen.
2. Primaere Entitaet und einen Hauptsuchbegriff festlegen.
3. wenige semantische Varianten bestimmen.
4. nur natuerlich in Titel, Caption, gesprochenem Inhalt, On-Screen-Text oder passenden Hashtags/Topics abbilden.
5. Inhalt muss die Suchintention tatsaechlich beantworten.
6. Search-Traffic getrennt von Feed-/Recommendation-Traffic messen.

Kein Keyword Stuffing und keine generischen Trendbegriffe nur fuer Reichweite.

## 5. Account Analytics Learning Loop

Observe -> Segment -> Compare -> Hypothesis -> Test -> Measure -> Update

Pro Post, soweit verfuegbar: platform, surface, format, topic, publish_time, duration, hook_type, creative_type, CTA_type, impressions/reach, starts/views, dwell/watch time, completion/APV, saves, shares/sends, comments, negative feedback, profile/channel actions, search traffic, recommendation traffic, paid/organic.

Regeln:

- organisch und bezahlt trennen.
- gleiche Surface und gleiches Format vergleichen.
- Median und Verteilung statt nur Best Post verwenden.
- Ausreisser markieren.
- kleine Stichproben als unsicher kennzeichnen.
- keine Kausalitaet aus Korrelation ableiten.
- ACCOUNT-Ergebnis nie zur universellen Plattformregel umdeuten.

## 6. Experiment Framework

Pro Test moeglichst nur eine primaere Variable aendern, zum Beispiel Hook, Titel/Thumbnail-Promise, Laenge, Creative, Caption, CTA oder Search-Formulierung.

Vorab festlegen:

    Wenn [Aenderung],
    dann verbessert sich [primaere Metrik]
    bei [Surface/Format],
    weil [Mechanismus].
    Evidenzstatus: ACCOUNT | OBSERVED | HYPOTHESIS.

Eine primaere Metrik vor dem Test bestimmen. Sekundaermetriken dienen der Diagnose. Keine nachtraegliche Auswahl nur der Metrik, die gut aussieht.

Test neu aufsetzen, wenn mehrere Hauptvariablen gleichzeitig geaendert wurden, Paid und Organic vermischt wurden, Eligibility/Policy-Status unterschiedlich war oder Messdefinitionen wechselten.

## 7. Quality Gates

Hard Fail bei:

- unklarer Platform/Surface.
- Vermischung von Ranking, Search, Eligibility, Policy und Monetization.
- OBSERVED/HYPOTHESIS als Plattformfakt.
- Reichweiten- oder Erfolgsgarantie.
- Hook/Title/Thumbnail liefert falsches Promise.
- Engagement-Bait, Pods, Bots oder inauthentische Interaktion.
- ignoriertem Originalitaets- oder Eligibility-Risiko.
- politischer Optimierung nach Ueberzeugbarkeit oder vermuteter Empfaenglichkeit.

## 8. Audit Score

Handwerklicher Qualitaetsscore, keine Reichweitenprognose:

- Surface Fit 15
- Evidence Discipline 20
- Promise/Hook Integrity 15
- Consumption/Retention Design 15
- Originality/Value 10
- Search/Topic Fit 10
- Negative-Signal/Eligibility Check 10
- Measurement Plan 5

Hard Gates haben Vorrang vor dem Score.

## 9. Anti-Patterns

Keine universelle fixe Ideal-Laenge, keine dauerhafte Golden-Hour-Regel, keine erfundenen Signalgewichte, keine Hashtag-Magie, keine FYP-Magie, keine kuenstliche Watch-Time-Verlaengerung, kein Minimaledit-Reupload als Originalitaetsstrategie, kein einzelner viraler Post als Beweis und keine Monetarisierungsformel als Rankingmodell.
