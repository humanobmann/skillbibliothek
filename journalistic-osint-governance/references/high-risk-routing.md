# Specialist routing for public-interest reporting

| Reporting question | Approved specialist path | Extra gate |
|---|---|---|
| Austrian public spending, law, register or parliamentary record | `austria-open-data-research` or `spoe-parlamentsforensik` → `fact-check` | Cite primary parliamentary/official record and observation date. |
| Corporate ownership, contracts or sanctions question | `x-ray-a-company` → `graph-the-network` → `write-the-intel-brief` | Confirm legal-entity identity across jurisdictions; do not identify beneficial owners from a weak proxy. |
| Political claim, campaign statement or public-office accountability | `politik-analyse` → primary sources → `fact-check` | Separate office-holder conduct from private/family material; offer response for material criticism. |
| Image/video authenticity or location | `is-this-photo-real`, `find-the-original-image`, `where-was-this-taken` | Preserve uncertainty and avoid publishing location information that creates foreseeable safety risk. |
| Publicly indexed data exposure | `google-like-a-spy` or `find-exposed-servers` | Observe/index only; no access, download, testing or scan. Responsible disclosure/CERT before publication where appropriate. |
| Social-media claim already attributable to a public actor | bounded `pattern-of-life-from-socials` | No private accounts, interactions, location/routine dossier or uninvolved third parties. |
| Leaks/breaches | `what-leaked-about-you` or `find-leaks-in-the-wild` only for lawful, necessary verification | No purchase, download of corpora, credential use or retention; legal/editor approval before handling. |

Every route remains subject to the case-intake, source-protection and publication gates. When a route is not listed, choose the least intrusive method or hold for review.
