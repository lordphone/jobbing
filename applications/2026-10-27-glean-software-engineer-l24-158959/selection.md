# Selection — Glean Software Engineer (L24-158959, search / ML)

Job duties are word for word the same as L25-163426; the special skills differ (ML/DL, MLOps, PyTorch, TensorFlow, anomaly detection, scikit-learn, AWS, NLP, security and data engineering). Started from the L25-163426 resume and moved it toward ML, AWS and security.

## NewsBreak title
Software Engineering Intern — JD title is plain "Software Engineer" and the duties are search / distributed systems; the ML skills list is not AI-as-product work. Heading plain "NewsBreak".

## Used
- nb-agentic-search (design + grounded) → bullet 1: hybrid retrieval (substring + `$text` + bge vector, RRF), degrade-to-survivors, RAG + bounded agent, server-resolved citations, SSE (NLP, "scalable enterprise search", "design an API").
- nb-agentic-search (entities) → bullet 2: entity resolver as query rewriter, 20/20, 0.4 ms, rejected embeddings with measurements (benchmarking).
- nb-llm-pipeline (design) → bullet 3: ingest → embed → LLM-score → dedupe → push; gate on the topic's rolling 7-day score percentile; 11 days shadow; filler 34% → 4% (ML, "data ingestion pipelines"; the percentile gate is the closest real fact to anomaly detection, described as what it is, not labeled "anomaly detection").
- nb-ownership + nb-fastapi-backend (believable) → bullet 4: sole backend author, 89 REST endpoints, ~1,450 offline tests in CI (Python, testing strategies).
- nb-eks-standup + nb-observability + nb-llm-failure → bullet 5: production AWS EKS on day 3, HPA, Prometheus / Grafana; Langfuse root cause of 65% failure (unbounded reasoning loop, 16,384-token ceiling) (AWS, MLOps).
- nb-third-party-proxy + nb-jira-process (audit) → bullet 6: nine integrations server-side, zero API credentials in the iOS binary; reopened two closed security tickets with line-level evidence ("Security").
- hd-lead-mvp + hd-mentor-process (PR reviews → "thorough code review"); hd-langchain-apis.
- za-mock-interview + za-demos-contracts (customer requirements).
- cm-nl-safety (multi-turn LLMs, Bayesian estimators; ML / NLP).
- pj-my-av (pipeline + short: PyTorch, data pipeline, CUDA, Vertex AI); pj-cs537-os (C, Linux-adjacent systems).
- Coursework: CMU Machine Learning, Large Language Model Systems, Distributed Systems, Data Science for Software Engineering; UW Large Language Models in Practice, Operating Systems, Algorithms.
- Skills: Python first; row 2 "ML & LLMs" (PyTorch, CUDA, NumPy, RAG, hybrid retrieval, bge, agents); row 3 "Cloud & MLOps" with AWS first. Both AWS certs kept.

## Skipped
- nb-catalog-cache: strong perf-tuning bullet, cut for the security bullet (security is a listed special skill).
- nb-cronjob-outage, nb-retired-detector, nb-morning-digest: space.
- nb-swiftui-app, nb-live-activities, nb-ads-max, nb-app-store, nb-server-driven-ui, nb-dramabreak-*: iOS / ads.
- cm-psc, ld-ece-fellow, pj-wisconsin-autonomous, pj-codingplans: space.
- Skills not listed (not in inventory): TensorFlow, scikit-learn, anomaly detection, MLOps tooling, NLP as a named skill, C++. Langfuse and Jenkins dropped from Skills (both in bullets) to keep rows on one line.

## Page-fill check
- Pages: 1 (first build spilled Projects to page 2; tightened bullets 1, 3, 5, the Haddee bullet and CMU coursework; then unwrapped two skill rows, restored the fourth CMU course and the Langfuse cause)
- Bottom margin: 0.36 in = 25.92 pt → content limit 766.08 pt
- Last content yMax: 762.44 pt
- Unused height: 3.6 pt
- Visual check: rendered at 80 dpi; no empty strip, clipping, overlap, or cramped text; all skill rows one line.
