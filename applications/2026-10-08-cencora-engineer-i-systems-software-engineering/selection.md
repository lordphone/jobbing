# Selection — Cencora, Engineer I, Systems Software Engineering (R2614401)

JD is a standardized job-profile description: routine development, configuration, testing, and support; following troubleshooting steps and validating results; coding standards and system requirements; communicating status/blockers; finding process or documentation gaps. Preferred: cloud fundamentals, Agile, Scrum certifications. No named stack.

## NewsBreak title
**Software Engineering Intern** (default). JD says "software engineering" / "systems software engineering", not backend, full-stack, AI, or SWE specifically. Heading is plain "NewsBreak" — no new-venture angle.

## Header city
Remote, Pennsylvania; no Bay/Canada/NY rule applies → Mountain View, CA.

## Used
- **nb-ownership + nb-swiftui-app** → bullet 1: sole SwiftUI / primary backend author, team of ~6, 1.4K ratings, 1,119 peak DAU, 344 PRs (340 merged).
- **nb-fastapi-backend** → bullet 2: first commit → 89 REST endpoints, ~1,450 offline tests (1:1), ruff / pyright / pytest gate. Maps to "testing" and "coding standards".
- **nb-eks-standup + nb-observability** → bullet 3: AWS EKS (Docker, Helm, Jenkins) on day 3, 7 CronJobs, Prometheus + Grafana, DNS → TLS → admission-policy diagnosis. Maps to "configuration … support tasks" and cloud fundamentals.
- **nb-cronjob-outage** → bullet 4: 5-day silent CronJob outage, paired deadlines. Maps to "analyzes routine issues … troubleshooting".
- **nb-llm-failure** → bullet 5: 65% failure rate, Langfuse traces, Helm env shadowing the default, 2048-token cap vs observed p95, timeout raise labeled a band-aid with a pre-registered falsification test. Maps to "validating expected results".
- **nb-third-party-proxy + nb-catalog-cache** → bullet 6: zero third-party credentials in the binary; 25–30 → 1 call; shared cache 78× smaller.
- **nb-llm-pipeline** → bullet 7: 11-day production shadow, 4,100+ decisions, filler 34% → 4%.
- **nb-jira-process (default + audit)** → bullet 8: Jira backlog, 34 API specs, ~10,000 lines of docs, onboarded second engineer, reopened two security tickets. Maps to "process or documentation gaps" and "communicates status".
- **hd-lead-mvp (agile) + hd-langchain-apis (schemas/APIs) + hd-mentor-process** → Haddee 2 bullets. Agile sprints and user stories map to the Agile/Scrum preference.
- **za-mock-interview + za-auth-db + za-demos-contracts** → ZenAI 2 bullets.
- **pj-codingplans** → Projects.
- Skills: Cloud & Systems row first (AWS, GCP, EKS, Docker, Helm, Jenkins, CI/CD, Linux, Bash, Prometheus, Grafana), Practices row second (Agile/Scrum, Unit Testing, pytest, Git, Jira, REST APIs), then Languages, Frameworks & Data, Certifications (both AWS — maps to "certification in cloud fundamentals").
- Coursework: CMU Foundations of SE, Distributed Systems, Software Refactoring; UW Software Engineering, Operating Systems, Algorithms.

## Skipped
- **nb-agentic-search, nb-morning-digest, nb-retired-detector** — LLM product work; the JD does not ask for AI, and the alert pipeline already covers it.
- **nb-app-store, nb-live-activities, nb-ads-max, nb-manual-broadcast, nb-server-driven-ui, nb-dramabreak-ads, nb-dramabreak-stripe, nb-coaching-marketplace** — mobile/ads/product, not in the JD.
- **cm-psc, cm-nl-safety** — controls research; not relevant, and the page is full.
- **ld-ece-fellow, pj-my-av, pj-wisconsin-autonomous** — no room; lower relevance.

## Constraints almost violated
- No Scrum certification exists in inventory; only "Agile/Scrum" as a practice is claimed. Only the two AWS certifications are listed.
- No pharma/healthcare domain claim.
- First build left 15.15 pt unused; filled it by expanding the nb-llm-failure bullet with real facts (2048-token cap, pre-registered falsification test) instead of loosening spacing.

## Page-fill verification (final PDF)
- Pages: 1 (letter, 612 × 792 pt)
- Bottom margin (preamble): 0.36 in = 25.92 pt → content limit 766.08 pt
- Last content bottom (pdftotext -bbox yMax): 764.34 pt
- Unused height: 1.74 pt (within 0–12 pt)
- Visual review at 110 dpi: no empty strip, clipping, overlap, or cramped text.
