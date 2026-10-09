# Selection — Roblox, Software Engineer, Foundation AI (Agent Infra), ID 40503

## NewsBreak title

**Software Engineering Intern**: the posting title is "Software Engineer". The team builds agent *infrastructure*, not AI product work, so the AI Engineer Intern title would mislabel the fit. The heading is plain "NewsBreak" because nothing in the JD is about new ventures.

Header city: Mountain View, CA (San Mateo, Bay Area).

## Items used

- **nb-agentic-search** → bullet 1 (deterministic RAG on turn 1; bounded tool loop ≤3 hops, 45 s, 5 whitelisted tools; server-resolved citations; failed retrieval leg degrades, only all failing is a 500). JD: "run autonomous AI agents", "safe, durable", "non-deterministic".
- **nb-llm-failure** → bullet 2 (65% failure rate, Langfuse, unbounded reasoning loop, p95 1,197 vs 16,384, cap truncates 0% of successes). JD: "you can tell us what broke"; long-running agent workloads.
- **nb-llm-pipeline** → bullet 3 (Kubernetes CronJob, ~1,200 LLM calls/day, 11 days production shadow, 4,100+ decision rows, shipped live, filler 34% → 4%).
- **nb-eks-standup** + **nb-cronjob-outage** → bullet 4 (production EKS on day 3; 5-day silent CronJob outage, paired deadlines). JD: infrastructure, durable.
- **nb-catalog-cache** → bullet 5 (cache written by an AI agent; 13.2 MB per user → 10.9 MB shared, 78×, 512 MiB pod). JD: "cost effective", plus the AI-agent "what broke" angle.
- **nb-fastapi-backend** + **nb-third-party-proxy** → bullet 6 (89 endpoints, ~1,450 offline tests in CI; nine integrations server-side, zero API credentials in the binary). JD: "real credentials against real systems", "security".
- **nb-ownership** + **nb-swiftui-app** → bullet 7 (sole SwiftUI, primary backend, ~6,000 installs, peak DAU 1,119, 344/340 PRs). JD: "systems already in front of real users".
- **hd-lead-mvp** + **hd-langchain-apis** → Haddee, one fused line.
- **za-mock-interview** + **za-demos-contracts** → ZenAI.
- **cm-nl-safety** → research fill (multi-turn LLMs).
- **pj-codingplans** → project (the JD asks for "experiment and share your agentic workflows" and keeping pace with the industry). **ld-ece-fellow** → leadership.
- Skills: Python and Go lead (the JD names Go, Python, Rust; Rust is not in skills.md, so it isn't claimed). AI & Agents row: LLM tool calling / agents, MCP, RAG, Langfuse, Claude Code / AI coding tools. Cloud & Infra and Backend rows follow. The Certifications row is kept.
- Coursework: CMU Distributed Systems, LLM Systems, ML; UW Operating Systems, LLMs in Practice, Algorithms (JD: "infrastructure, distributed, and agentic systems").

## Items skipped

- nb-retired-detector, nb-morning-digest, nb-jira-process: lower value than the infra and agent bullets.
- nb-observability: dropped for space. Prometheus/Grafana are still in Skills.
- nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-dramabreak-*, nb-coaching-marketplace, nb-manual-broadcast: mobile/product work.
- hd-mentor-process, za-auth-db: space.
- cm-psc: one research line is enough.
- pj-my-av, pj-wisconsin-autonomous: tried, but adding a 2-line project spilled to page two.

## Constraints nearly violated

- Rust appears in the JD but not in skills.md, so it is not claimed.
- "AI-agent-written cache": the inventory says the cache code was written by an AI agent and that he found the per-user key later. The bullet does not claim he wrote the cache.
- The first draft ran to two pages. Bullets 1–3 and 4–6 were tightened. Research was removed and then re-added once the orphan third lines were cut. Spacing was not loosened. Margins and font size are untouched.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, ECE Fellow line): **759.10 pt** from the top.
- Unused height: 792 − 25.92 − 759.10 = **6.98 pt** (passes 0–12 pt).
- Rendered at 90 dpi and inspected: no clipping, no overlap, no empty bottom strip.
