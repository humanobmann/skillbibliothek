# MCP and SDK discovery

Use this reference before invoking an unfamiliar Affinity integration or when an expected capability is missing.

## Discovery order

1. Identify connected MCP servers and inspect their advertised descriptions. Select a server only when its own metadata says it controls or reads Affinity products.
2. Read the selected server's preamble and safety notes completely. These override examples or assumptions in this skill when they describe the actual integration contract.
3. List the server's resources and resource templates. Look for SDK overview, document model, object identifiers, units, coordinate systems, transactions, save semantics, export, rendering, error handling, and application/version compatibility.
4. Read the documentation sections relevant to the current operation. Do not treat an example as a supported API unless the corresponding callable tool and schema are present.
5. Inspect callable tool schemas and record the exact required parameters, enum values, return fields, and error shape. Prefer read-only calls until document identity and capabilities are confirmed.

## Capability map

Build a small internal map from actual tools to these roles; leave a role unavailable when no documented tool exists:

| Role | Evidence required |
| --- | --- |
| Find active document | Tool schema and successful identity read |
| Open a named file | Supported extensions and path parameter documented |
| Inspect document/object tree | Read operation with stable object/page identifiers |
| Duplicate or save as | Documentation that the original remains unchanged |
| Mutate objects | Exact object selector, units, and property schema |
| Render preview | Render scope, scale/resolution, and returned artifact documented |
| Export | Format, destination, page/artboard selection, and overwrite behavior documented |
| Verify saved artifact | Readback/open or filesystem evidence plus render |

Do not infer write support from read support. Do not infer Publisher pages from Designer artboards, or Photo pixel layers from a generic layer endpoint.

## Identity and state checks

Before mutation, confirm that later calls address the same document observed during analysis. Prefer stable document and object IDs when the SDK exposes them. If the active document changes, a file is externally modified, or the integration reports stale IDs, stop the mutation batch and re-analyze.

Determine whether commands are immediate, transactional, queued, or require an explicit commit. Use only the documented completion signal. After an unknown or timed-out mutation, read current state before retrying so the operation is not duplicated.

## Errors and unsupported capabilities

- Parse and report the integration's actual error; do not paraphrase it into a fabricated Affinity error code.
- On validation errors, correct only parameters contradicted by the schema or documentation.
- On stale-object or changed-document errors, refresh document state and selectors before one retry.
- On authentication, connection, application-version, unsupported-object, missing-font, or missing-link errors, stop the affected operation and preserve the working copy.
- Do not repeatedly retry mutations with unknown completion. Read back first; if state cannot be established, report the ambiguity.

## No compatible MCP

State that production was not executed. Name the missing role from the capability map and request that the user connect or expose an Affinity MCP server with its preamble and SDK documentation. Do not invent installation URLs, server identifiers, commands, or configuration keys.
