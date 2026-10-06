# Selection — Retell AI, Software Engineer, Internal Deployed

## NewsBreak title
**AI Engineer Intern** — JD: "build the AI systems ... production-grade AI workflows, internal tools, and agent systems", "Design LLM-powered systems", "Experience with LLMs, AI agents ... is a strong plus". AI/LLM/agents is the product work here.

## Items used
- **Venture team** (inventory/newsbreak.md team line): printed as "NewsBreak (Venture Team)" in the role heading — matches Founders Initiatives' cross-functional, new-venture framing.
- **nb-llm-pipeline** → bullet 1: ingest/embed/LLM-score/select/LLM dedupe/push CronJob, ~1,200 LLM calls/day, 4,100+ shadow decisions, filler 34% → 4%. Maps to "production-grade AI workflows".
- **nb-agentic-search** → bullet 2: one SSE endpoint, deterministic RAG turn 1, bounded tool agent (≤3 hops, 5 tools, 45 s), server-resolved citations, 100% P@1. Maps to "agent systems".
- **nb-third-party-proxy** + **nb-dramabreak-stripe** → bullet 3: nine integrations server-side (five named from the inventory list), zero credentials in the binary; Stripe checkout with signature-verified idempotent webhook. Maps to "Own API-based integrations" and finance workflows.
- **nb-fastapi-backend** + **nb-eks-standup** → bullet 4: 89 endpoints, ~1,450 offline tests, ruff/pyright/pytest gate, EKS on day 3.
- **nb-manual-broadcast** + **nb-jira-process** → bullet 5: internal broadcast tool used during the World Cup (a minute before FOX); Jira backlog unprompted; 34 API specs. Maps to "internal tools", "reduce manual operational overhead", ownership.
- **nb-llm-failure** → bullet 6: 65% failure rate via Langfuse, p95 1,197 vs 16,384 runaways, 2048-token cap sized against observed successes.
- **nb-ownership** + **nb-swiftui-app** → bullet 7: sole SwiftUI engineer, ~6,000 installs, primary backend author, 344 PRs / 340 merged.
- **hd-langchain-apis** → Haddee bullet 1 (lead): resume parsing, improvement suggestions, AI job matching — direct match to "extract structured signals from resumes" and "role fit".
- **hd-lead-mvp** + **hd-mentor-process** → Haddee bullet 2.
- **za-mock-interview** + **za-auth-db** → ZenAI bullet 1: sole engineer, worked with recruiters on scoring categories (recruiting AI), auth/session/DB.
- **za-demos-contracts** → ZenAI bullet 2: three 200–500-person companies signed (GTM / founder mindset).
- **pj-codingplans** → LLM provider evaluation (JD lists OpenAI, Gemini, Claude and "other models").
- **pj-my-av** → fill.
- Skills: AI & Agents first (LLM tool calling / agents, RAG, LangChain, MCP, Langfuse, Claude Code), then languages, then Backend & APIs (REST APIs, Stripe, Supabase, PostgreSQL).
- Coursework: LLM Systems / Distributed Systems / ML / Data Science for SE; LLMs in Practice / Software Engineering / Algorithms / OS.

## Items skipped
- nb-catalog-cache, nb-cronjob-outage, nb-retired-detector: strong but infra/perf; less relevant than integrations and internal tools; space.
- nb-server-driven-ui, nb-live-activities, nb-ads-max, nb-app-store, nb-morning-digest, nb-dramabreak-ads, nb-coaching-marketplace: mobile/ads; role is internal automation.
- cm-psc, cm-nl-safety: control research; JD does not ask for research and the page filled without it.
- pj-wisconsin-autonomous, ld-ece-fellow: least relevant.

## Constraints nearly violated
- Salesforce, HubSpot, GoHighLevel, Zapier, n8n, Make, Lark, DocuSign, OpenAI/Gemini APIs are not in inventory — not claimed. Claude appears only as "Claude Code / AI coding tools" (inventory skill). Search uses DeepSeek, not Claude — not implied otherwise.
- "Lead scoring" / "predict interview success" not claimed; Haddee bullet states only resume parsing, suggestions, and AI job matching.
- Third-party integration list names five of the nine in inventory; the count stays nine.
- First compile spilled one line to page 2; shortened the SportsBreak bullet ("five repositories" dropped, "344 PRs, 340 merged") to one line.

## Verification (final PDF)
- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, my-av line): **765.84 pt** from the top.
- Unused height: 792 − 25.92 − 765.84 = **0.24 pt** (passes 0–12 pt).
- Re-verified after adding "(Venture Team)" to the NewsBreak heading; same measurements.
- Rendered at 90 dpi and inspected: no clipping, overlap, or empty bottom strip. CMU coursework wraps to a second line ("Software Engineering"); no layout defect.
