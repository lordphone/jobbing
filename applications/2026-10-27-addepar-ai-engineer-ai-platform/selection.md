# Selection — Addepar AI Engineer - AI Platform

Base: the Addepar Customer Facing Applied AI resume (2026-10-21), with ownership facts updated to the 2026-10-22 correction (primary iOS engineer, sole backend author).

## Header
New York, NY — the posting is New York only.

## NewsBreak title
AI Engineer Intern — JD title is "AI Engineer"; "working directly with LLMs and agentic frameworks". Heading plain "NewsBreak": platform team, not a new-venture / 0→1 team.

## Items used
- nb-ownership (believable): shipped SportsBreak, primary iOS engineer and sole backend author, ~6,000 installs / 1,119 peak DAU (JD: shipping and maintaining AI-native products, deep ownership)
- nb-fastapi-backend (believable) + nb-eks-standup: Python FastAPI, 89 endpoints, 7 Kubernetes CronJobs on AWS EKS, Docker / Helm / Jenkins, ~1,450 offline tests gating CI (JD: Python, AWS, Kubernetes, backend services)
- nb-agentic-search: hybrid RAG (keyword + bge vectors, RRF), capped tool-calling loop (5 tools, ≤3 hops), SSE streaming, server-resolved citations, eval harness 20/20 (JD: vector DBs, agentic frameworks, tool use, evaluation)
- nb-llm-pipeline: embeddings, LLM scoring, LLM duplicate check as a Kubernetes CronJob, prompt ablations, 11-day shadow, filler 34% → 4% (JD: prompt tuning, iterate on performance metrics, accuracy-sensitive)
- nb-llm-failure (backend + sizing): 65% failure rate via Langfuse, 16,384 ceiling, 2,048 cap vs p95 1,197 (JD: maintaining AI products, probabilistic systems)
- nb-catalog-cache (default facts): per-user key, 13.2 MB → one shared 10.9 MB copy at the 512 MiB limit (JD: scaling backend services)
- hd-lead-mvp + hd-langchain-apis (JD: LangChain preferred), hd-mentor-process
- za-mock-interview + za-auth-db, za-demos-contracts (JD: iterate on user feedback)
- cm-nl-safety (default)
- pj-codingplans (evaluating LLM providers — JD: evaluation and adoption of new AI technologies), ld-ece-fellow

## Skills
Python, Go first (JD names Python, Golang); LLM tool calling / agents, MCP (JD: MCP / cross-platform tool use), RAG; AWS, Kubernetes, Docker, Helm; asyncio (concurrency), REST APIs, LangChain. Java and SSE (skills row) dropped for space; Langfuse is in a bullet. gRPC, Databricks, MLFlow are not in inventory, so not listed. Certifications kept.

## Coursework
CMU: Large Language Model Systems, Distributed Systems, Machine Learning. UW: Large Language Models in Practice, Operating Systems, Algorithms (systems / concurrency).

## Skipped
- nb-swiftui-app, nb-live-activities, nb-ads-max, nb-server-driven-ui, nb-app-store, nb-morning-digest: mobile / not in JD
- nb-observability: dropped from the backend bullet to fit the page (Prometheus / Grafana stay in Skills)
- nb-cronjob-outage, nb-third-party-proxy, nb-retired-detector, nb-dramabreak-*, nb-jira-process, nb-coaching-marketplace: less relevant; space
- pj-my-av, pj-cs537-os, cm-psc: less relevant; space

## Page-fill check
- Pages: 1
- Bottom margin: 0.36 in = 25.92 pt → content limit y = 766.08 pt
- Last content yMax: 756.78 pt
- Unused height: 9.3 pt
- Visual: no empty strip, no clipping or overlap
