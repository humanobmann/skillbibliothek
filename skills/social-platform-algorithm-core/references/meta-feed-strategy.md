# Meta Feed Strategy (Facebook & Instagram) — Canonical Source of Truth

Abrufstand: 22. September 2026, Europe/Vienna. Dies ist die verbindliche, regressionsgeprüfte Quelle für alle Facebook- und Instagram-Feed-, Reichweiten-, Algorithmus-, Hashtag-, Grafik- und Recommendation-Eligibility-Regeln in dieser Bibliothek.

Jeder Skill, der Facebook- oder Instagram-Feed-Posts, Captions, Social-Media-Grafiken, Algorithmusoptimierung, Reichweitenoptimierung, Discovery, Recommendation Eligibility, Originalität, Hashtags, Feed-Layout oder kombinierte Text-Bild-Beiträge erstellt, analysiert oder optimiert, muss diese Datei als Meta-spezifische Ergänzung zu [framework.md](framework.md) und [SKILL.md](../SKILL.md) verwenden. Plattformspezifische Produktionsregeln dürfen lokal in den Fachskills bleiben; allgemeine Meta-Rankinglogik gehört ausschließlich hierher. Keine divergierenden Kopien dieser Regeln in anderen Dateien anlegen — bei Bedarf hierher verlinken.

Die strukturierten Quellen- und Claim-Records stehen in [evidence-records.json](evidence-records.json) und werden deterministisch mit `python scripts/validate_social_evidence.py` geprüft. Diese Datei fasst die Records production-tauglich zusammen; bei Widerspruch gilt `evidence-records.json` als Primärdatenquelle.

## 1. Kein Einheitsalgorithmus

Meta betreibt keinen einzelnen universellen Algorithmus. Nie von „dem Facebook-Algorithmus" oder „dem Instagram-Algorithmus" sprechen, wenn eine konkrete Surface gemeint ist.

Kanonisches Ranking-Modell (OFFICIAL, `META_HOW_AI_RANKS_2023`):

```
Inventory / Retrieval
-> Candidate Reduction
-> Predictions
-> Personalized Value Scoring
-> Integrity / Eligibility
-> Diversity / Final Composition
```

Intern zusätzlich die allgemeine Kette aus [framework.md](framework.md) verwenden: `Platform -> Surface -> Objective -> Signal -> Evidence -> Action -> Metric`.

Mindestens folgende Surfaces getrennt behandeln, da keine Signalgewichtung ohne Evidenz zwischen ihnen übertragen werden darf:

- Facebook Feed
- Facebook Feed Recommendations
- Instagram Feed
- Instagram Feed Recommendations
- Instagram Explore
- Instagram Reels
- Instagram Search

## 2. Facebook: verbindliche Regeln

### 2.1 Belegte Dimensionen (`META_FB_FEED_2026`, `META_FB_FEED_RECS_2026`)

Beziehung zum Absender, Interessen-/Themenpassung, Inhaltseigenschaften, Aktualität, bisheriges Nutzerverhalten, vorhergesagte Likes/Reaktionen, Kommentare, Shares, Betrachtungsdauer, qualitative Zufriedenheitssignale, negative Nutzerreaktionen, Originalität, Recommendation Eligibility, Diversität.

Keine fixe Gewichtung erfinden. Verboten sind insbesondere Aussagen wie „1 Share = 5 Likes", „1 Kommentar = 3 Likes" oder „Kommentare sind immer wichtiger als Likes" — siehe rejected claim in `evidence-records.json`.

### 2.2 Originalität (hohe Priorität, `META_FB_ORIGINAL_2026`)

Taxonomie gemäß [framework.md](framework.md) Abschnitt 3 verwenden: `ORIGINAL_CREATED`, `ORIGINAL_TRANSFORMATIVE`, `LICENSED_REUSE`, `COMMENTARY_REUSE`, `LOW_VALUE_REUSE`, `DUPLICATE`, `CROSS_PLATFORM_REUPLOAD`.

Eigene Fotos, Grafiken, Visualisierungen und substanziell eigene Analyse bevorzugen. Duplizierte oder nur minimal veränderte Fremdinhalte als Risiko kennzeichnen (`LOW_VALUE_REUSE`/`DUPLICATE`), niemals als gleichwertig zu `ORIGINAL_CREATED`/`ORIGINAL_TRANSFORMATIVE` behandeln. Rechtliche Nutzbarkeit und algorithmische Originalität strikt trennen.

### 2.3 Negative Signale

Hide, Show less, Not interested, Report, Block, Unfollow und vergleichbare Signale berücksichtigen. Hohe sichtbare Interaktion bei gleichzeitig starkem negativem Feedback nicht automatisch als Erfolg werten.

### 2.4 Links

Keine pauschale externe Link-Penalty behaupten (rejected claim). Stattdessen prüfen: Clickbait, schlechte/irreführende Landingpage, Spam-Domain, inhaltliche Relevanz. „Link in den ersten Kommentar" ist kein belegter Algorithmus-Hack (rejected claim).

### 2.5 Captions

Keine fixe Idealzeichenanzahl behaupten; lange Captions sind nicht automatisch negativ. Problematisch sind Spam-Muster: unnatürlich lange ablenkende Captions, inhaltlich unpassender Text, übermäßige Hashtags, Keyword Stuffing, Fake-Engagement-Muster (`META_FB_SPAM_CRACKDOWN_2025`).

## 3. Instagram: verbindliche Regeln

### 3.1 Kernsignale (`META_IG_FEED_2026`, `META_IG_EXPLORE_2026`, `META_IG_REELS_2026`)

Aktuelle öffentliche Priorisierung: Betrachtungszeit/Watch Time, Likes pro Reach, Sends pro Reach. Likes sind tendenziell relevanter für verbundene/bestehende Zielgruppen; Sends sind relevanter für Distribution/Discovery außerhalb bestehender Followerbeziehungen. Dies ist keine fixe Gewichtungsformel.

### 3.2 Statische Bildposts

Watch Time bei Bildern nicht als Videowiedergabezeit missverstehen. Praktisch: Zeit und Aufmerksamkeit am Post, Lesedauer, visuelle/inhaltliche Bindung. Keinen erfundenen statischen Dwell-Time-Schwellenwert einführen.

### 3.3 Saves

Positives Signal, aber nicht pauschal über Likes oder Sends stellen.

### 3.4 Kommentare

Relevant, aber niemals automatisch wichtiger als Likes (rejected claim). Keine erfundenen Multiplikatoren für Kommentar-Threads oder Creator Replies.

### 3.5 Search und Themenverständnis

Thema eindeutig benennen, natürlich relevante Begriffe verwenden. Kein Keyword Stuffing. Semantische Klarheit vor künstlicher Keyword-Dichte.

## 4. Hashtags

**Instagram: maximal 5 Hashtags.** Dieser Hard Cap gilt für `instagram-text-optimizer` und `instagram-hashtag-research` gleichermaßen; beide Skills dürfen keine widersprechende Zahl verwenden.

Hashtags sind primär Kontext, Kategorisierung, Search-/Discovery-Unterstützung — nicht automatischer Reach Booster (rejected claim). Bei Hashtag-Recherche: aktuelle Prüfung durchführen, semantische Passung priorisieren, keine erfundenen Volumen-/Trendwerte, generische Tags (`#viral`, `#fyp`, `#instagood`) nicht zur künstlichen Reichweitenoptimierung nutzen, keine fünf Tags erzwingen, wenn weniger sinnvoll sind. Bevorzugt: Thema, konkreter Sachbegriff, Ort/Region, Ereignis, legitime Kampagne/Organisation.

**Facebook**: Hashtagblöcke vermeiden; Hashtags nur bei tatsächlichem Informations- oder Suchwert.

## 5. Text-Bild-System

Bild und Caption bilden ein System, keine Wiederholung desselben Inhalts:

```
Bild:    Stoppen -> Orientieren -> Kernaussage verankern
Caption: Kontext -> Beleg -> Differenzierung -> Konsequenz -> natürliche Handlung
```

Produktionsheuristik (kein offizieller Meta-Mechanismus): `Stop -> Orientieren -> Verstehen -> Vertiefen -> Interagieren oder Weitergeben`.

## 6. Caption-Standard

Erste sichtbare Zeilen liefern möglichst früh: Aussage, Konflikt, Nutzen, relevante Zahl, Ergebnis oder konkrete Frage. Kein „Heute möchten wir euch darüber informieren, dass …", wenn die Sache direkt gesagt werden kann. Kein künstlicher Curiosity Gap, kein irreführender Clickbait.

Bevorzugter Aufbau: Zeile 1 unmittelbare Relevanz -> was ist passiert -> warum relevant -> Beleg/Zahl/Kontext/Konsequenz -> natürliche Frage, Handlung oder Weitergabeoption. Nur so lang wie nötig; notwendige Differenzierungen nicht für einen härteren Hook entfernen.

## 7. Engagement

Verboten: „Kommentiere JA", „Like wenn du zustimmst", „Markiere drei Freunde", „Teile unbedingt damit der Algorithmus …", Engagement Pods, Fake Accounts, koordinierte Scheinkommentare, Bots (`META_FB_ENGAGEMENT_BAIT_2017`).

Zulässig, wenn die Frage tatsächlich zum Inhalt gehört: „Wie erlebst du das?", „Welche Erfahrung hast du damit?", „Was müsste sich konkret ändern?". Weitergabe darf natürlich angeregt werden, wenn sachlich sinnvoll — nicht mechanisch bei jedem Post.

## 8. Original Content Standard

Bevorzugen: eigenes Foto, eigene Infografik/Visualisierung/Illustration, eigene journalistische Einordnung/Analyse, substanziell transformiertes Fremdmaterial.

Nicht gleichwertig: heruntergeladenes Meme, fremder Screenshot ohne Mehrwert, Repost mit neuem Rahmen, Wasserzeichen eines anderen Creators, minimal veränderter Fremdpost. Screenshots bleiben zulässig, wenn dokumentarisch notwendig — keine pauschale Screenshot-Strafe behaupten.

## 9. KI-Bilder

KI-Herkunft allein ist kein bestätigter allgemeiner organischer Rankingmalus (rejected claim). Separat prüfen: Kennzeichnung (`META_AI_LABELING_2024`), Authentizität, Täuschung, Identitätsmissbrauch, Manipulation, Qualität, Policy, Originalität, Recommendation Eligibility. Nie behaupten: „Meta erkennt KI und reduziert deshalb automatisch die Reichweite."

## 10. Feed-Grafik-Standard

Verbindlicher gemeinsamer Facebook/Instagram-Feed-Masterstandard: **Canvas 1080 x 1350 px, Aspect Ratio 4:5**. 4:5 ist Produktionsstandard wegen mobiler Bildschirmfläche — niemals als bestätigter Rankingbonus behaupten (rejected claim). Instagram unterstützt zusätzlich natives 3:4 als alternative Quell-/Ausgabestrategie, ohne den gemeinsamen 4:5-Masterstandard zu ersetzen.

Exakte Sicherheitsbereiche, Dateikonventionen und Cross-Platform-Delivery: [platform-safe-zones.md](../../adaptive-poster-image-series/references/platform-safe-zones.md) im `adaptive-poster-image-series`-Skill. Diese Werte sind interne Produktionsreserven, keine offiziellen Meta-Safe-Zones, und werden dort als Release-Gate technisch validiert (`scripts/validate_platform_delivery.py`, `scripts/validate_publication_plan.py`).

## 11. Grafische Informationshierarchie

Bei 1080 x 1350: Headline bevorzugt 4–9 Wörter (bis ~12 nur bei begründetem Bedarf), Arbeitsbereich x 100–980 / y 120–430, typische Headlinegröße 72–100 px. Unterzeile 38–52 px, maximal ein bis zwei kurze Zeilen. Quellenzeile 30–38 px, nur wenn mobil tatsächlich lesbar — keine mikroskopischen URLs im Bild. Maximal drei primäre aktive Ebenen: Hauptaussage, Zahl/Unterzeile/Motiv, Quelle/Absender. CTA bevorzugt in der Caption, außer er gehört zwingend zum Motiv.

## 12. Bild-Text-Verhältnis

Keine automatische prozentuale Meta-Textgrenze behaupten, insbesondere keine alte „20-Prozent-Text-Regel" als organischen Feed-Rankingfaktor (rejected claim — diese Regel war historisch eine Werbeanzeigen-Richtlinie, nie ein organischer Faktor). Standardmäßig begrenzen auf: eine Headline, eine kurze Unterzeile oder Hero-Zahl, eine kleine Quelleninformation, optional dezentes Branding. Längere Erklärung gehört in die Caption. Maßstab ist mobile Verständlichkeit, kein erfundener Bildtext-Algorithmusscore.

## 13. Personen und Gesichter

Keinen allgemeinen Gesichtsbonus behaupten (rejected claim). Gesichter können aus UX-Gründen Aufmerksamkeit fördern; reale Personen bevorzugen, wenn Person, Verantwortung, Betroffenheit, Emotion oder dokumentarische Authentizität Teil der Geschichte sind. Bei Personenmotiven (Designheuristiken, keine Rankingfaktoren): Gesicht/Oberkörper ca. 30–50 % Bildbreite, wesentliche Gesichtspartien innerhalb der zentralen 70–80 %, keine Headline über Augen/Mund, keine kritischen Gesichtsteile unmittelbar an der Außenkante.

## 14. Kontrast und Accessibility

Lesbarkeit verbindlich prüfen. Referenz: WCAG-Kontrastanforderungen (normaler Text 4.5:1, großer Text 3:1; [W3C WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)) — dies ist Accessibility-Orientierung, kein Meta-Rankingfaktor. Alt-Text für Zugänglichkeit erstellen, nicht als verstecktes Keywordfeld; keinen Reichweitenbonus durch Alt-Text behaupten (rejected claim).

## 15. Politische und gesellschaftspolitische Inhalte

Bestehende Sicherheitsregel aus [SKILL.md](../SKILL.md) und [framework.md](framework.md) gilt unverändert: keine Optimierung nach individueller politischer Überzeugbarkeit, keine psychografische Wähleransprache, keine Wahlverhaltensprognose, keine manipulative Zielgruppensegmentierung.

Zulässig: Lesbarkeit, Quellenklarheit, Faktenprüfung, Originalität, mobile Darstellung, Formatfit, Search-Passung, allgemeine dokumentierte Rankingmechanismen, Recommendation Eligibility, Accessibility. Die Pauschalaussage „Politischer Content wird generell heruntergestuft" nicht verwenden — Content Controls und Recommendation-Personalisierung differenziert behandeln.

Für EU Paid Media gilt separat und verbindlich (`META_EU_POLITICAL_ADS_2025`): seit 6. Oktober 2025 endet politische, wahlbezogene und gesellschaftspolitische Meta-Werbung in der EU. Dies betrifft ausschließlich bezahlte Werbung und darf nicht mit organischer Distribution gleichgesetzt werden.

## 16. Recommendation Eligibility

Eigener obligatorischer Prüfpunkt, strikt zu unterscheiden von reiner Policy-Konformität (`META_RECOMMENDATION_GUIDELINES_2020`):

```
Community Standards compliant
Recommendation eligible
normal gerankt
eingeschraenkt distribuiert
entfernt
Account Restriction
```

Ein erlaubter Post ist nicht automatisch vollständig empfehlungsfähig. Vor jeder Aussage über Non-Follower-Reach immer Recommendation Eligibility mitprüfen.

## 17. Posting-Zeit und First Hour

Keine universelle Golden Hour, keine harte First-Hour-Regel (rejected claim). Eigene Account Insights haben Vorrang vor globalen Benchmarks. Frühe Performance darf als korreliertes Signal/Account-Analysemerkmal behandelt werden, nicht als deterministische Schwelle. Nicht empfehlen: nach 30/60 Minuten löschen und neu posten, künstliche Erstinteraktionen organisieren.

## 18. A/B-Tests und Account Learning

Die Lernschleife aus [framework.md](framework.md) Abschnitt 5–6 unverändert verwenden: `Observe -> Segment -> Compare -> Hypothesis -> Test -> Measure -> Update`. Pro Test möglichst eine primäre Variable ändern (Headline, Gesicht vs. Typografie, kurze vs. lange Caption, Frage vs. Feststellung, 4:5 vs. 1:1, weniger vs. mehr Bildtext, Dokumentarfoto vs. Grafik, Fakt- vs. emotionaler Hook). Einzelposts erzeugen keine universelle Regel. Paid und Organic strikt trennen; Korrelation nicht als Kausalität ausgeben.

## 19. Mythen (regressionsgesichert)

Alle folgenden Aussagen sind in [evidence-records.json](evidence-records.json) als `claims` mit `status: "rejected"` erfasst und werden durch `python scripts/validate_social_evidence.py` sowie `tests/test_meta_feed_strategy.py` regressionsgeprüft:

1. Hashtags erhöhen automatisch die Reichweite.
2. Facebook bestraft grundsätzlich jeden externen Link.
3. Mehr Text im Bild reduziert automatisch die organische Reichweite.
4. Kommentare sind immer wichtiger als Likes.
5. 4:5 erhält automatisch mehr Reichweite als 1:1 (Facebook und Instagram).
6. Meta erkennt KI-Bilder und reduziert deshalb automatisch die Reichweite.
7. Bearbeitete Beiträge werden generell bestraft.
8. Das Wort „Link" reduziert die Reichweite.
9. Der Link muss in den ersten Kommentar.
10. Die ersten 60 Minuten entscheiden endgültig über einen Post.
11. Viele Kommentare bedeuten automatisch hochwertigen Content.
12. Gesichter erhalten automatisch einen Rankingbonus.
13. Alt-Text erzeugt automatisch zusätzliche Reichweite.

Ein `rejected`- oder `deprecated`-Claim darf niemals als aktive Produktionsregel verwendet werden. Ein neuer Mythos wird als zusätzlicher `claims`-Eintrag mit `status: "rejected"` ergänzt, nie als Prosa-Fußnote dupliziert.

## 20. Source of Truth, Freshness und Pflege

Abrufstand dieser Recherche: 22. September 2026, Europe/Vienna. Ohne bestätigten Live-Webzugriff gilt dieser Stand als eingefroren; keine zusätzliche Aktualität vortäuschen.

Priorität bei späteren zeitkritischen Aufträgen:

```
aktuelle offizielle Surface-Dokumentation
> aktuelle offizielle allgemeine Meta-Dokumentation
> ältere offizielle Engineering-/Newsroom-Dokumentation
> empirische Drittquellen
> Hypothese
```

Ältere offizielle Dokumentation (z. B. `META_NEWSFEED_PREDICT_2021`, `status: "superseded"`) bleibt als historischer Beleg gültig, hat aber keine automatische aktuelle Priorität gegenüber neueren Transparency-Center-Records.

Pflegeprozess für künftige Meta-Änderungen:

1. Primärquelle erneut über die in `evidence-records.json` hinterlegte URL prüfen.
2. Bei inhaltlicher Änderung: bestehenden Record/Claim nicht überschreiben, sondern neuen Record/Claim anlegen und den alten auf `status: "superseded"` oder `status: "deprecated"` setzen.
3. Neue oder geänderte Mythen als `claims` mit `status: "rejected"` ergänzen, nie als Freitext.
4. `python scripts/validate_social_evidence.py` und `python -m pytest tests/test_meta_feed_strategy.py` ausführen, bevor die Änderung als abgeschlossen gilt.

## 21. Quellenkorpus

Alle in dieser Datei referenzierten `source_id`-Werte sind in [evidence-records.json](evidence-records.json) mit echter URL, Publisher, Titel und Abrufdatum hinterlegt — keine internen Recherche-Marker, nur dauerhaft nachvollziehbare Quellen. Ergänzend für Accessibility: [WCAG 2.1 Contrast Minimum](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html) (kein Meta-Ranking-Mechanismus, reine Kontrastreferenz).
