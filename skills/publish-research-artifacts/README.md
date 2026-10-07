# Publish Research Artifacts

Publish completed research notebooks, per-metric CSV results, and figures to a specified GitHub repository and branch. Keep large file payloads out of conversation, preserve progress across interruptions, and verify the published files against the source artifacts.

## When to use

- Continue an interrupted research upload.
- Publish an executed notebook together with separate metric CSVs and figures.
- Handle uploads that repeatedly exhaust the conversation context.
- Publish complete phases, such as notebooks and CSVs first, then images.

This skill publishes existing results. It does not run experiments or provide an upload service.

## Setup

Copy the complete `publish-research-artifacts` folder into your agent host's supported skill directory, or use the host's skill import workflow. Read [SKILL.md](SKILL.md) for the operating instructions.

No additional Python packages or bundled scripts are required. The host must provide access to the artifact files, a supported authenticated GitHub transfer route, and a suitable location for persistent checkpoints. Do not assume that a connected GitHub account also authenticates the Git CLI.

## Example requests

> Use $publish-research-artifacts to publish my completed notebook and per-metric CSV files to OWNER/REPOSITORY on BRANCH. Replace the previous notebook, update its CSV links, and defer all figures until the next phase.

> Continue the interrupted figure upload from the saved checkpoint. Reuse remotely confirmed objects, publish the remaining files, and verify every image against its local hash.

Supply the repository, branch, artifact location, destination paths, and any requested replacements or exclusions. Use existing authorization within its scope.

## Workflow

1. Recover the checkpoint and the smallest sufficient artifact inventory.
2. Verify the prepared files and select a supported authenticated transfer route.
3. Read and transfer artifact bytes inside the supported runtime; report only counts, hashes, status, and errors.
4. Persist per-file progress after each confirmed file or bounded batch.
5. Build a commit that preserves unrelated repository files, then update the branch with an expected-head check.
6. Verify the published branch, required paths, file hashes, requested deletions, and notebook links.
7. Report the verified phase and any deferred work.

If the branch moves during publication, rebuild against its current state. If a write outcome is uncertain, inspect the remote state before retrying.

## Checkpoint and output discipline

Record destination paths, source hashes, remotely confirmed object IDs, pending files, the expected branch head, and the next action. Keep checkpoints free of credentials.

Keep notebook JSON, CSV tables, base64 strings, and image bytes out of conversation output. Save full logs outside the conversation where supported. A locally computed hash alone does not prove that a remote object exists, and uploaded objects alone do not prove that the branch was updated.

## Included files

| File | Role |
| --- | --- |
| [SKILL.md](SKILL.md) | Agent instructions, recovery rules, publication workflow, and verification requirements. |
| [agents/openai.yaml](agents/openai.yaml) | Display metadata and default invocation prompt. |
| [assets/icon.svg](assets/icon.svg) | Skill icon. |
| [references/upload-case.md](references/upload-case.md) | Recorded upload failure and recovery case; historical counts are examples, not defaults. |

## Completion criteria

Treat a phase as complete only after the target branch contains its required files and remote verification succeeds. Report remaining work explicitly. Preserve resumable state if authentication, permissions, or transport limits block publication.
