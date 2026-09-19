# Data Model and ID Contract

Stand: 2026-08-24

## Stabile IDs

```text
SOURCE_000001
QUERY_000001
RUN_000001
DOCUMENT_000001
PROTOCOL_000001
SPEECH_000001
PERSON_000001
MOTION_000001
CLAIM_000001
PROMISE_000001
VOTE_000001
ISSUE_000001
FINDING_000001
REJECTED_000001
```

IDs werden nie recycelt.

## Canonical parliamentary object key

Für Gegenstände bevorzugt:

```text
chamber | gp | identification_type | number | suffix
```

Zusätzlich wird die `canonical_url` als Integritätsanker gespeichert.

Titel sind kein Schlüssel.

## Source Record

```text
source_id
source_type
canonical_url
dataset
retrieved_at
document_date
license_status
raw_path
sha256
http_status
content_type
byte_size
```

## Query Record

```text
query_id
source_id
endpoint
method
body
partition_type
partition_value
parent_query_id
run_id
status
api_count
rows_received
unique_rows
started_at
finished_at
```

## Parliamentary Object

```text
object_id
chamber
gp
object_type
document_type
number
suffix
citation
date_incoming
date_last_stage
status
phase
canonical_url
source_id
```

## Person Timeline

```text
person_id
pad
name
valid_from
valid_to
gremium
party
club
function
wahlkreis
source_id
confidence
```

## Speech Record

```text
speech_id
protocol_id
person_id
start_marker
end_marker
agenda_item
start_time
end_time
party_at_time
function_at_time
text_source
parser_quality
official_individual_html
```

## Motion Record

```text
motion_id
object_id
motion_type
core_demand
reasoning
financing
target_group
competence
responsible_body
requested_effective_date
status
```

## Claim Record

```text
claim_id
speech_id_or_document_id
person_id
party_at_time
claim_type
original_span
normalized_claim
verification_question
external_reference
result
confidence
```

## Provenance Edge

Jede Derived oder Analysis Aussage benötigt mindestens:

```text
derived_id
source_id
source_span
transformation
parser_version
review_status
confidence
```

## Graph Beziehungen

```text
PERSON -> PARTY_AT_TIME
PERSON -> FUNCTION_AT_TIME
PERSON -> SPEECH
SPEECH -> CLAIM
CLAIM -> ISSUE
MOTION -> ISSUE
MOTION -> COMMITTEE
MOTION -> VOTE
MOTION -> DECISION
DECISION -> LAW
LAW -> IMPLEMENTATION
CLAIM -> CONTRADICTS -> CLAIM
FINDING -> COUNTEREVIDENCE
FINDING -> SPOE_SYMMETRY_CASE
```

## Null Regeln

`null` bedeutet unbekannt oder nicht vorhanden.

Folgende Werte dürfen nicht aus null inferiert werden:

* Partei
* Abstimmungsverhalten
* Ablehnung
* Zustimmung
* Zuständigkeit
* Finanzierung
* Rechtsstatus

## Negative Evidence

Nicht gefunden wird gespeichert als:

```text
SEARCH_SCOPE
QUERY_SET
SEARCH_DATE
RESULT_COUNT=0
INTERPRETATION=NO_MATCH_IN_SEARCHED_CORPUS
```

Nie automatisch als `DOES_NOT_EXIST`.
