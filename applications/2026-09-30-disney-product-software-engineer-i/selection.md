# Selection — Disney Entertainment & ESPN Technology, Product Software Engineer I (10157015)

## NewsBreak title
**Software Engineering Intern** (default). The JD is data pipelines, telemetry, and reliability ("Create and maintain optimal data pipeline architecture"), not pure backend, AI product, or infra, and it does not say "SWE", so the full default title is printed.

## Items used
- **nb-swiftui-app**: sole SwiftUI engineer, SportsBreak link, peak DAU 1,119, ~6,000 installs, 72-event Amplitude catalog, 74 typed emit methods, server-side allowlist. Matches "client-side event generation" and "synchronizing instrumentation".
- **nb-llm-pipeline** (design + shadow facts, two bullets): Kubernetes CronJob ingest → embed → LLM-score → select → dedupe → push, ~1,200 LLM calls/day, percentile vs the topic's rolling 7-day distribution, decision log row per item; 4,100+ shadow decisions, hand-graded alerts, filler 34% → 4%, 2/day cap over 11,745 user-days with zero violations. Matches "data pipeline architecture", "algorithm development", and "data quality checks".
- **nb-agentic-search** (default + hybrid retrieval): RAG, full-text + bge vector with RRF, server-resolved citations, 0% → 100% P@1. Matches "foundation models, RAG".
- **nb-fastapi-backend** + **nb-eks-standup** (fused): FastAPI / MongoDB from first commit, 89 REST endpoints on EKS (Docker, Helm), ~1,450 offline tests, ruff / pyright / pytest.
- **nb-llm-failure** + **nb-cronjob-outage** (fused): 65% failure rate via Langfuse traces, 16,384-token ceiling; 5-day silent CronJob outage fixed with paired deadlines. Matches "Service Reliability/Operational experience" and observability.
- **hd-lead-mvp** + **hd-langchain-apis** (fused into one bullet).
- **za-mock-interview** (with-auth) + **za-auth-db** + **za-demos-contracts** (recruiter-scoring fact and midsize contracts): two bullets as fill.
- **cm-nl-safety** + **cm-psc** (fused, one bullet).
- **pj-my-av** (data pipeline over 33 h of Comma2k19), **ld-ece-fellow**.
- Skills: Python and SQL lead Languages; Data & ML second (PyTorch, NumPy, RAG, ...); Ops & Cloud third (Langfuse, Amplitude, Grafana for monitoring).
- Coursework: CMU — Data Science for SE, Machine Learning, Distributed Systems; UW — LLMs in Practice, Algorithms, Operating Systems.

## Skipped
- nb-live-activities, nb-ads-max, nb-app-store, nb-server-driven-ui, nb-dramabreak-*: mobile/ads detail, off-JD.
- nb-catalog-cache, nb-third-party-proxy, nb-retired-detector: good, but lower value than the pipeline/reliability items; space.
- nb-ownership, nb-jira-process, nb-morning-digest: space.
- hd-mentor-process, pj-wisconsin-autonomous: space / not relevant.

## Constraints almost violated
- Databricks, Snowflake, Scala, anomaly detection, and data-quality tooling are in the JD but not in inventory — not added or claimed. The percentile gate is described as what it is, not as "anomaly detection".
- First compile: Skills rows "Data & ML" and "Observability & Infra" wrapped with orphan words. Shortened the label to "Ops & Cloud", dropped hybrid retrieval (already in a bullet) and CronJobs (already in bullets) from Skills, then re-added the second ZenAI bullet to fill.

## Verification (final PDF)
- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax): **759.17 pt** from top.
- Unused height: 792 − 25.92 − 759.17 = **6.91 pt** (passes 0–12 pt).
- Rendered at 90 dpi and inspected the whole page: no clipping, overlap, cramped text, orphan lines, or empty bottom strip.

## Referral notes
Default pitch. UW note uses "Product SWE I" (full title put it at 306). Why-this-team line from the JD's "client-side event generation to backend processing".
