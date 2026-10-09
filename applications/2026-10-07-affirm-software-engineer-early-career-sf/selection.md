# Selection — Affirm, Software Engineer, Early Career (SF)

Started from the 2026-10-05 Affirm intern resume (same company, overlapping JD) and retargeted the NewsBreak bullets to this JD.

## NewsBreak title

**Software Engineering Intern** — general "Software Engineer, Early Career" posting with teams matched across stacks. JD doesn't say "SWE", so the full title is printed.

Header city: Mountain View, CA (SF posting; NYC is the other office).

## JD keywords

Solutions that interact with multiple software components; clear, well tested, extensible code; navigating a large code base; debugging others' code; code reviews; protecting systems from downtime; visibility into risks and trade-offs; written communication; seeking feedback.

## Items used

- **nb-fastapi-backend** → NB 1: first commit, Python/FastAPI/MongoDB, 89 REST endpoints, 27 routers, ~1,450 offline tests, 1:1 line ratio, ruff/pyright/pytest gate. ("well tested and extensible code")
- **nb-eks-standup + nb-cronjob-outage** → NB 2: EKS on day 3, Helm, Jenkins, 7 CronJobs, stale ArgoCD app, 5-day silent outage fixed with paired deadlines. ("protecting our systems from downtime")
- **nb-llm-failure** → NB 3: another team's pipeline, 1,661-commit repo, 65% failure rate, Langfuse traces, unbounded reasoning loop, Helm env shadowing code default, cap sized against p95 (1,197). ("navigating a large code base, debugging others' code")
- **nb-dramabreak-ads (codebase facts) + nb-dramabreak-stripe** → NB 4: mature two-repo codebase, 20 PRs / 19 merged, Stripe web checkout, signature-verified webhook as only trusted fulfillment, idempotent with stale-pending reclaim. (Large codebase + payments, Affirm's domain.)
- **nb-llm-pipeline** → NB 5: K8s CronJob, production shadow on 4,100+ decisions, filler 34% → 4%. (Speed vs. quality: shadow before going live.)
- **nb-jira-process** → NB 6: 34 contract-first API specs, ~10,000 lines of docs, reopened two closed security tickets with line-level evidence. (Written communication; surfacing risk.)
- **nb-ownership + nb-swiftui-app** → NB 7: sole SwiftUI engineer, SportsBreak link, ~6,000 installs, peak DAU 1,119, 344 PRs / 340 merged, onboarded next engineer.
- **hd-lead-mvp + hd-langchain-apis** → Haddee 1. **hd-mentor-process** → Haddee 2 (PR reviews = "feedback through code reviews").
- **za-mock-interview + za-auth-db** → ZenAI 1. **za-demos-contracts** → ZenAI 2 (stakeholder communication).
- **pj-my-av**, **pj-codingplans**, **ld-ece-fellow** — fill.
- Skills: kept the intern resume's rows (Python/Java first; Testing & Practices row covers testing and code-review practice). Certifications row kept.
- Coursework: CMU Distributed Systems, Foundations of SE, Machine Learning; UW Software Engineering, Data Structure & Programming III, Algorithms, Operating Systems.

## Skipped

- nb-third-party-proxy, nb-catalog-cache — used on the intern resume; displaced by debugging / large-codebase bullets that hit this JD harder.
- nb-agentic-search, nb-retired-detector, nb-morning-digest — LLM depth; JD isn't AI-focused.
- nb-server-driven-ui, nb-live-activities, nb-ads-max, nb-app-store, nb-manual-broadcast, nb-coaching-marketplace, nb-observability — mobile/ads detail or lower fit.
- Research (cm-psc, cm-nl-safety), pj-wisconsin-autonomous — off JD; page already full.

## Constraints nearly violated

- nb-llm-failure says "helped debug" and has no post-deploy confirmation — bullet says "Debugged … sized a token cap" and claims no fix outcome.
- Did not claim code reviews at NewsBreak; the code-review fact comes from Haddee (led PR reviews).

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, ECE Fellow line): **754.13 pt** from the top.
- Unused height: 792 − 25.92 − 754.13 = **11.95 pt** (passes 0–12 pt).
- Rendered at 90 dpi and inspected: no clipping, overlap, or empty bottom strip.
