# Selection — Apple, Software Engineer, Triage Services (200683343)

## NewsBreak title

**AI Engineer Intern.** The JD's core work is agents as the product: "design and build agentic systems", "hands-on agent development", "AI agent workflows that automate low-level software triage", with min quals in LLM/agent development, RAG/embeddings, and agent eval frameworks. The intern work printed here is almost all LLM pipelines, agents, and evaluation. Heading is plain "NewsBreak" (not new-product / 0→1 work).

Header city: Mountain View, CA (posting is Cupertino, Bay Area).

## Items used

- **nb-llm-pipeline** → bullet 1: Python, Kubernetes CronJob, ingest → bge embeddings → LLM scoring → percentile gate → LLM same-story dedupe → APNs, ~2 min, ~1,200 LLM calls/day. JD: agent/LLM workflows, scalable data platform, embedding generation.
- **nb-llm-pipeline** → bullet 2: 4,100+ decision rows, 11 days of production shadow, 127-alert holdout, prompt ablations, filler and fact both scored 89–90 → categorical gate, filler 34% → 4%. JD: eval frameworks (offline benchmarks), prompt design, regression testing, low-confidence decisions.
- **nb-retired-detector** → bullet 3: 19 h production shadow, 901 min p50 vs 1.8 min, kept corroboration as offline ground truth. JD: rigorous evaluation, offline benchmarks.
- **nb-agentic-search** → bullet 4: SSE, deterministic RAG turn 1, bounded tool loop (≤3 hops, 5 tools, 45 s), hybrid retrieval (substring + `$text` → "keyword"; bge vectors), RRF, degrades to surviving legs. JD: RAG, tool-calling, guardrails, reliability.
- **nb-agentic-search** → bullet 5: eval harness on the real committed catalog, 0% → 100% P@1 on logged queries that previously returned nothing, 28/28 recall, 0.4 ms, embeddings rejected with measurements. JD: eval frameworks, offline benchmarks.
- **nb-llm-failure** → bullet 6: another team's LLM workers, 65% failure rate, Langfuse traces, unbounded reasoning loop, Helm env shadowing code default, 2,048 cap vs p95 1,197. JD: instrument agent pipelines so failures surface; root-cause investigation; work beyond his own team.
- **nb-ownership + nb-fastapi-backend + nb-eks-standup + nb-observability + nb-swiftui-app** → bullet 7: primary backend author, SportsBreak link (1.4K ratings), 89 endpoints, EKS on day 3, Prometheus / Grafana. JD: distributed systems, telemetry/observability.
- **nb-cronjob-outage + nb-live-activities** → bullet 8: 5-day silent CronJob outage, ImagePullBackOff + Forbid, paired deadlines; iOS drops start push lacking `aps.alert` while APNs returns 200. JD: root-cause investigation, on-call ownership of critical infrastructure.
- **hd-lead-mvp (agile)**, **hd-langchain-apis** → Haddee 2 bullets (LLM features, leading engineers ≈ mentoring).
- **za-mock-interview**, **za-demos-contracts / za recruiters fact** → ZenAI 2 bullets (LLM scoring iterated from feedback ≈ "refine agent behavior through feedback").
- **cm-nl-safety** → Research 1 bullet: NL → formal safety specs with multi-turn LLMs (user's angle).
- **pj-codingplans** → LLM provider benchmarking (offline benchmarks).
- **pj-cs537-os** → C, pthreads, xv6 syscalls (JD preferred: kernel / OS-level background).
- Coursework: CMU Large Language Model Systems, Distributed Systems, Machine Learning; UW Operating Systems, Large Language Models in Practice, Computer Architecture.
- Skills: Python first; row 1 is agents/RAG/embeddings/MCP; row 2 is Kubernetes + Prometheus/Grafana/Langfuse (observability). Certifications row kept.

## Items skipped

- nb-server-driven-ui, nb-app-store, nb-ads-max, nb-manual-broadcast, nb-dramabreak-ads, nb-dramabreak-stripe, nb-coaching-marketplace, nb-morning-digest, nb-third-party-proxy, nb-catalog-cache: mobile / product / perf work, weaker for agentic triage; no room.
- nb-jira-process, nb-cross-dept: process; no room.
- hd-mentor-process: cut for space (mentoring is a minor JD line).
- cm-psc: control-theory research; NL→spec bullet is the LLM-relevant one.
- pj-my-av, pj-wisconsin-autonomous, ld-ece-fellow: less relevant; no room.
- Data Science for Software Engineering (CMU coursework): cut to keep coursework on one line.

## Constraints almost violated

- **Vector databases:** not in inventory. The search uses an in-process bge vector index over MongoDB, not a vector DB; resume says "bge vectors" only.
- **Drift detection / confidence scoring:** not claimed as such. The per-topic rolling 7-day percentile and the 0.70–0.84 cosine band routed to an LLM judge are real but not drift detection; the cosine-band clause was cut for space.
- **Kernel / crash debugging:** only OS coursework (C, pthreads, xv6 syscall entry points + clone wrapper) is claimed; kernel `clone` itself is a teammate's and not claimed.
- **Tools adopted by other teams:** only the nb-llm-failure fix on another team's pipeline is claimed; no post-deploy confirmation the failure rate dropped, so no outcome claimed.
- Prometheus / Grafana: no alerts or specific metrics claimed (not recorded).
- MCP and Go are in skills.md but no printed bullet shows them; listed in Skills only.
- "Built an eval harness": inventory says the harness runs against the real committed catalog; it is part of his entity-resolution work.
- Page fill: first draft ran ~12 lines onto page 2; trimmed bullets, then added back the entity-resolution eval bullet and the second ZenAI line. A third added line (cosine-band routing) spilled to two pages, so it was cut. No spacing changes; template preamble spacing as-is.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 612 × 792 pt)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 758.08 pt
- Unused height: 792 − 25.92 − 758.08 = 8.00 pt (passes 0–12 pt)
- Visual review: rendered at 110 dpi. No empty bottom strip, clipping, overlap, or cramped text; all skill rows on one line; SportsBreak hyperlinked.

## Revision 2026-10-09: shared with the Agentic AI MLE application
This resume is also used for `2026-10-09-apple-machine-learning-engineer-agentic-ai` (same title, AI Engineer Intern). Added `Claude Code` to the AI & Agents skills row for the MLE minimum qual "LLM-assisted coding" (inventory: Claude Code / AI coding tools). Dropped `hybrid retrieval` from that row to keep it on one line; the search-agent bullet still states hybrid retrieval.
Final check: 1 page; bottom margin 0.36in = 25.92 pt; last content yMax 758.08 pt; unused 792 − 25.92 − 758.08 = 8.00 pt. Rendered at 90 dpi: no empty strip, clipping, or overlap.

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

## Revision 2026-10-20: rebuilt from the current inventory
He asked to redo it after inventory changes (zenai.md company line, new pj-cs537-os and nb-cross-dept).
- ZenAI heading: `F23` per the new `company-line` rule (was "2023 Fall Batch").
- NewsBreak 5 → 6 bullets: added **nb-cronjob-outage** (empty image tag → non-terminal ImagePullBackOff → Forbid skipped every run; paired deadlines). JD: root-cause investigation, on-call ownership of triage-critical infrastructure. Calibration bullet now opens with the **nb-llm-pipeline** decision log (one row per item, why it fired or not) for "instrument agent pipelines so ... routing decisions surface"; per-day stats compressed to keep it two lines.
- Projects → "Projects & Leadership": **pj-cs537-os** replaces pj-my-av (JD preferred: kernel / OS-level background). Claims only the pthread quicksort and the xv6 syscall entry points + clone wrapper; no speedup, kernel `clone`, or `join` claimed. ld-ece-fellow kept.
- Haddee: fused hd-lead-mvp + hd-langchain-apis into one bullet; hd-mentor-process second bullet (same facts, one line shorter).
- Research: cut cm-psc (control theory, weakest for this JD) to fit the page; cm-nl-safety kept.
- Skipped: nb-cross-dept (legal / cross-department, not relevant here); pj-my-av (cut for the OS project).
- Note: the Apple Agentic AI MLE folder still has its own copy of the old resume; it was not changed.
Final check: 1 page; bottom margin 0.36 in = 25.92 pt; last content yMax 757.33 pt; unused 792 − 25.92 − 757.33 = 8.75 pt. Rendered at 90 dpi: no empty strip, clipping, overlap, or cramped text; SportsBreak hyperlinked.
