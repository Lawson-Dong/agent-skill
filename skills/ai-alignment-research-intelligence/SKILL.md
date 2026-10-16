---
name: ai-alignment-research-intelligence
description: Produce research-grade AI alignment and interpretability weekly intelligence with primary-source verification, auditable retrieval, evidence cards, scientific synthesis, testable experiments, illustrated PDFs and longitudinal claim tracking. Use for critical weekly literature updates spanning mechanistic interpretability, representation geometry, causal control, behavioral safety, evaluation and theory; support English or Chinese.
---

# AI Alignment & Interpretability Research Intelligence

Build an evolving map of scientific evidence, giving particular analytical attention to representation geometry, dynamics, PR, causal interpretability and experimental methodology.

## Establish the reporting contract

- Declare the reporting window, cutoff timestamp and timezone. Interpret “this week” as local Monday through the request cutoff unless specified; label a partial week.
- Default to research-grade depth, 3-5 deep reviews and 15-30 indexed works. Treat these as capacities, never quotas; report fewer when verification does not support more.
- Default to Chinese with English terminology; follow explicit language requests, including English-only output.
- Generate one edition unless the user explicitly requests recurring automation. Do not imply that a single report creates monitoring.
- Read available previous reports and ledgers before claiming longitudinal novelty. Label a baseline when none is accessible.

## Cover six scientific question families

Scan (1) mechanistic interpretability, (2) representation geometry and dynamics, (3) alignment and behavioral safety, (4) causal interventions and model control, (5) evaluations and scientific methodology, and (6) theory and foundations. Apply multiple tags where appropriate. Organize by questions, not institutions.

## Retrieve before selecting

Read [retrieval-and-evidence.md](references/retrieval-and-evidence.md). Search primary preprints, proceedings, journals, author technical reports, original lab experiments and community criticism. Use news and aggregators only to discover leads; trace scientific claims to primary material. Do not equate institutional provenance with evidence strength.

Maintain exact queries, platform, retrieval time, returned candidates, canonical IDs, deduplication decisions and access gaps using [report-and-ledgers.md](references/report-and-ledgers.md). Never invent screened counts or describe a bounded search as exhaustive.

Search all six domains, include academic and less visible authors, and actively seek negative results, failed replications, critiques and competing explanations. Follow backward references for key claims and search forward citations when possible; disclose incomplete citation chaining.

Verify first-publication, revision, conference and blog dates separately. Deduplicate papers, code and blog posts into one study. Classify old research publicized this week as resurfaced; count a revision as new evidence only after verifying a substantive change. Never use crawl dates as publication dates.

## Build claim-grounded evidence cards

Read full text for every deep review. Label abstract-only items **Abstract Only** and keep them in the index. Do not infer unobserved design details from snippets.

Record canonical title, authors, URL, version, distinct dates, status and access level. Extract the question, tested hypothesis, rivals, operational definitions, models, data, controls, variables, metrics, sampling unit, uncertainty and analysis choices. For numerical claims preserve denominators, units, comparisons and section/table/figure locators.

Separate **observation**, **statistical inference**, **authors' interpretation**, **mechanistic hypothesis**, **controlled causal evidence** and **report synthesis**. Do not let an intervention establish a complete or uniquely identified mechanism by implication. Treat absent uncertainty as unavailable, not zero.

Assess five dimensions independently using Strong / Moderate / Limited / Unclear, each with reasons: methodological rigor, reproducibility, external validity, causal identification and independent corroboration. Never create a single numerical trust score. Distinguish code linked, inspected and executed; state when no independent replication was located.

Include limitations, alternative explanations, open questions, code/data/weights/prompts and resource requirements when verified. Restrict claims to the tested conditions.

## Synthesize and design discriminating experiments

Compare estimands, definitions, normalization, model/task populations and component budgets before calling results corroborating or contradictory. Distinguish a genuine dispute from different measurements. State bounded absence of located counterevidence without claiming none exists.

Use [geometry-and-visuals.md](references/geometry-and-visuals.md) for PR and intervention safeguards. Never claim an LLM study verifies a ResNet hypothesis. Label transfers as hypotheses.

For each original opportunity state the falsifiable hypothesis, rival explanation, intervention, matched controls, contrasting predictions, discovery/holdout split, sampling unit, resources and disconfirmation criterion. Label **Proposed experiment - not performed**. Do not design the analysis to guarantee a favored explanation.

## Produce and preserve the report

Use the ten-section outline and ledgers in [report-and-ledgers.md](references/report-and-ledgers.md). Use stable source IDs, primary URLs and precise locators. Clearly label original synthesis and author-proposed versus report-derived questions.

For requested visuals, use accurate vector diagrams, attributed author figures or plots of verified values. Mark reported, redrawn, recomputed and schematic content. Label synthetic data prominently. Never fabricate error bars or raw series. Do not use generated imagery to depict exact evidence.

For PDF output, use the host's PDF skill, inspect every rendered page, verify citations and links, and save the final deliverable through the supported persistent-file workflow.

When prior ledgers exist, preserve stable IDs, conflicting evidence and dated transitions: supported, challenged, narrowed, replicated, retracted or unresolved. Do not invent earlier comparisons. Save checkpoints for long runs and resume verified work.

## Completion gates

Require a declared cutoff; six-domain scan with gaps; deduplicated index; full text for all deep reviews; primary citations for claims; five-dimensional evidence assessments; explicit synthesis labels; honest screening counts and novelty; source-audited visuals; and a verified, saved artifact when requested. Report material access or saving failures. Never pad sparse weeks.
