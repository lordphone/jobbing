# Selection — Affirm, Software Engineer Intern (Summer 2027)

## NewsBreak title

**Software Engineering Intern** — general "Software Engineer Intern" posting with no specialty (team is matched later). JD doesn't say "SWE", so the full title is printed.

Header city: Mountain View, CA (San Francisco posting, remote-first → Bay).

## Items used

JD keywords: Python/Java, JavaScript/React, OOP, deployment and testing frameworks, API development/documentation, AWS/PaaS, "ship code and monitor the deployment", consumer finance.

- **nb-fastapi-backend** → NB 1: first commit, Python/FastAPI/MongoDB, 89 REST endpoints, 27 routers, ~1,450 offline tests, 1:1 line ratio, ruff/pyright/pytest gate. (Testing frameworks, API development, Python.)
- **nb-eks-standup + nb-cronjob-outage** → NB 2: production EKS on day 3, Helm, Jenkins, 7 CronJobs, stale ArgoCD app that would have wiped Jenkins deploys, 5-day silent CronJob outage fixed with paired deadlines. (Deployment, AWS, verifying work in production.)
- **nb-jira-process + nb-third-party-proxy** → NB 3: 34 contract-first API specs, ~10,000 lines of docs; nine integrations moved server-side, zero third-party credentials in the binary. (API documentation; security matters in fintech.)
- **nb-dramabreak-stripe** → NB 4: Stripe web checkout across backend + iOS, signature-verified webhook as only trusted fulfillment, idempotent, 60s stale-pending reclaim. (Payments — closest fact to Affirm's domain.)
- **nb-catalog-cache** → NB 5: 25–30 → 1 call, 10.9 MB shared cache, 78×, 512 MiB pod. (Fill; backend performance.)
- **nb-llm-pipeline** → NB 6: shipped as a K8s CronJob, production shadow on 4,100+ decisions before live, filler 34% → 4%. ("Verifying that it works in production"; JD mentions a data-processing pipeline.)
- **nb-ownership + nb-swiftui-app** → NB 7: sole SwiftUI engineer, SportsBreak link, ~6,000 installs, peak DAU 1,119, primary backend author, 344 PRs / 340 merged, onboarded next engineer (from nb-jira-process).
- **hd-lead-mvp + hd-langchain-apis** → Haddee 1 (React/Next.js web app, GCP App Engine PaaS, REST APIs).
- **hd-mentor-process** → Haddee 2 (testing protocols, PR reviews).
- **za-mock-interview + za-auth-db** → ZenAI 1 (React frontend web app, auth).
- **za-demos-contracts** → ZenAI 2 (communication).
- **pj-my-av** (short), **pj-codingplans** (shortened), **ld-ece-fellow**.
- Skills: Languages leads with Python, Java, JavaScript; Web & APIs row leads with React and REST APIs, includes Stripe; Cloud & Deploy leads with AWS; separate Testing row (pytest, Unit Testing, TDD).
- Coursework: CMU Distributed Systems, Foundations of SE, Machine Learning; UW Software Engineering, Data Structure & Programming III (OOP/C++-adjacent course), Algorithms, Operating Systems.

## Skipped

- nb-agentic-search, nb-llm-failure, nb-retired-detector — LLM depth; JD isn't AI-focused.
- nb-server-driven-ui, nb-live-activities, nb-ads-max, nb-app-store, nb-morning-digest, nb-manual-broadcast, nb-dramabreak-ads, nb-coaching-marketplace — mobile/ads detail.
- Research (cm-psc, cm-nl-safety), pj-wisconsin-autonomous — off JD.

## Constraints nearly violated

- First draft said "monitored my deploys in production" to echo the JD; not an inventory fact (the outage ran 5 days with no cron metrics). Replaced with the ArgoCD catch.
- C++, AngularJS, and OOP are in the JD but not in `inventory/skills.md` — not added.
- First compile spilled to 2 pages; second underfilled by ~67 pt. Trimmed widows (coursework, skills rows), then added nb-catalog-cache and pj-codingplans to fill.
- codingplans wording shortened ("expose nerfed caching and heavy quantization") to keep it to two lines; facts unchanged.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, ECE Fellow line): **754.13 pt** from the top.
- Unused height: 792 − 25.92 − 754.13 = **11.95 pt** (passes 0–12 pt).
- Rendered at 90 dpi and inspected: no clipping, overlap, or empty bottom strip. One short last line ("scalable code practices.") but no layout defect.
