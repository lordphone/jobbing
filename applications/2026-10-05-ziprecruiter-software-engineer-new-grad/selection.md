# Selection — ZipRecruiter, Software Engineer - New Grad

## NewsBreak title

**Software Engineering Intern** — general "Software Engineer - New Grad" posting spanning Big Data / Full Stack / ML; no single specialty title fits better. JD doesn't say "SWE", so the full title is printed.

Header city: Mountain View, CA (Santa Monica-only posting, no Bay option → default).

## Items used

- **nb-fastapi-backend** → bullet 1: first commit, Python/FastAPI/MongoDB, 89 endpoints, 27 routers, 26 collections, ~1,450 offline tests, 1:1 line ratio, ruff/pyright/pytest gate. (JD: "write, test… with good test coverage", non-relational DB.)
- **nb-eks-standup + nb-cronjob-outage** (fused) → bullet 2: EKS day 3, Helm, Jenkins, 7 CronJobs, two-stage amd64 image; 5-day silent CronJob outage fixed with paired deadlines. (JD: "deploy… to our Kubernetes environment".)
- **nb-server-driven-ui + nb-catalog-cache** (fused) → bullet 3: 27 widget types, no App Store release needed; 25–30 → 1 call; 10.9 MB shared cache, 78×. (Full stack / scale.)
- **nb-agentic-search** → bullet 4: hybrid retrieval (substring/keyword, Mongo $text/full-text, bge, RRF), bounded tool loop, SSE, server-resolved citations, 100% P@1 on real logged queries. (ML / matching.)
- **nb-llm-pipeline** → bullet 5: personalized pipeline embed → score → judge → push; 4,100+ shadow decisions; filler 34% → 4%. (Personalization/matching, ML.)
- **nb-ownership + nb-swiftui-app + nb-jira-process** → bullet 6: sole SwiftUI engineer, SportsBreak link, ~6,000 installs, peak DAU 1,119, primary backend author, 344 PRs/340 merged, 34 specs, ~10,000 lines docs, onboarded next engineer.
- **hd-lead-mvp + hd-langchain-apis** → Haddee 1: 8 interns, Agile, React/Next.js/FastAPI/Supabase, 0→1, GCP App Engine; schemas + REST APIs for resume parsing and AI job matching (directly on ZipRecruiter's domain).
- **hd-mentor-process** → Haddee 2.
- **za-mock-interview + za-auth-db** → ZenAI 1 (React, PostgreSQL — relational DB pairing with MongoDB above).
- **za-demos-contracts** → ZenAI 2 (recruiter collaboration — hiring domain).
- **pj-my-av** (short) → ML project for the ML archetype.
- **ld-ece-fellow** → leadership.
- Skills: Languages row leads with JD's examples (Python, Java, Go, JavaScript); second row Full Stack & Data has React, HTML/CSS (row 1), relational + non-relational DBs; Kubernetes first in Cloud row.
- Coursework: CMU Distributed Systems, Machine Learning, Data Science for SE, Foundations of SE (Big Data / ML / SE); UW Software Engineering, Algorithms, Operating Systems, LLMs in Practice.

## Skipped

- nb-third-party-proxy, nb-dramabreak-stripe — good full-stack items but no room once K8s and ML bullets were in.
- nb-llm-failure, nb-retired-detector — debugging/LLM depth; lower value than the deploy and matching bullets here.
- nb-live-activities, nb-ads-max, nb-app-store, nb-morning-digest, nb-manual-broadcast, nb-dramabreak-ads, nb-coaching-marketplace — mobile/ads detail.
- pj-codingplans — cut to fit one page (first draft spilled 3 lines).
- Research (cm-psc, cm-nl-safety), pj-wisconsin-autonomous — off JD; page already full.

## Constraints nearly violated

- First compile ran to 2 pages; dropped codingplans and shortened the Haddee bullet ("database schemas" → "schemas") to remove a one-word widow.
- C++ is in the JD's language list but not in `inventory/skills.md` — not added.
- No Big Data tools (Spark, Hadoop, etc.) in inventory — none added.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, ECE Fellow line): **765.56 pt** from the top.
- Unused height: 792 − 25.92 − 765.56 = **0.52 pt** (passes 0–12 pt).
- Rendered at 90 dpi and inspected: no clipping, overlap, or empty bottom strip. A few short last lines ("pytest CI gate.", "per-user key.", "Supabase") but no layout defect.
