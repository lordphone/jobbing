# Selection - Finstock, Inc. Software Engineer

Date: 2026-09-17

## Title and priorities

- NewsBreak title: **Backend Engineer Intern**, selected from the allowed titles because the JD specifies “design, develop, and maintain backend services and APIs.” AI supports the product; the role centers on backend engineering.
- Header: Mountain View, CA, consistent with the United States remote location.
- Highest fit (5/5): backend API ownership, databases, tests and CI, secure external integrations, performance optimization, and production model integration.
- Strong supporting fit (4/5): technical documentation, Agile delivery, code review, Git/testing mentorship, and recruiter collaboration.
- Supporting fit (3/5): stochastic-systems research and a data-intensive ML project. Leadership fills the page with a distinct inventory-backed activity.
- First skill rows prioritize Python/Java/Go/SQL, FastAPI, REST APIs, MongoDB, PostgreSQL, and MySQL. Every listed skill appears in inventory/skills.md.
- Coursework: CMU Distributed Systems, Machine Learning, Software Refactoring; Wisconsin Algorithms, Data Structure & Programming III, Operating Systems.

## Selected items and facts

### NewsBreak

1. **nb-fastapi-backend + nb-jira-process**: Python/FastAPI/MongoDB service from its first commit to 89 endpoints on EKS, approximately 1,450 fully offline tests, CI lint/type/test gates, and 34 contract-first API specifications. The specifications are team documentation; no claim that every spec covers this service.
2. **nb-third-party-proxy**: nine third-party integrations moved server-side, including DeepInfra LLM and embeddings; zero third-party credentials in the iOS binary. Specific security evidence without claiming blanket system security.
3. **nb-catalog-cache**: consolidated 25–30 client requests into one call, shared 10.9 MB cache, 78-times smaller footprint, 512 MiB pod. Performance metrics appear once.
4. **nb-llm-pipeline**: shipped personalized news-alert scoring and same-story deduplication as a Kubernetes CronJob, calibrated using 4,100+ production-shadow decisions, filler reduced from 34% to 4% by count. The count-based denominator is explicit.

### Haddee

1. **hd-lead-mvp + hd-mentor-process**: eight interns, Agile sprints, React/Next.js/FastAPI/Supabase web app shipped on GCP App Engine, user stories, PR reviews, Git and testing mentorship.
2. **hd-langchain-apis**: database schemas and REST APIs for LangChain resume parsing, improvement suggestions, and AI job matching.

### ZenAI

1. **za-mock-interview + za-auth-db**: sole engineer, ground-up LLM mock-interview web app, React/Next.js/Supabase/PostgreSQL, authentication, session state, and database interactions. One product.
2. **za-mock-interview + za-auth-db + za-demos-contracts**: recruiter collaboration on hiring criteria, UI iteration from user testing, product demos, contracts, and mid-sized company users. No claim that this remained the company's direction following its pivot.

### Research and projects

- **cm-psc**: developed adaptive PSC with PhD researchers; outperformed Adaptive MPC in 3-DOF vehicle simulations under environmental uncertainty. Quantitative systems evidence, with no financial-domain claim.
- **pj-my-av**: PyTorch CNN-GRU, steering/speed from 1s video, 33 hours of Comma2k19, local CUDA and GCP Vertex AI training, streaming inference.
- **ld-ece-fellow**: CMU fellow since August 2026, budgeting/marketing/outreach for student programs, company-sponsored hackathons, alumni events, tech outings.

## Skipped items and why

- **nb-ownership**: commit shares, PR totals, and temporary sole staffing window are less useful than direct backend delivery evidence.
- **nb-eks-standup**: detailed deployment setup omitted; EKS and CI already represented. No duplicate infrastructure metrics.
- **nb-cronjob-outage**, **nb-llm-failure**: debugging examples are relevant but lower priority than the four chosen bullets; no unverified post-deploy outcome claimed.
- **nb-swiftui-app**, **nb-server-driven-ui**, **nb-app-store**, **nb-live-activities**, **nb-ads-max**, **nb-manual-broadcast**, **nb-dramabreak-ads**: mobile/advertising focus is weaker for this backend role.
- **nb-morning-digest**, **nb-retired-detector**, **nb-agentic-search**: overlapping AI evidence; selected the calibrated production alert pipeline.
- **nb-dramabreak-stripe**: relevant payment integration, but this JD centers on AI analytics rather than payment processing; chose model integration and backend performance.
- **nb-coaching-marketplace**: flag-disabled product, lower value than shipped services.
- Unused **nb-jira-process** and **nb-catalog-cache** details: avoid crowding and repeating ownership/performance signals.
- **cm-nl-safety**: removed additional Bayesian-estimator detail to preserve one page; production AI work is already prominent.
- **pj-wisconsin-autonomous**: less relevant than the data-intensive my-av project.
- Mobile and lower-priority frontend/infrastructure skills omitted for focus.

## Constraints and verification

- All claims come from inventory; no C#, microservices architecture, OOP skill label, trading-system experience, or financial-service outcomes were inferred from the JD.
- Preserved expected May 2027 graduation and the actual role dates. No availability or graduation promise added.
- Preserved shared preamble, 11pt font, margins, header layout, and role/education macros. No spacing overrides or manual padding.
- Saved the pasted company description, role description, qualifications, and posting URL; omitted LinkedIn interface text and keyword-score advertising.
- Final deliverable freshly compiled successfully with tectonic: Lordphone_Wen_Resume.pdf.
- Final page count: **1**, Letter, **792 pt** high.
- Configured bottom margin: **0.36 in = 25.92 pt**.
- Last visible content bottom (pdfplumber): **757.002703072 pt** from the top.
- Unused height: **792 - 25.92 - 757.002703072 = 9.077296928 pt**, passing the required 0–12 pt range.
- Rendered final PDF at 1600px and inspected the entire page: readable, no overlap, clipping, or obvious extra bottom strip.
