# Selection — Together AI, Software Engineer, New Grad (2027)

## NewsBreak title

**Software Engineering Intern** (default). The JD is a general "early career Software Engineer" role with team placement across ML, Platform, Infrastructure, and Inference, and its own words are "Software Engineer". AI Infrastructure Intern was considered because the company is AI infra, but the role itself is not scoped to infra. Bullets lean infra / LLM / performance instead.

Header: Mountain View, CA (SF on-site).

## Items used

- **nb-fastapi-backend + nb-ownership + nb-eks-standup**: FastAPI / MongoDB backend from first commit, 89 endpoints, AWS EKS, ~1,450 offline tests, ruff / pyright / pytest gate, 344 PRs (340 merged). Covers "own projects end to end", Git and collaborative workflows.
- **nb-llm-pipeline**: CronJob ingest → embed → LLM-score → dedupe → push, ~1,200 LLM calls/day, 4,100+ shadow decisions, filler 34% → 4%. Covers ML / inference teams.
- **nb-catalog-cache**: 25–30 → 1 call, shared cache 78× smaller, 512 MiB pod, home-load copy 9.0 ms → 0.89 ms via shallow copies. Covers "optimizing performance-critical code".
- **nb-agentic-search**: entity resolution 0.4 ms, 0% → 100% P@1, 206-entity catalog, hybrid RRF retrieval, ≤3-hop tool loop, SSE, server-resolved citations.
- **nb-llm-failure + nb-cronjob-outage**: 65% LLM failure rate traced via Langfuse to an unbounded reasoning loop (p95 1,197 vs 16,384 runaways); 5-day CronJob outage fixed with paired deadlines. Covers "debugging" and inference reliability.
- **nb-swiftui-app**: sole SwiftUI engineer, ~6,000 installs, 1,119 peak DAU, Firebase auth, 72-event catalog, server-side allowlist. Covers "customer-facing UIs". SportsBreak hyperlinked.
- **hd-lead-mvp + hd-mentor-process**: 8-intern team, 0→1 on GCP App Engine, user stories, PR reviews, mentoring on Git workflows and testing (JD: code reviews, Git).
- **hd-langchain-apis**: schemas and REST APIs for LangChain features (databases bonus).
- **za-mock-interview + za-auth-db**, **za-demos-contracts**: unchanged from the template.
- **pj-my-av**, **ld-ece-fellow**, **pj-wisconsin-autonomous**: projects / leadership fill.
- Coursework: CMU Distributed Systems, Large Language Model Systems, Machine Learning; UW Operating Systems, Algorithms, Computer Architecture (systems / fundamentals first).
- Skills: Languages lead with Python, Go, C (low-level to UI); row 2 Cloud & Infra (cloud platforms bonus); ML & LLMs row 3; Practices leads with Git.

## Items skipped

- **cm-psc / cm-nl-safety**: JD does not ask for research; page full.
- **nb-third-party-proxy, nb-server-driven-ui, nb-live-activities, nb-app-store, nb-ads-max, nb-retired-detector, nb-morning-digest, nb-manual-broadcast, nb-dramabreak-*, nb-jira-process, nb-coaching-marketplace**: lower value for this JD; no room.
- Dropped from the first draft to fit one page: "stood up on EKS on day 3", the 2,048-token cap detail, "personalized" on the alert pipeline, UW Data Structure & Programming III, Bash, and DeepSeek / DeepInfra in skills.

## Constraints nearly violated

- First compile spilled to two pages (orphan words on several bullets and wrapped skill rows); trimmed as above rather than touching spacing.
- No OSS contributions in inventory, so the JD's OSS bonus is not claimed.
- Template's local `\setlist*[itemize]{itemsep=0.7pt}` unchanged; margins and font size unchanged.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, "Jetson."): **755.49 pt** from the top.
- Unused height: 792 − 25.92 − 755.49 = **10.59 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, or empty bottom strip.

## Referral notes

Role shortened to "SWE New Grad". The posting text has no job ID (the Greenhouse URL number 5211582007 is a board ID, not printed in the JD), so none is used. Default pitch. The why-this-team line uses the JD's "400+ trillion tokens a month".
