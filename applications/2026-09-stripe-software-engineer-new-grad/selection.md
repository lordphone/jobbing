# Selection — Stripe Software Engineer, New Grad

Revised 2026-09-14 after reviewing the posting, complete inventory, and original PDF.

## Title and location

NewsBreak: **Software Engineering Intern**. The JD says "Software Engineer, New Grad" without a narrower specialty, so use the inventory's general SWE title.
Header: **Mountain View, CA** because the posting includes South San Francisco.

## Printed facts

### NewsBreak — four bullets

1. **nb-fastapi-backend + nb-jira-process**: SportsBreak production FastAPI/MongoDB backend from first commit to 89 endpoints; approximately 1,450 offline tests; lint/type/test CI checks; 34 contract-first API specifications. Combines implementation ownership, safe changes, and concrete technical writing. Drops router, line-count, runtime, and PR-count detail to improve readability.
2. **nb-catalog-cache**: 25–30 client calls consolidated to one backend call; per-user cache replaced by 10.9 MB shared catalog; OOM risk in a 512 MiB pod identified before production. Omits 78× because the inventory does not specify the aggregate baseline needed to explain that multiplier on the page.
3. **nb-dramabreak-stripe**: shipped Stripe checkout, signature-verified webhook as the sole trusted fulfillment path, idempotency, and stale-pending recovery. Direct payment-correctness evidence is more useful here than a standalone contribution-count bullet.
4. **nb-llm-pipeline**: built and shipped personalized alerts; hand-grading found filler and confirmed events scored similarly; categorical gate; filler reduced from 34% to 4% by count. Emphasizes evaluation and intervention. This is product-output validation, not a claim about reviewing AI-generated code.

### Haddee

- **hd-lead-mvp + hd-langchain-apis**: eight-intern team, resume parsing/job matching, Next.js/FastAPI/Supabase, GCP App Engine deployment. Product purpose comes from the API/features item.
- **hd-mentor-process**: user stories, PR reviews, mentoring on Git/testing/code practices.

### ZenAI

- **za-mock-interview + za-auth-db**: one VC-backed mock-interview product; React/Next.js/Supabase; authentication, sessions, database interactions.
- **za-mock-interview + za-demos-contracts**: recruiter-informed scoring, user feedback, demos, contracts, mid-sized company customers. Customer acquisition is tied to demos/contracts, not attributed solely to user testing. No claim that this remained the company's direction after its pivot.

### Research and activities

- **cm-psc**: collaboration with PhD researchers, adaptive PSC, outperforming Adaptive MPC in 3-DOF simulations under uncertainty.
- **ld-ece-fellow**: CMU program budgeting, marketing, outreach.
- **pj-my-av**: CNN-GRU, steering/speed prediction from 1s video, 33 hours of Comma2k19, local CUDA/GCP Vertex AI training.

## Skipped and tradeoffs

- **nb-ownership**: no standalone PR/commit-count bullet. Backend ownership is demonstrated by the first bullet; leadership/review remains in Haddee. Do not imply sole-full-time ownership lasted the entire internship; the inventory limits it to a staffing transition.
- **nb-eks-standup**, **nb-from-scratch-stack**, **nb-tests-offline**: overlapping backend/deployment/testing stories; no duplicate bullet. The latter two ids occur in the old selection notes but are not standalone items in the current inventory.
- **nb-third-party-proxy**, **nb-cronjob-outage**, **nb-retired-detector**, **nb-agentic-search**, **nb-llm-failure**: good alternate reliability/judgment stories, but the four selected bullets balance backend, capacity, payments, and evaluation. No unverified post-deploy fix outcome claimed.
- **nb-swiftui-app**, **nb-server-driven-ui**, **nb-app-store**, **nb-live-activities**, **nb-ads-max**, **nb-morning-digest**, **nb-manual-broadcast**, **nb-dramabreak-ads**: lower priority for this general SWE application than the selected backend/payment evidence.
- **nb-coaching-marketplace**: never re-enabled after submission; shipped production work takes priority.
- **cm-nl-safety**: removed the second research bullet to accommodate stronger customer-facing experience while retaining one page.
- **pj-wisconsin-autonomous**: lower-priority additional project.
- No standalone **nb-entity-resolution** item exists in the current inventory; those facts are under **nb-agentic-search**.

## Skills, coursework, and checks

- Skills all come from inventory/skills.md. Python and TypeScript/JavaScript lead based on demonstrated work; Java and Go remain visible. pytest moved to Testing & Practices.
- CMU: Distributed Systems, Software Refactoring, Foundations of Software Engineering; removes ambiguous "DS for SWE" abbreviation. Wisconsin coursework unchanged.
- Existing shared preamble and application spacing retained. Rebuilt with tectonic; PDF is one Letter page, visually inspected with no clipping/overlap and no obvious empty bottom strip.
- Kept source resume.tex and output Lordphone_Wen_Resume.pdf in the existing application folder. Existing tracker row remains draft; no duplicate application created.
