# Selection — LinkedIn, Software Engineer - Applications

## NewsBreak title

**Backend Engineer Intern.** The posting title is "Software Engineer - Applications", but the work is APIs and services: "design extensible APIs and backend services that elegantly handle synchronous and asynchronous workflows" and "design and optimize data layers, selecting appropriate relational or non-relational database architectures".

## Framing

JD keywords: sync / async design patterns, APIs and backend services, data layers (relational / non-relational), unit tested + code reviewed + CI/CD, AI tools in the SDLC, telemetry / monitoring / profiling for production bottlenecks, documentation and post-mortems, autonomous agentic systems, performance optimization, collaboration.

- APIs / async: 89 REST endpoints on async MongoDB, SSE search endpoint, async push pipeline.
- Tests / CI / review: ~1,450 offline unit tests, ruff / pyright / pytest CI gate, 344 PRs; Haddee PR reviews.
- Performance: cache 78× smaller, 25–30 requests → 1 call.
- Telemetry / post-mortem: Langfuse diagnosis; 5-day CronJob outage root cause.
- Agentic systems: bounded tool-calling agent in search; LLM-scored pipeline.
- Documentation: 34 contract-first API specs, ~10,000 lines of docs.
- Data layers: MongoDB (non-relational) at NewsBreak, PostgreSQL / Supabase at ZenAI and Haddee.

Header: **Mountain View, CA** (the posting is Mountain View).

## Items used

- **nb-fastapi-backend + nb-ownership**: first commit → 89 REST endpoints, 26 collections, ~1,450 offline unit tests, ruff / pyright / pytest CI gate, 344 PRs. "async MongoDB" = Motor.
- **nb-eks-standup + nb-cronjob-outage** (fused): EKS / Helm / Jenkins on day 3, 7 CronJobs; 5-day silent outage (ImagePullBackOff + Forbid concurrency), paired job and scheduler deadlines.
- **nb-catalog-cache**: 13.2 MB per user → 10.9 MB shared, 78×, 512 MiB pod, 25–30 requests → 1 call.
- **nb-agentic-search** (`design` variant, compressed): one SSE endpoint, deterministic RAG on turn 1, bounded tool-calling agent turn 2+ (≤3 hops, 5 tools), hybrid Mongo text + vector RRF, degrades to surviving legs.
- **nb-llm-pipeline**: ingest → embed → LLM-score → dedupe → APNs ("push"), ~1,200 LLM calls/day, 4,100+ shadow decision rows, filler 34% → 4%, 2/day cap held over 11,745 user-days. "async" describes the CronJob-driven background pipeline.
- **nb-llm-failure**: 65% via Langfuse traces ("telemetry"), p95 1,197 vs. 16,384, binomial 49–66% vs. 65%.
- **nb-swiftui-app + nb-jira-process** (fused): sole SwiftUI engineer, App Store link on "SportsBreak", ~6,000 installs, 1,119 peak DAU; 34 contract-first API specs, ~10,000 lines of docs, onboarded the second engineer.
- **hd-lead-mvp + hd-langchain-apis** (fused): 8-intern team, Agile sprints, React / Next.js / FastAPI / Supabase, 0→1, GCP App Engine, schemas and REST APIs, LangChain resume parsing.
- **hd-mentor-process**: user stories, PR reviews, mentoring on Git, testing, scalable code (code review / best practices).
- **za-mock-interview + za-auth-db** (fused): sole engineer, React / Next.js / Supabase / PostgreSQL, auth, session, DB.
- **za-demos-contracts** (`contracts`): cross-functional / client collaboration.
- **cm-psc** (`default`): fill.
- **pj-my-av** (`short`): fill.

## Items skipped

- **nb-third-party-proxy, nb-retired-detector, nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-morning-digest, nb-manual-broadcast, nb-dramabreak-***, **nb-coaching-marketplace**: less relevant to backend APIs / data layers; no room.
- **cm-nl-safety**: research kept to one bullet for space.
- **ld-ece-fellow, pj-codingplans, pj-wisconsin-autonomous**: no room.
- Skills dropped: Pydantic, Motor, HTML, CSS, Express, Tailwind, Firebase, Supabase, Stripe, mobile tooling, Terraform, NGINX, Grafana, ArgoCD, Jira, certifications.

## Constraints almost violated

- C++, C#, Objective-C, Ruby are in the JD but not in inventory; not claimed. "Distributed transactions" and "query optimization" are not in inventory; not claimed (~48 indexes exists but was cut for space).
- First compile was 2 pages (~11 lines over). Tightened four bullets to two lines, dropped Pydantic and Grafana from skills, removed Research and the ZenAI contracts line. That left 94 pt unused, so I restored Research with one bullet and the ZenAI contracts line, shortening the Haddee bullet so "AI job matching" did not leave a one-word third line.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 792 pt tall)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 760.59 pt
- Unused height: 792 − 25.92 − 760.59 = 5.49 pt (passes 0–12 pt)
- Visual review: rendered at 110 dpi; no empty bottom strip, clipping, or overlap; spacing even.
