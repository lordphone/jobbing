# Selection — Rivian, Software Engineer (EV Charging, 34249)

Started from the 2026-10-19 Affirm Fullstack (Search) resume and retargeted it to backend microservices, Kubernetes, databases, and cloud deploys.

## NewsBreak title

**Backend Engineer Intern**: every qualification is backend or services work ("microservices using container technologies… Kubernetes", "Databases design (SQL, NoSQL)", "deploying applications and services into cloud environments"), and the responsibility is software that will "interact with numerous other services". Heading is plain "NewsBreak" because this is not a new-ventures team.

Header city: Mountain View, CA (Palo Alto role).

## JD keywords

Microservices, containers, Kubernetes; Node.js, TypeScript/JavaScript; database design (SQL, NoSQL) and analytics; cloud deploys (AWS, Azure, GCP); scalable, secure, maintainable; interacting with numerous other services; capturing requirements and use cases; communication with technical and non-technical people; self-starter.

## Items used

- **nb-fastapi-backend** → NB 1: first commit, Python/FastAPI, 89 REST endpoints, MongoDB data layer (26 collections, ~48 indexes, 129 Pydantic models), ~1,450 offline tests, ruff/pyright/pytest gate. (NoSQL database design, maintainable)
- **nb-eks-standup** → NB 2: production AWS EKS on day 3, Docker/Helm/Jenkins, 7 CronJobs, HPA, DNS → TLS → admission-policy chain, stale ArgoCD app. (Containers, Kubernetes, AWS deploy)
- **nb-third-party-proxy** → NB 3: nine integrations server-side, zero third-party credentials in the binary, ESPN proxy rolled back after 2.5 hours (no key, so only latency and a health dependency). (Secure, interacting with numerous other services, independent decisions)
- **nb-catalog-cache** → NB 4: 25–30 request fan-out → 1 call, per-user cache → shared 10.9 MB, 78×, 512 MiB pod. (Scalable)
- **nb-observability + nb-cronjob-outage + nb-llm-failure** → NB 5: Prometheus/Grafana, 5-day silent CronJob outage with paired deadlines, 65% failure rate in another team's LLM pipeline. (Problem solving)
- **nb-ownership + nb-swiftui-app + nb-jira-process** → NB 6: sole SwiftUI / primary backend, SportsBreak link, ~6,000 installs, peak DAU 1,119, 72-event Amplitude catalog (analytics), 344 PRs / 340 merged, 34 contract-first API specs (requirements), onboarded the next engineer (communication).
- **hd-lead-mvp + hd-langchain-apis** → Haddee 1: React/Next.js (JS/TS), FastAPI, Supabase, GCP App Engine deploy, schemas + REST APIs. **hd-mentor-process** → Haddee 2: user stories (requirements and use cases), PR reviews.
- **za-mock-interview + za-auth-db** → ZenAI 1: PostgreSQL (SQL), React/Next.js. **za-mock-interview (recruiters) + za-demos-contracts** → ZenAI 2: non-technical stakeholders, clients.
- **pj-codingplans**, **pj-my-av**, **ld-ece-fellow**: fill.
- Skills: TypeScript/JavaScript lead Languages; Cloud & Containers is row 2. Express is the closest inventory skill to Node.js. Node.js and Azure are not in inventory, so not listed. Certifications row kept.
- Coursework: CMU Distributed Systems (microservices), Data Science for SE (analytics), Machine Learning; UW Software Engineering, Operating Systems, Algorithms, Data Structure & Programming III.

## Skipped

- nb-agentic-search, nb-llm-pipeline, nb-morning-digest, nb-retired-detector: LLM product work. The JD is backend and infra.
- nb-server-driven-ui, nb-live-activities, nb-ads-max, nb-app-store, nb-manual-broadcast, nb-coaching-marketplace, nb-dramabreak-ads, nb-dramabreak-stripe, nb-cross-dept: lower fit or no room.
- Research (cm-psc, cm-nl-safety): vehicle-safety research is adjacent to Rivian but off this backend JD; page full without it.
- pj-wisconsin-autonomous, pj-cs537-os: off JD.
- Foundations of Software Engineering (CMU coursework): cut to stop a one-word wrap.
- Kubernetes HPA and Redis Streams skills: cut to stop row wraps (HPA is still in NB 2).

## Constraints nearly violated

- No Node.js in inventory. TypeScript/JavaScript come from Next.js/React work at Haddee and ZenAI. Express is listed as a skill but no bullet claims Node.js services.
- nb-llm-failure: "helped debug", no post-deploy confirmation. The bullet says "debugged" and claims no fix.
- nb-observability: metrics, dashboards, and alerts are not recorded, so the bullet says only "Set up Prometheus and Grafana".

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, ECE Fellow line): **764.89 pt** from the top.
- Unused height: 792 − 25.92 − 764.89 = **1.19 pt** (passes 0–12 pt).
- Rendered at 80 dpi and checked: no clipping, overlap, or empty bottom strip. NB 1 and NB 6 end in short lines of two to five words.
