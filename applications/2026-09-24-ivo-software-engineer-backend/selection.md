# Selection - Ivo Software Engineer, Backend

Date: 2026-09-24

## Title and priorities

- NewsBreak title: **Backend Engineer Intern**. The JD is titled "Software Engineer, Backend" ("Role: Backend Engineer") and centers on "systems that process and analyze millions of contracts reliably."
- Chosen over the Fullstack posting at the same company: stronger match on search/retrieval and LLM pipelines; web-UI evidence is thinner than backend evidence.
- Header: Mountain View, CA (SF on-site, Bay allowed).
- Highest fit: "most accurate search and retrieval systems" → agentic search + entity resolution; "pipelines that orchestrate LLMs ... at scale" → LLM alert pipeline; "process ... reliably" → FastAPI backend with offline test gate + LLM failure diagnosis. Ivo's "ditching embeddings for agentic RAG" mirrors the measured rejection of embeddings for entity resolution.
- Skills: Python/SQL first; Backend & LLM row carries FastAPI, REST APIs, RAG, hybrid retrieval, RRF, LangChain, Langfuse. All from inventory/skills.md.
- Coursework: CMU LLM Systems, Distributed Systems, Machine Learning; Wisconsin LLMs in Practice, Algorithms, Operating Systems.

## Selected items and facts

### NewsBreak
1. **nb-fastapi-backend** (+ nb-ownership "primary backend author"): first commit → 89 endpoints on EKS, ~1,450 fully offline tests, ruff/pyright/pytest gate.
2. **nb-agentic-search** (design): turn-1 deterministic RAG, turn-2+ bounded tool-calling agent, hybrid keyword + vector retrieval fused by RRF, server-resolved citations the model cannot author.
3. **nb-agentic-search** (entities): real logged queries 0% → 100% P@1, deterministic entity resolver as query rewriter, 0.4 ms, embeddings measured and rejected.
4. **nb-llm-pipeline**: embed → LLM-score → percentile gate → LLM same-story dedupe as a Kubernetes CronJob; 4,100+ production-shadow decisions; filler 34% → 4% by count.
5. **nb-llm-failure**: 65% failure rate in another team's LLM pipeline, Langfuse traces, unbounded reasoning loop at 16,384 tokens, 2,048 cap sized against p95 1,197. No claim the fix lowered the rate (no post-deploy confirmation).

### Haddee
1. **hd-lead-mvp + hd-mentor-process**: 8 interns, Agile, React/Next.js/FastAPI/Supabase 0→1 on GCP App Engine, PR reviews, mentoring.
2. **hd-langchain-apis**: schemas and REST APIs for LangChain resume parsing, suggestions, AI job matching.

### ZenAI
1. **za-mock-interview + za-auth-db**: sole engineer, 0→1 LLM mock-interview app, React/Next.js/Supabase/PostgreSQL, auth/session/DB.
2. **za-mock-interview + za-demos-contracts**: recruiter-aligned AI scoring, fast client iteration, demos, contracts with mid-sized companies. No claim about lasting company direction.

### Research / projects
- **cm-nl-safety + cm-psc**: NL → formal safety specs with multi-turn LLMs; adaptive probabilistic safety certificate outperformed Adaptive MPC in simulation.
- **pj-my-av**: CNN-GRU, 1s video, 33 h Comma2k19 data pipeline, local CUDA + Vertex AI.
- **ld-ece-fellow**: fill line; startup/ownership signal.

## Skipped and why

- **nb-catalog-cache**: strong backend metric, but cut for page length; search and LLM pipelines map more directly to the JD.
- **nb-eks-standup**, **nb-cronjob-outage**, **nb-third-party-proxy**: infra/security detail less relevant than retrieval and LLM orchestration.
- **nb-swiftui-app**, **nb-server-driven-ui**, **nb-app-store**, **nb-live-activities**, **nb-ads-max**, **nb-manual-broadcast**, **nb-dramabreak-***: mobile/ads/payments.
- **nb-morning-digest**, **nb-retired-detector**: overlapping LLM evidence.
- **nb-jira-process**, **nb-coaching-marketplace**: lower value for this JD.
- **pj-wisconsin-autonomous**: embedded work, least relevant.

## Constraints almost violated

- First draft spilled to 2 pages (~80 pt over). Cut detail from bullets (dropped ~83% commit share, 0.17 s, ≤3 hops / 5 tools, 206-entity catalog, ~1,200 calls/day, bge from skills row, 4th CMU course, 3-DOF detail) rather than dropping a bullet.
- "4,100+ decisions" and "34% → 4%" kept by-count; no device-weighted number mixed in.
- nb-llm-failure bullet does not claim the failure rate went down.

## Verification (final PDF)

- Compiled freshly with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdfplumber): **757.50 pt** from top.
- Unused height: 792 − 25.92 − 757.50 = **8.58 pt** (passes 0–12 pt).
- Rendered at 110 dpi and inspected the whole page: no clipping, overlap, cramped text, or empty bottom strip.
