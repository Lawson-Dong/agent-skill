# Report outline and longitudinal ledgers

Record title, local date window, cutoff/timezone, edition ID, language, access date, baseline/prior-ledger state and scope limitations. Label week-to-date editions.

## Ten report sections

1. Executive Scientific Brief: 3-5 takeaways, importance and strongest boundary.
2. Research Landscape: six-domain map and complete retained index; new/revised/resurfaced/background/access labels.
3. Deep Reviews: normally 3-5 full-text evidence cards, with hypotheses, design, findings, five evidence dimensions, alternatives and materials.
4. Cross-Paper Synthesis: reconcile estimands and conditions; label report-derived analysis.
5. Disagreements and Negative Evidence: criticism, failed replication and null results, or bounded no-result disclosure.
6. Open Questions: distinguish author-proposed from report-derived and retain IDs.
7. Experimental Opportunities: hypotheses, rivals, predictions, controls, resources, holdout and failure criteria; not performed.
8. Personal Research Relevance: cautious links to PR, geometry and causal experiments.
9. Reading Queue: read closely / skim / monitor and why.
10. Coverage & Source Audit: exact queries, channels, dates, real counts, exclusions, gaps and primary bibliography.

Complete retained index means all works retained from the recorded screening set, never every study in the field. Do not pad counts.

## CSV/JSONL schemas

Search log: search_id, retrieved_at, platform, exact_query, date_start, cutoff, raw_results_recorded, candidate_ids, access_gap.

Paper registry: paper_id, title, authors, canonical_url, first_public_date, revised_date, blog_date, venue_status, version_read, domains, access_level, code_url, code_access_state, data_state, novelty_class, decision, decision_reason.

Claim registry: claim_id, paper_id, claim_text, epistemic_type, source_locator, population_scope, estimand, sampling_unit, numeric_result, uncertainty, rigor, reproducibility, external_validity, causal_identification, independent_corroboration, assessment_reasons, status, edition_id.

Question tracker: question_id, question, origin_author_or_report, first_seen, last_updated, related_claim_ids, supporting_ids, challenging_ids, status, next_discriminating_test.

Escape fields correctly. Use canonical IDs and ISO dates. Unknown is not negative evidence. Append dated transitions rather than silently replacing conclusions; distinguish partial replication, narrowed scope and falsification.
