---
name: research-evidence-brief
description: Produce a citation-traceable weekly AI alignment and interpretability research evidence brief, with version-aware literature discovery, claim-level evidence assessment, cross-paper synthesis, disagreement tracking, reproducibility checks, and longitudinal evidence ledgers. Use when asked for a research weekly, scientific intelligence brief, new evidence review, or updates to prior research judgments.
---

# Research Evidence Brief

Produce an **evidence update**, not a news or paper-summary digest. The central question is: **What evidence should change a researcher's judgment, what does it support or not support, and what experiment could discriminate between remaining explanations?**

This skill is an execution protocol. Follow its gates rather than claiming rigor based on tone. Use the reader's interests to prioritize deep reading; never let those interests determine whether evidence is judged credible.

## 0. Set the contract and honest scope

- Set report interval as half-open `[start, end)`, explicit timezone (default `America/Los_Angeles`), actual search cutoff, language (Chinese default; English when requested), intended audience, focus areas, reading budget, and whether previous ledgers/reports are accessible.
- For a current rolling week, use the actual cutoff; do not imply the remainder of the day has been searched.
- Report the actual coverage achieved. This is a **targeted, non-systematic evidence scan**, not an exhaustive field census or a systematic review. Never claim undiscovered work does not exist.
- Default coverage: technical AI alignment (objectives/reward/preference learning, scalable oversight, control/monitoring, evaluations and misalignment, theory); interpretability (representation geometry/dynamics, features and circuits, causal intervention, faithfulness, method validity). Do not assume only LLMs matter.
- For a user researching representation geometry, layer-wise dynamics, participation ratio (PR), and causal mechanistic interpretability, prioritize relevance in a separate section. Seek constraints and counterexamples, not only agreement.

## 1. Build a source register by *function*, not prestige

Use and update `references/source-register.md` as starting points, never as an exclusive whitelist.

1. **Primary evidence**: paper full text, version history, appendices, technical reports, verified conference/journal proceedings, review records where actually visible, code, data and model artifacts.
2. **Original research communications**: lab research pages, original technical blogs, preliminary notes, author replies. These can be important direct sources without constituting peer-reviewed or independently replicated evidence.
3. **Criticism and independent tests**: actual reproductions, methodological criticisms, negative results, errata, contrasting papers.
4. **Discovery only**: aggregators, newsletters, social media, press. Follow their links to primary sources before asserting scientific conclusions.

Source authenticity and evidence quality are separate axes. An authoritative institution can publish an unreplicated claim; a preprint can contain meaningful controlled evidence. Publication at a venue is not a guarantee that every interpretation is established. A posted OpenReview submission is not automatically an accepted paper.

Maintain both fixed-lab tracking and topic/method/author-driven open discovery, including unfamiliar institutions.

## 2. Perform an auditable retrieval pass

1. Search by **questions and methods**, not only 'alignment' or 'interpretability'. Include equivalents/neighboring formulations: e.g., causal tracing, activation patching, linear probes, sparse autoencoders, readout geometry, reward hacking, chain-of-thought monitorability, policy compliance, evaluation validity.
2. Record for each query: UTC or local search timestamp, source, literal query, date filters, limitations/failures, and result IDs/URLs. If search result counts are unavailable, write 'not measured'; do not invent PRISMA-like flow counts.
3. Discover candidate records first. Deduplicate arXiv, journal, lab blog, tweets and news about the same underlying investigation. Preserve canonical work ID and **separate events** (initial posting, revision, publication, blog, third-party response).
4. Verify first-public date, version examined, version/date of revisions, any venue status and search access date. Categorize events: new study, substantive revision, replication/criticism, correction, instrument/tool update, late discovery/background, lab interpretation of older work.
5. For selected papers, search backward for nearest predecessors and outward for counterexamples, author replies, replicators and alternative methods. Only call a revision 'substantive' after inspecting relevant changed material.
6. Curate for **research judgment change**, methodological information gain, importance of unresolved disputes and relevance; not lab prestige, web popularity or headline language. Permit an empty finding in any category.

Maintain counts only for a real tracked candidate set, not for every unseen web result. Explicitly disclose failed access, abstracts-only reads and excluded dated work.

## 3. Analyze the *claim*, not a single paper score

For each important claim, preserve three distinct layers:

- **Author claims**: what authors propose or argue.
- **Reported evidence**: what observations, experiments, controls or derivations are actually in the accessible materials; include units, denominators and settings.
- **Brief's assessment**: what those materials warrant, what alternatives remain and what test would change the assessment. Label any new hypothesis as the brief's proposal.

Separate fields, never conflate:
- Publication status: preprint / accepted (verified venue and track) / journal / working note / original blog / unverified.
- Reading depth: abstract only / selected sections and figures / full text and relevant appendix / code inspected / code executed.
- Evidence status: author's experiments / author follow-up / independent reproduction / external challenge / this-run reproduction (only if performed).
- Artifact status: code, data, model, weights, run scripts available, inspected or run (each independently).
- Claim type and strength: observation, statistical inference, interpretation, mechanistic hypothesis, causal evidence, formal derivation, policy/normative argument, and bounds.
- Methodological profile: design/controls, construct validity, uncertainty, cross-model/data generalization, dependence among observations, independent corroboration. For each use Supported / Limited / Unclear / Not applicable with evidence-based explanation; do **not** generate pseudo-precise confidence scores.

Include authors, title, stable link/ID, version, dates, research question, nearest related work, hypotheses, model/checkpoint, task, dataset, sample/analysis unit, comparison, metrics definitions, effect estimates, variability measures, and precisely what remains untested. Do not require experimental measures for purely theoretical/conceptual studies; instead expose definitions, assumptions, proof claim and *actual* verification depth.

Figure/chart extraction: inspect original caption/axes/table before citing a value; preserve denominator, baseline, uncertainty and evaluation split. Distinguish a single sample, model, task, random seed, paper, run, and independent replication. Plot only commensurable metrics on common axes; label when juxtaposed panels concern different estimands.

**Inference boundaries**:
- Decodable information is not proof it is used in a computation.
- An intervention affecting output is not a complete, exclusive and transportable causal mechanism.
- A plausible linguistic description is not necessarily a faithful explanation.
- Success on a safety proxy is not demonstration of broad alignment or real-world deployment safety.
- Failure to observe an adverse behavior is not proof of its absence.
- An apparent conflict may be construct/measurement/task mismatch; assess comparability before declaring disagreement.

For limitations, distinguish author-stated, published specific criticism, and brief-origin **unverified** questions. Do not fabricate critiques merely to appear adversarial. 'Not reported in checked excerpts', 'not verified', 'inaccessible', 'not applicable' mean different things.

## 4. Synthesize across work, not just abstracts

Compare works under a named research question. Check whether they study the same latent object, measurement, denominator, model scale, setting, threat model, protocol and end point. Report evidence dependence (shared authors, source datasets, model weights, judge, benchmark, metrics). Common citations or multiple webpages do not constitute independent confirmation.

Classify relationships: direct convergence, conditional consistency, genuine contradiction, construct/operational mismatch, unresolved, or not meaningfully comparable. When appropriate define **discriminating experiments** specifying intervention/manipulation, predicted observations under at least two competing hypotheses, controls, analysis unit and generalization tests. Do not guarantee novelty without an actual literature check.

If past ledger/reports exist, identify changes to previous judgments, including corrections. If none exist, mark current issue as a baseline: do not fabricate historical comparisons.

## 5. Report outline

A. **Scope, cutoff and coverage note**: interval, retrieval timestamp, actual sources and gaps, how many distinct records were *actually* curated.
B. **Evidence changes worth updating on**: 3-6 grounded claim-level findings or a candid 'no substantial change found'.
C. **Landscape index**: a broader table linking all selected unique works, their event type, claim, access and priority. Few-line entries, not essays.
D. **Deep evidence reviews**: normally 3-5; fewer if evidence/verification insufficient. Research design, actual estimates, source location, interpretation, limits, independent status.
E. **Cross-paper comparison, disagreement and evidence dependence**: keep incompatible metrics separated; explain contested/negative results.
F. **Methods/resources and reader-specific experimental interfaces**: direct / transferable / background; testable hypotheses and rival accounts clearly author-attributed vs brief-generated.
G. **Corrections, open verification and search audit**: source/query/date register, excluded background, access failures, read limits, versions and actual counts.

Always end with a **reading queue** ranked by information gain and a **claim-level reference list** (prefer figure/table/section anchor where verified). Never pad to reach a quota.

## 6. Quality gates before delivery

- Every consequential result or numeric statement has a direct primary citation/URL and the appropriate figure/table/section if inspected.
- Work/event distinction is correct (a new blog discussing an old preprint is not a new paper). Track versions and venue/track precisely.
- No fabricated paper, author, peer-review, replications, tool use, search totals or code execution.
- Numerical comparisons preserve metric semantics, evaluation unit, baseline, sample size, variability and uncertainty; check chart captions.
- An author's reported result is never styled as 'we independently verified it' without actually reproducing it.
- Unsupported superlatives ('first', 'proved general mechanism', 'field consensus', 'solved alignment') are removed.
- Accessibility and lack-of-evidence statements are qualified to what was actually checked.
- References and hyperlinks resolve or are accurately marked unavailable.
- PDF or other requested artifact is rendered and inspected for clipping, corrupted glyphs and chart readability.

## 7. Portable persistent records

Use `templates/evidence-ledger.csv` as a minimal machine-readable baseline. Store one row per **claim/event/version** as applicable, with a stable canonical study ID and flags describing dependencies. Append future evidence rather than overwriting past versions. Supplement with JSON/YAML notes for multi-valued claim relationships, quoted estimates and conflicts. Store a separate run-level search log and correction log.

Keep three things distinct: **this execution prompt**, the **source register**, and the **longitudinal evidence ledger**. Multiple language-model agents agreeing about a paper is a production check, not independent scientific replication.

## If tools are limited

Report only searches/materials actually accessed. Do not invent a fresh weekly scan from memory or claim code re-execution. Provide a clearly scoped partial report with outstanding verification tasks. If current evidence is insufficient for a deep review, include an abstract-only, low-commitment index entry instead.
