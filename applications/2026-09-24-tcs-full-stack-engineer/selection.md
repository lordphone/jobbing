# Selection - TCS Full Stack Engineer (Job Id 427336)

Date: 2026-09-24

## Title and priorities

- NewsBreak title: **Full-Stack Engineer Intern**. The JD title is "Full Stack Engineer" and asks to "develop and maintain full-stack applications using React, TypeScript, Python, and REST APIs."
- Header: **New York, NY**. The posting lists only New York, NY, with no Bay Area option.
- What matters most in the JD: React + TypeScript front end; Python/FastAPI REST APIs and data contracts; SQL; reusable components; surfacing data pipelines and model outputs to users; testing and CI/CD; cloud (GCP/AWS); troubleshooting with platform/data teams; prototyping and iterating on user feedback.
- Not in inventory, so not claimed: Figma, Streamlit, Storybook, Jest, Flask, Azure, data warehousing, CTEs/window functions.
- Posted as 6–8 years of experience; nothing inflated to match.
- Coursework: CMU Data Science for SE, Distributed Systems, Software Refactoring; UW Software Engineering, Algorithms, LLMs in Practice.
- Skills: Python/TypeScript/JavaScript/SQL lead Languages; React/Next.js/Tailwind CSS/FastAPI lead Frameworks; relational DBs lead Data & AI; GCP/AWS lead Cloud. All from inventory/skills.md.

## Selected items and facts

### NewsBreak
1. **nb-ownership + nb-swiftui-app + nb-fastapi-backend**: sole SwiftUI engineer, primary backend author, ~6,000 installs, 1,119 peak DAU; FastAPI/MongoDB from first commit to 89 endpoints, ~1,450 fully-offline tests, ruff/pyright/pytest CI gate.
2. **nb-server-driven-ui + nb-jira-process**: 27 widget types, new surface without an App Store release, unknown kinds drop; 34 contract-first API specs. Maps to reusable components and data contracts.
3. **nb-llm-pipeline**: ingest → embed → LLM-score → dedupe → push; 4,100+ shadow decisions; filler 34% → 4%. Maps to "surface data and model outputs".
4. **nb-agentic-search**: hybrid retrieval, SSE streaming, server-resolved citations, 0% → 100% P@1.
5. **nb-morning-digest + nb-third-party-proxy**: digest to 5,026 users (~81%); nine integrations server-side, zero third-party credentials in the client. Maps to data integrations.
6. **nb-llm-failure** (backend variant + sizing facts): helped debug another team's pipeline; 65% failure rate via Langfuse; 16,384-token ceiling; 2048 cap vs p95 1,197. Maps to "troubleshoot ... in collaboration with platform and data engineering teams".
7. **nb-catalog-cache + nb-eks-standup**: 25–30 request fan-out → one call; shared cache 78× smaller; production EKS (Helm, Jenkins, Docker) on day 3.

### Haddee
1. **hd-lead-mvp + hd-mentor-process**: 8 interns, Agile sprints, React/Next.js/FastAPI/Supabase 0→1 on GCP App Engine, user stories, PR reviews, Git/testing mentoring.
2. **hd-langchain-apis** (llm): schemas and REST APIs for LangChain features.

### ZenAI
1. **za-mock-interview + za-auth-db**: VC-backed, 0→1, sole engineer, React/Next.js/Supabase/PostgreSQL, auth/session/DB.
2. **za-auth-db + za-demos-contracts**: iterated AI scoring and UI from user testing and fast client iteration; demos; contracts with mid-sized companies. Maps to "rapidly iterate ... on end-user feedback".

### Projects & leadership
- **pj-my-av**: data pipeline, GCP Vertex AI, streaming inference.
- **ld-ece-fellow**: fill after research did not fit.

## Skipped and why

- **cm-nl-safety / cm-psc**: tried twice; the Research section (heading + role + 2 lines) spilled to page 2 both times. The JD does not ask for research.
- **nb-cronjob-outage**, **nb-retired-detector**, **nb-app-store**, **nb-live-activities**, **nb-ads-max**, **nb-dramabreak-***, **nb-manual-broadcast**, **nb-coaching-marketplace**: iOS/ads specifics or covered elsewhere; cut for length.
- **pj-wisconsin-autonomous**: embedded work, not relevant.

## Constraints almost violated

- First draft said "typed Pydantic data contracts" on the server-driven UI bullet. Inventory does not tie Pydantic to the widget registry, so I removed it.
- First draft called SwiftUI "front-end"; changed back to "Sole SwiftUI engineer".
- Figma, Streamlit, Storybook, Jest, and Flask are JD keywords but are not in inventory; none added.
- "AWS EKS": EKS is the AWS service, and AWS is in skills.md.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax): **754.30 pt** from top.
- Unused height: 792 − 25.92 − 754.30 = **11.78 pt** (passes the 0–12 pt check).
- Rendered at 90 dpi and inspected the whole page: no clipping, overlap, cramped text, or empty bottom strip.
