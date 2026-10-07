# Selection — Astera Labs, Applied AI NCG (Non Silicon)

## NewsBreak title
**AI Engineer Intern** — JD is applied AI as product work ("Applied AI team", "AI/ML applications, copilots, agents, and workflow automations"). Heading is plain "NewsBreak" (internal tools, not new ventures).

## Header
Mountain View, CA — role is in San Jose (Bay Area).

## Items used
- **nb-llm-pipeline** (two bullets)
  - Bullet 1: embed → LLM classify/score → per-topic percentile select → LLM same-story dedupe → push; Kubernetes CronJob; ~1,200 LLM calls/day; decision log — JD "workflow automations", "logs".
  - Bullet 2: 11-day production shadow, 4,100+ decision rows, hand-graded 89 vs 90 → categorical gate, 127-alert holdout, prompt ablations, rejected roundup rule (91% / two highest-reach alerts), filler 34% → 4% — JD "evaluation approaches, failure modes, improving output quality".
- **nb-agentic-search** (two bullets)
  - Bullet 3: one SSE endpoint, deterministic RAG turn 1, hybrid retrieval (RRF), bounded agent with 5 whitelisted tools (≤3 hops, 45 s), server-resolved citations — JD "tool use … permissions, and governance", "retrieval or knowledge experiences".
  - Bullet 4: eval harness on real logged queries against the committed catalog; 0% → 100% P@1, 28/28 recall, 0.4 ms; embeddings ruled out by measurement.
- **nb-llm-failure** (llm): Langfuse traces, 65% failure, p95 1,197 vs 16,384, 2,048-token cap — JD "investigate failures, diagnose reliability issues", "observability".
- **nb-fastapi-backend** + **nb-third-party-proxy** (fused): 89 endpoints on AWS EKS, ~1,450 offline tests, ruff / pyright / pytest gate; nine integrations moved server-side, zero client credentials — JD "integrations", "permissions".
- **nb-swiftui-app** + **nb-morning-digest** (fused): SportsBreak hyperlink (required), ~6,000 installs, LLM morning digest to 5,026 users (~81%), 72-event Amplitude catalog — JD "measuring adoption", "metrics".
- **hd-langchain-apis** (llm): LangChain resume parsing / suggestions / matching.
- **hd-lead-mvp** (agile) + **hd-mentor-process**: 8 interns, Agile, stack, GCP App Engine; PR reviews, mentoring on Git and testing.
- **za-mock-interview** + **za-auth-db** + **za-demos-contracts** (fused): sole engineer; recruiters shaped AI scoring; iterated from user testing until three 200–500-person companies signed — JD "stakeholder needs", "end-user testing, feedback".
- **pj-codingplans**: LLM evaluation (KV caching, long context, needle-in-a-haystack).

## Skills
AI & ML first (tool calling / agents, RAG, hybrid retrieval, LangChain, Langfuse, PyTorch), Languages second (Python first). Full Stack & Data, then Cloud & Observability (Amplitude for dashboards/metrics), then Practices (incl. Claude Code / AI coding tools). Dropped mobile, ads, Terraform, etc.

## Coursework
CMU: Large Language Model Systems, Machine Learning, Data Science for Software Engineering, Distributed Systems. UW: Large Language Models in Practice, Software Engineering, Algorithms.

## Skipped
- **nb-jira-process**: first draft had it (docs/communication); cut to fit one page.
- **pj-my-av**: first draft had it; cut to fit — least relevant to non-silicon GenAI tooling.
- **cm-psc / cm-nl-safety**: no room once NewsBreak GenAI bullets were in; control research is less relevant here.
- nb-catalog-cache, nb-eks-standup, nb-cronjob-outage, nb-retired-detector, nb-dramabreak-*, mobile items (server-driven UI, Live Activities, ads, App Store), coaching marketplace: less relevant or overlap.
- ld-ece-fellow, pj-wisconsin-autonomous: space.

## Constraints nearly violated
- JD mentions copilots, enterprise systems, HR / Finance stakeholders, governance — none claimed beyond inventory facts. "Whitelisted tools" and "zero API credentials" are the real permission-like facts.
- First compile was two pages (projects spilled). Cut the Jira bullet and my-av, shortened two skill rows and the Haddee/ZenAI bullets; dropped MCP and Grafana from skills for width.

## Verification (final PDF)
- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, codingplans line): **763.84 pt**.
- Unused height: 792 − 25.92 − 763.84 = **2.24 pt** (passes 0–12 pt).
- Rendered at 90 dpi and inspected: no clipping, overlap, or empty bottom strip. The AI & ML skills row wraps "PyTorch" to a second line, and CMU coursework wraps; no layout defect.
