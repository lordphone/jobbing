# Selection — Sydecar Software Engineer 1, Platform

Date: 2026-09-18

## Title and location

- NewsBreak title: **Infrastructure Engineer Intern**. The JD is the Platform Team owning “developer productivity, core services and infrastructure, release and test automation, and security,” plus CI/CD, Terraform, GCP, and Kubernetes-style operations. That matches the inventory’s general infra / cloud / Kubernetes title, not AI infra.
- Header: **Mountain View, CA** because the posting is hybrid San Francisco or New York City (Bay option present).

## Printed facts

### NewsBreak — four bullets

1. **nb-eks-standup + nb-fastapi-backend**: production EKS on day 3 (Helm, Jenkins), 7 CronJobs, two-stage amd64 image, ruff/pyright/pytest GitHub Actions gate, suite grown to ~1,450 fully offline tests. CI/CD and test automation for the golden-path / release-automation ask. Dropped the “Jenkins previously only built the image” and 0.17s runtime clauses so the bullet stays two lines.
2. **nb-cronjob-outage + nb-eks-standup (ArgoCD)**: 5-day silent CronJob outage (non-terminal ImagePullBackOff + Forbid concurrency) fixed with paired job and scheduler deadlines; stale ArgoCD app with prune and self-heal that would have wiped Jenkins deploys. Reliability and safe-release evidence. ArgoCD is from eks-standup; the day-3 standup metrics are not repeated.
3. **nb-third-party-proxy + nb-jira-process (audit)**: nine third-party integrations moved server-side so the iOS binary ships zero API credentials; two closed security tickets spot-checked against the code, fixes absent, reopened with line-level evidence. Secrets/security-practice evidence. Does not claim OWASP scanning or org-wide security ownership.
4. **nb-dramabreak-stripe**: Stripe web checkout, signature-verified webhook as the only trusted fulfillment path, idempotent fulfillment, 60-second stale-pending reclaim. Fintech/payments bonus on a private-markets platform.

### Haddee

1. **hd-lead-mvp + hd-mentor-process**: eight-intern team, Agile sprints, React/Next.js/FastAPI/Supabase shipped on GCP App Engine, user stories, PR reviews, Git and testing mentorship. GCP familiarity and enabler/standards behavior.
2. **hd-langchain-apis**: database schemas and REST APIs for LangChain resume parsing, improvement suggestions, and AI job matching.

### ZenAI

1. **za-mock-interview + za-auth-db**: sole engineer, ground-up LLM mock-interview web app, React/Next.js/Supabase/PostgreSQL, authentication, session state, database interactions. TypeScript-adjacent web stack and PostgreSQL.
2. **za-mock-interview + za-demos-contracts**: recruiter-informed scoring, UI iteration from user testing, demos, contracts, mid-sized company users. No claim that this remained the company direction after the pivot.

### Research and activities

- **cm-psc**: kept as fill. The JD does not ask for controls/ML research; one systems-collaboration bullet remains so the page stays full. No second research bullet.
- **pj-my-av**: CNN-GRU, 1s video, 33 hours of Comma2k19, local CUDA and GCP Vertex AI, streaming inference. Extra GCP signal.
- **ld-ece-fellow**: CMU fellow since August 2026; budgeting, marketing, outreach for student programs.

## Skipped items and why

- **nb-ownership**: commit/PR totals and the temporary sole-staffing window are weaker than the infra/CI/security bullets.
- **nb-catalog-cache**: pod-memory / cost-efficiency story; overlapped the EKS reliability theme and lost the slot to Stripe (fintech bonus).
- **nb-llm-failure**: Langfuse/Helm observability debugging is relevant, but no unverified post-deploy outcome, and four platform bullets were already selected.
- **nb-jira-process** (board, 34 specs, ~10k docs, onboarding): enabler/standards work; the printed slice is the security-ticket audit only.
- **nb-swiftui-app**, **nb-server-driven-ui**, **nb-app-store**, **nb-live-activities**, **nb-ads-max**, **nb-morning-digest**, **nb-manual-broadcast**, **nb-dramabreak-ads**: mobile/ads, lower value for Platform.
- **nb-llm-pipeline**, **nb-retired-detector**, **nb-agentic-search**: product LLM work, not developer-platform.
- **nb-coaching-marketplace**: flag-disabled.
- **cm-nl-safety**: extra research line; production infra already fills the page.
- **pj-wisconsin-autonomous**: lower priority than the GCP-backed my-av line.
- NestJS, Prisma, Playwright, Jest, and Figma are JD stack items that are not in `inventory/skills.md`; not added. Terraform is listed as a skill, not claimed as a NewsBreak tool.

## Skills, coursework, and constraints

- First skill rows lead with TypeScript/Python/SQL and GCP/Terraform/Kubernetes/CI/CD. Grafana is on the Cloud row for the observability bonus. Every skill is from `inventory/skills.md`.
- CMU: Distributed Systems, Foundations of Software Engineering, Software Refactoring. Wisconsin: Operating Systems, Algorithms, Data Structure & Programming III (CS foundation the JD names).
- Did not invent IaC-at-NewsBreak, preview environments, or AI-assisted-editor fluency.
- Preserved shared preamble, 11pt, margins, header layout, and `\role`/`\edu` macros. No spacing overrides.

## Verification

- Fresh `tectonic` compile of this revision; deliverable is `Lordphone_Wen_Resume.pdf` (source `resume.tex`).
- Final page count: **1**, Letter, **792 pt** high.
- Configured bottom margin: **0.36 in = 25.92 pt**.
- Last visible content bottom (pdfplumber): **756.006443072 pt** from the top.
- Unused height: **792 - 25.92 - 756.006443072 = 10.073556928 pt**, inside the required 0–12 pt range.
- Rendered the final page at 180 dpi and inspected the full page: readable, no overlap or clipping, no obvious empty bottom strip. Cloud & DevOps wraps to a second line (`AWS, Grafana`); that wrap is intentional and does not crowd the page.
