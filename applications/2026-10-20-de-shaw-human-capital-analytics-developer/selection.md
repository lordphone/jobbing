# Selection — D. E. Shaw, Human Capital Analytics Developer

Started from the 2026-10-19 Affirm resume and retargeted it to Python reporting, dashboards, data pipelines, troubleshooting, and Git/GitHub collaboration.

## NewsBreak title

**Full-Stack Engineer Intern** — "This role combines full stack development with data analysis."

Header city: New York, NY (posting is New York only, no Bay option).

## JD keywords

Python (reporting, package maintenance, robust and well-documented code); SQL; GraphQL; dashboards for senior leadership; ETL pipelines; troubleshooting; process improvements; Git/GitHub and code review; ad hoc analyses; confidential information; generative AI; communication; advanced analytics / data science.

## Items used

- **nb-fastapi-backend** → NB 1: Python FastAPI / MongoDB, first commit, 89 REST endpoints, 27 routers, ~1,450 offline tests, 99.7% annotation coverage, ruff / pyright / pytest gate. ("Python packages … robust")
- **nb-observability + nb-swiftui-app (analytics catalog) + nb-dramabreak-ads (A/B test)** → NB 2: Prometheus + Grafana dashboards on EKS, 72-event Amplitude catalog, server-side allowlist, A/B test read on click-through. ("dashboards", "reporting")
- **nb-llm-pipeline** → NB 3: personalized LLM alert pipeline (ingest → embed → score → select → dedupe), decision log row per item, 4,100+ rows, hand-graded alerts, production shadow, filler 34% → 4%. ("ETL pipelines", "ad hoc analyses", "generative AI")
- **nb-agentic-search + nb-third-party-proxy** → NB 4: agentic search, server-resolved citations, conversation state client-held (no PII at rest); nine integrations server-side, zero API credentials in the binary. ("confidential information with discretion", "generative AI")
- **nb-llm-failure + nb-cronjob-outage** → NB 5: 65% failure rate in another team's LLM pipeline via Langfuse, token cap sized against p95; 5-day silent CronJob outage, paired deadlines. ("troubleshoot technical issues")
- **nb-ownership + nb-swiftui-app + nb-jira-process** → NB 6: sole SwiftUI / primary backend, SportsBreak link, ~6,000 installs, peak DAU 1,119, 344 PRs (340 merged), Jira backlog, 34 contract-first API specs, ~10,000 lines of docs, onboarded next engineer. ("Git and GitHub", "well-documented", "process improvements", communication)
- **hd-lead-mvp + hd-langchain-apis** → Haddee 1. **hd-mentor-process** → Haddee 2 (PR reviews, Git workflows = "code review processes").
- **za-mock-interview + za-auth-db** → ZenAI 1 (PostgreSQL / database interactions = SQL). **za-mock-interview (recruiters) + za-auth-db (user-testing) + za-demos-contracts** → ZenAI 2.
- **cm-nl-safety** (priors variant, shortened) → Research: multi-turn LLMs, formal safety specs, Bayesian priors. ("advanced analytics and data science", generative AI)
- **pj-codingplans**, **ld-ece-fellow** — fill.
- Skills: Python and SQL lead Languages; "Data & Analytics" row (PostgreSQL, MySQL, MongoDB, Grafana, Prometheus, Amplitude, NumPy, Langfuse). Git and GitHub Actions in row 3. Certifications row kept.
- Coursework: CMU Data Science for Software Engineering, Machine Learning, Large Language Model Systems; UW Software Engineering, Algorithms, Large Language Models in Practice, Operating Systems.

## Skipped

- GraphQL — not in inventory; not listed.
- nb-catalog-cache, nb-eks-standup — infra/perf; slots went to dashboards, analysis, and troubleshooting.
- nb-server-driven-ui, nb-live-activities, nb-ads-max, nb-app-store, nb-manual-broadcast, nb-morning-digest, nb-retired-detector, nb-dramabreak-stripe, nb-coaching-marketplace, nb-cross-dept — lower fit or no room.
- pj-my-av — cut to fit one page (ECE Fellow line was spilling to page 2).
- cm-psc, pj-wisconsin-autonomous, pj-cs537-os — off JD.

## Constraints nearly violated

- A/B test was on DramaBreak and the winner / lift / sample size are not recorded — the bullet says only that it ran, on click-through.
- nb-llm-failure: "helped debug", no post-deploy confirmation — bullet says "Troubleshot" and claims no fixed outcome.
- Prometheus collected metrics from the EC2 nodes under EKS; which metrics / dashboards are not recorded — bullet claims none.
- Code reviews are claimed only from Haddee (led PR reviews).

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, ECE Fellow line): **758.44 pt** from the top.
- Unused height: 792 − 25.92 − 758.44 = **7.64 pt** (passes 0–12 pt).
- Rendered at 80 dpi and inspected: no clipping, overlap, or empty bottom strip; no one-word orphan lines.
