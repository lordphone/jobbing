# Selection — Whatnot, Software Engineer, 2027 New Grad

## NewsBreak title

**Software Engineering Intern** (default). The JD title is "Software Engineer" and the role is general product engineering ("Writing product or system development code"), not backend-, mobile-, or AI-specific.

## Header city

Mountain View, CA — the JD lists San Francisco among the four hubs.

## JD emphasis

Product instincts, shipping fast, owning projects end to end, live-stream features, growth in buyer/seller flows, scale, a high-trust marketplace, tradeoffs, and triage/debugging.

## Items used

- **nb-fastapi-backend + nb-ownership** → bullet 1: primary backend author, first commit → 89 endpoints on EKS, ~1,450 offline tests, ruff/pyright/pytest gate, 344 PRs (340 merged). End-to-end ownership.
- **nb-swiftui-app + nb-app-store** → bullet 2: sole SwiftUI engineer, ~6,000 installs, 1,119 peak DAU, App Store launch through three trademark rejections by cutting the hero World Cup feature (product tradeoff to ship), guest-first Firebase auth, 72-event Amplitude catalog (growth instrumentation). SportsBreak hyperlinked.
- **nb-manual-broadcast + nb-live-activities** → bullet 3: live segment-broadcast tool during the World Cup, beat other sports apps, a minute before FOX's goal broadcast; ActivityKit Live Activities. Maps to "new features for users in our live-streams".
- **nb-server-driven-ui + nb-morning-digest** → bullet 4: 27 widget types, new surfaces ship without an App Store release (ship fast); digest reached 5,026 users (~81%) (growth).
- **nb-catalog-cache** → bullet 5: 25–30 requests → 1 call, shared cache 78× smaller, 512 MiB pod (scalable systems).
- **nb-third-party-proxy** → bullet 6: nine integrations server-side, zero third-party credentials in the binary (trust); ESPN proxy rolled back after 2.5 hours (tradeoff judgment).
- **nb-cronjob-outage + nb-dramabreak-stripe** → bullet 7: 5-day silent CronJob outage fixed with paired deadlines (triage); Stripe web checkout with signature-verified, idempotent webhook fulfillment (commerce / trust).
- **hd-lead-mvp (agile) + hd-mentor-process** → Haddee bullet 1.
- **hd-langchain-apis (llm)** → Haddee bullet 2.
- **za-mock-interview + za-auth-db** → ZenAI bullet 1.
- **za-demos-contracts + za-mock-interview facts (recruiters, client iteration, user-testing)** → ZenAI bullet 2.
- **pj-my-av (short)**, **ld-ece-fellow** → Projects & Leadership.
- Coursework: CMU — Distributed Systems, Foundations of SE, ML; UW — Algorithms, Mobile Computing Laboratory, Software Engineering, Operating Systems.
- Skills: Python / TypeScript / Swift first; FastAPI, React, Next.js, SwiftUI, MongoDB, PostgreSQL in the second row. All from `inventory/skills.md`.

## Items skipped

- **nb-llm-pipeline**: strong, but AI news alerts are less relevant to live commerce; cut first when the page spilled.
- **nb-agentic-search, nb-llm-failure, nb-retired-detector**: LLM/search depth the JD does not ask for.
- **nb-eks-standup**: infra detail; EKS is already in bullet 1.
- **nb-ads-max, nb-dramabreak-ads, nb-coaching-marketplace, nb-jira-process**: lower value; no room.
- **cm-psc, cm-nl-safety**: research is irrelevant to this JD; no room.
- **pj-wisconsin-autonomous**: tried as fill but wrapped to two lines and spilled the page; replaced by the ESPN-rollback clause.
- **pj-codingplans**: no room.

## Constraints nearly violated

- First draft (8 NewsBreak bullets + 3 project lines) spilled to two pages; cut the LLM alert bullet and tightened widow lines.
- "Live Activities for live scores": inventory says ActivityKit Live Activities with a shared scoreboard (ScoreboardKit); "live scores" describes that scoreboard, nothing more.
- No Whatnot-specific stack is claimed; JD names none.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, last line of the ECE Fellow item): **754.82 pt** from the top.
- Unused height: 792 − 25.92 − 754.82 = **11.26 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, or empty bottom strip.
