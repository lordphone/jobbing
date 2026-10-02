# Selection — Voleon, Software Engineer - University Hire 2027

## NewsBreak title

**Backend Engineer Intern.** The posting title is generic "Software Engineer", but the requirements are backend three times over: "Demonstrated excellence in backend engineering via work with databases, large-scale data processing, highly available services" and "design, develop, and deploy a back-end application given design specs".

## Framing

JD keywords: Linux, performance, concurrency, correctness, Python / Java / Go / C, databases, large-scale data processing, highly available services, deploying a back-end, Kubernetes (Bazel is not in inventory, so it is not claimed; R and C++ are not claimed either).

- Correctness: offline test suite, ruff / pyright / pytest gate.
- Performance: cache 78×, entity resolution 0.4 ms.
- Concurrency: Forbid-concurrency CronJob outage.
- Availability: retrieval legs degrade to survivors instead of failing.
- Data processing: ingest → embed → score → dedupe → push pipeline.

Header: **Mountain View, CA**. The posting lists Berkeley, CA (Bay) alongside New York.

## Items used

- **nb-fastapi-backend + nb-ownership**: first commit → 89 endpoints, 26 collections, ~1,450 fully offline tests, ruff / pyright / pytest gate, 344 PRs.
- **nb-eks-standup + nb-cronjob-outage** (fused): production EKS / Helm / Jenkins on day 3, 7 CronJobs; 5-day silent outage (ImagePullBackOff + Forbid concurrency), fixed with paired job and scheduler deadlines.
- **nb-catalog-cache**: 13.2 MB per user → 10.9 MB shared, 78×, 512 MiB pod, 25–30 requests → 1 call.
- **nb-llm-pipeline**: ingest → embed → LLM-score → dedupe → APNs ("push"), ~1,200 LLM calls/day, 4,100+ shadow decision rows, filler 34% → 4% by count, 2/day cap held over 11,745 user-days.
- **nb-agentic-search**: hybrid retrieval (Mongo `$text` + vector, RRF), failing legs degrade to survivors, 0% → 100% P@1, 0.4 ms, rejected embeddings.
- **nb-llm-failure**: 65% via Langfuse, p95 1,197 vs. 16,384, binomial 49–66% vs. 65%.
- **nb-swiftui-app**: sole SwiftUI engineer, App Store link on "SportsBreak", ~6,000 installs, 1,119 peak DAU.
- **hd-lead-mvp + hd-langchain-apis** (fused).
- **za-mock-interview + za-auth-db** (fused; auth / session / DB fits the backend framing).
- **cm-psc + cm-nl-safety**: kept as fill; Voleon is AI/ML-research-heavy.
- **pj-my-av**, **pj-wisconsin-autonomous**.
- Coursework: CMU Distributed Systems, Data Science for SE, Machine Learning; UW Operating Systems, Algorithms, Computer Architecture.
- Skills: Languages row led by Python, Go, Java, C (JD list order); Cloud & Infra row led by Linux, Kubernetes. Databases moved to the front of Data & ML.

## Items skipped

- **nb-third-party-proxy**: first draft had it at the end of the SwiftUI bullet; cut to bring the page from 2 to 1 (lowest-value clause for this JD).
- **nb-retired-detector**, **nb-server-driven-ui**, **nb-app-store**, **nb-live-activities**, **nb-ads-max**, **nb-morning-digest**, **nb-manual-broadcast**, **nb-dramabreak-***, **nb-coaching-marketplace**: mobile / product work, weaker for a backend trading-platform role.
- **nb-jira-process**, **hd-mentor-process**, **za-demos-contracts**: process / sales; no room.
- **ld-ece-fellow**, **pj-codingplans**: no room; projects kept for systems / ML signal.
- Skills dropped: HTML, CSS, Express, Tailwind, Firebase, Supabase, mobile ad tooling, Terraform, NGINX, Grafana, Jira, certifications.

## Constraints almost violated

- Bazel, R, and C++ are in the JD but not in inventory; not claimed.
- First compile was 2 pages (Projects spilled); tightened four NewsBreak bullets to two lines (dropped ~48 indexes, 99.7% typed, 2–4 pod autoscaling, ~2 min ingest-to-decision, "non-terminal"), then still 1 line over, so dropped the nine-integrations clause.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 792 pt tall)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 761.86 pt
- Unused height: 792 − 25.92 − 761.86 = 4.22 pt (passes 0–12 pt)
- Visual review: rendered at 110 dpi; no empty bottom strip, clipping, or overlap; spacing even.
