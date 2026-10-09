# Selection — McKinsey & Company, Software Engineer - QuantumBlack, AI by McKinsey (112342)

## NewsBreak title
**Full-Stack Engineer Intern** — the JD says "contribute across the full stack" and asks for "experience developing full-stack applications".
Heading is plain "NewsBreak" (client delivery, not a 0→1 ventures team).

## Header
Mountain View, CA. Offices are Atlanta, Boston, Chicago, Denver, New Jersey, and NYC, with no Bay option. The New York rule applies only to NYC-only postings, so the default stays.

## Items used
- **nb-ownership + nb-swiftui-app + nb-server-driven-ui** → bullet 1: sole SwiftUI engineer, primary backend author, team of ~6, 1.4K ratings, peak DAU 1,119, Firebase auth, 72-event analytics catalog, server-driven UI over 27 widget types (no App Store release needed). Maps to "full-stack applications".
- **nb-fastapi-backend + nb-eks-standup (gate)** → bullet 2: 89 REST endpoints, 129 Pydantic models, 26 collections, ~1,450 offline tests, ruff / pyright / pytest CI gate. Maps to "readable, testable, and maintainable", "unit tests using … PyTest", NoSQL.
- **nb-third-party-proxy + nb-dramabreak-stripe** → bullet 3: nine integrations server-side, zero third-party credentials in the binary; Stripe checkout via signature-verified, idempotent webhook. Maps to "security mindset … secure code".
- **nb-catalog-cache** → bullet 4: 25–30 → 1 call; AI-agent-written cache he wrote tests for; re-keyed to shared 78× smaller cache near 512 MiB limit. Maps to "AI-assisted development workflows … integrate their outputs into production".
- **nb-agentic-search** → bullet 5: RAG, bounded tool-calling agent, server-resolved citations, 0% → 100% P@1. Maps to "production-ready, AI-enabled systems".
- **nb-llm-pipeline** → bullet 6: 11-day production shadow, 4,100+ decisions, filler 34% → 4%.
- **nb-morning-digest** → bullet 7: 5,026 users (~81%), re-sourced onto highlight clusters so bullets link sources.
- **nb-eks-standup + nb-observability** → bullet 8: AWS EKS (Docker, Helm, Jenkins, GitHub Actions) from day 3, Prometheus + Grafana. Maps to "cloud platforms (AWS…)" and "CI/CD tooling (Jenkins, Docker…)".
- **nb-jira-process (default + audit)** → bullet 9: Jira backlog, 34 API specs, ~10,000 lines of docs, onboarded second engineer, reopened two closed security tickets with evidence. Maps to "cross-functional teams", "communication", "cybersecurity governance".
- **hd-lead-mvp + hd-mentor-process, hd-langchain-apis** → Haddee 2 bullets (React/Next.js; user stories, PR reviews, Git/testing mentoring; schemas + REST APIs).
- **za-mock-interview + za-auth-db + za-demos-contracts** → ZenAI 2 bullets; client iteration and demos map to "client-facing technologist".
- **pj-codingplans** → Projects.
- Skills: TypeScript/JavaScript/Java first (JD stack list), Full Stack row (React, Next.js, Express, SQL + NoSQL), Cloud & CI/CD row (AWS, GCP, Docker, Jenkins, pytest, Unit Testing), AI row led by Claude Code / AI coding tools, Certifications.
- Coursework: CMU Foundations of SE, LLM Systems, Distributed Systems; UW Software Engineering, LLMs in Practice, Algorithms.

## Skipped
- **cm-psc, cm-nl-safety** — controls research; the JD does not ask for it, and the page is full.
- **nb-llm-failure, nb-cronjob-outage, nb-retired-detector** — good debugging stories, but lower priority than security/testing/AI-workflow evidence; keep for interviews.
- **nb-app-store, nb-live-activities, nb-ads-max, nb-manual-broadcast, nb-dramabreak-ads, nb-coaching-marketplace** — mobile/ads, not in the JD.
- **ld-ece-fellow, pj-my-av, pj-wisconsin-autonomous** — no room; lower relevance.

## Constraints almost violated
- Not claimed: Node.js, Angular, Vue, Spring, C#, Jest, Azure, CircleCI — none are in inventory. Express is listed (in skills.md) but Node.js is not added.
- "Security governance" is supported only by the reopened-ticket audit and credential/webhook work; no compliance frameworks claimed.
- Adding the digest bullet spilled to two pages; trimmed it to one line, then fixed an orphan "Auth" in Skills (Firebase Auth → Firebase) and filled bullet 1 / the digest bullet with real facts. Tightened itemsep 0.7 → 0.55 pt to clear a 0.3 pt overflow.

## Page-fill verification (final PDF)
- Pages: 1 (letter, 612 × 792 pt)
- Bottom margin (preamble): 0.36 in = 25.92 pt → content limit 766.08 pt
- Last content bottom (pdftotext -bbox yMax): 765.89 pt
- Unused height: 0.19 pt (within 0–12 pt)
- Visual review at 110 dpi: no empty strip, clipping, overlap, or orphan lines.
