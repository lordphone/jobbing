# Selection — Affirm, Software Engineer I, Fullstack (Search)

Started from the 2026-10-07 Affirm Early Career (SF) resume (same company, near-identical "What We Look For") and retargeted it to Search and full-stack.

## NewsBreak title

**Full-Stack Engineer Intern** — the posting title is "Fullstack (Search)" and asks for JS/TS plus Python backend.

Header city: Mountain View, CA (Remote US; Bay Area allowed).

## JD keywords

Search (Ads, Marketplace); JavaScript/TypeScript; backend systems at scale in Python or Kotlin; solutions across multiple software components; clear, well tested, extensible code; navigating a large code base; debugging others' code; code reviews; protecting systems from downtime; written communication.

## Items used

- **nb-agentic-search** → NB 1: hybrid retrieval (substring + Mongo `$text` + bge vector, RRF, recency decay), degrade to surviving legs, entity resolver 0% → 100% P@1 on real logged zero-result queries at 0.4 ms, one SSE answer endpoint, server-resolved citations (model cannot author a URL). (Search team.)
- **nb-fastapi-backend** → NB 2: first commit, Python/FastAPI/MongoDB, 89 REST endpoints, 27 routers, ~1,450 offline tests, 1:1 line ratio, ruff/pyright/pytest gate. ("Python", "well tested and extensible code")
- **nb-catalog-cache** → NB 3: 25–30 request fan-out → 1 backend call, per-user cache with structurally-zero hit rate re-keyed to shared 10.9 MB, 78×, 512 MiB pod. ("backend systems at scale", multiple components)
- **nb-eks-standup + nb-cronjob-outage** → NB 4: EKS day 3 (Docker, Helm, Jenkins), stale ArgoCD app, 5-day silent CronJob outage, paired deadlines. ("protecting our systems from downtime")
- **nb-llm-failure + nb-dramabreak-ads (codebase facts) + nb-dramabreak-stripe** → NB 5: another team's 1,661-commit repo, 65% failure rate, Langfuse; Stripe checkout, signature-verified idempotent webhook, mature codebase. ("navigating a large code base, debugging others' code"; payments domain)
- **nb-ownership + nb-swiftui-app + nb-server-driven-ui + nb-jira-process** → NB 6: sole SwiftUI / primary backend, SportsBreak link, ~6,000 installs, peak DAU 1,119; server-driven UI over 27 widget types incl. search sections, no App Store release, unknown kinds drop; 344 PRs / 340 merged; 34 contract-first specs; onboarded next engineer. (Full-stack; written communication.)
- **hd-lead-mvp + hd-langchain-apis** → Haddee 1 (React / Next.js = JS/TS work experience). **hd-mentor-process** → Haddee 2 (led PR reviews = "code reviews").
- **za-mock-interview + za-auth-db** → ZenAI 1 (React / Next.js). **za-auth-db (user-testing iteration) + za-demos-contracts** → ZenAI 2 (seeking feedback, stakeholders).
- **pj-codingplans**, **pj-my-av**, **ld-ece-fellow** — fill.
- Skills: TypeScript / JavaScript lead the Languages row; "Full-Stack & Search" row adds hybrid retrieval and RRF. Kotlin is not in inventory, so not listed. Certifications row kept.
- Coursework: CMU Distributed Systems, Foundations of SE, Software Refactoring; UW Software Engineering, Algorithms, Data Structure & Programming III, Operating Systems.

## Skipped

- nb-llm-pipeline — ranking-adjacent, but the six NB slots went to search, testing, scale, uptime, and large-codebase work.
- nb-third-party-proxy, nb-observability, nb-morning-digest, nb-retired-detector, nb-live-activities, nb-ads-max, nb-app-store, nb-manual-broadcast, nb-coaching-marketplace, nb-cross-dept — lower fit or no room.
- Research (cm-psc, cm-nl-safety), pj-wisconsin-autonomous, pj-cs537-os — off JD; page full without them.
- Machine Learning (CMU coursework) — cut to stop a one-word wrap.

## Constraints nearly violated

- nb-llm-failure: "helped debug", no post-deploy confirmation — bullet says "Debugged" and claims no fix outcome.
- Code reviews are claimed only from Haddee (led PR reviews), not NewsBreak.
- "Shipped search" — nb-agentic-search shipped 2026-08-07; the bullet claims retrieval, resolver, and endpoint facts only.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, ECE Fellow line): **765.56 pt** from the top.
- Unused height: 792 − 25.92 − 765.56 = **0.52 pt** (passes 0–12 pt).
- Rendered at 90 dpi and inspected: no clipping, overlap, or empty bottom strip; no one-word orphan lines.
