# Selection — Lam Research, Software Engineer 2 (196302)

## NewsBreak title
**Software Engineering Intern** — JD title is "Software Engineer"; general SWE work ("design, develop, troubleshoot, and debug software programs"). Heading is plain "NewsBreak" (not a new-ventures role).

## Header
Mountain View, CA — role is in Fremont (Bay Area).

## Angle
The JD centres on troubleshooting/debugging, maintaining an existing code base, documentation, and hardware/software integration, plus OOP, multithreading, and I2C/SPI/UART. NewsBreak bullets lean on root-cause debugging (device, linker, scheduler, concurrency), working inside a mature codebase, and docs.

## Items used
- **nb-ownership**: sole SwiftUI / primary backend, SportsBreak hyperlink (required), ~6,000 installs, peak DAU 1,119 (nb-swiftui-app), 344 PRs / 340 merged.
- **nb-live-activities**: iOS drops start push with no `aps.alert` while APNs returns 200; fixed by raising on the sender — JD "troubleshoot and debug".
- **nb-ads-max**: `NSClassFromString` → linker dead-strip of static archives; `-ObjC` proved with +7.5 MB and 0 → 2 symbols — closest low-level/build debugging fact.
- **nb-cronjob-outage**: ImagePullBackOff + Forbid concurrency, paired deadlines — scheduling / concurrency.
- **nb-llm-failure** (infra): stalled read killed `asyncio.gather` batch, unbounded loop to 16,384 tokens, Helm env shadowing default — "another team's" code = JD "existing code base … resolving problem areas"; concurrency.
- **nb-dramabreak-ads**: 43 of 565 iOS commits in a mature codebase; AVPlayer resource contention; −3-line `Package.resolved` fix unblocked SPM for the team — JD "existing application".
- **nb-fastapi-backend**: first commit → 89 endpoints, 29 repositories, ~1,450 offline tests (0.17 s), ruff / pyright / pytest gate.
- **nb-jira-process**: 34 contract-first API specs, ~10,000 lines of docs, Jira backlog, onboarded second engineer — JD "clear documentation".
- **hd-lead-mvp** (agile) + **hd-langchain-apis** (schemas/REST) + **hd-mentor-process**: fused into one bullet.
- **za-mock-interview** + **za-demos-contracts**: sole engineer; client iteration until three 200–500-person companies signed — JD "customer requirements".
- **cm-psc**: control-systems research (3-DOF vehicle sims, ice) — closest to equipment/control software.
- **pj-wisconsin-autonomous** (encoders): only hardware-integration fact (encoders, V-to-F converters, Jetson) — JD "hardware compatibility … integration between software and hardware".

## Skills
Languages first with C and Java (OOP) up front; second row Systems & Debugging (Linux, asyncio, NVIDIA Jetson, Xcode, mitmproxy, testing). Then Backend & Data, Cloud & Infra, Certifications. Dropped LLM, frontend, mobile-ads skills.

## Coursework
CMU: Foundations of Software Engineering, Software Refactoring (maintaining code), Distributed Systems. UW: Operating Systems (threads/scheduling), Computer Architecture, Data Structure & Programming III, Mobile Computing Laboratory.

## Skipped
- **nb-catalog-cache**: first draft had it; cut to fit one page.
- **pj-my-av**: first draft had it; cut to fit (ML, less relevant).
- nb-live-activities shared-ScoreboardKit clause: cut for space.
- nb-llm-pipeline, nb-agentic-search, nb-morning-digest, nb-retired-detector: LLM product work, off-target.
- nb-eks-standup, nb-third-party-proxy, nb-server-driven-ui, nb-app-store, nb-manual-broadcast, nb-dramabreak-stripe, nb-coaching-marketplace: space / less relevant.
- cm-nl-safety, ld-ece-fellow, pj-codingplans: space.

## Constraints nearly violated
- JD asks for I2C / SPI / UART, design patterns, finite state machines, and preemptive thread scheduling. None are in inventory, so none are claimed. "29 repositories" is the real data-access-layer fact; no "repository pattern" or FSM wording added. No C++ or assembly in skills.
- First compile ran to two pages; cut the cache bullet, my-av, the ScoreboardKit clause, CI/CD from skills, and the Motor-fake clause (it left a one-word widow line).

## Verification (final PDF)
- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, Wisconsin Autonomous line): **754.18 pt**.
- Unused height: 792 − 25.92 − 754.18 = **11.90 pt** (passes 0–12 pt). After inventory cuts, a full extra line would spill; itemsep loosened 0.5 → 0.7 pt (same as the Everpure resume) to close the last ~1.4 pt.
- Rendered at 90 dpi and inspected: no clipping, overlap, or empty bottom strip. UW coursework wraps "Computing Laboratory" to a second line; no layout defect.
