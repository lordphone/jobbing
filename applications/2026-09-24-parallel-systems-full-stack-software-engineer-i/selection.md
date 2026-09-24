# Selection - Parallel Systems Full Stack Software Engineer I

Date: 2026-09-24

## Title and priorities

- NewsBreak title: **Full-Stack Engineer Intern**. The JD title is "Full Stack Software Engineer I" and asks for "full-stack product work ... data models, APIs".
- Header: Mountain View, CA. The role is Los Angeles–only, and the rule says to use Mountain View unless the role is Canada-only or New York–only.
- What matters most in the JD: owning features end to end ("implement, test, document, and follow through after merge"); component-based UI (React); TypeScript; performance and reliability of "software that talks to the real world"; "pairing with AI coding tools and being honest about what they got wrong"; networks/OS/distributed systems coursework; a vehicle domain (autonomous rail).
- Rust and Electron are not in inventory, so they are not claimed.
- Coursework: CMU Distributed Systems, Foundations of SE, Software Refactoring ("leave it better than you found it"); UW Operating Systems, Computer Architecture, Algorithms, Software Engineering.
- Skills: TypeScript/JavaScript lead Languages; React/Next.js lead Frameworks. Linux added to Cloud row as an OS signal. All from inventory/skills.md.

## Selected items and facts

### NewsBreak
1. **nb-fastapi-backend** (+ nb-ownership first commit): first commit → 89 FastAPI/MongoDB endpoints on EKS, ~1,450 fully offline tests, ruff/pyright/pytest gate.
2. **nb-swiftui-app + nb-server-driven-ui**: sole SwiftUI engineer, ~6,000 installs, 1,119 peak DAU; server-driven UI over 27 widget types, new surfaces with no App Store release. Maps to component-based UI.
3. **nb-catalog-cache**: 25–30 requests → 1 call; the cache was written by an AI agent; per-user key found when pod memory neared 512 MiB; re-keyed to a shared 10.9 MB cache, 78× smaller. Maps to "honest about what AI tools got wrong" and performance/reliability.
4. **nb-cronjob-outage + nb-live-activities**: 5-day silent CronJob outage (ImagePullBackOff + Forbid) fixed with paired deadlines; iOS drops push-to-start without `aps.alert` while APNs returns 200. Maps to reliability and follow-through after merge.
5. **nb-jira-process** (default + audit): Jira backlog, 34 contract-first API specs, ~10,000 lines of docs, onboarded the second engineer, reopened two closed security tickets with evidence. Maps to documentation, follow-through, and clear communication.

### Haddee
1. **hd-lead-mvp + hd-mentor-process**: 8 interns, React/Next.js/FastAPI/Supabase 0→1 on GCP App Engine, user stories, PR reviews, mentoring.
2. **hd-langchain-apis**: schemas and REST APIs for LangChain features.

### ZenAI
1. **za-mock-interview + za-auth-db**: sole engineer, React/Next.js/Supabase/PostgreSQL, auth/session/DB.
2. **za-mock-interview + za-demos-contracts**: AI scoring and UI iterated with recruiters and user testing; demos; contracts with mid-sized companies. No claim about the company's lasting direction.

### Research / projects
- **cm-psc** (with "extreme conditions including ice") and **cm-nl-safety**: vehicle safety research, which fits the autonomous-vehicle domain and "picking up a new domain."
- **pj-my-av**: autonomous-driving model with streaming inference, a vehicle-domain fit.
- **pj-wisconsin-autonomous**: real-time vehicle data to the onboard Jetson, as a "software that talks to the real world" signal.

## Skipped and why

- **ld-ece-fellow**: cut for page length; the rover and my-av vehicle projects matter more for this JD.
- **nb-llm-pipeline**, **nb-agentic-search**, **nb-llm-failure**, **nb-morning-digest**, **nb-retired-detector**: LLM work is not a focus of this JD.
- **nb-eks-standup**, **nb-third-party-proxy**: covered in part by the backend and outage bullets; cut for length.
- **nb-app-store**, **nb-ads-max**, **nb-dramabreak-***, **nb-manual-broadcast**, **nb-coaching-marketplace**: mobile, ads, and payments work is less relevant.

## Constraints almost violated

- Rust and Electron are core JD keywords but are not in inventory. Neither was added.
- The cache bullet says the cache was "AI-agent-written" and "keyed per user." Both are inventory facts. It does not claim the problem was caught before production.
- The first draft spilled to 2 pages (~90 pt over). I shortened five bullets, dropped the ECE fellow line, and then re-expanded my-av to fill the page.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax): **759.99 pt** from top.
- Unused height: 792 − 25.92 − 759.99 = **6.09 pt** (passes the 0–12 pt check).
- Rendered at 110 dpi and inspected the whole page: no clipping, overlap, cramped text, or empty bottom strip.
