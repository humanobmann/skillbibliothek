# Canva Account Router 5.0

## Owner mapping

Resolve Canva link_id from the live connector's account list by exact display name. Never store connector tokens, link IDs, private design IDs or OAuth secrets in this public GitHub repository.

| project_scope | Canva display name | Brand namespace |
| --- | --- | --- |
| parliamentary | SPÖ | Robert Laimer / parliamentary |
| party | SPÖ | Official SPÖ, SPÖ Klub, SPÖ NÖ, SPÖ St. Pölten Sektion VII |
| personal | Peter | Peter Schuller personal, author projects, independent political commentary |
| ngo | Peter | Menschlichkeit Österreich, separate NGO Brand Kit |

The same account can hold multiple unrelated brand kits. The personal political role does not automatically authorize official party branding.

## Decision rules

1. Route from the explicitly named mandate, organization and intended publisher, not biography or previous unrelated jobs.
2. Robert Laimer / PAMI / official SPÖ / Sektion VII events, newsletters and newspaper: SPÖ.
3. Personal editorial, portraits, book promotion, private satire and the user's own political commentary: Peter.
4. Menschlichkeit Österreich: Peter account but NGO namespace, never borrow SPÖ assets.
5. Split mixed assignments into distinct jobs, brand kits, asset libraries, output IDs and review states.
6. When ambiguous, state the reasonable assumption for read-only work; stop any uncertain write or publication.
7. Historical official party designs stored in Peter are references only. To migrate, rebuild a new master in SPÖ with authorized assets, explicit rights and technical capability. No automatic cross-account copy or upload.

## Write gate

Use only the live account-specific link_id accepted by the Canva connector. If the target account is inaccessible, report BLOCKED. Do not fall back to the other account. Every master keeps its original design ID untouched; changes occur only in independent design copies. Brand, legal, identity and content approval remain separate.
