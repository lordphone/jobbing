# Selection — Mutual of Omaha, Full Stack Engineer I/II (505205)

## NewsBreak title

**Full-Stack Engineer Intern** — the JD title is "Full Stack Engineer I/II"; he was primary on both the iOS app and the FastAPI backend.

## Header

Remote (US) role → Mountain View, CA.

## Items used

- `nb-ownership` + `nb-swiftui-app` → bullet 1: sole SwiftUI engineer, primary backend author, ~6,000 installs, peak DAU 1,119, 1.4K ratings, 344 PRs across five repos (340 merged).
- `nb-fastapi-backend` → bullet 2: FastAPI / MongoDB from the first commit, 89 REST endpoints, 26 collections, ~1,450 offline tests (1:1), ruff / pyright / pytest CI gate. Hits "RESTful APIs", "MongoDB", "unit testing".
- `nb-jira-process` → bullet 3: 34 contract-first API specs ("defining API contracts"), ~10,000 lines of docs, Jira backlog, onboarded second engineer ("teacher, or mentor").
- `nb-third-party-proxy` → bullet 4: nine third-party integrations server-side, zero credentials in the binary. Closest real match to "integration development" / MuleSoft-style platform integration.
- `nb-catalog-cache` → bullet 5: fan-out 25–30 → 1, 13.2 MB per-user → 10.9 MB shared, 78×, 512 MiB pod. Hits "performance tradeoffs" / "optimize applications".
- `nb-eks-standup` + `nb-cronjob-outage` → bullet 6: AWS EKS, Docker (two-stage image), Helm, Jenkins, day 3, 7 CronJobs; 5-day CronJob outage fix. Hits "AWS containerized microservices", "Docker, Kubernetes, CI/CD".
- `nb-dramabreak-stripe` → bullet 7: Stripe checkout, signature-verified webhook as only trusted fulfillment, idempotent, 60s stale-pending reclaim. Event/webhook-driven integration with an external vendor.
- `nb-llm-pipeline` → bullet 8: ingest → embed → LLM-score → dedupe → push, 4,100+ shadow decisions, 34% → 4%, 11,745 user-days. Keeps the "AI agentic" angle and a pipeline/data-solution story.
- `hd-lead-mvp` + `hd-langchain-apis` → Haddee 1; `hd-mentor-process` → Haddee 2 (leader/mentor in JD).
- `za-mock-interview` + `za-auth-db` → ZenAI 1; `za-demos-contracts` (contracts) → ZenAI 2.
- `cm-psc` → research, kept as fill.
- `pj-my-av` (short) → projects, fill.
- Skills: Java, JavaScript first (JD languages); row 2 REST APIs, MongoDB, AWS, Docker, Kubernetes, CI/CD (JD preferred list); React in row 3; Claude Code / AI coding tools for "AI Agentic driven Software Development"; AWS Solutions Architect cert for the AWS emphasis.
- Coursework: CMU Distributed Systems, Foundations of SE, Software Refactoring (legacy modernization); UW Software Engineering, Algorithms, Operating Systems.

## Items skipped

- `nb-agentic-search` — strong but LLM-heavy; JD is integration/backend. Space went to Stripe and integrations.
- `nb-server-driven-ui`, `nb-live-activities`, `nb-app-store`, `nb-ads-max`, `nb-dramabreak-ads`, `nb-morning-digest`, `nb-manual-broadcast` — mobile-specific.
- `nb-llm-failure`, `nb-retired-detector`, `nb-coaching-marketplace` — lower relevance.
- `cm-nl-safety`, `pj-wisconsin-autonomous`, `pj-codingplans`, `ld-ece-fellow` — not relevant / no room.

## Constraints almost violated

- JD wants Spring Boot, Groovy, Kafka/RabbitMQ, MuleSoft, JUnit/Spock, Gradle, TKG — none are in `inventory/skills.md`, so none are printed. Redis Streams exists in inventory but was cut from the skills row for space.
- First draft spilled the Projects section onto page 2 and had three wrapping skills rows; tightened skills rows to one line each and shortened the Haddee mentoring bullet ("testing protocols, and scalable code practices" → "testing, and scalable code").

## Page-fill verification (final PDF)

- Pages: 1 (letter, 612 × 792 pt)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 760.90 pt
- Unused height: 792 − 25.92 − 760.90 = 5.18 pt (within 0–12 pt)
- Visual review: rendered at 110 dpi; no empty bottom strip, no clipping, overlap, or wrapping skill rows.
