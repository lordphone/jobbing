# Selection — Scopely, Software Engineer, Machine Learning (00103420)

## NewsBreak title

**AI Engineer Intern.** The JD is ML / GenAI infrastructure: "deployment of Artificial Intelligence (AI) and Machine Learning (ML) models", "integrate AI and ML models into products", "model evaluation and deployment workflows", and a required "Generative AI" line. The LLM pipeline, search agent, and LLM-worker debugging are the closest work in inventory.

Heading: plain "NewsBreak" (not a new-venture JD). Header city: Mountain View, CA (SF posting, US telecommuting allowed).

## JD → items

| JD ask | Items |
|---|---|
| Deploy AI/ML models, integrate into products | nb-llm-pipeline, nb-agentic-search |
| Automate model evaluation and deployment | nb-llm-pipeline (production shadow, holdout, ablations) |
| Resource utilization, inference latency | nb-catalog-cache (78×, 512 MiB pod), nb-agentic-search (0.4 ms resolve, bare lookups skip the LLM), nb-llm-failure (token cap) |
| Monitoring and reliability | nb-observability, nb-cronjob-outage, nb-eks-standup |
| Troubleshoot ML infra, root causes | nb-llm-failure |
| Code reviews | hd-lead-mvp + hd-mentor-process (PR reviews) |
| Python, ML, GenAI, SQL, system programming, cloud | Skills rows, research, my-av, pj-cs537-os, codingplans, AWS certs |

## Bullets

NewsBreak (6):
1. nb-llm-pipeline (`design`/`llm`): ingest → bge embed → LLM score → 7-day percentile gate → LLM same-story judge, Kubernetes CronJob, ~1,200 LLM calls/day.
2. nb-llm-pipeline (`shadow`): 4,100+ decision rows, 127-alert holdout, prompt ablation, filler 34% → 4% by count, 1.8 median sends/day. Framed as model evaluation before going live.
3. nb-agentic-search (`design` + `entities`): deterministic RAG then bounded tool loop (≤3 hops, 5 tools), hybrid retrieval with RRF, 100% P@1 at 0.4 ms.
4. nb-llm-failure (`infra`): 65% failure rate, Langfuse, unbounded reasoning loop, Helm env shadowing, 2,048 cap vs p95 1,197. Claims no confirmed fix.
5. nb-eks-standup + nb-observability + nb-cronjob-outage: EKS day 3 (Docker, Helm, Jenkins), Prometheus / Grafana, 5-day CronJob outage fixed with paired deadlines.
6. nb-fastapi-backend + nb-catalog-cache: SportsBreak link with 1.4K ratings (nb-swiftui-app), first commit to 89 endpoints, cache re-keyed to shared, 78× smaller, sized for a 512 MiB pod.

Haddee (1): hd-lead-mvp (`agile`) + hd-mentor-process (PR reviews) + hd-langchain-apis (REST APIs for LangChain resume parsing, job matching).

ZenAI (1): za-mock-interview (`sole`, PostgreSQL) + za-demos-contracts (`contracts`).

Research (2): cm-nl-safety (`default`), cm-psc (`default`). The JD asks for ML and Generative AI academic training; both fit.

Projects (3): pj-my-av (`short`, trimmed), pj-codingplans (`default`, shortened as in the Rivian resume; KV caching and quantization tie to inference efficiency), pj-cs537-os (shortened; the JD requires "System programming").

Skills: ML & GenAI first (Python, PyTorch, CUDA, NumPy, LLM agents, RAG, bge embeddings, Langfuse), Cloud & Infra second, Data & Systems third (SQL, C, Go first for the SQL and system-programming asks). Certifications row kept.

Coursework: CMU Machine Learning, Large Language Model Systems, Distributed Systems. UW Operating Systems, Large Language Models in Practice, Computer Architecture.

## Skipped

- nb-swiftui-app, nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-dramabreak-*: mobile and ads, not ML infra. SportsBreak link kept in the backend bullet.
- nb-ownership, nb-jira-process: ownership stats less relevant than ML infra and space was tight.
- nb-third-party-proxy, nb-manual-broadcast, nb-morning-digest, nb-retired-detector, nb-coaching-marketplace, nb-cross-dept: lower JD fit. Morning digest overlaps the alert pipeline's LLM story.
- za-auth-db: folded into the single ZenAI line as sole-engineer work.
- ld-ece-fellow, pj-wisconsin-autonomous: lower fit than the systems-programming and GenAI projects.
- Removed in fitting: UW Algorithms, "CI/CD" and "tool calling" wording in Skills, the 11,745 user-days cap claim, and the second Haddee bullet.

## Constraints nearly violated

- nb-observability: metrics, dashboards, and alerts are not recorded. The bullet says "set up Prometheus and Grafana monitoring" and does not claim alerting, though the JD asks for it.
- nb-llm-failure: no post-deploy confirmation. The bullet claims a diagnosis and a sized cap, not a fixed failure rate.
- "6K-user" in the outreach pitch: 5,999 installs and 6,215 lifetime users are both in inventory.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, OS project line): **756.67 pt** from the top.
- Unused height: 792 − 25.92 − 756.67 = **9.41 pt** (passes 0–12 pt).
- Rendered at 70 dpi and checked: no clipping, overlap, or empty bottom strip.
