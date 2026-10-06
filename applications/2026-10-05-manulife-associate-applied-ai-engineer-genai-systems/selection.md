# Selection — Manulife, Associate Applied AI Engineer – GenAI Systems (JR26091743)

## NewsBreak title
**AI Engineer Intern** — JD is applied AI / GenAI as product work ("Applied AI Engineer – GenAI Systems", "RAG … tool-using workflows", "production-ready outcomes").

## Header
Toronto, ON — posting is Toronto-only (hybrid), no Bay option.

## Items used
- **nb-llm-pipeline** (two bullets)
  - Bullet 1: embed → LLM score (categorical happened/speculative/no_event = LLM classification) → per-topic percentile select → LLM same-story dedupe → APNs push; Kubernetes CronJob; ~1,200 LLM calls/day; per-item decision log (why fired / not) — maps to JD "decision logs", traceability.
  - Bullet 2: 11 days of production shadow; 4,100+ decision rows; hand-graded alerts (89 vs 90) → categorical gate; 127-alert holdout; prompt ablation; rejected the 91%-filler "roundup" rule that killed the two highest-reach real alerts; filler 34% → 4% by count. Maps to JD "holdouts, error analysis, human review rubrics, edge cases, trade-offs".
- **nb-agentic-search** (two bullets)
  - Bullet 3: one SSE endpoint; turn 1 deterministic RAG; hybrid retrieval (substring + $text + vector, RRF); bounded tool loop ≤3 hops, 5 tools, 45 s; server-resolved citations (guardrail).
  - Bullet 4: eval harness against the real committed catalog on real logged queries; 0% → 100% P@1; 28/28 recall; 0.4 ms; rejected embeddings with measurements.
- **nb-llm-failure** (llm variant): Langfuse traces, 65% failure, p95 1,197 vs 16,384, 2,048-token cap — JD "monitoring … investigate issues".
- **nb-fastapi-backend** + **nb-jira-process** (fused): 89 endpoints, ~1,450 offline tests, ruff / pyright / pytest CI gate, AWS EKS; 34 contract-first API specs — JD "tested code, CI/CD, APIs/services".
- **nb-ownership** + **nb-swiftui-app**: SportsBreak hyperlink line (required), ~6,000 installs, 344 PRs / 340 merged.
- **hd-langchain-apis** (llm): LangChain resume parsing = structured extraction.
- **hd-lead-mvp** (agile) + **hd-mentor-process**: 8 interns, Agile, stack, GCP App Engine; PR reviews, mentoring on Git workflows and testing — JD "code review".
- **za-mock-interview** + **za-demos-contracts** (fused): sole engineer, recruiters shaped AI scoring categories (rubric), three 200–500-person companies signed.
- **pj-my-av** (short + streaming inference): PyTorch model development — JD "PyTorch".
- **pj-codingplans**: LLM evaluation tests (KV cache, long context, needle-in-a-haystack).

## Skills
First two rows: AI & ML (RAG, hybrid retrieval, tool calling / agents, LangChain, Langfuse, PyTorch) and Languages (Python, SQL first). Testing row next for "unit testing, Git, code reviews". Dropped mobile, frontend, Terraform, etc.

## Coursework
CMU: Machine Learning, Large Language Model Systems, Data Science for Software Engineering, Distributed Systems. UW: Large Language Models in Practice, Software Engineering, Algorithms.

## Skipped
- **cm-psc / cm-nl-safety** (research): first draft included cm-nl-safety; it pushed the resume to two pages, and the NewsBreak evaluation bullets carry the JD better. Cut.
- nb-catalog-cache, nb-eks-standup, nb-cronjob-outage, nb-third-party-proxy, nb-dramabreak-*: infra / mobile / payments; less relevant than evaluation and GenAI.
- nb-morning-digest: LLM but no evaluation story; space.
- nb-retired-detector: good error-analysis story but overlaps the alert-pipeline bullets.
- Mobile items (server-driven UI, Live Activities, ads, App Store), coaching marketplace: not relevant.
- ld-ece-fellow, pj-wisconsin-autonomous: space.

## Constraints nearly violated
- JD names scikit-learn, TensorFlow, Spark / Databricks, forecasting, anomaly detection, backtesting — none in inventory; not claimed.
- "LLM-classify" is the categorical happened / speculative / no_event output in nb-llm-pipeline — real, not invented.
- "logging why each item fired or did not" is the decision-log fact (sent / below_bar / not_event / …).
- First compile was two pages (research + skills + projects spilled); cut research, the 2/day cap clause, and two skills; then 14.3 pt unused, so added the rejected-rule fact to the eval bullet.

## Verification (final PDF)
- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, codingplans line): **765.23 pt** from the top.
- Unused height: 792 − 25.92 − 765.23 = **0.85 pt** (passes 0–12 pt).
- Rendered at 90 dpi and inspected: no clipping, overlap, or empty bottom strip. CMU coursework wraps to a second line ("Distributed Systems"); no layout defect.
- Re-verified after removing "(Venture Team)" from the NewsBreak heading (carried over from the Retell template; not relevant here): 1 page, same last-content bottom 765.23 pt, 0.85 pt unused.
