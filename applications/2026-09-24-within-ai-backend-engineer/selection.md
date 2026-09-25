# Selection - Within (formerly Klarity) AI Backend Engineer

Date: 2026-09-24

## Title and priorities

- NewsBreak title: **Backend Engineer Intern**. The posting is "AI Backend Engineer" and describes "Backend + Applied AI Engineers" who "design and ship backend services that ingest messy real-world data, orchestrate model/agent workflows." The backend rule applies first because the role owns services, APIs, data models, and background processing. The AI half is covered by the bullets. AI Engineer Intern was the runner-up.
- Header: Mountain View, CA (SF / Bay Area role).
- Highest fit:
  - "structured outputs, tool calling, state management, grounding, and other guardrails" → agentic search (bounded tool-calling agent, server-resolved citations, degrade-to-survivors retrieval)
  - "evals, model regression tests" → entity resolver P@1 measured by an eval harness run against the real catalog
  - "traceability" → alert pipeline per-item decision log, plus Langfuse-trace diagnosis
  - "correctness, observability" → offline test suite behind the CI gate
- Skills: Python/SQL first; the Backend & LLM row carries FastAPI, REST APIs, Pydantic, RAG, hybrid retrieval, RRF, LangChain, and Langfuse. All come from inventory/skills.md.
- Coursework: CMU LLM Systems, Distributed Systems, Machine Learning; Wisconsin LLMs in Practice, Operating Systems, Algorithms.

## Selected items and facts

### NewsBreak
1. **nb-fastapi-backend** (+ nb-ownership "primary backend author"): first commit → 89 endpoints on EKS, ~1,450 fully offline tests, ruff/pyright/pytest gate.
2. **nb-agentic-search** (design): turn-1 deterministic RAG, turn-2+ tool-calling agent, hybrid retrieval where a failing leg degrades to the survivors, server-resolved citations the model cannot author.
3. **nb-agentic-search** (entities): real logged queries 0% → 100% P@1, deterministic entity resolver as the query rewriter, 0.4 ms, eval harness runs against the real committed catalog.
4. **nb-llm-pipeline**: embed → LLM-score → categorical `happened/speculative/no_event` gate → LLM same-story dedupe, as a Kubernetes CronJob; per-item decision log; 4,100+ shadow decision rows; filler 34% → 4% by count.
5. **nb-llm-failure**: 65% failure rate in another team's LLM pipeline, Langfuse traces, unbounded reasoning loop at 16,384 tokens, 2,048 cap sized against p95 1,197. No claim that the fix lowered the rate.

### Haddee
1. **hd-lead-mvp + hd-mentor-process**: 8 interns, Agile, React/Next.js/FastAPI/Supabase 0→1 on GCP App Engine, PR reviews, mentoring.
2. **hd-langchain-apis**: schemas and REST APIs for LangChain resume parsing, suggestions, AI job matching.

### ZenAI
1. **za-mock-interview + za-auth-db**: sole engineer, 0→1 LLM mock-interview app, React/Next.js/Supabase/PostgreSQL, auth/session/DB.
2. **za-mock-interview + za-demos-contracts**: recruiter-aligned AI scoring, client iteration, demos, contracts with mid-sized companies. No claim about lasting company direction.

### Research / projects
- **cm-nl-safety + cm-psc**: NL → formal safety specs with multi-turn LLMs; adaptive probabilistic safety certificate outperformed Adaptive MPC in simulation.
- **pj-my-av**: CNN-GRU, 1s video, 33 h Comma2k19 data pipeline, local CUDA + Vertex AI.
- **ld-ece-fellow**: fill line.

## Skipped and why

- **nb-third-party-proxy** (zero API credentials in the iOS binary): matches "secure data handling." It was in the first draft, but cut to fit one page.
- **nb-catalog-cache**, **nb-eks-standup**, **nb-cronjob-outage**: good backend/infra evidence, but less direct than AI orchestration, evals, and guardrails.
- **nb-retired-detector**, **nb-morning-digest**: overlapping LLM evidence.
- **nb-swiftui-app**, **nb-server-driven-ui**, **nb-app-store**, **nb-live-activities**, **nb-ads-max**, **nb-manual-broadcast**, **nb-dramabreak-***: mobile, ads, and payments.
- **nb-jira-process** (contract-first API specs): relevant to "ambiguous product asks into clean technical specs," but no room.
- **nb-coaching-marketplace**, **pj-wisconsin-autonomous**: least relevant.

## Constraints almost violated

- First draft spilled to 2 pages (about 5 lines over). Cut the third-party-proxy clause, the "≤3 hops, 5 whitelisted tools" detail, "same-story" / "production-" qualifiers, and "personalized" to fix a one-word orphan.
- The alert-pipeline number is by count (34% → 4%). No device-weighted number is mixed in.
- The nb-llm-failure bullet does not claim that the failure rate went down.

## Verification (final PDF)

- Compiled freshly with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdfplumber): **757.50 pt** from top.
- Unused height: 792 − 25.92 − 757.50 = **8.58 pt** (passes 0–12 pt).
- Rendered at 110 dpi and inspected the whole page: no clipping, overlap, cramped text, or empty bottom strip.
