# Selection — Notion, Software Engineer, Early Career

Template: `2026-09-30-roblox-software-engineer-early-career-2027/resume.tex` (the newest general early-career SWE resume), retuned for Notion.

## NewsBreak title

**Software Engineering Intern** (the default). The JD is "Software Engineer, Early Career" with team matching across product features, AI, growth, and platform. No specialty wins, and the JD does not use "SWE".

## Header

Mountain View, CA. The role is in San Francisco (Bay Area).

## Items used

- **nb-fastapi-backend** + **nb-eks-standup** + **nb-ownership**: backend from the first commit, 89 endpoints on AWS EKS, ~1,450 offline tests, CI gate, 344 PRs. Maps to "plan, build, and ship" and "code quality".
- **nb-swiftui-app** + **nb-morning-digest**: sole SwiftUI engineer, ~6,000 installs, 1,119 peak DAU, Firebase auth, 72-event Amplitude catalog, LLM morning digest viewed by 5,026 users (~81%). Maps to "features used by millions", "activation/retention", "AI features", and partnering with data.
- **nb-agentic-search**: hybrid retrieval (substring, full-text, vector, RRF), bounded tool loop, SSE, citations, 0% → 100% P@1. Maps to "AI and automation" and the Elasticsearch nice-to-have (search relevance), without claiming Elasticsearch.
- **nb-llm-pipeline**: CronJob pipeline, 4,100+ shadow decisions, filler 34% → 4%. Maps to "run experiments … iterate based on insights".
- **nb-catalog-cache**: fan-out → one call, 78× smaller shared cache, AI coding agent wrote the cache and he tested it. Maps to "performance" and the JD's Cursor / Claude Code line.
- **nb-cronjob-outage** + **nb-llm-failure**: maps to "reliability" and "platform and infrastructure".
- **hd-lead-mvp** + **hd-mentor-process**, **hd-langchain-apis**: React / Next.js (JD stack), team norms and PR reviews, REST APIs.
- **za-mock-interview** + **za-auth-db**, **za-demos-contracts**: React / Next.js / PostgreSQL (JD stack); second line reworded to lead with "iterated … from user-testing sessions and fast client feedback" for the JD's "iterate based on … customer feedback".
- **pj-my-av**, **ld-ece-fellow**, **pj-wisconsin-autonomous**: fill.
- Coursework: CMU Distributed Systems, LLM Systems, Machine Learning; UW Algorithms, Data Structure & Programming III, Operating Systems, Software Engineering (JD: "data structures, algorithms, and distributed systems").
- Skills: row 1 Languages led by TypeScript, JavaScript, Python, SQL; row 2 Frameworks & Data led by React, Next.js, Express, then PostgreSQL. Matches the JD stack (React, TypeScript, Node.js, Postgres).

## Items skipped

- **cm-psc / cm-nl-safety**: JD does not ask for research; page is full.
- **nb-server-driven-ui**, **nb-app-store**, **nb-live-activities**, **nb-ads-max**, **nb-third-party-proxy**, **nb-retired-detector**, **nb-manual-broadcast**, **nb-jira-process**, **nb-dramabreak-***, **nb-coaching-marketplace**: lower value or no room.
- "guest-first" (Firebase auth) and "personalized" (digest) were cut from the iOS bullet for length.

## Constraints nearly violated

- First build spilled 3 lines onto page 2 (CMU coursework wrapped, iOS bullet at 3 lines, Frameworks row wrapped). Swapped "Data Science for Software Engineering" for "Machine Learning", shortened the iOS bullet, and dropped Tailwind CSS from the Frameworks row.
- JD lists Node.js and Elasticsearch; neither is in `inventory/skills.md`, so neither was added. Express (in inventory) is listed instead.
- Margins, font size, and the template's `itemsep=0.7pt` are unchanged.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax): **755.49 pt** from the top.
- Unused height: 792 − 25.92 − 755.49 = **10.59 pt** (passes 0–12 pt).
- Rendered the full page at 90 dpi and inspected it: no clipping, overlap, cramped text, or empty bottom strip.

## Referral notes

No job ID in the posting (the Ashby URL holds only a UUID), so ` ([Job ID])` is dropped. Role shortened to "SWE Early Career". Default pitch. Why-this-team names two areas the JD lists (AI and growth/activation).
