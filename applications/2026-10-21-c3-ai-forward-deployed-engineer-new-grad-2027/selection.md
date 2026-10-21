# Selection — C3 AI, Forward Deployed Engineer, New Grad 2027

Regenerated 2026-10-21 from the 2026-10-09 version (folder renamed to today). Main changes: the inventory believability rules (one or two headline numbers per bullet, 20/20 instead of 0% → 100% P@1, no bare 78×, no 340/344 PRs, no 1.4K ratings), ZenAI printed as F23, and specs / docs added for the JD's "Develop specifications, technical documentation".

## NewsBreak title

**Full-Stack Engineer Intern** — JD: "This is a full-stack software engineering role with direct customer exposure." Heading is plain "NewsBreak".

Header city: Mountain View, CA (posting is Redwood City, CA).

## Items used

- **nb-ownership + nb-swiftui-app + nb-jira-process** → bullet 1: shipped SportsBreak as sole SwiftUI engineer and primary backend author, ~6,000 installs, 1,119 peak DAU; 34 contract-first API specs, onboarded the second engineer — "specifications, technical documentation".
- **nb-fastapi-backend + nb-eks-standup + nb-observability** → bullet 2: first commit to 89 REST endpoints on EKS (Docker, Helm, Jenkins), ~1,450 offline unit tests gating CI, Prometheus / Grafana — "unit testing", "cloud computing".
- **nb-agentic-search** → bullet 3: fixed RAG on turn 1, capped tool-calling agent (5 tools, ≤3 hops), 20/20 logged queries — "agentic AI", "LLM tool calling and function execution".
- **nb-llm-pipeline** → bullet 4: embeddings, LLM scoring, LLM dedupe; prompt ablations in 11-day production shadow; filler 34% → 4% — "prompt engineering".
- **nb-catalog-cache** → bullet 5: tests for an AI-agent-written cache; redesigned as pod memory neared 512 MiB; 13.2 MB per user → one shared 10.9 MB copy (per user made explicit) — "profiling & optimization", "developer AI workflows".
- **nb-cronjob-outage + nb-llm-failure** → bullet 6: 5-day silent CronJob outage, 65% LLM worker failure via Langfuse — "debugging, troubleshooting".
- **hd-lead-mvp + hd-langchain-apis + hd-mentor-process** → Haddee, 2 bullets (React, Next.js — JD prefers React; Git — preferred).
- **za-mock-interview + za-auth-db + za-demos-contracts** → ZenAI, 2 bullets; second is customer-facing: demos, client iteration, recruiters, three 200–500-person companies signed — "technical demonstrations, proofs-of-technology".
- **cm-nl-safety** → research, 1 bullet (multi-turn LLMs).
- **pj-my-av, ld-ece-fellow** → Projects & Leadership.
- Skills: Python, JavaScript, TypeScript, Java, SQL + LLM tool calling / agents, RAG in row 1; React / full-stack / relational + NoSQL in row 2; cloud + Claude Code / AI coding tools; certifications kept.
- Coursework: CMU — Distributed Systems, LLM Systems, ML; UW — Algorithms, Data Structure & Programming III (JD data structures), Software Engineering, LLMs in Practice.

## Skipped

- cm-psc: second research bullet, cut for space (least relevant to FDE).
- nb-third-party-proxy, nb-cross-dept, nb-morning-digest: space; 6-bullet cap.
- nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-manual-broadcast, nb-dramabreak-*, nb-coaching-marketplace, nb-retired-detector: mobile- or product-specific, not the JD.
- pj-codingplans, pj-wisconsin-autonomous, pj-cs537-os: less relevant; no room.
- Skills dropped for fit: Helm, Prometheus, Grafana (all still in bullet 2), Langfuse (bullet 6), LangChain (Haddee bullet), Swift.

## Constraints almost violated

- Java is in skills.md but no bullet shows Java work; listed only in Skills.
- No travel, trial, or customer-training facts beyond ZenAI demos and contracts; did not claim customer training.
- "Claude Code / AI coding tools" kept as the exact skills.md name.
- First compile spilled ~10 lines; shortened NewsBreak bullets 1–4 and Haddee, merged two skills rows, cut cm-psc.

## Page-fill verification (final PDF)

- Pages: 1
- Bottom margin: 0.36 in = 25.92 pt (from shared/preamble.tex)
- Last content line bottom (pdftotext -bbox yMax): 758.00 pt of 792 pt
- Unused height: 792 − 25.92 − 758.00 = 8.08 pt (within 0–12 pt)
- Visual review at 90 dpi: no empty bottom strip, clipping, overlap, or orphaned skills wraps.
