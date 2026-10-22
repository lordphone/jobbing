# Selection — EvenUp Machine Learning Engineer

Base: the Addepar Customer Facing Applied AI resume (2026-10-21), the closest LLM / applied-AI fit, reworked toward ML / NLP.

## NewsBreak title
AI Engineer Intern — JD is "machine learning, natural-language processing, and generative AI", RAG, embeddings, LLMs. Heading plain "NewsBreak" (not a new-ventures JD).

## Header city
Mountain View, CA — JD allows San Francisco (hybrid).

## Items used
- nb-agentic-search: RAG agent over hybrid retrieval (substring + Mongo `$text` + bge vector, RRF), capped tool-calling loop, server-resolved citations (JD: retrieval-augmented generation, embeddings, LLMs)
- nb-agentic-search (entities): benchmarked embeddings vs span-based entity resolution, rejected embeddings with measurements, 20/20 on logged queries, eval harness on the real catalog (JD: explore, implement, and benchmark methods; evaluation metrics)
- nb-llm-pipeline: bge embeddings, LLM scoring into categorical + 0–100 importance, LLM same-story judge, hand-graded alerts, prompt ablations, 11-day shadow, filler 34% → 4% (JD: design experiments, analyze results, annotate data, prompt engineering)
- nb-llm-failure: 65% failure rate via Langfuse, 2,048 cap vs p95 1,197 (JD: monitoring production models)
- nb-fastapi-backend (believable) + nb-eks-standup + nb-observability: FastAPI / MongoDB, 89 endpoints on EKS, Docker, Helm, ~1,450 offline tests, Prometheus / Grafana (JD: integrate models into production, testing, monitoring; Docker / Kubernetes nice-to-have)
- nb-ownership (believable) + nb-morning-digest (llm): SportsBreak shipped, ~6,000 installs, 1,119 peak DAU, LLM digest to 5,026 users (~81%)
- hd-lead-mvp + hd-langchain-apis (llm): LangChain resume parsing and suggestions (closest to document understanding)
- za-mock-interview + za-demos-contracts: LLM app, recruiters shaped AI scoring categories (JD: pair with domain experts), three companies signed
- cm-nl-safety, cm-psc (research; JD mentions research and representation learning)
- pj-my-av (pipeline + training fused): PyTorch CNN-GRU, data pipeline with shuffling / temporal windowing / frame processing, CUDA + Vertex AI (JD: PyTorch, build reusable datasets and data loaders, GCP)

## Skills
Python, SQL, PyTorch first (JD core requirements); NLP & LLMs row (RAG, embeddings, tool calling, LangChain, Langfuse); AWS / GCP Vertex AI / Docker / Kubernetes (nice-to-haves). Certifications kept.

## Coursework
CMU: Machine Learning, Large Language Model Systems, Data Science for Software Engineering. UW: Large Language Models in Practice, Algorithms, Data Structure & Programming III.

## Skipped
- nb-dramabreak-ads A/B test: JD asks for A/B tests, but winner, lift, and sample size are not recorded; a bare "ran an A/B test" line was weaker than the shadow-mode experiment line
- nb-swiftui-app, nb-live-activities, nb-ads-max, nb-server-driven-ui, nb-app-store, nb-third-party-proxy: mobile, not in JD
- nb-catalog-cache, nb-cronjob-outage, nb-jira-process: backend / infra; space
- pj-codingplans: cut to fit one page (first draft spilled to two)
- ld-ece-fellow, hd-mentor-process, za-auth-db, pj-cs537-os, pj-wisconsin-autonomous: less relevant; space
- Not in inventory, so not claimed: LLM fine-tuning, Hugging Face, TensorFlow, spaCy, MLflow / W&B, ETL tooling

## Page-fill check
- Pages: 1
- Bottom margin: 0.36 in = 25.92 pt → content limit y = 766.08 pt
- Last content yMax: 757.28 pt
- Unused height: 8.8 pt
- Visual: no empty strip, no clipping or overlap
