# Recorded Research Upload Case

## Evidence and limits

Use this case to recognize a failed transport pattern. Do not hard-code its counts, paths, commits, or authorization into future projects. Evidence comes from recovered conversation records, local preparation code, and completed checkpoints. No complete per-call token telemetry was available; do not assign exact token shares to individual causes.

## Observed failure pattern

The October 6, 2026 workflow published a completed stratified-bootstrap experiment to `Lawson-Dong/representation-alignment-`, branch `representation-vector-geometric-dynamics`. Multiple attempts ended at the conversation-length limit.

Recovered records describe repeated notebook-fragment reads and encoding, including an earlier extremely granular reading strategy. User-supplied histories contain long sequences of fragment-reading and encoding calls. Transferring payload through conversation accumulated file text and tool overhead. Repeated recovery and verification added more context. CLI publication initially lacked credentials, prompting a connector fallback. Some earlier upload claims were unreliable: at least one object required repair despite a locally recorded hash.

Treat payload emission and repeated reconstruction as the primary recorded workflow causes. Treat repeated discovery and authentication detours as amplifiers. Do not infer that experiments needed rerunning because publication failed. Base64 expansion explains additional character overhead, not measured token consumption in this case.

## Successful sequence

Recover the completed export, reuse confirmed remote objects, repair missing objects, and pass file data directly in the supported transfer runtime instead of emitting it for reconstruction.

First publish the notebook/CSV phase according to the user's instruction to defer images:

- Replace the original notebook with the completed run.
- Publish 18 CSVs in `experiments/geometric_dynamics/results/block_geometry_metrics/`.
- Remove the former `block_geometry_metrics.csv` aggregate file.
- Include notebook links covering all 18 CSV exports.
- Preserve code, execution counts, and numerical/text outputs; record deferred image outputs.
- Verify remote publication and save the completed checkpoint.

The checkpoint records commit `803e4796e41f30169506bd2d8232aeb4d1f4b9da`, phase `completed`, and zero pending blobs. The rewritten notebook has 45 cells and approximately 92 KB of JSON, with no embedded PNG data. Avoid explaining failure solely as an inherently enormous notebook; the repeated transfer strategy mattered.

After explicit authorization for the image phase, publish 52 PNGs on top of that commit. Its checkpoint records commit `ce2945f1b997d083701f17c5c00df9be69d3a677`, 52 remotely verified images, and matching remote hashes.

Checkpoints contain stale fields alongside final results. The image checkpoint retains an earlier blocking reason despite successful completion. Resolve such contradictions using final verification fields and current remote evidence during resumption.

## Reusable lesson

Separate control information from artifact bytes. Keep control information small enough for reasoning; transfer bytes through supported routes. Persist progress and verify remote publication so the next turn can resume without rereading payloads or trusting optimistic summaries.
