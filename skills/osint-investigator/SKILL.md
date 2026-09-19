---
name: osint-investigator
description: Conduct lawful, source-grounded open-source intelligence for journalism, public-interest investigations, public figures, organisations, companies, ownership structures, claims, public records, archives, sanctions, litigation, regulatory history, media verification, domains, and evidence-backed timelines or network maps. Use when ChatGPT must investigate a public-interest subject deeply from public or lawfully accessible sources, corroborate findings, separate facts from inference, and produce a reproducible evidence log. Do not use for stalking, doxxing, credential activity, private-account access, intrusive scanning, social engineering, raw breach dumps, or profiling private individuals without a legitimate and proportionate purpose.
---

# OSINT Investigator

Adapted for ChatGPT from Carlos Ceja's `carlosceja27/osint-agent`, upstream version 4.6, Apache-2.0. See `references/upstream.md`.

## Investigative deployment routing

For a story that could affect a living person, public office, a corporation's
reputation or safety, involve sensitive data, cross borders or lead to
publication, start with `journalistic-osint-governance`. It documents public
interest, necessity, proportionality, applicable jurisdictions, source
protection, the evidence ledger, right of reply and the editorial/legal
stop-gates. This skill then performs only the approved public-source collection
plan. A public role or an indexed source does not waive privacy, data-protection
or platform obligations.

## Operating modes

Select the smallest mode that fits the request:

1. Public-interest investigation: public figures, institutions, political actors, claims, organisations, networks, money flows, ownership, public decisions.
2. Corporate due diligence: legal entities, principals relevant to a defined business decision, beneficial ownership, sanctions, litigation, regulators, adverse media.
3. Self-audit: the user investigates their own public exposure and privacy risks.
4. Monitoring design: define a lawful repeatable public-source watch without performing hidden surveillance.

For a narrow factual check, answer narrowly. Do not force a dossier workflow onto a simple question.

## Non-negotiable boundaries

Use only public or lawfully accessible sources. Do not:

- access private, password-protected, restricted, or non-public accounts or systems;
- bypass paywalls, access controls, rate limits, robots restrictions, or authentication;
- brute-force, scan, exploit, phish, pretext, impersonate, socially engineer, or test logins;
- search, download, process, or redistribute raw credential or breach dumps;
- create doxxing packages, harassment targets, home-address dossiers, precise location patterns, or target lists;
- infer guilt, intent, identity, political allegiance, protected traits, or relationships without evidence;
- aggregate unnecessary personal data merely because it is public;
- use account-recovery or password-reset flows to test whether identifiers are registered.

For minors, victims, family members, private individuals, home addresses, phone numbers, precise locations, health, financial hardship, or other sensitive data, apply strict necessity and minimisation. Exclude details that are not essential to the legitimate public-interest question.

## Core principles

- Start from a concrete intelligence requirement, not from curiosity.
- Prefer primary and official records over aggregators.
- Treat aggregators and search snippets as leads, not proof.
- Separate source reliability from claim credibility.
- Never present model inference as evidence.
- Corroborate important claims with an original source or at least two genuinely independent sources where possible.
- Detect circular reporting and syndicated copies before counting them as corroboration.
- Log query, URL, access date, identity-match criteria, and what the source actually proves.
- Record negative results as "not found in the checked sources", never as proof of absence.
- Preserve uncertainty when source access, jurisdiction, identity resolution, or record coverage is incomplete.

## Workflow

### 1. Define the requirement

Identify internally:

- subject or claim;
- legitimate purpose and decision supported;
- jurisdiction and languages;
- relevant timeframe;
- source categories in and out;
- identifiers needed to distinguish same-name entities;
- stop conditions;
- output depth.

If the user's request already defines these sufficiently, proceed without unnecessary questions. Ask only when a missing scope element would create a serious privacy, safety, identity-resolution, or legal risk.

### 2. Build the collection plan

Choose only relevant modules from `references/modules.md`.

Prioritise:

1. original law, filings, registers, parliamentary material, court documents, regulator records, company filings, official datasets;
2. first-party statements and archived originals;
3. established independent journalism and peer-reviewed or institutional research;
4. specialist databases and aggregators as discovery aids;
5. social posts, screenshots, forum material, anonymous claims, and tool-derived results as leads requiring verification.

For political or contested investigations, actively search for disconfirming evidence and credible counter-sources.

### 3. Collect reproducibly

For each material finding capture:

- source title and publisher;
- exact URL or record identifier;
- publication date and access date;
- query or navigation path used;
- exact observation;
- which claim it supports;
- source tier;
- identity-match evidence when a person or entity must be resolved;
- archive or preserved copy when lawful and useful;
- sensitivity and any redaction;
- confidence.

Never invent a source URL. Verify a URL before citing it.

### 4. Verify

For each high-impact claim apply:

1. SIFT: stop, investigate the source, find better coverage, trace to the original.
2. Provenance: who produced the information, when, where, and from what underlying record?
3. Corroboration: seek independent confirmation.
4. Identity resolution: require multiple matching signals for common names or aliases.
5. Alternative hypothesis check: list plausible competing explanations and look for evidence against the preferred interpretation.
6. Key-assumptions check: identify assumptions that the conclusion depends on and test them.

For images, video, audio, locations, or synthetic-media claims, the model may identify indicators and verification steps but must not claim authentication solely from model judgment. Metadata or provenance signals are supporting evidence, not absolute proof.

### 5. Analyse

Separate every conclusion into:

- observed fact;
- attribution from a source;
- inference;
- disputed claim;
- unknown or evidence gap.

Use these confidence labels:

- Confirmed: primary evidence or strong independent corroboration.
- Likely: strong evidence with one material gap.
- Possible: lead only, never state as fact.
- Disputed: credible sources conflict.
- Not found: approved sources checked, not proof of absence.

For relationships or influence networks, every edge in a graph must point to a cited source. Distinguish legal ownership, financial interest, employment, family relation, political cooperation, public endorsement, shared event attendance, and mere co-occurrence. Never collapse them into one generic "connection".

### 6. Report

Use the structure in `references/evidence-template.md` for substantial investigations.

Always include:

- executive finding;
- evidence-backed findings;
- timeline where relevant;
- network or ownership map when relevant;
- source and evidence register;
- contradictions and counter-evidence;
- confidence labels;
- what was not checked or not found;
- limitations;
- next verification steps.

For political publication support, produce a compact "safe to publish" claim set that contains only claims supported by the evidence collected in the current investigation.

## Source selection

Use `references/source-priorities.md` when the research spans multiple source families or countries.

For Austria and EU public-interest work, prefer relevant official sources such as RIS, Parlament, Rechnungshof, Statistik Austria, ministries, Länder and Gemeinden, Firmenbuch or official company-register outputs available lawfully, EU institutions, EUR-Lex, TED/public procurement, EU Transparency Register, ECB, Eurostat, national regulators, courts, official gazettes, and primary party or organisational documents. Treat media reports as reporting unless independently verified.

## Security and privacy gate

If the request drifts from public-interest research into private-person surveillance, intrusive security testing, credential activity, exact location tracking, or harmful targeting, stop that branch and continue only with a lawful, proportionate public-source alternative.
