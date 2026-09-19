# Platform Profiles

Pruefstand: 2026-09-19. Volatile Regeln bei spaeteren zeitkritischen Aufgaben erneut gegen die verlinkten Primaerquellen pruefen.

Die kanonischen Source Records stehen in [evidence-records.json](evidence-records.json). Jeder Record verwendet genau einen Mechanismustyp aus `RANKING`, `SEARCH`, `RECOMMENDATION_ELIGIBILITY`, `POLICY` oder `MONETIZATION`. Kombinierte Mechanismustypen sind unzulaessig.

## Facebook

Verwendete Source IDs:

- `META_FB_FEED_RECS_2026` fuer Feed Recommendations Ranking
- `META_FB_FEED_2026` fuer Feed Ranking
- `META_FB_ORIGINAL_2026` fuer Originalitaet und Recommendation Eligibility

Belegt: Feed und Feed Recommendations sind getrennte Systeme. Meta dokumentiert personalisierte Predictions und dynamische Signale; fuer Feed Recommendations unter anderem Betrachtungsdauer und Share-/Like-Wahrscheinlichkeit. Meta dokumentiert 2026 eine staerkere Priorisierung origineller bzw. substanziell transformierter Inhalte und Depriorisierung duplizierter oder minimal veraenderter Inhalte.

Nicht behaupten: fixe Idealtextlaenge, feste First-Hour-Verteilung oder garantierte Kommentarhebel.

## Instagram

Verwendete Source IDs:

- `META_IG_FEED_RECS_2026` fuer Feed Recommendations
- `META_IG_FEED_2026` fuer Feed
- `META_IG_EXPLORE_2026` fuer Explore
- `META_IG_REELS_2026` fuer Reels

Belegt: Feed, Feed Recommendations, Explore und Reels sind getrennte Surfaces. Explore dokumentiert unter anderem Like-/Save-Wahrscheinlichkeit, Viewing und negative Feedbacksignale. Reels dokumentiert Watch- und Auswahlverhalten sowie Interessennaehe.

Nicht behaupten: feste Hashtag-Anzahl, universelle Caption-Laenge oder dauerhaften Postingzeit-Boost.

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
