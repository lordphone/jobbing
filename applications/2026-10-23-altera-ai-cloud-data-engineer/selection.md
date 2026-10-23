# Selection — Altera, AI Cloud Data Engineer (R03371)

## NewsBreak title
**AI Engineer Intern** — the JD is AI / GenAI product work ("AI-powered applications", "RAG systems, vector databases, AI agents", "Generative AI solutions").

## Header
Toronto, ON — posting is Toronto-only.

## Items used
- **nb-llm-pipeline** (two bullets)
  - Bullet 1: ingest → embed → LLM-score (categorical happened/speculative/no_event = classify) → per-topic percentile select → LLM same-story dedupe → push; ~2 min; Kubernetes CronJob; ~1,200 LLM calls/day; decision log. Framed as a "data pipeline" for JD "data pipelines", "process and integrate data".
  - Bullet 2: 11-day production shadow, 4,100+ decision rows, hand-graded 89 vs 90, categorical gate, 127-alert holdout, prompt ablation, rejected 91%-filler rule that blocked the two highest-reach real alerts, filler 34% → 4%. JD "experimentation, model evaluation, performance benchmarking".
- **nb-agentic-search** (two bullets)
  - Bullet 3: one SSE endpoint, deterministic RAG on turn 1, hybrid retrieval (substring + $text + bge vector, RRF), bounded tool-calling agent (≤3 hops, 5 tools), server-resolved citations. JD "RAG systems, vector databases, AI agents, intelligent search".
  - Bullet 4: eval harness on real logged queries against the real committed catalog; 20/20 P@1 (denominator per believability rule); 0.4 ms; embeddings rejected by measurement.
- **nb-llm-failure** (llm): Langfuse, 65% failure, p95 1,197 vs 16,384, 2,048-token cap. JD "troubleshooting, monitoring".
- **nb-ownership** + **nb-fastapi-backend** + **nb-eks-standup** + **nb-observability** (fused): sole backend author, primary iOS engineer, SportsBreak link, ~6,000 installs, 89 endpoints, 7 CronJobs, AWS EKS, Docker, Helm, ~1,450 offline tests in CI, Prometheus + Grafana dashboards. JD "cloud", "containers, Kubernetes, CI/CD", "dashboards".
- **hd-langchain-apis** (llm), **hd-lead-mvp** (agile) + **hd-mentor-process**.
- **za-mock-interview** + **za-demos-contracts** (fused).
- **pj-my-av**: PyTorch, data pipeline, CUDA + Vertex AI training, streaming inference. JD "training, inference", "deep learning", "PyTorch".
- **pj-codingplans**: LLM benchmarking.

## Skills
First two rows: AI & ML (RAG, hybrid retrieval, tool calling / agents, LangChain, PyTorch, Langfuse) and Languages (Python, SQL first). Then Cloud & MLOps, Data & Backend, Certifications (both AWS). Dropped Jenkins, GitHub Actions, CUDA, bge embeddings, mobile and frontend to keep rows on one line.

## Coursework
CMU: Machine Learning, Large Language Model Systems, Data Science for Software Engineering, Distributed Systems. UW: Large Language Models in Practice, Algorithms, Operating Systems.

## Skipped
- **cm-nl-safety / cm-psc** (research): first draft included cm-nl-safety; spilled to two pages. Cut.
- nb-catalog-cache, nb-cronjob-outage, nb-third-party-proxy, nb-morning-digest, nb-retired-detector, mobile / ads / payments items: less relevant than evaluation, RAG, and pipeline work, or overlapping.
- ld-ece-fellow, pj-wisconsin-autonomous: space.

## Constraints nearly violated
- JD names TensorFlow, Semantic Kernel, Azure, ETL/ELT tools, data warehousing, distributed data processing (Spark etc.), vector database products — none in inventory; not claimed. "vector embeddings" refers to the bge vector leg of hybrid retrieval.
- "1+ years' experience with ML / GenAI / LLMs": internship + Haddee + ZenAI + projects; not claimed as a duration.

## Verification (final PDF)
- Compiled with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, codingplans line): **763.13 pt**.
- Unused height: 792 − 25.92 − 763.13 = **2.95 pt** (passes 0–12 pt).
- Rendered at 80 dpi and inspected: no clipping, overlap, cramped text, or empty bottom strip.
- History: first compile 2 pages (projects spilled); cut research and trimmed two skill rows → 16.4 pt unused; added the rejected-rule fact to the eval bullet → 2.95 pt.
