# Selection — Roku, Software Engineer, Early Careers focused on AI and UI (ID 11490)

## NewsBreak title

**Software Engineering Intern** — posting title is "Software Engineer" and the JD says "This is a systems engineering job first"; AI Engineer Intern would undersell the systems half the JD "will not compromise on". JD doesn't say "SWE", so the full title is printed.

Header city: Mountain View, CA (San Jose, in office Mon–Thu → Bay).

## Items used

JD keywords: multi-step agents in production, internal tooling, real-time telemetry / event processing, CPU and memory constraints, devices / hardware in the loop, schema changes shipping to millions of devices, accountable for code you did not type (gates, review), where agents fall short, AI tool fluency, OS Platform UI (home screen, content discovery).

- **nb-llm-pipeline** → NB 1: multi-step embed → LLM-score → select → LLM dedupe → push in a K8s CronJob, ~1,200 LLM calls/day, production shadow on 4,100+ decisions, live, filler 34% → 4%. ("Multi-step agents that do real work in production.")
- **nb-agentic-search** → NB 2: one SSE endpoint, turn 1 deterministic RAG with RRF hybrid retrieval, bounded tool-use agent (≤3 hops, 5 tools, 45s), leg failure degrades to survivors, server-resolved citations. ("Something agentic… multi-step rather than a wrapper"; "what broke".)
- **nb-fastapi-backend** (regression) + **nb-catalog-cache** (AI-written fact) → NB 3: ~1,450 offline tests, 0.17s, ruff/pyright/pytest gate, Motor fake reproducing the prod failure behind HTTP 200. "AI-written code" is grounded in nb-catalog-cache ("cache code was written by an AI agent… he wrote tests for it") and profile (uses Claude Code heavily). ("Accountable for code you did not type… your own gates.")
- **nb-catalog-cache** → NB 4: 512 MiB pod, 13.2 MB per user → 10.9 MB shared, 78×, 25–30 → 1 call. ("CPU and memory constraints.")
- **nb-server-driven-ui + nb-swiftui-app** (analytics) → NB 5: 27 widget types, no App Store release for a new catalog surface, unknown kinds drop; 72-event typed analytics catalog with server-side allowlist. ("Why a schema change matters when it ships to millions of devices"; Platform UI / content discovery; telemetry.)
- **nb-llm-failure + nb-live-activities** → NB 6: 65% failure via Langfuse traces, p95 1,197 vs 16,384; iOS drops a start push while APNs returns 200. (Telemetry debugging; "signals you cannot simulate on a laptop".)
- **nb-ownership + nb-swiftui-app + nb-eks-standup + nb-cronjob-outage** → NB 7: sole SwiftUI engineer, SportsBreak link, ~6,000 installs, primary backend author, EKS day 3, 5-day CronJob outage.
- **hd-lead-mvp + hd-langchain-apis** → Haddee 1. **hd-mentor-process** → Haddee 2 (review discipline; also fill).
- **za-mock-interview + za-demos-contracts** → ZenAI 1.
- **pj-wisconsin-autonomous** (encoders) → hardware in the loop, real-time data to a Jetson.
- **pj-my-av** (short) → streaming inference. **pj-codingplans** → fill; also a view on where LLM providers fall short.
- Skills: Systems & Infra row first (Kubernetes, CronJobs, Redis Streams, Jetson), AI & Agents second (tool calling / agents, Claude Code / AI coding tools, MCP).
- Coursework: CMU Distributed Systems, LLM Systems, ML; UW Operating Systems, Computer Architecture, Mobile Computing Laboratory.

## Skipped

- nb-retired-detector — good "what broke" story, but no room; NB 1 already covers the pipeline.
- nb-ads-max, nb-dramabreak-ads, nb-dramabreak-stripe, nb-app-store, nb-coaching-marketplace, nb-manual-broadcast, nb-morning-digest, nb-third-party-proxy, nb-jira-process — off JD or no room.
- Research (cm-psc, cm-nl-safety) — off JD; projects used as fill instead (hardware/real-time fits better).
- ld-ece-fellow — off JD.

## Constraints nearly violated

- First draft said "home-catalog surface"; inventory says "catalog surface" only — changed to avoid implying a home screen.
- Abbreviated "Server-Sent Events (SSE)" to "SSE" in skills for space; restored the inventory name.
- Telemetry, event processing, C++, BrightScript, and Roku-specific device work are not in inventory — not claimed. "AI-written" is only applied to the cache code (inventory fact) and the tests gating it.
- First compile spilled to 2 pages by ~12 lines; tightened NB bullets, dropped the GCP/HPA/hybrid retrieval/PostgreSQL skill entries, then refilled with codingplans and the Haddee mentoring bullet. Role-break `\vspace` reduced 1pt → 0.5pt to bring the last line inside the margin.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, codingplans line): **765.23 pt** from the top.
- Unused height: 792 − 25.92 − 765.23 = **0.85 pt** (passes 0–12 pt).
- Rendered at 90 dpi and inspected: no clipping, overlap, or empty bottom strip. Short last lines on the server-driven UI, Langfuse, and Haddee mentoring bullets; no layout defect.
