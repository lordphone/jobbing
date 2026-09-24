# Selection — Exelixis, Associate Engineer - AI and Agentic

## NewsBreak title

**AI Engineer Intern.** The posting treats AI and agents as product work ("AI-enabled prototypes, internal tools, and workflow automations", "prompt engineering, basic agent workflows, retrieval-assisted use cases"). It is not AI infra or serving.

## Header

Mountain View, CA. The role is in Alameda, CA (SF Bay).

## Items used

- **nb-llm-pipeline**: personalized alert pipeline (embeddings, LLM scoring, same-story dedupe), hand-graded alerts, prompt ablation, categorical `happened / speculative / no_event` gate, filler 34% → 4% by count. Maps to "prompts, tests", "validation checks", and "responsible AI".
- **nb-agentic-search**: SSE streaming, deterministic RAG on turn 1, bounded tool loop on turn 2+ (5 whitelisted tools, ≤3 hops), server-resolved citations so the model cannot author a URL. Maps to "agent workflows" and "retrieval-assisted use cases".
- **nb-fastapi-backend + nb-third-party-proxy** (fused): FastAPI / MongoDB backend from the first commit, 89 endpoints on EKS, ~1,450 offline tests, ruff / pyright / pytest gate, plus nine integrations moved server-side so the iOS binary ships zero API credentials. "With AI coding assistance" is grounded in the newsbreak.md note that the intern work was written with AI (and the AI-agent-written cache code he tested). Maps to "AI-assisted development tools… with appropriate review", "unit tests", "API integrations", and "information security".
- **nb-jira-process**: 34 contract-first API specs, ~10,000 lines of docs, security tickets reopened with evidence, onboarded the second engineer. Maps to "documentation" and "security expectations".
- **hd-langchain-apis**: default approved line (LangChain resume parsing, suggestions, AI job matching).
- **hd-lead-mvp + hd-mentor-process** (fused): Agile sprints, the 8-intern team, Next.js / FastAPI / Supabase on GCP App Engine, user stories, PR reviews, testing / Git mentoring. Maps to "code reviews" and "backlog discussions".
- **za-mock-interview + za-auth-db**: sole engineer on an LLM app; auth, session state, and database interactions.
- **za-auth-db + za-demos-contracts** (fused): AI scoring refined with recruiters, UI iterated from user testing, demos and contracts with mid-sized companies. Maps to "demos" and "testing sessions".
- **cm-nl-safety** (listed first, because it uses LLMs) and **cm-psc**.
- **pj-my-av** (default line, as a GitHub portfolio item: the posting asks for a portfolio or GitHub repository) and **ld-ece-fellow**.
- Coursework: CMU LLM Systems, Machine Learning, Data Science for SE; UW LLMs in Practice, Software Engineering, Algorithms.
- Skills: the first two rows are Python / TypeScript / JavaScript / Java and LangChain / RAG / hybrid retrieval / Langfuse. Every skill listed comes from `inventory/skills.md`.

## Items skipped

- nb-llm-failure (Langfuse 65% failure diagnosis): drafted as a fifth NewsBreak bullet and cut when the page spilled to two pages. It was the lowest-value line for this JD.
- nb-catalog-cache, nb-eks-standup, nb-cronjob-outage: infra and performance work. The posting does not ask for it.
- nb-swiftui-app, nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-dramabreak-*: iOS, ads, and payments. Not relevant here.
- nb-morning-digest: LLM work, but the alert-pipeline and search bullets already cover LLM product work. Skipped for space.
- nb-retired-detector, nb-manual-broadcast, nb-coaching-marketplace, nb-ownership: skipped for space and relevance.
- pj-wisconsin-autonomous: embedded work. Not relevant.

## Constraints almost violated

- The first draft ran to two pages with five NewsBreak bullets. I cut nb-llm-failure and tightened widow lines (UW coursework swapped DS&P III for Algorithms, and three bullets were shortened) until the page fit.
- I dropped "no conversation data is stored server-side" from the search bullet for space. It is still true (client-held state, no PII at rest) and can go back in if space allows.

## Final page-fill check

- Page count: 1
- Configured bottom margin: 0.36 in = 25.92 pt (`shared/preamble.tex`)
- Last content bottom: 759.49 pt from the top (`pdftotext -bbox`, page height 792 pt)
- Unused height: 792 − 25.92 − 759.49 = **6.59 pt**, within the 0–12 pt limit
- Visual review at 100 dpi: full page, no empty bottom strip, no clipping or overlap, and no one-word widow lines.
