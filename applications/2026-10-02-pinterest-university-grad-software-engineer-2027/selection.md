# Selection — Pinterest, University Grad Software Engineer 2027 (USA)

## NewsBreak title

**Software Engineering Intern.** General SWE posting: "Contribute to engineering work across backend, full stack, mobile, web, and security domains, depending on team." The title says "Software Engineer", not "SWE", so the full form is printed.

## Framing

JD keywords: well-documented, tested, operable code; end-to-end ownership; AI tools as a coding partner; backend / full stack / mobile / web; Python, Java, JS/TS, Go, React; SWE internship strongly preferred; product sense; cross-functional collaboration.

- Ownership / end-to-end: sole SwiftUI engineer + primary backend author, first commit → 89 endpoints, 344 PRs.
- Tested: ~1,450 offline tests, 1:1 with production lines, ruff / pyright / pytest CI gate.
- Operable: EKS on day 3, 5-day CronJob outage fix.
- Documented: 34 contract-first API specs, ~10,000 lines of docs.
- Mobile / web / full stack: SwiftUI app, server-driven UI, React / Next.js at Haddee and ZenAI.
- Product sense: install / DAU / ratings, filler 34% → 4%, iterating with users and clients.
- AI: agentic search, LLM pipeline, "Claude Code / AI coding tools" in skills.

Header: **Mountain View, CA** (the posting is San Francisco / Remote, so Bay is allowed).

## Items used

- **nb-swiftui-app + nb-ownership** (fused): sole SwiftUI engineer, primary backend author, App Store link on "SportsBreak", ~6,000 installs, 1,119 peak DAU, 1.4K ratings, Firebase auth, 72-event analytics catalog, 344 PRs.
- **nb-fastapi-backend**: first commit → 89 REST endpoints, 26 collections, ~1,450 fully offline tests, 1:1 line ratio, ruff / pyright / pytest CI gate. "async MongoDB" = Motor.
- **nb-server-driven-ui** (`default`): 27 widget types, no App Store release for new surfaces, unknown kinds drop.
- **nb-catalog-cache**: 25–30 requests → 1 call, 13.2 MB per user → 10.9 MB shared, 78×, 512 MiB pod.
- **nb-eks-standup + nb-cronjob-outage** (fused): EKS / Helm / Jenkins on day 3, 7 CronJobs; 5-day silent outage, ImagePullBackOff + Forbid, paired deadlines.
- **nb-llm-pipeline**: ingest → embed → LLM-score → dedupe → APNs ("push"), personalized, 4,100+ shadow decision rows, filler 34% → 4%, 2/day cap over 11,745 user-days.
- **nb-agentic-search** (`design` + `entities`, compressed): one SSE endpoint, deterministic RAG turn 1, bounded agent (≤3 hops, 5 tools), 0% → 100% P@1 on real logged queries.
- **nb-jira-process** (`default`): Jira backlog unprompted, 34 specs, ~10,000 lines of docs, onboarded second engineer.
- **hd-lead-mvp + hd-langchain-apis** (fused): 8 interns, Agile, React / Next.js / FastAPI / Supabase, 0→1, GCP App Engine, schemas + REST APIs, LangChain resume parsing.
- **hd-mentor-process**: user stories, PR reviews, mentoring on Git, testing, scalable code.
- **za-mock-interview** (sole + iteration facts): sole engineer, React / Next.js / Supabase / PostgreSQL, iterated AI scoring and UI from user-testing.
- **za-demos-contracts** (`contracts`).
- **cm-psc** (`default`): fill.
- **pj-my-av** (`short`): fill.

## Items skipped

- **nb-llm-failure**: strong debugging story, but no room after mobile / docs bullets; less tied to this JD than ownership and testing.
- **nb-third-party-proxy** (security domain is mentioned but secondary), **nb-live-activities, nb-app-store, nb-ads-max, nb-morning-digest, nb-manual-broadcast, nb-retired-detector, nb-dramabreak-*, nb-coaching-marketplace**: no room.
- **cm-nl-safety**: research kept to one bullet.
- **ld-ece-fellow, pj-codingplans, pj-wisconsin-autonomous**: no room.
- Coursework dropped: Operating Systems (space), others less relevant.
- Skills dropped: TDD, CI/CD (CI gate is in the bullets), Motor, Express, Tailwind, Stripe, mobile tooling, Terraform, Jenkins, Langfuse, certifications, and more.

## Constraints almost violated

- C++ is in the JD but not in inventory; not claimed.
- AI-collaboration: the inventory fact "cache code was written by an AI agent; he wrote tests for it" was considered for the cache bullet, but fusing it would imply the AI wrote the per-user bug, which inventory does not say. Left out; AI tooling shows in Skills only.
- First compile was 2 pages (Projects spilled, ~3 lines). Dropped Operating Systems, TDD, CI/CD, and shortened the mentoring bullet and server-driven UI bullet; that left 19 pt unused, so the server-driven UI clause ("unknown widget kinds drop") was restored.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 792 pt tall)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 760.29 pt
- Unused height: 792 − 25.92 − 760.29 = 5.79 pt (passes 0–12 pt)
- Visual review: rendered at 110 dpi; no empty bottom strip, clipping, or overlap; spacing even.
