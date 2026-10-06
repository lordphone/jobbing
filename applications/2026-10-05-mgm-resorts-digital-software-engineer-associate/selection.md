# Selection — MGM Resorts, Digital Software Engineer Associate (280074)

## NewsBreak title

**Full-Stack Engineer Intern** — JD requires a "strong understanding of all software layers including UI, service, data store and communication layers"; he was primary on both SwiftUI and FastAPI.

## Items used

- `nb-ownership` + `nb-swiftui-app` (bullet 1): sole SwiftUI engineer, primary backend author, ~6,000 installs, peak DAU 1,119, 1.4K ratings, 344 PRs / 340 merged. Maps to "production grade code" and "customer experiences".
- `nb-fastapi-backend` (bullet 2): 89 endpoints, 26 collections, ~1,450 offline tests 1:1, ruff/pyright/pytest gate. Service + data store layers.
- `nb-server-driven-ui` (bullet 3): 27 widget types, no App Store release, unknown kinds drop. UI layer + "simple and intuitive products that work".
- `nb-catalog-cache` (bullet 4): fan-out 25–30 → 1, 13.2 MB → 10.9 MB shared (78×), 512 MiB pod. "Platform performance".
- `nb-eks-standup` + `nb-cronjob-outage` (bullet 5): EKS day 3, Docker/Helm/Jenkins, 7 CronJobs, 5-day outage fix. "Deployment and sustainment", "DevOps culture", "reliability".
- `nb-llm-failure` (bullet 6, `backend` variant + 2,048 cap): Langfuse traces, 65% failure rate. "Observability" and supportability across services.
- `nb-third-party-proxy` + `nb-dramabreak-stripe` (bullet 7): nine integrations server-side; Stripe idempotent webhook. Communication layer + commerce.
- `nb-jira-process` (bullet 8): Jira backlog, 34 API specs, ~10,000 lines docs, onboarded second engineer. "Effectively communicate", Agile/Kanban, cross-team.
- `hd-lead-mvp` + `hd-langchain-apis` (Haddee 1), `hd-mentor-process` (Haddee 2): Agile sprints, user stories, PR reviews.
- `za-mock-interview` / `za-auth-db` (ZenAI 1), `za-demos-contracts` (ZenAI 2).
- `cm-psc` (research, as fill).
- `pj-my-av` (`short`, project fill).
- Coursework: CMU Distributed Systems first ("distributed computing"); UW Computer Architecture added for "all software layers".
- Skills: Java first (JD: "java/C++/other"); C included (no C++ in inventory). DevOps row for "DevOps culture"; Agile/Scrum + Jira for "Scrum, Kanban".

## Items skipped

- `nb-llm-pipeline`, `nb-agentic-search`, `nb-retired-detector` — LLM-heavy; JD is general digital product engineering. Langfuse bullet kept only for observability.
- `nb-live-activities`, `nb-ads-max`, `nb-app-store`, `nb-dramabreak-ads`, `nb-morning-digest`, `nb-manual-broadcast` — mobile/ads specifics; lower relevance.
- `nb-coaching-marketplace`, `cm-nl-safety`, `pj-wisconsin-autonomous`, `pj-codingplans`, `ld-ece-fellow` — no room / lower relevance.

## Constraints almost violated

- JD names C++ and Kanban; neither is in `inventory/skills.md`, so neither is printed (C and Agile/Scrum instead).
- "Previous experience working in a similar resort setting" — no inventory fact; not claimed.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 612 × 792 pt)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 760.29 pt
- Unused height: 792 − 25.92 − 760.29 = 5.79 pt (within 0–12 pt)
- Visual review: rendered at 110 dpi; no empty bottom strip, no clipping, overlap, or wrapping skill rows.
