---
name: publish-research-artifacts
description: Publish completed research notebooks, per-metric CSVs, and figures to a specified GitHub repository and branch using bounded conversation output, resumable checkpoints, and remote hash verification. Use for large research uploads, interrupted uploads, repeated context-window failures, or requests to continue publishing existing experiment results.
---

# Publish Research Artifacts

Keep artifact bytes in files and transfer runtimes. Keep decisions, counts, hashes, errors, and the next action in conversation. Make publication resumable independently of conversation memory.

## Recover the smallest sufficient state

1. Preserve the user's repository, branch, paths, replacements, authorization, and current exclusions. Honor instructions such as “notebooks and CSVs first; defer images.”
2. Find the current checkpoint and artifact manifest before searching earlier conversations. Read summary fields and pending entries; do not dump entire manifests.
3. Retrieve prior conversation only for missing instructions or unresolved historical claims. Stop retrieval once the task can proceed.
4. Locate the prepared notebook, results directory, and export archive. Parse them locally. Return counts, byte sizes, and validation outcomes instead of file contents.
5. Treat upload resumption as publication work. Do not rerun completed experiments or repeat passed scientific checks unless changed artifacts, missing evidence, or a failed check justify it.

## Diagnose context failures accurately

Distinguish observed behavior from inference about token usage.

| Failure pattern | Consequence | Prevention |
| --- | --- | --- |
| Printing notebook JSON or encoded payloads | Artifact bytes become conversation text | Pass data directly within the transfer runtime |
| Reconstructing tiny fragments through messages | Payload, call overhead, and repeated fragments accumulate | Read whole files or transport-sized chunks inside the runtime |
| Printing base64 | Encoding adds roughly one-third more characters before tokenization | Encode only as required by the transport; never emit the value |
| Repeating discovery after interruptions | Each attempt rebuilds the same history | Resume from checkpoints; inspect only uncertain state |
| Treating local object hashes as uploaded objects | Missing objects trigger late repairs | Separate computed, uploaded, confirmed, and published states |
| Waiting for every artifact category | Late failures delay complete work | Publish complete authorized phases |

Do not invent exact token totals, context limits, or internal compaction failures. Consult [the recorded case](references/upload-case.md) only when historical evidence is needed.

## Choose a supported transfer route once

1. Inspect actual tool schemas and authentication. Prefer an authenticated Git CLI or supported file-capable bulk route. Never assume connector credentials are available to the CLI.
2. If the CLI lacks credentials, switch to connected GitHub tools when sufficient. Do not repeatedly retry the same authentication failure. Never print credentials.
3. Read bytes once in a supported runtime and invoke the transfer tool with the resulting variable. Use UTF-8 for notebook text when supported; use binary/file transfer or base64 for images only as required by the schema.
4. Keep reading, encoding, and uploading in a runtime that actually supports those operations. Do not invent filesystem access or tool methods in an orchestration runtime. Use documented materialization, file transfer, or permitted browser capabilities as available.
5. Pass supported file/resource references between runtimes. Do not shuttle raw bytes through model-visible outputs. If no supported route exists, preserve state and identify the narrow transport blocker.
6. Choose chunks using documented request limits. Keep chunks out of conversation. Do not invent a resumable blob endpoint.
7. Use bounded concurrency for independent uploads. Await every started call and inspect every outcome. Keep checkpoint mutations, tree construction, commit creation, and branch updates sequential.

Execute the following conceptually within the supported transfer runtime:

```text
read local artifact
compute expected hash
upload using the documented schema
validate the returned object identifier
atomically checkpoint the result
emit only {path, bytes, object_id, status}
```

## Maintain a durable checkpoint

Save a checkpoint before the first upload and after every confirmed file or bounded batch. Write a temporary file and atomically replace the previous checkpoint. Merge concurrent worker outcomes through one writer.

Record:

- Repository, branch, destination paths, expected branch head, and artifact location.
- Authorized phase, exclusions, replacements, and deletions.
- Per-file path, byte size, SHA-256, Git blob ID where relevant, and status.
- Uploaded and remotely confirmed object IDs, pending files, failures, and retry counts.
- Created tree/commit IDs, branch-update outcome, and remote verification results.
- The next concrete action and detailed log location.

Use states `prepared`, `uploaded`, `remote_confirmed`, `published`, and `verified`, with separate status per phase. Persist recovery state with the project when appropriate; use the permitted persistent artifact store for expensive or irreplaceable exports. Do not rely on transient workspace paths or conversation-only stores as durable storage. Exclude credentials and unrequested experiment data.

On resumption, validate local hashes and resolve uncertain remote status. Reuse matching confirmed remote objects. A computed object ID alone does not prove remote existence. Resolve stale fields and conflicting completion claims against actual remote evidence.

## Publish a complete, verified phase

1. Build the expected inventory locally. Preserve executed code, execution counts, and outputs according to the user's requirements. Do not silently strip notebook outputs. If images are explicitly deferred, handle embedded image outputs consistently and record any transformation.
2. Verify per-metric CSV names, schemas, expected counts, notebook links, and replacements. Recompute hashes after every edit.
3. Confirm required remote objects. Compare Git blob IDs with Git blob hashes and use SHA-256 for byte-integrity manifests; never compare these hash types directly. Account for repository object format and LFS pointers when applicable.
4. Build the phase tree from the current base tree, preserving unrelated files and applying only requested changes. Create a commit with the correct parent.
5. Update the branch after all required objects are confirmed, using an expected-head check or supported equivalent. Never force-update or overwrite concurrent changes.
6. If the branch advanced, fetch current state, rebuild against the new base, and resolve genuine overlaps. Do not resend confirmed blobs because the branch moved.
7. Verify the actual branch head, required paths, counts, hashes, requested deletions, and notebook CSV links. Emit only mismatches and a compact summary.
8. Mark the phase `verified` only after branch publication and remote checks succeed. Distinguish uploaded blobs, created commits, and updated branches.

For uncertain write outcomes, inspect remote state before retrying. Bound transient retries, for example to three attempts with backoff. Change routes or report a blocker for deterministic permission, authentication, schema, or payload-size errors.

Reuse existing authorization within its scope. Do not ask again merely because a conversation resumed. If an actual approval review rejects publication, preserve prepared work, pursue a materially safer supported route, and explain the rejected action and reason if still blocked.

## Enforce a conversation output budget

- Emit zero notebook payloads, base64 strings, complete CSV tables, or image bytes for upload bookkeeping.
- Target about 1,000 tokens or less per orchestration result. Treat this as a workflow target, not a measured platform limit. Return counts, IDs, failed paths, and the next action.
- Project large responses before emitting them. Keep full responses/logs outside conversation where permitted. Output truncation after dumping data is insufficient protection.
- Discover only relevant tools; never print the full registry. Read only necessary references.
- Return compact batch summaries instead of repetitive per-file narration. Keep the user informed during long operations without reproducing logs.
- If a response unexpectedly emits bulk payload, stop that route, checkpoint, and change the transfer method. Do not shrink fragments while continuing to print the same bytes.
- Before context becomes constrained, write a compact handoff with checkpoint location, phase, verified counts, failures, and next action. Continue authorized work after compaction or resumption.
- Do not promise on-demand compaction or zero risk of context exhaustion. Make correctness and recovery independent of compaction.

## Report completion precisely

Report the verified published phase, artifact counts, repository/branch link, and deferred work. Never claim publication based only on a local commit or upload intention. If blocked, name the incomplete step and confirm that resumable state has been retained.
