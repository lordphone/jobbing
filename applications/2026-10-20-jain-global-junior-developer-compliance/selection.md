# Selection — Jain Global, Junior Developer, Compliance

Started from the 2026-10-20 D. E. Shaw resume (also NYC, Python/SQL) and retargeted it to compliance alerts, data feeds, auditability, production code, on-call, Docker / CI/CD, and AWS.

## NewsBreak title

**Backend Engineer Intern** — the responsibilities are all services and data: "Develop and maintain data feeds", "Maintain critical compliance alerts", "REST APIs, and SQL". The JD never says full-stack; React / TypeScript is covered by Haddee and ZenAI.

Header city: New York, NY (New York or London; no Bay option).

## JD keywords

Python; React / TypeScript; REST APIs; SQL; Snowflake; AWS RDS / Postgres / MySQL; Git; committing code into production; data feeds; compliance alerts, escalation, auditability; data standardization / enrichment / integrations; translating policies into controls with Legal & Compliance; on-call for critical systems; AWS; Docker; CI/CD; analytical / problem-solving / communication.

## Items used

- **nb-fastapi-backend** → NB 1: Python FastAPI / MongoDB, first commit, 89 REST endpoints, 27 routers, production, ~1,450 offline tests, ruff / pyright / pytest CI gate. ("committing code into production", Python, REST)
- **nb-llm-pipeline** → NB 2: ingest → score → select → dedupe → notify; decision log one row per item with why it fired or not; 4,100+ rows in production shadow; filler 34% → 4%; 2/day cap held over 11,745 user-days with zero violations. ("compliance alerts", "auditability", "controls")
- **nb-third-party-proxy + nb-dramabreak-stripe** → NB 3: nine third-party integrations server-side (SportsDataIO, YouTube, SerpApi, DeepInfra LLM, APNs named), zero API keys in the binary; Stripe checkout with signature-verified, idempotent webhook. ("data feeds", "integrations")
- **nb-eks-standup + nb-observability + nb-cronjob-outage** → NB 4: production EKS on day 3 (Docker image, Helm, Jenkins, 7 CronJobs), Prometheus and Grafana, 5-day silent CronJob outage fixed with paired job / scheduler deadlines. ("on-call for critical systems", AWS, Docker, CI/CD)
- **nb-llm-failure + nb-jira-process (audit)** → NB 5: 65% failure rate in another team's LLM pipeline via Langfuse; audited two closed security tickets against the code, found fixes absent, reopened with line-level evidence. ("problem-solving", control verification)
- **nb-ownership + nb-swiftui-app + nb-cross-dept + nb-jira-process** → NB 6: primary backend author, sole SwiftUI engineer, SportsBreak link, ~6,000 installs, 344 PRs (340 merged), worked with legal on launch guidance, 34 API specs, onboarded the next engineer. ("Work closely with ... Legal & Compliance", Git)
- **hd-lead-mvp + hd-langchain-apis** → Haddee 1 (React, REST APIs, schemas). **hd-mentor-process** → Haddee 2.
- **za-mock-interview + za-auth-db** → ZenAI 1 (React, PostgreSQL, database interactions = SQL). **za-mock-interview + za-auth-db + za-demos-contracts** → ZenAI 2.
- **cm-nl-safety** (priors variant, shortened) → Research: natural-language instructions → formal specs, a loose parallel to "translate policies ... into technical workflows and controls".
- **pj-codingplans**, **ld-ece-fellow** — fill.
- Skills: Python, TypeScript, SQL lead Languages; row 2 has REST APIs, PostgreSQL, MySQL, React; row 3 has AWS, Docker, CI/CD, Git; Monitoring row (Prometheus, Grafana, Langfuse, Amplitude, pytest, ruff, pyright) backs the alerts / on-call ask. Certifications row kept.
- Coursework: CMU Distributed Systems, Data Science for Software Engineering, Machine Learning; UW Software Engineering, Algorithms, Operating Systems, Data Structure & Programming III.

## Skipped

- Snowflake, AWS RDS — not in inventory; not listed.
- Trading platforms / order and execution data — no inventory facts.
- nb-catalog-cache, nb-agentic-search, nb-server-driven-ui, nb-live-activities, nb-ads-max, nb-app-store, nb-manual-broadcast, nb-morning-digest, nb-retired-detector, nb-dramabreak-ads, nb-coaching-marketplace — lower fit for compliance data / alerts or no room.
- pj-my-av, cm-psc, pj-wisconsin-autonomous, pj-cs537-os — off JD.

## Constraints nearly violated

- nb-cross-dept: what legal advised and his exact part are not recorded — bullet says only "worked with legal on launch guidance".
- nb-llm-failure: helped debug, no post-deploy confirmation — bullet says "Diagnosed" and claims no fix outcome.
- nb-observability: which metrics / dashboards are not recorded — bullet names only Prometheus and Grafana.
- "data integrations" names five of the nine integrations from the inventory list (DeepInfra shown as "LLM").

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, ECE Fellow line): **759.05 pt** from the top.
- Unused height: 792 − 25.92 − 759.05 = **7.03 pt** (passes 0–12 pt).
- Rendered at 80 dpi and inspected: no clipping, overlap, or empty bottom strip; no one-word orphan lines.
