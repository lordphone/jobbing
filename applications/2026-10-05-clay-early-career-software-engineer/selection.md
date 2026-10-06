# Selection — Clay, Early Career Software Engineer

## NewsBreak title

**Software Engineering Intern.** Posting title is "Early Career Software Engineer" (general SWE). The "What We're Looking For" section leans developer tooling / infrastructure / internal platforms, which could argue for Engineering Intern, but the role title and the full-stack + AI qualifications favor the default.

Header: New York, NY (posting is New York hybrid only; no Bay option).

## Items used

- **nb-fastapi-backend + nb-eks-standup (CI gate)**: built with AI coding tools, first commit → 89 endpoints, ~1,450 fully-offline tests (0.17 s), ruff / pyright / pytest gate added after two tests sat red on `main`. JD: "developer experience and engineering productivity", "clean, maintainable code", "AI will transform the software development lifecycle".
- **nb-eks-standup**: production EKS day 3 (Helm, Jenkins), 7 CronJobs, two-stage amd64 image, DNS → TLS → admission-policy chain, stale ArgoCD app. JD: "infrastructure, or internal platforms", AWS.
- **nb-cronjob-outage + nb-llm-failure**: 5-day silent CronJob outage fixed with paired deadlines; 65% LLM failure rate traced via Langfuse. JD: "decompose tricky problems", observability tools.
- **nb-llm-pipeline**: automated alert pipeline in one CronJob, production shadow, filler 34% → 4%. JD: "systems that automate complex workflows", AI enthusiast.
- **nb-agentic-search**: deterministic RAG over hybrid retrieval (keyword, full-text, bge embeddings, RRF), bounded tool-use agent, server-resolved citations, 100% P@1. JD: "LLMs, embeddings".
- **nb-swiftui-app + nb-ownership + nb-jira-process**: sole SwiftUI engineer (hyperlinked SportsBreak), ~6,000 installs, peak DAU 1,119, primary backend author, 344 PRs (340 merged), 34 contract-first API specs, ~10,000 lines of docs, onboarded the next engineer. JD: "owning systems end-to-end", "removing obstacles to productivity".
- **hd-lead-mvp (agile) + hd-langchain-apis**, **hd-mentor-process**: two lines; React, PR reviews, Git workflows, testing protocols. JD: React, collaboration.
- **za-mock-interview + za-auth-db**, **za-demos-contracts**: React / Next.js / PostgreSQL, recruiter-aligned scoring, client iteration. JD: "talking to customers", React, Postgres.
- **cm-nl-safety**: fill; multi-turn LLMs.
- **pj-codingplans**: AI enthusiast; tests LLM coding plans (AI in the SDLC).
- Coursework: CMU Large Language Model Systems, Distributed Systems, Foundations of Software Engineering; UW Software Engineering, Large Language Models in Practice, Operating Systems, Algorithms.
- Skills: Languages first (Python, TypeScript, JavaScript, SQL match the JD stack); Cloud & DevOps second (AWS, Terraform, Docker, CI/CD match the JD's AWS / IaC / deployment lists). PostgreSQL and Redis Streams in row three. Node.js, CircleCI, Playwright, Datadog, and the specific AWS services are not in skills.md, so left out.

## Items skipped

- **nb-catalog-cache**: strong infra fact but no room after the six NB bullets; would have repeated the backend bullet.
- **nb-third-party-proxy, nb-server-driven-ui, nb-live-activities, nb-app-store, nb-ads-max, nb-retired-detector, nb-manual-broadcast, nb-dramabreak-*, nb-coaching-marketplace, nb-morning-digest**: lower value for a dev-tooling / AI JD; no room.
- **cm-psc**: control theory, less relevant than cm-nl-safety.
- **pj-my-av, pj-wisconsin-autonomous, ld-ece-fellow**: less relevant; no room.

## Constraints nearly violated

- First compile spilled the Projects section to page 2: every NB bullet ran to a short third line. Tightened all six to two lines, which left ~28 pt empty, so added Research (cm-nl-safety) as fill.
- Node.js is in the JD stack but not in skills.md; not added (Express is listed and kept).
- "caught a stale ArgoCD app" compresses the inventory fact (stale app pinned to v0.1.0 that would have wiped Jenkins deploys); no outcome invented.
- Third-party LLM failure bullet says "traced a 65% LLM failure rate via Langfuse" — inventory: diagnosed via Langfuse traces in another team's pipeline.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, codingplans line): **759.54 pt** from the top.
- Unused height: 792 − 25.92 − 759.54 = **6.54 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, wrapped skill rows, or empty bottom strip.

## Referral notes

Role shortened to "Early Career SWE". No job ID (Ashby UUID is not a printed ID). Pitch: "I built the backend and CI for a 6K-install sports app." (shorter than the default; matches the JD's dev-tooling / infra emphasis). Why-this-team uses the JD's "building systems that improve how software gets built".
