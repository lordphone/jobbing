# Selection — Cantor Fitzgerald, Machine Learning Engineer

## NewsBreak title

**AI Engineer Intern.** The role is LLM applications as product work ("Design and implement LLM-driven features in production systems", "prompts, tool-calling workflows, and retrieval pipelines"). It is not AI infra or serving.

## Header

New York, NY. The posting lists only 55 Water St, New York, with no Bay option.

## Items used

- **nb-llm-pipeline**, bullet 1: embed, LLM-score, LLM same-story dedupe, CronJob, per-item decision log, hand-graded alerts, prompt ablation, 127-alert holdout, categorical gate, filler 34% → 4%, 4,100+ shadow decisions. Maps to "evaluation suites, define success metrics, and analyze failures" and "iterating on prompts".
- **nb-llm-pipeline**, bullet 2: `NEWS_ALERTS_DRY_RUN` held until 11 days of formal shadow reviews, 2/day and 1/topic caps, 11,745 user-days with zero violations. Maps to "responsible-AI guardrails and human-in-the-loop processes".
- **nb-agentic-search**, bullet 3: SSE streaming, RAG on turn 1, bounded tool loop (5 tools, ≤3 hops), hybrid retrieval, server-resolved citations. Maps to "tool-calling", "retrieval", and mitigating "hallucination".
- **nb-agentic-search**, bullet 4: 0% → 100% P@1 on real logged queries, entity resolver as the query rewriter, 0.4 ms, eval harness against the real catalog, 28/28 recall. Maps to "building test sets" and "iterating on retrieval".
- **nb-llm-failure**, bullet 5: 65% failure rate, Langfuse traces, 16,384-token ceiling, 2,048 cap against p95 1,197. Maps to "latency, and cost issues" and "monitoring, logging".
- **nb-fastapi-backend + nb-eks-standup + nb-third-party-proxy** (fused), bullet 6: FastAPI / MongoDB backend from the first commit, 89 endpoints on EKS (Docker, Helm, Jenkins), ~1,450 offline tests, ruff / pyright / pytest gate, nine integrations moved server-side. Maps to "clean, testable Python", "cloud deployment, containers, and modern release pipelines", and "security".
- **hd-langchain-apis** (default) and **hd-lead-mvp + hd-mentor-process** (fused).
- **za-mock-interview + za-auth-db** (fused): sole engineer, recruiters shaped the scoring, iterated from user testing.
- **cm-nl-safety** and **cm-psc**. They cover "ML, statistics… interpret technical papers" (Bayesian estimators, probabilistic safety).
- **pj-my-av** (default line). It covers PyTorch and a data pipeline.
- Coursework: CMU LLM Systems, Machine Learning, Data Science for SE. UW LLMs in Practice, Algorithms, Software Engineering.
- Skills: the first two rows are Python / SQL and RAG / hybrid retrieval / RRF / DeepSeek / DeepInfra / LangChain / Langfuse / PyTorch. All of them are from `inventory/skills.md`.

## Items skipped

- nb-catalog-cache, nb-cronjob-outage: infra work. The EKS stack is already covered in bullet 6.
- nb-morning-digest: LLM work, but it overlaps with the alert and search bullets. Skipped for space.
- nb-retired-detector: strong on "analyze failures", but it would repeat the alert-pipeline story. Skipped for space.
- nb-swiftui-app, nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-dramabreak-*, nb-manual-broadcast, nb-coaching-marketplace: iOS, ads, and payments. Not relevant.
- nb-jira-process (docs / specs): relevant to "Document designs", but cut for space. It is the next line to add if there is room.
- za-demos-contracts, ld-ece-fellow, pj-wisconsin-autonomous: skipped for space and relevance.

## Constraints almost violated

- The first draft ran to two pages (about 10 lines over). I fused the two alert bullets and shortened the search, backend, and Haddee lines. I also dropped cm-psc and the proxy clause, then added them back once there was room.
- There were two widows: CMU coursework ("Distributed Systems") and the LLM & ML skills row. I dropped Distributed Systems, NumPy, and bge embeddings so each fits on one line.
- The link is the careers-site "View More Jobs" URL from the paste. The direct job URL was not in the paste, so I did not build one.

## Final page-fill check

- Page count: 1
- Configured bottom margin: 0.36 in = 25.92 pt (`shared/preamble.tex`)
- Last content bottom: 757.17 pt from the top (`pdftotext -bbox`, page height 792 pt)
- Unused height: 792 − 25.92 − 757.17 = **8.91 pt**, within the 0–12 pt limit
- Visual review at 100 dpi: full page, no empty bottom strip, no clipping or overlap, and no one-word widow lines.
