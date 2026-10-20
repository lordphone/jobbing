# Selection — ServiceNow, Software Engineer (JB0075018)

## NewsBreak title

**Software Engineering Intern** — the posting title is plain "Software Engineer" (IC2, early career) spanning Python / Java / JavaScript, testing, CI/CD, AI feature integration, and platform work; no single backend / full-stack / AI specialty dominates, so the general-SWE default fits. The JD says "Software Engineer", not "SWE", so the full title is printed. Heading is plain "NewsBreak" (not a new-venture JD).

Header city: Mountain View, CA (posting is Santa Clara, Bay Area).

## Items used

- **nb-ownership** → bullet 1 (backend-first on request; SwiftUI ownership dropped): primary backend author, opened the service with its first commit, ~83% of backend commits (397/475), SportsBreak link with 1.4K ratings / peak DAU 1,119, 344 PRs / 340 merged — "take ownership", "participate in code reviews".
- **nb-fastapi-backend + nb-eks-standup** → bullet 2: 89 endpoints ("first commit" moved to bullet 1), ~1,450 fully-offline tests, pytest CI gate, EKS (Docker, Helm, Jenkins) on day 3 — "RESTful APIs", "comprehensive unit tests", "CI/CD ... automated testing and deployment pipelines".
- **nb-llm-pipeline** → bullet 3: ~1,200 LLM calls/day, prompt ablations, production shadow on 4,100+ decisions, filler 34% → 4% — "prompt design assistance, API integration, and basic evaluation".
- **nb-agentic-search** → bullet 4: RAG turn 1, ≤3 hops / 5 tools, server-resolved citations, 0% → 100% P@1 — "hands-on experience with LLMs or AI APIs".
- **nb-cronjob-outage + nb-llm-failure** → bullet 5: 5-day CronJob outage, 65% failure via Langfuse — "troubleshoot and debug issues", "understanding root causes".
- **nb-jira-process** → bullet 6: Jira backlog, 34 API specs, ~10,000 lines of docs, onboarded second engineer — "documentation and internal knowledge bases", "sprint planning", "support ... newer developers".
- **hd-lead-mvp (agile) + hd-langchain-apis (llm) + hd-mentor-process** → Haddee 3 lines — "Agile development", "REST APIs", "code reviews", "support junior teammates".
- **za-mock-interview (with-auth) + za-demos-contracts** → ZenAI 2 lines — "database interactions", "understand customer needs".
- **cm-nl-safety** → research (multi-turn LLMs; JD asks "understanding of AI/ML concepts"; kept as fill).
- **pj-my-av** (default) → project line, linked to GitHub (replaced pj-codingplans on request; ML concepts — "understanding of AI/ML concepts").
- **ld-ece-fellow** → leadership line (added on request, replacing the integrations/observability NewsBreak bullet; section renamed Projects & Leadership).
- Skills: Python, Java, JavaScript first (JD's three languages), SQL ("relational databases and SQL"), LLM / RAG; REST APIs, PostgreSQL, Git, Agile/Scrum in row 2; pytest, CI/CD in row 3; certifications kept.
- Coursework: CMU — Foundations of Software Engineering, LLM Systems, Machine Learning; UW — Software Engineering, Algorithms, LLMs in Practice.

## Skipped

- nb-third-party-proxy, nb-observability: cut on request to keep NewsBreak at six bullets; swapped for ld-ece-fellow (same two lines).
- nb-catalog-cache, nb-server-driven-ui, nb-live-activities, nb-ads-max, nb-app-store, nb-morning-digest, nb-manual-broadcast, nb-retired-detector, nb-cross-dept, nb-dramabreak-*, nb-coaching-marketplace: performance / mobile / ads depth the JD does not ask for; space.
- pj-codingplans: swapped out for pj-my-av on request.
- cm-psc, pj-wisconsin-autonomous, pj-cs537-os: off-JD; space.

## Constraints almost violated

- No ServiceNow, GlideScript, or Java project experience is in inventory; Java is listed only as a skill (it is in skills.md). Not claimed anywhere else.
- JD asks 2–5 years of professional experience; inventory has internships and a startup role only. Not inflated.
- Bullet 2 dropped "ruff / pyright" from the CI gate for space; the gate is still real (ruff + pyright + pytest).
- First compile spilled ~10 lines to page 2. Cut Distributed Systems coursework, MySQL / Jira / Unit Testing skills, and shortened the Haddee lead line; that left ~37 pt, so restored the integrations/observability bullet and the Haddee mentoring line.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 792 pt tall)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 757.50 pt
- Unused height: 792 − 25.92 − 757.50 = 8.58 pt (passes 0–12 pt)
- Visual review (after the ECE and my-av swaps): rendered at 110 dpi. No empty bottom strip, clipping, overlap, or cramped text. The Languages & AI Skills row wraps to a second line ("AI coding tools"); kept because removing it would leave ~21 pt unused.
