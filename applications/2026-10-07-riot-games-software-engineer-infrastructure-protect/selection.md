# Selection — Riot Games, Software Engineer, Infrastructure (Optimize & Protect)

## NewsBreak title

**Engineering Intern** — the JD is infrastructure ("infrastructure or tooling", "core infrastructure services", on-call / uptime / SLAs / RCAs), which the title list maps to the official title. Heading plain "NewsBreak" (no new-venture angle).

Header city: Mountain View, CA (JD is Los Angeles only; no New York / Canada rule applies → default).

## Items used

- **nb-eks-standup** → bullet 1 (production EKS day 3, Docker/Helm/Jenkins, DNS → TLS → admission-policy chain, public-domain fix) — JD: networking "HTTP down to … DNS", cloud + containers + orchestration. Bullet 2 (stale ArgoCD app pinned to v0.1.0 with prune/selfHeal; two-stage amd64 image, C extension SIGILL on arm64) — JD: Argo CD, CI/CD. Bullet 5 (GitHub Actions ruff/pyright/pytest gate added after two tests red on main, Jenkins only built the image). Bullet 6 (HPA min 2 / max 4).
- **nb-cronjob-outage** → bullet 3 (5-day silent outage, ImagePullBackOff + Forbid, paired deadlines; "fixed the mechanism") — JD: on-call, RCAs, uptime.
- **nb-llm-failure** → bullet 4 (65% failure rate, Langfuse, p95 1,197 vs 16,384, Helm env shadowing code default) — RCA. Says "root-caused", claims no post-deploy fix outcome.
- **nb-observability** → bullet 5 (Prometheus + Grafana on EKS; no metric/dashboard counts invented).
- **nb-catalog-cache** → bullet 6 (13.2 MB per-user → 10.9 MB shared, 78×, 512 MiB pod) — JD: efficiency/improvement opportunities.
- **nb-fastapi-backend** + **nb-third-party-proxy** → bullet 7 (89 endpoints, 7 CronJobs, ~1,450 offline tests 0.17 s; nine integrations server-side, zero API keys in the client) — "Protect"/secure operations, microservices.
- **nb-ownership** + **nb-swiftui-app** → bullet 8 (sole SwiftUI, primary backend, ~6,000 installs, peak DAU 1,119, 344 PRs / 340 merged).
- **hd-lead-mvp** + **hd-mentor-process** → Haddee (Agile sprints, GCP App Engine, PR reviews) — JD: agile, code reviews, full SDLC.
- **za-mock-interview** + **za-demos-contracts** → ZenAI.
- **pj-wisconsin-autonomous** (encoders variant) → first project — closest inventory fact to "software/firmware for hardware environments".
- **pj-my-av**, **pj-codingplans**, **ld-ece-fellow** → projects / leadership fill.
- Skills: Languages lead with Python, Go, Java, C (JD's OO language list); Cloud & Infra and CI/CD & Observability rows carry AWS, GCP, Kubernetes, Docker, Terraform, Linux, Jenkins, GitHub Actions, ArgoCD. All from `inventory/skills.md`. Certifications row kept.
- Coursework: CMU Distributed Systems, Foundations of SE, Software Refactoring; UW Operating Systems, Computer Architecture, Algorithms.

## Items skipped

- nb-llm-pipeline, nb-agentic-search, nb-retired-detector, nb-morning-digest — LLM product work; off an infra/network-protect JD.
- nb-swiftui-app detail, nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-dramabreak-*, nb-coaching-marketplace, nb-manual-broadcast — mobile/product.
- nb-jira-process — process; space better used on infra.
- hd-langchain-apis, za-auth-db — tried a second ZenAI line (za-auth-db); it overflowed the page by ~1 pt, so it was removed.
- cm-psc, cm-nl-safety — research off JD.
- UW "Data Structure & Programming III" — dropped to stop an orphan "III" wrap.
- Skills Kubernetes HPA, asyncio, pyright (pyright still in bullet 5) — dropped from skill rows to stop one-word wraps.

## Constraints nearly violated

- JD wants networking down to TCP/IP / routing; inventory only supports the DNS → TLS chain, so no TCP/IP or routing claim and no "networking" skill (not in skills.md).
- "Linux kernel / firmware" desired — not claimed; only Linux (skills.md) and the Wisconsin Autonomous encoder integration.
- Observability bullet does not invent dashboards, metrics, or alerts.
- Page fill: after the za-auth-db line overflowed, loosened itemsep 0.5 → 0.6 pt locally in resume.tex (the other list settings restated unchanged); margins and font size untouched.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, ECE Fellow line): **754.25 pt** from the top.
- Unused height: 792 − 25.92 − 754.25 = **11.83 pt** (passes 0–12 pt).
- Rendered at 90 dpi and inspected: no clipping, overlap, orphan wraps, or empty bottom strip.
