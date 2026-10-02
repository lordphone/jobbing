# Selection — Chicago Trading Company, Associate Engineer - 2027 Start

## NewsBreak title

**Software Engineering Intern** (default). The JD asks for "software engineers" building "trading tools and risk applications"; it is general SWE, not backend-, infra-, or AI-specific.

## JD signals

- "data structures, algorithms, and multi-threading concepts" → Algorithms / Data Structure & Programming III / Operating Systems coursework; cache redesign with copy-time numbers; deterministic entity resolution.
- "distributed real-time systems" → Distributed Systems coursework; Kubernetes / CronJob work; failure-tolerant hybrid retrieval.
- "designing, coding, and testing" → ~1,450 offline tests, ruff / pyright / pytest gate; Practices row moved up.
- "Java, C++, or Python" / "object oriented programming language" → Languages row led by Python, Java.
- "analytical skills" → binomial model on the LLM failure rate; shadow calibration.

Header: **Mountain View, CA**. The posting is Chicago / New York only, with no Bay option, so the default applies.

## Items used

- **nb-fastapi-backend + nb-ownership**: first commit → 89 endpoints, 26 collections, ~1,450 fully offline tests (0.17 s), ruff / pyright / pytest gate, 344 PRs.
- **nb-catalog-cache**: 13.2 MB per user → 10.9 MB shared, 78×, 512 MiB pod; home-load copy 9.0 ms → 0.89 ms (shallow vs. deep copy).
- **nb-llm-pipeline**: ingest → embed → LLM-score → dedupe → push, ~2 min ingest-to-decision, 4,100+ shadow decision rows, filler 34% → 4% by count, 2/day cap held over 11,745 user-days.
- **nb-eks-standup + nb-cronjob-outage** (fused).
- **nb-agentic-search**: 0% → 100% P@1, span-based entity resolution, 0.4 ms, 206-entity catalog; hybrid retrieval (RRF) degrading to surviving legs.
- **nb-llm-failure**: 65% via Langfuse, p95 1,197 vs. 16,384, binomial 49–66% vs. 65%.
- **nb-swiftui-app**: sole SwiftUI engineer, App Store link on "SportsBreak", ~6,000 installs, 1,119 peak DAU.
- **hd-lead-mvp (agile) + hd-mentor-process (PR reviews) + hd-langchain-apis (schemas, REST APIs)**: fused; collaboration and team signal.
- **za-mock-interview + za-auth-db** (fused).
- **cm-psc + cm-nl-safety**: fill; stochastic systems / Bayesian estimation is loosely relevant to pricing and risk curiosity.
- **pj-my-av**, **pj-wisconsin-autonomous**.
- Coursework: CMU Distributed Systems, Foundations of SE, Machine Learning; UW Algorithms, Data Structure & Programming III, Operating Systems.

## Items skipped

- **nb-third-party-proxy**, **nb-server-driven-ui**, **nb-app-store**, **nb-live-activities**, **nb-ads-max**, **nb-morning-digest**, **nb-manual-broadcast**, **nb-dramabreak-***, **nb-coaching-marketplace**: mobile / product work, weaker for trading systems.
- **nb-retired-detector**, **nb-jira-process**, **za-demos-contracts**: no room.
- **ld-ece-fellow**, **pj-codingplans**: no room; projects kept for systems signal.
- Skills dropped: HTML, CSS, Express, Tailwind, Firebase, Supabase, mobile tooling, Terraform, NGINX, Grafana, Jira, certifications.

## Constraints almost violated

- C++ and "multi-threading" are in the JD, but inventory has no C++ and no multithreading claim. I did not claim either; the only concurrency facts are asyncio / Kubernetes ones.
- I first called the alert pipeline "real-time", then removed the word: a ~2 min latency is not real-time in a trading reader's sense.
- The first compile was 2 pages because UW coursework wrapped. Dropping Computer Architecture fixed it.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 792 pt tall)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 761.86 pt
- Unused height: 792 − 25.92 − 761.86 = 4.22 pt (passes 0–12 pt)
- Visual review: rendered at 110 dpi; no empty bottom strip, clipping, or overlap; spacing even.
