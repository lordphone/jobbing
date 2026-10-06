# Selection — EvenUp, Software Engineer (New Grad), AI Entities

## NewsBreak title

**Backend Engineer Intern** — the JD puts the role at "the intersection of backend engineering, document processing, and AI" and asks for "reliable backend services and systems". Most of the intern work was backend.

## Header

Mountain View, CA — posting allows San Francisco (hybrid) or Toronto.

## Items used

- `nb-agentic-search` (two bullets) — lead bullet: deterministic span-based entity resolution over the 206-entity catalog as query rewriter, 0% → 100% P@1 on real logged queries, 0.4 ms, eval harness on the real catalog, 28/28 recall, embeddings rejected by measurement. Leads because the team is "AI Entities" and the JD asks for tools to "evaluate" AI systems. Second bullet: one SSE endpoint, deterministic RAG over hybrid retrieval (substring + Mongo `$text` + bge, RRF), legs degrade to survivors, bounded tool agent for follow-ups, server-resolved citations.
- `nb-llm-pipeline` — framed as structured extraction from unstructured text: per-article categorical label (happened / speculative / no_event) + 0–100 importance, ~1,200 LLM calls/day, decision log (why each item fired), 4,100+ decision rows in production shadow, shipped live, filler 34% → 4%.
- `nb-fastapi-backend` + `nb-catalog-cache` — first commit → 89 endpoints on EKS, ~1,450 offline tests; per-user cache re-keyed to shared, 78× smaller, as pod memory neared 512 MiB ("performance, reliability, and scalability").
- `nb-llm-failure` + `nb-cronjob-outage` — reliability: 65% failure rate via Langfuse traces (p95 1,197 vs runaways at 16,384); 5-day silent CronJob outage fixed with paired deadlines.
- `nb-ownership` + `nb-swiftui-app` + `nb-morning-digest` — sole SwiftUI engineer, ~6,000 installs, peak DAU 1,119, primary backend author, 344 PRs (340 merged), digest to 5,026 users.
- `hd-lead-mvp` + `hd-langchain-apis` — fused into one bullet (8-intern team, stack, GCP App Engine, schemas + REST APIs for LangChain resume parsing and AI job matching). Resume parsing = document processing.
- `za-mock-interview` + `za-demos-contracts` — one bullet.
- `cm-nl-safety` — research: natural language → formal specs with multi-turn LLMs (unstructured → structured).
- `pj-codingplans` — project line.
- Coursework: CMU LLM Systems, Distributed Systems, Machine Learning; UW Algorithms, Data Structure & Programming III, LLMs in Practice (JD asks for data structures and algorithms).
- Skills: Python first (backend + AI); AI & LLMs and Backend & Data in rows 2–3; Java kept high for the OOP ask.

## Items skipped

- `nb-third-party-proxy`, `nb-jira-process` audit — security not in JD; space.
- `nb-eks-standup` — EKS already named; infra depth not asked.
- `nb-server-driven-ui`, `nb-app-store`, `nb-live-activities`, `nb-ads-max`, `nb-dramabreak-*`, `nb-manual-broadcast`, `nb-coaching-marketplace` — mobile/ads, not relevant.
- `nb-retired-detector` — good story but space.
- `hd-mentor-process` — collaboration covered by team lead line.
- `cm-psc`, `pj-my-av`, `pj-wisconsin-autonomous`, `ld-ece-fellow` — less relevant than codingplans; space.

## Constraints nearly violated

- First compile spilled ~11 lines to page 2. Fused the two Haddee bullets, cut ZenAI to two lines, dropped "129 Pydantic models" and the CI-gate clause from the backend bullet, dropped SSE from the Backend & Data skills row (still in the search bullet), and cut UW coursework to three. Then restored the CronJob outage clause to fill a 21 pt gap.
- "keyword, full-text, and bge vectors" stands for the substring + Mongo `$text` + bge vector legs.
- Renamed the "Practices" skills row to "Web & Practices" since it carries React / Next.js / Supabase; skill names unchanged.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, codingplans line): **758.55 pt** from the top.
- Unused height: 792 − 25.92 − 758.55 = **7.53 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, wrapped skill rows, or empty bottom strip. One short last line on the reliability bullet ("scheduler deadlines.").
