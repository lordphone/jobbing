# Selection — Apple, Machine Learning Engineer - Agentic AI (200688057)

Shared resume: copied from the Triage Services resume as of its 2026-10-09 revision (that folder is now `2026-10-20-apple-software-engineer-triage-services` and was rebuilt on 2026-10-20, so the two no longer match). See that folder's `selection.md` (2026-10-09 sections) for item ids and facts.

- NewsBreak title: AI Engineer Intern — the JD is LLM agents as product work ("design and build end-to-end agentic systems").
- JD → resume mapping:
  - multi-step workflows, tool use, retrieve context → search-agent bullet (RAG turn 1, bounded tool loop ≤3 hops / 5 tools, hybrid retrieval, degrades to surviving legs = failure handling)
  - deterministic vs LLM-driven tradeoffs; latency/cost/accuracy → alert pipeline (deterministic percentile gate + LLM scoring/dedupe; ~2 min, ~1,200 calls/day), entity resolution chosen over embeddings at 0.4 ms
  - evaluation infra for quality/reliability → shadow eval, holdout, prompt ablations, eval harness
  - monitoring / observability in production → Langfuse root-cause, Prometheus / Grafana
  - shipping agentic systems in production → search agent and alert pipeline were live
  - LLM-assisted coding → Claude Code in Skills
  - concept to launch, user-facing at scale → SportsBreak (App Store, 1.4K ratings), ZenAI 0→1
- Gaps: no vision / Face ID work (role is LLM agents, so not required); "strong system design" rests on pipeline architecture, not years.
- Page check: 1 page; 8.00 pt unused (same PDF as the Triage folder).

## Revision 2026-10-09 (2): NewsBreak cut to 5 bullets, framed as what he built
Per his feedback: 8 NewsBreak bullets was too many, and bullets must not read as fixing his own earlier mistakes (he owned the whole backend).
- Kept: nb-llm-pipeline (design), nb-llm-pipeline (shadow calibration, stated as live results: filler 4%, 2/day cap with zero violations over 11,745 user-days — no own before→after), nb-agentic-search (design + entity resolution 100% P@1, no "0% →"), nb-llm-failure (another team's pipeline), nb-fastapi-backend + nb-eks-standup + nb-observability (SportsBreak linked).
- Dropped: nb-retired-detector and nb-cronjob-outage (both read as his own work failing first), the APNs push-to-start finding.
- Filled with: hd-mentor-process, cm-psc (second research bullet), pj-my-av; ZenAI first bullet gained za-auth-db ownership clause.
- Cut for space: OS coursework project (Operating Systems stays in UW coursework).
Final check: 1 page; bottom margin 25.92 pt; last content yMax 758.44 pt; unused 792 − 25.92 − 758.44 = 7.64 pt. Rendered at 90 dpi: no empty strip, clipping, or overlap.

## Revision 2026-10-09 (3)
- Pipeline bullet: dropped "~1,200 LLM calls/day" (one call per article, reads small); ends on "~2 min ingest-to-decision".
- Calibration bullet: added the per-user rate (1.8 median sends per user per day); trimmed wording to keep two lines.
- Projects: replaced codingplans with ld-ece-fellow (he wants it on).
Final check: 1 page; bottom margin 25.92 pt; last content yMax 758.44 pt; unused 7.64 pt. Rendered at 90 dpi: no empty strip, clipping, or overlap.
