# Selection — SeatGeek, Software Engineer - New Grad

Template: `2026-09-30-roblox-software-engineer-early-career-2027/resume.tex` (the closest general new-grad SWE posting), retuned for SeatGeek.

## NewsBreak title

**Software Engineering Intern** (the default). The JD is a general "Software Engineer - New Grad" posting with five tracks (Backend, Frontend Web, Mobile, Platform, ML) and placement by area of interest. No single track wins, and the JD does not say "SWE", so the full default title is printed.

## Header

New York, NY. The role is New York–only, in office at least 3 days a week, with no Bay Area option.

## Items used

- **nb-fastapi-backend** + **nb-eks-standup** + **nb-ownership**: Python FastAPI / MongoDB from the first commit, 89 endpoints on AWS EKS, ~1,450 offline tests, ruff / pyright / pytest gate, 344 PRs (340 merged). Covers Backend (Python), Platform (AWS), and "hold yourself and your code to a high standard".
- **nb-agentic-search**: moved to bullet 2 and rewritten to lead with entity resolution (206-entity catalog, 0.4 ms, 0% → 100% P@1 on real logged queries), then agentic search (RRF hybrid retrieval, ≤3 hops, SSE, server-resolved citations). This matches the JD's "event matching" ticketing problem. "Sports catalog" is grounded in the SportsBreak entity catalog. The 45 s wall clock was dropped for length.
- **nb-swiftui-app**: sole SwiftUI engineer, ~6,000 installs, 1,119 peak DAU, Firebase auth, 72-event Amplitude catalog. Covers the Mobile (Swift) track and "data-driven company".
- **nb-catalog-cache**: fan-out → one call, shared cache 78× smaller, 512 MiB pod, AI agent wrote the cache and he tested it. Covers "help scale our software" and "leverage cutting-edge AI tools … while upholding … standards".
- **nb-llm-pipeline**: LLM alert pipeline as a Kubernetes CronJob, 4,100+ shadow decisions, filler 34% → 4%. Covers "run experiments" and the ML track.
- **nb-cronjob-outage** + **nb-llm-failure**: Platform track and problem solving.
- **hd-lead-mvp** + **hd-mentor-process**, **hd-langchain-apis**: React / Next.js (Frontend Web track), LangChain (ML track), and mentoring ("take pride in mentoring").
- **za-mock-interview** + **za-auth-db**, **za-demos-contracts**: React, PostgreSQL (the JD's datastore), and product iteration from user testing ("passion for … product").
- **pj-my-av**: PyTorch (ML track).
- **ld-ece-fellow**, **pj-wisconsin-autonomous**: fill.
- Coursework: CMU Distributed Systems, Machine Learning, Foundations of Software Engineering (replaced LLM Systems: the JD is about software craft, not LLMs). UW Algorithms, Data Structure & Programming III, Operating Systems.
- Skills: Languages reordered to the JD's stack (Python, Go, TypeScript, Swift first). Row 2 is Frameworks & Data with React and PostgreSQL first. Cloud & Platform leads with AWS and Docker (the Platform track). ML & LLMs leads with PyTorch and LangChain.

## Items skipped

- **cm-psc / cm-nl-safety** (research): the JD does not ask for research, and the page is full.
- **nb-third-party-proxy, nb-server-driven-ui, nb-live-activities, nb-app-store, nb-ads-max, nb-retired-detector, nb-morning-digest, nb-manual-broadcast, nb-dramabreak-*, nb-jira-process, nb-coaching-marketplace**: lower value for this JD, and there was no room. Server-driven UI would fit the frontend/mobile track; it is the first swap if he picks Mobile as his first choice.

## Constraints nearly violated

- The JD's stack includes C#, .NET Core, Kotlin, Redis, Elasticsearch, GitLab, lightGBM, and Strands. None of them is in `inventory/skills.md`, so none was added. The search bullet describes Mongo `$text` and vector retrieval only as "hybrid retrieval", with no Elasticsearch claim.
- The rewritten search bullet wraps to three lines. The page still fits with the same bottom position as the template, so nothing was cut.
- The template's local `\setlist*[itemize]{itemsep=0.7pt}` is unchanged. Margins and font size are unchanged.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, "Jetson."): **755.49 pt** from the top.
- Unused height: 792 − 25.92 − 755.49 = **10.59 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, or empty bottom strip.

## Referral notes

The role is shortened to "SWE New Grad". The posting has no job ID, so none is used. The notes use the default pitch; a sports app is a natural fit for a live-events company. The why-this-team line names "event matching", which the JD lists as a ticketing problem its engineers solve.
