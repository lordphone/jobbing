# Selection - City and County of San Francisco Technology Engineer Associate (Security)

Date: 2026-09-18

## Title, location, and priorities

- NewsBreak title: **Infrastructure Engineer Intern**, an allowed inventory title. The class builds, implements, and maintains core technology infrastructure / systems or platforms; the specialty is security operations on those systems (network path, admission policy, CronJobs, EKS). It is not an AI-infra posting.
- Header: **Mountain View, CA**. The posting is San Francisco onsite, which is SF Bay.
- Highest fit: credential hygiene and mobile binary hardening, authentication/account linking, privacy of conversation state, security-ticket verification, TLS/admission-policy incident diagnosis, destructive-deploy prevention, outage recovery, and signature-verified fulfillment.
- Supporting fit: Haddee delivery and mentorship, ZenAI authentication ownership, CMU safety-under-uncertainty research as risk-adjacent fill, ECE fellow and my-av as page fill.
- Skills: first two rows lead with Python/SQL/C/Go and AWS/Kubernetes/Linux/NGINX/Grafana. Every listed skill is in `inventory/skills.md`. No security-operations skill name was added, because it is not in inventory.
- Coursework: CMU Distributed Systems, Foundations of Software Engineering, Software Refactoring; Wisconsin Operating Systems, Computer Architecture, Algorithms.

## Selected inventory facts

### NewsBreak

1. **nb-third-party-proxy + nb-swiftui-app + nb-agentic-search**: nine integrations moved server-side; iOS binary ships zero third-party API credentials; Firebase auth (Google, Apple, email/password) with guest/anonymous sessions upgraded via account linking; search conversation state held on the client so no PII sat at rest. Related controls, not one system.
2. **nb-jira-process**: two closed security tickets reopened with line-level evidence that the fixes were absent; team doc line that a status field is not evidence of a code change.
3. **nb-eks-standup**: production EKS with Helm and Jenkins on day 3; DNS → TLS → admission-policy chain blocking iOS on public networks; stale ArgoCD prune/selfHeal that would have wiped Jenkins deploys.
4. **nb-cronjob-outage + nb-dramabreak-stripe**: 5-day silent CronJob outage from non-terminal ImagePullBackOff plus Forbid concurrency, fixed with paired job and scheduler deadlines; Stripe webhook as the only trusted fulfillment via signature verification.

### Haddee

1. **hd-lead-mvp + hd-mentor-process**: eight interns, Agile sprints, React/Next.js/FastAPI/Supabase on GCP App Engine, user stories, PR reviews, testing and Git mentorship.
2. **hd-langchain-apis**: schemas and REST APIs for LangChain resume parsing, improvement suggestions, and AI job matching.

### ZenAI

1. **za-mock-interview + za-auth-db**: sole engineer, ground-up LLM mock-interview app, React/Next.js/Supabase/PostgreSQL, authentication, session state, database interactions. One product. Did not print it as the company's lasting direction.

### Research and projects

- **cm-psc**: Online Adaptive Probabilistic Safety Certificate with PhD researchers; outperformed Adaptive MPC in 3-DOF vehicle simulations under environmental uncertainty. Printed as safety/risk research, not information-security operations.
- **ld-ece-fellow**: CMU fellow since August 2026; budgeting, marketing, outreach.
- **pj-my-av**: PyTorch CNN-GRU, 20-frame (1s) video, 33 hours of Comma2k19, shuffling/temporal windowing/240×320, local CUDA and GCP Vertex AI. Streaming inference omitted to keep the line on one page.

## Skipped items and why

- **za-demos-contracts**: client demos and contracts are weaker than authentication ownership for this JD; a second ZenAI line overflowed the page when stacked with extra research.
- **cm-nl-safety**: formal safety specs are relevant, but a second research bullet spilled my-av onto page 2.
- **nb-fastapi-backend**, **nb-catalog-cache**, **nb-ownership**, **nb-llm-pipeline**, **nb-llm-failure**, **nb-retired-detector**: backend/LLM product work is less on-point than access, privacy, and incident diagnosis. Test-suite volume was not printed as a security-assessment claim.
- **nb-swiftui-app** (DAU/installs), **nb-server-driven-ui**, **nb-app-store**, **nb-live-activities**, **nb-ads-max**, **nb-morning-digest**, **nb-manual-broadcast**, **nb-dramabreak-ads**: mobile product and ads, except the auth and credential facts already used.
- **nb-coaching-marketplace**: access-leak testing is relevant; dropped because four NewsBreak bullets already cover controls, assessment, network incidents, and fulfillment authz.
- **pj-wisconsin-autonomous**: less useful than my-av for page fill.
- Unused Stripe idempotency/US-gate details, CronJob Live Activity name, and ArgoCD exact flags: avoid crowding.

## Constraints and verification

- No SOC, SIEM, law-enforcement IR, compliance-assessment, or security-awareness-program experience was invented. Grafana is listed as an inventory skill, not as a claim that he ran a city SOC.
- Did not add IAM, Security Operations, or similar skill labels absent from `inventory/skills.md`.
- Preserved expected May 2027 graduation and actual role dates.
- Preserved shared preamble, 11pt font, margins, header layout, and role/education macros. No spacing overrides or manual padding.
- JD saved from the official SmartRecruiters posting plus the pasted URL; LinkedIn UI chrome omitted.
- Final deliverable freshly compiled with tectonic: `Lordphone_Wen_Resume.pdf`.
- Final page count: **1**, Letter, **792 pt** high.
- Configured bottom margin: **0.36 in = 25.92 pt**.
- Last visible content bottom (pdfplumber): **756.504573072 pt** from the top.
- Unused height: **792 - 25.92 - 756.504573072 = 9.575426928 pt**, passing the required 0–12 pt range.
- Rendered the final PDF at ~188 dpi (~1600 px wide) and inspected the entire page: readable, no overlap, clipping, or obvious extra bottom strip.
