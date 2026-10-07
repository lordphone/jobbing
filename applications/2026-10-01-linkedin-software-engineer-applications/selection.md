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

## Revision 2026-10-07 (referral version)

Rebuilt after the Wenyu Liu referral, for a reviewer reading in seconds: one claim per bullet, ordered as the JD reads (backend → infra/monitoring → post-mortem → performance → data integrity → agentic → telemetry → product).

- Split the old EKS + CronJob bullet: infra stand-up now carries HPA + Prometheus / Grafana (new **nb-observability**), and the outage reads as its own post-mortem.
- Added **nb-dramabreak-stripe** (signature-verified webhook as sole trusted fulfillment, idempotent, 60 s stale-pending reclaim) for "data layers" and "distributed transactions" without claiming either term.
- Backend bullet now carries ~83% of backend commits (nb-ownership) instead of the 344 PR count.
- SwiftUI bullet uses 1.4K App Store ratings (nb-swiftui-app) instead of ~6,000 installs.
- Langfuse bullet adds the Helm env shadowing the code default instead of the binomial model.
- ZenAI line 2 adds working with recruiters on AI scoring (cross-functional partners).
- Dropped Research (cm-psc): the JD does not ask for it, and the space went to Stripe, observability, and the split outage bullet.
- Skills: new "Cloud & Observability" row with Prometheus and Grafana; dropped GitHub Actions (CI/CD stays under Practices).

## Items used

- **nb-fastapi-backend + nb-ownership**: first commit → 89 REST endpoints, 26 collections, ~83% of backend commits, ~1,450 offline unit tests, ruff / pyright / pytest CI gate.
- **nb-eks-standup + nb-observability**: EKS / Docker / Helm / Jenkins on day 3, HPA, 7 CronJobs; Prometheus metrics and Grafana dashboards.
- **nb-cronjob-outage**: 5-day silent outage, non-terminal ImagePullBackOff kept the Job active, Forbid skipped later runs; paired deadlines.
- **nb-catalog-cache**: 25–30 requests → 1 call; 13.2 MB per user → 10.9 MB shared, 78×, 512 MiB pod.
- **nb-dramabreak-stripe**: Stripe web checkout, signature-verified webhook, idempotent, 60 s stale-pending reclaim.
- **nb-agentic-search** (`design`, compressed): SSE, deterministic RAG turn 1, bounded agent (≤3 hops, 5 tools), hybrid RRF retrieval degrades to surviving legs.
- **nb-llm-pipeline**: ingest → embed → LLM-score → dedupe → push, ~1,200 LLM calls/day, 4,100+ shadow decisions, filler 34% → 4%, 2/day cap over 11,745 user-days.
- **nb-llm-failure**: 65% via Langfuse, p95 1,197 vs. 16,384, Helm env shadowing the code default.
- **nb-swiftui-app + nb-jira-process**: sole SwiftUI engineer, App Store link, 1.4K ratings, 1,119 peak DAU; 34 API specs, ~10,000 lines of docs, onboarded the second engineer.
- **hd-lead-mvp + hd-langchain-apis**: 8 interns, Agile, React / Next.js / FastAPI / Supabase, 0→1, GCP App Engine, schemas and REST APIs, LangChain.
- **hd-mentor-process**: user stories, PR reviews, mentoring.
- **za-mock-interview + za-auth-db**: sole engineer, React / Next.js / Supabase / PostgreSQL, auth, session, DB.
- **za-mock-interview (recruiters) + za-demos-contracts**: scoring matched to real hiring, demos, three 200–500-person companies signed.
- **pj-my-av** (`short`).

## Items skipped

- **cm-psc, cm-nl-safety**: JD does not ask for research; space went to backend content.
- **nb-third-party-proxy, nb-retired-detector, nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-morning-digest, nb-manual-broadcast, nb-dramabreak-ads, nb-coaching-marketplace**: less relevant; no room.
- **ld-ece-fellow, pj-codingplans, pj-wisconsin-autonomous**: no room.
- Skills dropped: GitHub Actions, Stripe (in a bullet), Pydantic, Motor, HTML, CSS, Express, Tailwind, Firebase, Supabase, mobile tooling, Terraform, NGINX, ArgoCD, Jira, certifications (later restored as their own skills row).

## Constraints almost violated

- C++, C#, Objective-C, Ruby are in the JD but not in inventory; not claimed. "Distributed transactions" and "query optimization" not claimed; the Stripe bullet states only what was built.
- Prometheus / Grafana: printed only as "set up Prometheus metrics and Grafana dashboards"; which metrics and any alerts are not in inventory, and they did not detect the CronJob outage, so the two are not linked.
- First compile was 2 pages (~3 lines over): cut Haddee mentoring, then unwrapped two skills rows (dropped Stripe, GitHub Actions) and restored the Haddee line.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 792 pt tall)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 765.95 pt
- Unused height: 792 − 25.92 − 765.95 = 0.13 pt (passes 0–12 pt). On request, filled with a Certifications skills row (both AWS certs from inventory/skills.md) instead of extra spacing; itemsep 0.4 pt to fit it.
- Visual review: rendered at 110 dpi; no empty bottom strip, clipping, or overlap; spacing even.
