# Selection — Glean Software Engineer (L25-163426, search / distributed systems)

## NewsBreak title
Software Engineering Intern — JD title is plain "Software Engineer" with search, distributed systems, ingestion, and UI duties. Heading plain "NewsBreak".

## Used
- nb-agentic-search (design + grounded) → bullet 1: hybrid retrieval (substring + `$text` + bge vector, RRF), degrade-to-survivors (fault tolerance), RAG + bounded agent, server-resolved citations, SSE ("scalable enterprise search", "design an API to build other search-based applications").
- nb-agentic-search (entities) → bullet 2: entity resolver as query rewriter, 20/20 logged queries, 0.4 ms, rejected embeddings with measurements (performance benchmarking).
- nb-llm-pipeline (design + believable) → bullet 3: ingest → embed → score → dedupe → push in one CronJob, 11 days shadow, filler 34% → 4% ("data ingestion pipelines").
- nb-ownership + nb-fastapi-backend (believable) → bullet 4: sole backend author, 89 REST endpoints, ~1,450 offline tests in CI (CI/CD, testing strategies).
- nb-eks-standup + nb-observability + nb-cronjob-outage + nb-llm-failure → bullet 5: production EKS, HPA, Prometheus / Grafana, two root-caused failures (fault-tolerant systems).
- nb-catalog-cache (default) → bullet 6: memory/performance tuning.
- hd-lead-mvp + hd-mentor-process → PR reviews ("thorough code review for peers"), GCP App Engine; hd-langchain-apis (API structure, reviewed).
- za-mock-interview + za-demos-contracts → customer requirements ("understand customer requirements"), recruiters' input on scoring.
- cm-nl-safety (LLMs, Bayesian estimators; ML).
- pj-my-av (PyTorch, CUDA, GCP Vertex AI — JD: ML, PyTorch, GCP); pj-cs537-os (C, OS / Linux-adjacent systems).
- Coursework: CMU Distributed Systems, Machine Learning, LLM Systems; UW Operating Systems, Algorithms, Computer Architecture.
- Skills: Languages lead with Python, Java, Go, JavaScript (JD order minus C++); row 2 Search & ML (RAG, hybrid retrieval, RRF, bge, PyTorch); row 3 GCP first, CI/CD, Linux. Both AWS certs kept.

## Skipped
- nb-swiftui-app, nb-live-activities, nb-ads-max, nb-app-store, nb-server-driven-ui, nb-dramabreak-*: iOS / ads.
- nb-third-party-proxy, nb-jira-process, nb-retired-detector, nb-morning-digest, nb-cross-dept, nb-coaching-marketplace: space; weaker fit.
- cm-psc: cm-nl-safety is closer (LLMs + ML).
- ld-ece-fellow, pj-wisconsin-autonomous, pj-codingplans: space.
- Skills not listed: C++ (not in inventory). GCP Vertex AI dropped from Skills (it's in the my-av line) to keep the Cloud row on one line.

## Page-fill check
- Pages: 1 (first build spilled Projects to page 2; tightened bullets 2–4, the Haddee bullet and the Cloud row, then added Projects back and lengthened the Haddee bullet)
- Bottom margin: 0.36 in = 25.92 pt → content limit 766.08 pt
- Last content yMax: 762.44 pt
- Unused height: 3.6 pt
- Visual check: rendered at 80 dpi; no empty strip, clipping, overlap, or cramped text; all skill rows one line.
