---
name: journalistic-osint-governance
description: >-
  Govern a public-interest or investigative-journalism OSINT inquiry before collection, publication,
  or cross-border sharing. Use for corruption, public-office accountability, corporate ownership,
  human-rights, conflict, political, media-forensics, source-protection, or sensitive-personal-data
  investigations. Establishes lawful scope, necessity and proportionality, source protection, data
  minimisation, a verifiable evidence record, publication fairness and mandatory editor/legal stop-gates.
---

# Investigative Journalism and OSINT Governance

Use this Skill before `investigate-anything` whenever an OSINT inquiry could identify a living person,
affect reputation or safety, use sensitive data, concern a public official or alleged wrongdoing, cross
borders, or lead to publication. It is a governance and documentation layer, not a substitute for
jurisdiction-specific legal advice.

## Non-negotiable boundary

The purpose is defensible public-interest reporting, not private intelligence gathering. A public role,
an indexed page or a technically exposed system does not remove privacy, contractual, criminal-law or
source-protection duties.

Do not use this workflow to:

- obtain or use credentials, access accounts, join closed groups under false pretences, bypass access
  restrictions, evade a platform's anti-abuse controls, scan or exploit a target, or retrieve exposed
  material beyond a minimal public search result;
- track an individual's location or routine, identify uninvolved relatives, publish personal contact,
  home, health, immigration, financial, sexual, religious or other sensitive data without a compelling,
  documented public-interest necessity and completed approval gate;
- buy, solicit, trade or retain leaked datasets or credentials; nor turn a lead into an accusation
  without independent verification and a fair opportunity to respond.

If the requested action falls in either category, stop collection. Record the boundary and seek an
editorial, legal, safeguarding or authorised-security route as appropriate.

## Case intake: write before searching

Create the compact record in [references/case-intake.md](references/case-intake.md). At minimum it must
state the story question, decision/publication purpose, target discriminators, public-interest rationale,
jurisdictions, allowed sources and methods, excluded people/data/methods, intended retention and the
editorially accountable person. A vague request to "look into" a private individual is not enough.

Use the least intrusive source that can answer the question. Start with official records, disclosures,
archives, reputable reporting, public institutional data, direct on-the-record questions and passive
third-party observations. Record a negative result as a result; do not widen collection merely because
the first route is inconclusive.

## International baseline; local law still controls

Apply the working principles in [references/international-standards.md](references/international-standards.md):
freedom to seek, receive and impart information, protection of private life and data, source protection,
necessity, proportionality, accuracy, fairness and remedy. In Europe, GDPR Article 85 requires national
law to reconcile data protection with freedom of expression and information, including journalism. It is
not a blanket exemption. Identify the countries of collection, subject, storage, publication and audience;
where a material legal question remains, route it to a qualified local reviewer.

## Mandatory routing and stop-gates

1. **Scope and risk gate.** Complete case intake and the risk screen. No authorisation or defensible
   public-interest purpose: do not proceed.
2. **Collection gate.** Run `investigate-anything` to formulate falsifiable hypotheses and a passive plan.
   Use the narrow specialist (for example `x-ray-a-company`, `spoe-parlamentsforensik`,
   `austria-open-data-research`, `where-was-this-taken`) only for the approved question.
3. **Evidence gate.** Keep the provenance ledger in [references/evidence-and-publication.md](references/evidence-and-publication.md).
   Distinguish source fact, corroborated fact, inference, allegation and unknown. Do not use an AI output,
   search snippet, data-broker result or scan banner as proof.
4. **Fairness gate.** For an adverse material claim, seek a meaningful right of reply with a clear,
   proportionate summary of the evidence and a realistic deadline, unless doing so would create a concrete
   safety, evidence-destruction or legal risk recorded by an editor.
5. **Publication gate.** Use `write-the-intel-brief` for the internal record, then `fact-check` and a
   named editor. Apply minimisation: publish only what is necessary to substantiate the public-interest
   claim, with dates, confidence and limitations.

The following always require senior editorial and jurisdiction-specific legal review before collection
continues or anything is published: minors or vulnerable people; special-category data; private location
or routine; leak material; protected/confidential sources; active criminal allegations; conflict-zone or
authoritarian-state work; cross-border transfer of personal data; or foreseeable serious safety/reputation
harm.

## Source protection and safe handling

Separate a source's identity from reporting notes; do not put contact details, raw sensitive material or
credentials into prompts, shared chat, public documents or the evidence ledger. Use the handling standard
in [references/source-protection.md](references/source-protection.md). Record access, retention and deletion
decisions. Never promise anonymity that the outlet cannot technically or legally protect.

## High-risk upstream skill overrides

When these installed upstream skills are relevant, this local policy narrows their use:

- `pattern-of-life-from-socials`: only bounded, publication-relevant public material; no ongoing location
  or routine monitoring, no family/minor profiling, no following, messaging, story viewing or engagement.
- `google-like-a-spy` and `find-exposed-servers`: discovery from already indexed/passive data only;
  no retrieval, enumeration, probing, direct scan, credential use or circumvention. For third-party
  security research, written authority is required; for journalism, report a minimal verified observation
  through a responsible disclosure/CERT route and pause.
- `investigate-without-getting-made`: source and reporter safety may justify compartmentalised, lawful
  non-interactive browsing. It never authorises a deceptive persona, false-pretext entry, a burner account,
  a residential proxy, Tor or other tooling to defeat platform safeguards or observe a person covertly.

## Output contract

Before any collection, return: **approved question**, **public-interest rationale**, **jurisdictions and
assumptions**, **in/out of bounds**, **risk level**, **collection plan**, **approval status** and **stop
conditions**. For an investigation result, return an internal evidence brief—not a dossier—with source
grades, confidence, adverse-claim response status, uncertainty, retention decision and a publication
recommendation of `PROCEED`, `HOLD FOR REVIEW`, or `DO NOT PUBLISH`.

Read [references/high-risk-routing.md](references/high-risk-routing.md) when selecting a specialist
workflow or handling political, corporate, cross-border or security-related reporting.
