# Selection — Roblox, [2027] Software Engineer, Early Career (37483)

Template: `2026-09-29-google-software-engineer-early-career-campus/resume.tex` (the closest general early-career SWE posting), retuned for Roblox.

## NewsBreak title

**Software Engineering Intern** (the default). The JD is a general "Software Engineer, Early Career" posting with placement by team matching across Infra, Engine, Search & Discovery, Foundational AI, and Economy. No single specialty wins, and the JD does not use "SWE", so the full default title is printed.

## Header

Mountain View, CA. The role is at the San Mateo HQ, which is in the Bay Area.

## Items used

- **nb-fastapi-backend** + **nb-eks-standup** + **nb-ownership**: FastAPI / MongoDB from the first commit, 89 endpoints on AWS EKS, ~1,450 offline tests, ruff / pyright / pytest gate, 344 PRs (340 merged). Covers "full development lifecycle from initial design to production deployment" and "coding standards".
- **nb-swiftui-app**: sole SwiftUI engineer, ~6,000 installs, 1,119 peak DAU, Firebase auth, 72-event Amplitude catalog, 74 typed emit methods, server-side allowlist. Swift is in the JD's language list, and the analytics catalog matches the JD's "2 trillion analytics events a day".
- **nb-agentic-search**: hybrid retrieval with RRF, bounded tool loop (≤3 hops, 45 s), SSE, server-resolved citations, 0% → 100% P@1. Matches the JD's "LLMs" and the Search & Discovery team.
- **nb-llm-pipeline**: LLM news-alert pipeline as a Kubernetes CronJob, 4,100+ shadow decisions, filler 34% → 4%. Matches "experiment with … LLMs" and the Foundational AI team.
- **nb-catalog-cache**: fan-out → one call, shared cache 78× smaller, 512 MiB pod, AI agent wrote the code and he wrote tests for it. Matches "distributed systems … at scale".
- **nb-cronjob-outage** + **nb-llm-failure**: 5-day CronJob outage fixed with paired deadlines; 65% LLM failure rate traced through Langfuse. Matches "support the continuous evolution of our distributed systems" and Infra.
- **hd-lead-mvp** + **hd-mentor-process**, **hd-langchain-apis**: two Haddee lines (cross-functional work, the full lifecycle, and REST APIs).
- **za-mock-interview** + **za-auth-db**, **za-demos-contracts**: two ZenAI lines.
- **pj-my-av** (short / pipeline fusion): the ML-frameworks line (PyTorch).
- **ld-ece-fellow**, **pj-wisconsin-autonomous**: fill.
- Coursework: CMU Distributed Systems, Machine Learning, LLM Systems; UW Algorithms, Data Structure & Programming III, Operating Systems.
- Skills: row 1 is Languages, reordered so the JD's languages come first (Python, Go, Java, Swift). Row 2 is renamed "ML & LLMs" and moved up for the JD's "machine learning frameworks and LLMs". Systems & Cloud follows.

## Items skipped

- **cm-psc / cm-nl-safety** (research): the JD does not ask for research, and the page is full without it. The Google layout, which drops research, fit better.
- **nb-third-party-proxy**: this replaced the Google resume's second clause in the iOS bullet. For Roblox, the analytics-catalog clause maps to the JD's analytics-events scale.
- **nb-retired-detector, nb-ads-max, nb-app-store, nb-live-activities, nb-server-driven-ui, nb-dramabreak-*, nb-jira-process, nb-coaching-marketplace, nb-manual-broadcast, nb-morning-digest**: lower value for this JD, and there was no room.
- "~1,200 LLM calls/day" was dropped from the pipeline bullet for length (see below).

## Constraints nearly violated

- The first build spilled one line onto page 2 because the pipeline bullet wrapped to three lines. I dropped "~1,200 LLM calls/day", which still wrapped, then changed "Designed and shipped" to "Shipped", which brought it to two lines and one page.
- The template's local `\setlist*[itemize]{itemsep=0.7pt}` (shared default 0.5 pt) is kept unchanged from the Google/Visa resumes. Margins and font size are unchanged.
- The JD lists C#, Lua, Node.js, Ruby, and C++. None of them is in `inventory/skills.md`, so none was added.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax): **755.49 pt** from the top.
- Unused height: 792 − 25.92 − 755.49 = **10.59 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, or empty bottom strip.

## Referral notes

The role is shortened to "SWE Early Career", with job ID 37483 (Roblox's own ID, not the Greenhouse gh_jid 8072244). The notes use the default pitch. The why-this-team line names two teams the JD lists for team matching. It claims no team details.
