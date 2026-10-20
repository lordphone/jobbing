# Selection — C3 AI, Forward Deployed Engineer, New Grad 2027

## NewsBreak title

**Full-Stack Engineer Intern** — JD: "This is a full-stack software engineering role with direct customer exposure." Heading is plain "NewsBreak" (not a new-venture JD).

Header city: Mountain View, CA (posting is Redwood City, CA).

## Items used

NewsBreak is capped at 6 full bullets at his request (2026-10-09): the original 7 minus the integrations / docs bullet.

- **nb-ownership + nb-swiftui-app** → bullet 1: sole SwiftUI engineer, primary backend author, SportsBreak link, 1.4K ratings, peak DAU 1,119, 344 PRs / 340 merged.
- **nb-fastapi-backend + nb-eks-standup + nb-observability** → bullet 2: 89 endpoints, ~1,450 offline tests, EKS on day 3 (Docker, Helm, Jenkins), Prometheus / Grafana.
- **nb-agentic-search** → bullet 3: RAG turn 1, bounded tool-calling loop (≤3 hops, 5 tools), server-resolved citations, 0% → 100% P@1 — "agentic AI", "LLM tool calling".
- **nb-llm-pipeline** → bullet 4: ~1,200 LLM calls/day, production shadow on 4,100+ decisions, prompt ablations, filler 34% → 4% — "prompt engineering".
- **nb-catalog-cache** → bullet 5: AI-agent-written cache, redesigned as pod memory neared 512 MiB, 78× smaller, 9.0 → 0.89 ms — "profiling & optimization", "developer AI workflows".
- **nb-cronjob-outage + nb-llm-failure** → bullet 6: 5-day silent CronJob outage; 65% failure rate traced via Langfuse — "debugging, troubleshooting".
- **hd-lead-mvp + hd-langchain-apis + hd-mentor-process** → Haddee 3 lines (React, Next.js — JD prefers React).
- **za-mock-interview + za-auth-db + za-demos-contracts** → ZenAI: sole engineer 0→1; demoed and iterated with clients until three 200–500-person companies signed — "technical demonstrations, proofs-of-technology", customer-facing.
- **cm-nl-safety + cm-psc** → research, two bullets (fill).
- **pj-my-av** → project, default line (he asked for it over codingplans).
- **ld-ece-fellow** → leadership line, page fill; outreach / events fits the customer-facing role.
- Skills: Python, JavaScript, Java first (JD languages); LLM tool calling / agents, RAG, Claude Code / AI coding tools (JD AI + preferred dev AI workflows); TypeScript / React (preferred); SQL, PostgreSQL, MongoDB (relational / NoSQL); cloud row; certifications kept.
- Coursework: CMU — Distributed Systems, LLM Systems, ML; UW — Algorithms, Software Engineering, LLMs in Practice (data structures / algorithms).

## Skipped

- nb-server-driven-ui, nb-app-store, nb-live-activities, nb-manual-broadcast, nb-dramabreak-ads, nb-coaching-marketplace: mobile-specific, not the JD.
- nb-third-party-proxy, nb-jira-process (specs / docs): the 7th bullet, cut for the 6-bullet cap.
- nb-retired-detector, nb-cross-dept, nb-dramabreak-stripe: space.
- pj-wisconsin-autonomous, pj-cs537-os: less relevant; no room.
- pj-codingplans: replaced by my-av at his request.

## Constraints almost violated

- Java is in skills.md but no inventory bullet shows Java work; listed only in Skills.
- No travel, trial, or customer-training facts beyond ZenAI demos and contracts; did not claim customer training.
- "Claude Code / AI coding tools" kept as the exact skills.md name (shortening it changed the name).
- First compile spilled ~9 lines onto page 2; shortened NewsBreak bullets 2–5, Haddee and ZenAI lines, and skills rows; then added the Haddee mentoring line, ZenAI auth, and the ECE fellow line to fill.

## Page-fill verification (final PDF)

- Pages: 1
- Bottom margin: 0.36 in = 25.92 pt (from shared/preamble.tex)
- Last content line bottom (pdftotext -bbox yMax): 758.99 pt of 792 pt
- Unused height: 792 − 25.92 − 758.99 = 7.08 pt (within 0–12 pt)
- Visual review at 110 dpi: no empty bottom strip, clipping, overlap, or orphaned wraps.
