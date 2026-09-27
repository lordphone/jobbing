# Selection - Meow Software Engineer - New graduate

Date: 2026-09-17

## Title, location, and priorities

- NewsBreak title: **Full-Stack Engineer Intern**, an allowed inventory title selected by the JD's "Build full-stack web features (front-end, back-end) from zero to one."
- Header: **New York, NY**, following the resume skill's rule for a New York-only posting. NewsBreak's actual workplace remains Mountain View, CA.
- Highest fit: React/FastAPI/PostgreSQL, end-to-end product ownership, third-party API integration, payment-state correctness, tests, and customer iteration. Research is supporting evidence of problem-solving, not the focus.
- Skills: TypeScript and Python lead the first row; React, FastAPI, and PostgreSQL lead the second. Every listed skill is in inventory/skills.md; PostgreSQL retains its inventory name rather than changing it to Postgres.
- Coursework: CMU Distributed Systems, Software Refactoring, Foundations of Software Engineering; Wisconsin Algorithms, Operating Systems, Software Engineering. All names match inventory.

## Selected inventory facts

### NewsBreak

1. **nb-fastapi-backend + nb-jira-process**: Python/FastAPI/MongoDB backend from first commit, 89 endpoints, EKS, approximately 1,450 fully offline tests, lint/type/test CI gates; 34 contract-first API specifications. Combines ownership, quality, and technical communication. The API-spec count is team documentation, not an assertion that every spec describes this backend.
2. **nb-dramabreak-stripe**: shipped Stripe web checkout, signature-verified webhook as the only trusted fulfillment path, idempotent fulfillment, 60-second stale-pending reclaim. Concrete evidence relevant to Meow's state-machine requirement without inventing a formal state-machine implementation.
3. **nb-third-party-proxy + nb-catalog-cache**: nine server-side integrations, named examples SportsDataIO/YouTube Data/DeepInfra, zero third-party credentials in the iOS binary; 25-30 catalog requests consolidated to one backend call with a 3-second per-source budget. These are related API-boundary improvements, not a claim that all nine integrations served the catalog.
4. **nb-swiftui-app + nb-server-driven-ui**: sole SwiftUI engineer, roughly 6,000 installs and 1,119 peak DAU, 27 backend widget types, new catalog surfaces without an App Store release. App metrics are product/team results, not sole attribution of growth.

### Haddee

1. **hd-lead-mvp + hd-mentor-process**: led eight interns to build and deploy a React/Next.js/FastAPI/Supabase web app on GCP App Engine; user stories, PR reviews, testing and Git mentorship.
2. **hd-langchain-apis**: database schemas and REST APIs for LangChain resume parsing, improvement suggestions, and AI job matching.

### ZenAI

1. **za-mock-interview + za-auth-db**: sole engineer, ground-up mock-interview web app, React/Next.js/Supabase/PostgreSQL, authentication, session state, database interactions. These describe one product.
2. **za-mock-interview + za-auth-db + za-demos-contracts**: user-testing and recruiter feedback for scoring/UI, product demos, contracts, and mid-sized company users. No claim that the product remained the company's direction after the eventual pivot.

### Research, projects, leadership

- **cm-psc**: adaptive PSC with PhD researchers, outperforming Adaptive MPC in 3-DOF simulations under environmental uncertainty.
- **pj-my-av**: PyTorch CNN-GRU, steering-angle/speed prediction from 1s video, 33 hours of Comma2k19, local CUDA and GCP Vertex AI training, streaming inference. Demonstrates building beyond employment; inventory does not establish whether it was outside required coursework, so that claim is not added.
- **ld-ece-fellow**: CMU budgeting, marketing, outreach, company-sponsored hackathons, alumni events, tech outings.

## Skipped items and facts

- **nb-ownership**: PR counts, commit shares, and temporary sole-full-time staffing window add less than shipped work. Do not imply sole backend ownership throughout the internship.
- **nb-eks-standup**: detailed infrastructure setup and deployment debugging are lower priority for this full-stack role; EKS is already included via nb-fastapi-backend.
- **nb-cronjob-outage**: useful state-transition/debugging example, but payment fulfillment provides a closer domain match within four bullets.
- **nb-app-store**, **nb-live-activities**, **nb-ads-max**, **nb-manual-broadcast**, **nb-dramabreak-ads**: mobile/ads details have lower relevance than the selected full-stack, API, and payment work.
- **nb-morning-digest**, **nb-retired-detector**, **nb-llm-pipeline**, **nb-agentic-search**, **nb-llm-failure**: AI-specific details are less relevant to the stated web stack; no unsupported post-deploy reliability outcome claimed.
- **nb-coaching-marketplace**: flag-disabled and never re-enabled; prioritize launched work.
- Remaining **nb-catalog-cache** cache sizing/copy/payload metrics and **nb-jira-process** issue/doc counts are omitted to avoid crowding and repeated ownership signals.
- **cm-nl-safety**: second research bullet is less useful than added API integration and specification detail.
- **pj-wisconsin-autonomous**: less relevant than my-av for demonstrating a substantial project.
- Remaining languages, infrastructure, mobile, and ML skills were dropped for focus. No new skills were inferred from the JD.

## Constraints and final verification

- Preserved the shared preamble, margins, 11pt font, role/education macros, and root header structure. No spacing overrides or manual vertical padding added.
- Kept the expected May 2027 graduation date; did not imply graduation was complete or promise an earlier start.
- Did not label native SportsBreak work as web work, add TypeScript to an employer's stack without evidence, invent financial reporting work, or claim formal state-machine design.
- Saved the pasted JD with its posting URL; third-party keyword-score copy and site footer were omitted.
- Final deliverable compiled successfully with tectonic: **Lordphone_Wen_Resume.pdf**.
- Final page count: **1** (Letter, 792 pt high).
- Configured bottom margin: **0.36 in = 25.92 pt**.
- Last visible content bottom from pdfplumber text bounding boxes: **757.002703072 pt** from the top.
- Unused height: **792 - 25.92 - 757.002703072 = 9.077296928 pt**, within the required 0-12 pt range.
- Rendered the final deliverable at 1600px and reviewed the entire page: readable text, no clipping or overlap, no obvious extra bottom strip. Shared compact layout retained.
