# Research Evidence Brief Skill

An auditable weekly **AI Alignment & Interpretability Research Evidence Brief**: what changed the evidence, what does it support, and what would differentiate unresolved explanations?

## Trigger
Ask for a weekly alignment/interpretability research report, evidence update, cross-paper synthesis, or recurring scientific literature review.

## Run parameters
- `window_start`, `window_end` (half-open interval), `timezone` (default `America/Los_Angeles`), `search_cutoff`.
- `language`: English or Chinese.
- `reader_focus`: optional topics; e.g. representation geometry, participation ratio, mechanistic interpretability, causal intervention.
- `read_budget`: default 3-5 deep reviews; broader landscape index without an artificial minimum.
- `prior_ledger`: optional path/repository to previous evidence records; absent means baseline, not tracked change.

## Operating model
1. **Retrieve** with open topic searches and source monitoring; log literal searches, dates and gaps.
2. **Normalize** research IDs and events; resolve versions and avoid mistaking multiple outlets for independent evidence.
3. **Inspect** claims, results, controls, figure captions, appendices, code availability and genuine third-party responses.
4. **Evaluate** each *claim*, keeping author interpretation, reported evidence and report hypothesis separate.
5. **Synthesize** by scientific question, not institution. Explain comparability and propose discriminating tests.
6. **Publish** a traceable report with working primary links, evidence ledger, corrections and a coverage audit.

## Files
- [SKILL.md](SKILL.md) - full execution standard.
- [references/source-register.md](references/source-register.md) - a non-exhaustive source discovery seed list.
- [templates/evidence-ledger.csv](templates/evidence-ledger.csv) - longitudinal field schema.

## Scientific guardrails
Original publication date is not an update date. Author results are not independent reproductions. Decoding is not mechanism; interventions are not necessarily complete mechanisms. Safety proxy improvements do not alone establish broad alignment. No fabricated search counts or comprehensive-review claims.

## Output
A research-grade brief can be exported as PDF. Its plots should be freshly constructed from verified cited results, with axis labels that preserve sampling units and metrics.
