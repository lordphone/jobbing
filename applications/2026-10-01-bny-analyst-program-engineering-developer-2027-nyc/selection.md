# Selection — BNY, 2027 Analyst Program - Engineering (Developer), New York

## NewsBreak title

**Software Engineering Intern** (default). The JD is a general developer rotational program ("end-to-end software development lifecycle"); it does not say SWE, backend, or AI specifically.

## Framing

The JD names JavaScript, Python, CSS, Java; APIs, automation, developer tools; AI coding tools with validated outputs ("evaluating AI-generated code", "maintaining human oversight"); source control, code review, automated testing, CI/CD; secure coding and vulnerability management; cloud/containers, observability, performance, resilience; technical documentation. Built from the Goldman Sachs NYC resume and re-pointed at those phrases.

Header: **New York, NY**. This posting (82247) is New York only; the Pittsburgh posting (82248) is separate.

## Items used

- **nb-fastapi-backend + nb-eks-standup** (CI gate fact): first commit → 89 endpoints, ~1,450 fully offline tests, ruff / pyright / pytest GitHub Actions gate added after tests had been red on `main`. For "automated testing, CI/CD".
- **nb-eks-standup + nb-third-party-proxy** (fused): production EKS (Docker, Helm, Jenkins) on day 3; nine integrations server-side, zero third-party API credentials in the iOS binary. For "cloud and container" and "secure coding … protecting information".
- **nb-catalog-cache**: cache code written by an AI agent and tested by him; redesigned after pod memory climbed toward 512 MiB; 13.2 MB per user (structurally zero hit rate) → 10.9 MB shared, 78×. For "evaluating AI-generated code" and "performance".
- **nb-jira-process** (`audit` + `default`): reopened two closed security tickets with evidence the fixes were absent; 34 contract-first API specs, ~10,000 lines of docs. For "vulnerability management", "technical documentation", "code review".
- **nb-llm-pipeline**: score on arrival, rolling 7-day percentile, 4,100+ shadow decisions, filler 34% → 4%.
- **nb-swiftui-app**: sole SwiftUI engineer, App Store link on "SportsBreak", ~6,000 installs, 1,119 peak DAU.
- **nb-llm-failure**: 65% failure traced via Langfuse traces, p95 1,197 vs. 16,384 runaways, sized 2,048-token cap. For "observability", "debugging".
- **hd-lead-mvp (`agile`) + hd-mentor-process** (fused): Agile sprints, PR reviews, Git workflows, testing protocols. For "Agile Projects", "code review", "source control".
- **za-mock-interview + za-demos-contracts** (fused): sole engineer, React/Next.js/Supabase/PostgreSQL, client iteration, contracts with mid-sized companies. For "client needs".
- **cm-psc + cm-nl-safety**: kept as fill.
- **pj-my-av**, **pj-wisconsin-autonomous**.
- Coursework: CMU Foundations of SE, Software Refactoring, Distributed Systems; UW Software Engineering, Algorithms, Operating Systems.
- Skills: Languages row leads with Python, Java, JavaScript, TypeScript, CSS, HTML (JD's named languages); Practices row second (Git, CI/CD, GitHub Actions, Unit Testing, pytest, TDD, REST APIs, Agile/Scrum, Jira). Added Grafana and Langfuse for observability. Dropped OpenCV, NumPy, Firebase, Tailwind, ruff/pyright (named in bullet), certifications.

## Items skipped

- **nb-agentic-search**: dropped for the security-audit/docs bullet, which maps to more JD phrases.
- **nb-ownership** (344 PRs): cut to keep the page at one page (it pushed the last line to page 2).
- **nb-retired-detector, nb-cronjob-outage, nb-live-activities, nb-server-driven-ui, nb-app-store, nb-ads-max, nb-morning-digest, nb-manual-broadcast, nb-dramabreak-*, nb-coaching-marketplace**: lower value for this JD; no room.
- **hd-langchain-apis, za-auth-db**: one bullet per role to keep research.
- **ld-ece-fellow, pj-codingplans**: lower value than the two technical projects.

## Constraints nearly violated

- "Code review" and "secure coding" are not skills in `inventory/skills.md`, so they appear only through bullet facts (PR reviews, security tickets), not in the Skills table.
- The JD mentions financial services outcomes, risk, and controls; no finance experience is in inventory, so none is claimed.
- First draft spilled one line onto page 2; fixed by cutting the PR count, not by spacing changes.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, "Jetson." line): **761.86 pt** from the top.
- Unused height: 792 − 25.92 − 761.86 = **4.22 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, or empty bottom strip.

## Referral notes

Role shortened to "Engineering Analyst Program". Job ID 82247. Default pitch. Why-this-team line uses the JD's "secure, reliable solutions" at a financial services company.
