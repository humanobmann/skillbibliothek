# Platform Profiles

Pruefstand: 2026-09-22. Volatile Regeln bei spaeteren zeitkritischen Aufgaben erneut gegen die verlinkten Primaerquellen pruefen.

Die kanonischen Source Records stehen in [evidence-records.json](evidence-records.json). Jeder Record verwendet genau einen Mechanismustyp aus `RANKING`, `SEARCH`, `RECOMMENDATION_ELIGIBILITY`, `POLICY` oder `MONETIZATION`. Kombinierte Mechanismustypen sind unzulaessig.

## Facebook

Fuer Facebook gilt zusaetzlich zu diesem Profil verbindlich [meta-feed-strategy.md](meta-feed-strategy.md) als kanonische Quelle fuer Ranking-Modell, Originalitaet, Links, Captions, Hashtags, Feed-Grafik-Standard, Recommendation Eligibility und Mythen.

Verwendete Source IDs:

- `META_FB_FEED_RECS_2026` fuer Feed Recommendations Ranking
- `META_FB_FEED_2026` fuer Feed Ranking
- `META_FB_ORIGINAL_2026` fuer Originalitaet und Recommendation Eligibility
- `META_FB_ENGAGEMENT_BAIT_2017` fuer Engagement-Bait-Policy
- `META_FB_SPAM_CRACKDOWN_2025` fuer Spam-/Unoriginal-Content-Policy
- `META_FB_DISTRIBUTION_GUIDELINES_2021` fuer Distribution Guidelines
- `META_RECOMMENDATION_GUIDELINES_2020` fuer Recommendation Eligibility
- `META_HOW_AI_RANKS_2023` fuer das Retrieval/Predictions/Value-Scoring-Modell
- `META_NEWSFEED_PREDICT_2021` (superseded) fuer historische Signalbeispiele
- `META_EU_POLITICAL_ADS_2025` fuer das Ende politischer/wahlbezogener/gesellschaftspolitischer Meta-Werbung in der EU (Paid Media, keine organische Reichweite)

Belegt: Feed und Feed Recommendations sind getrennte Systeme. Meta dokumentiert personalisierte Predictions und dynamische Signale; fuer Feed Recommendations unter anderem Betrachtungsdauer und Share-/Like-Wahrscheinlichkeit. Meta dokumentiert 2026 eine staerkere Priorisierung origineller bzw. substanziell transformierter Inhalte und Depriorisierung duplizierter oder minimal veraenderter Inhalte.

Nicht behaupten: fixe Idealtextlaenge, feste First-Hour-Verteilung oder garantierte Kommentarhebel — siehe die regressionsgepruefte Mythenliste in [meta-feed-strategy.md](meta-feed-strategy.md).

## Instagram

Fuer Instagram gilt zusaetzlich zu diesem Profil verbindlich [meta-feed-strategy.md](meta-feed-strategy.md), insbesondere der Hashtag-Hard-Cap (maximal 5) und der 4:5-Feed-Grafik-Standard.

Verwendete Source IDs:

- `META_IG_FEED_RECS_2026` fuer Feed Recommendations
- `META_IG_FEED_2026` fuer Feed
- `META_IG_EXPLORE_2026` fuer Explore
- `META_IG_REELS_2026` fuer Reels
- `META_IG_CREATOR_BEST_PRACTICES_2024` fuer Originalitaet und Recommendation Eligibility
- `META_AI_LABELING_2024` fuer KI-Kennzeichnung (Policy, kein Rankingfaktor)

Belegt: Feed, Feed Recommendations, Explore und Reels sind getrennte Surfaces. Explore dokumentiert unter anderem Like-/Save-Wahrscheinlichkeit, Viewing und negative Feedbacksignale. Reels dokumentiert Watch- und Auswahlverhalten sowie Interessennaehe.

Nicht behaupten: feste Hashtag-Anzahl ueber 5, universelle Caption-Laenge oder dauerhaften Postingzeit-Boost.

## TikTok

Verwendete Source IDs:

- `TIKTOK_FYF_RANKING_2026` fuer For You Ranking
- `TIKTOK_SEARCH_2026` fuer TikTok Search
- `TIKTOK_FYF_ELIGIBILITY_2026` fuer For You Recommendation Eligibility
- `TIKTOK_CREATOR_REWARDS_2024` fuer Creator Rewards Monetization

### For You: OFFICIAL RANKING

TikTok dokumentiert User Interactions, darunter Like, Share, Comment, Full Watch und Skip, Content Information und User Information. Watch-Verhalten ist Teil der Interaktionssignale.

### Search: OFFICIAL SEARCH

TikTok dokumentiert vergangenes Search- und Watch-Verhalten, Query Match als Content Information, Hashtags, Sounds und User Information. Fuer die meisten Nutzer wird Content Information einschliesslich Match zur konkreten Suchanfrage generell staerker gewichtet.

### Creator Rewards: OFFICIAL MONETIZATION

Originality, Play Duration, Search Value und Audience Engagement sind in der zitierten Quelle Metriken der Creator-Rewards-Verguetungsformel.

Hard Rule: Diese Creator-Rewards-Metriken nicht als bestaetigte For-You-Rankingfaktoren ausgeben, sofern keine separate aktuelle Rankingquelle dies dokumentiert.

## YouTube

Verwendete Source IDs:

- `YT_RECOMMENDATION_PERFORMANCE_2026` fuer Recommendation Ranking
- `YT_SEARCH_DISCOVERY_2026` fuer Search
- `YT_SHORTS_RANKING_2026` fuer Shorts Ranking

Belegt: YouTube beschreibt Performance in Appeal, Engagement und Satisfaction. AVD und APV sind dokumentierte Rankinginformationen. Bei Shorts ist Chose-to-view zusaetzlich dokumentiert. Search und Recommendations nicht gleichsetzen. Titel und Thumbnail muessen das tatsaechliche Video korrekt repraesentieren.

Nicht behaupten: fixe ideale Videolaenge, Upload-Uhrzeit als dauerhaften Rankinghebel oder Tags als zentralen Discovery-Hebel.

## LinkedIn

Verwendete Source IDs:

- `LI_FEED_HELP_2026` fuer Feed Ranking
- `LI_CONTENT_RECS_2026` fuer Recommendation Eligibility
- `LI_SUGGESTED_2026` fuer Suggested Posts Ranking
- `LI_ENGAGEMENT_POLICY_2026` fuer Engagement Policy
- `LI_FEED_ENGINEERING_2026` fuer Feed Engineering
- `LI_DWELL_ENGINEERING` fuer Dwell-Time Engineering

Belegt: LinkedIn Feed nutzt viele Kontext-, Profil-, Netzwerk- und Aktivitaetssignale. Aktuelle LinkedIn-Dokumentation nennt professionelle Relevanz und Qualitaet fuer Recommendations/Suggested Posts. LinkedIn Engineering dokumentiert long dwell und skip sowie aktive Interaktionen im Feed-Ranking. Keine festen universellen Dwell-Schwellen ableiten. Kuenstliche Engagement-Manipulation kann begrenzt werden.

Nicht behaupten: fixe Kommentar-zu-Like-Gewichte, Golden-Hour-Regel oder pauschale Link-Penalty ohne aktuelle offizielle Quelle.
