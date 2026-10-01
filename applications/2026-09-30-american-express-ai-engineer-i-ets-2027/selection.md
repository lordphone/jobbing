# Selection — American Express AI Engineer I, ETS (26013256)

## NewsBreak title
**AI Engineer Intern** — JD is "AI Engineer I" building "LLM integrations, AI agents, agentic workflows, retrieval patterns, model evaluation" as product work, not serving infra.

## Items used
- **nb-agentic-search** (grounded + design): deterministic RAG turn 1, bounded agent with native tool calling (≤3 hops, 5 tools), hybrid full-text + bge vector retrieval with RRF, SSE, server-resolved citations. Hits LLM APIs, function calling, retrieval patterns, embeddings, agent workflows.
- **nb-llm-pipeline** (shadow): CronJob ingest → embed → LLM-score → LLM dedupe → push; 4,100+ shadow decisions, hand-graded alerts, filler 34% → 4%. Hits data pipelines, evaluation routines, prompt evaluation.
- **nb-agentic-search** (entities): 0% → 100% P@1, entity resolver as query rewriter, embeddings measured on an eval harness. Hits evaluation and experimentation.
- **nb-fastapi-backend** + **nb-eks-standup** + **nb-jira-process** (fused): FastAPI / MongoDB from first commit to 89 REST endpoints on EKS (Docker, Helm), ~1,450 offline tests behind ruff / pyright / pytest CI gate; 34 contract-first API specs and ~10,000 lines of docs. Hits APIs, containers, CI/CD, testing, documentation.
- **nb-llm-failure** (backend + sizing): Langfuse traces, 65% failure, 16,384 ceiling, 2,048 cap vs p95 1,197. Hits debugging/improving reliability, monitoring.
- **hd-lead-mvp** (agile) + **hd-langchain-apis** + **hd-mentor-process** (PR reviews): Agile, code reviews, LLM features.
- **za-mock-interview** (with-auth) + **za-demos-contracts** / recruiter-scoring fact.
- **cm-nl-safety** + **cm-psc** (fused): LLMs, safety — fits the JD's responsible-AI / safety language.
- **pj-my-av** (ML model training, data pipeline), **ld-ece-fellow**.
- Skills: Python leads Languages, Java and JavaScript next (both named in JD); AI & ML row second; Practices row (Git, CI/CD, REST APIs, Agile, testing) third.
- Coursework: CMU — Machine Learning, LLM Systems, Data Science for SE; UW — LLMs in Practice, Algorithms, Data Structure & Programming III (JD asks for data structures and algorithms).

## Skipped
- nb-swiftui-app, nb-live-activities, nb-ads-max, nb-app-store, nb-server-driven-ui, nb-dramabreak-*, nb-manual-broadcast: mobile/ads, not in JD.
- nb-morning-digest: LLM but thinner than chosen items; space.
- nb-catalog-cache, nb-cronjob-outage, nb-third-party-proxy, nb-retired-detector: lower JD value; space.
- pj-wisconsin-autonomous: embedded, not relevant.
- GitHub Actions dropped from skills to fit the Cloud & Data row on one line (CI/CD stays).

## Constraints almost violated
- JD lists fuzzy matching, BERT, transformers, R, ETL — not in `inventory/skills.md`; not added. The entity resolver is span-based, so it was not called "fuzzy matching".
- First compile spilled 1 line to page 2; tightened the Haddee bullet (orphan "reviews.") and dropped GitHub Actions (orphan "PostgreSQL").

## Verification (final PDF)
- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax): **757.20 pt** from top.
- Unused height: 792 − 25.92 − 757.20 = **8.88 pt** (passes 0–12 pt).
- Rendered at 90 dpi and inspected the whole page: no clipping, overlap, cramped text, orphan lines, or empty bottom strip.

## Referral notes
Default pitch. Role shortened to "AI Engineer I". Why-this-team from the JD's "enterprise AI platforms" and "AI agents, agentic workflows".
