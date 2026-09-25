# Selection — Penguin Random House, Junior AI Engineer (Open to remote)

## NewsBreak title

**AI Engineer Intern.** The posting treats AI and LLMs as product work: "Design, test, and improve language model based workflows", "hands-on experience building LLM-based or applied AI workflows". It is not AI infra or serving.

## Header

Mountain View, CA, as Lordphone asked. The posting is New York (1745 Broadway) but open to remote, so it does not require a New York address. Final interviews are in person at a PRH location.

## Items used

- **nb-llm-pipeline**: alert pipeline (embeddings, LLM scoring, same-story dedupe), hand-graded alerts, prompt ablation, categorical `happened / speculative / no_event` gate (printed as "categorical event classifier"), filler 34% → 4% by count. Maps to "classification", "Design, test, and improve", and "identify edge cases".
- **nb-agentic-search**: SSE streaming, RAG on turn 1, bounded tool loop (5 tools, ≤3 hops), server-resolved citations, entity resolution 0% → 100% P@1 on real logged queries. Maps to "search support", "evaluate… quality", and agentic frameworks.
- **nb-fastapi-backend + nb-third-party-proxy** (fused): FastAPI / MongoDB backend from scratch, 89 endpoints on EKS, ~1,450 offline tests, ruff / pyright / pytest gate, nine integrations moved server-side (SportsDataIO, YouTube, SerpApi, DeepInfra LLM, APNs named from the inventory list). "With AI coding agents" comes from the newsbreak.md note that the intern work was written with AI, and from the nb-catalog-cache fact that an AI agent wrote the cache code and he tested it. Maps to "Python-based services, APIs" and "agentic coding tools".
- **nb-llm-failure** (`llm` variant plus the 2,048-token cap that truncates 0% of observed successes): Langfuse traces, 65% failure rate, unbounded reasoning loop. Maps to "evaluate and refine system performance for quality, speed, reliability, and cost".
- **hd-langchain-apis**: default line. Maps to LangChain, "extraction" (resume parsing), and "generation" (suggestions).
- **hd-lead-mvp + hd-mentor-process** (fused): same line as the Exelixis resume.
- **za-mock-interview + za-auth-db**, **za-auth-db + za-demos-contracts** (fused): the recruiter-scoring line maps to "translate stakeholder needs"; iterating the UI maps to front-end prototyping.
- **cm-nl-safety**, **cm-psc**.
- **pj-my-av**, **ld-ece-fellow**.
- Coursework: CMU LLM Systems, Machine Learning, Data Science for SE; UW LLMs in Practice, Software Engineering, Algorithms.
- Skills: the first two rows are Python / TypeScript / JavaScript / Java / SQL / Go and LangChain / RAG / hybrid retrieval / Langfuse / FastAPI. Every skill comes from `inventory/skills.md`. Claude Code, Cursor, LangGraph, MLflow, and LangSmith are **not** in the inventory, so none of them are listed.

## Items skipped

- nb-jira-process: I used this line on the Exelixis resume. Here nb-llm-failure replaced it, because the posting stresses reliability and cost evaluation.
- nb-morning-digest: LLM summarization would fit, but the pipeline and search bullets already cover LLM product work. Skipped for space.
- nb-catalog-cache, nb-eks-standup, nb-cronjob-outage, the iOS / ads / payments items, nb-retired-detector, nb-manual-broadcast, nb-coaching-marketplace, nb-ownership, pj-wisconsin-autonomous: less relevant, and there is no room.

## Constraints almost violated

- The first draft ran to two pages. I cut "in Python" and "whitelisted… for follow-ups", and dropped "SportsBreak" from the backend line.
- The backend bullet left a one-line widow ("ships zero API keys."). I filled that line with the real integration names instead of cutting content.
- The posting asks for agentic coding tools and eval frameworks. None of them are in skills.md, so I did not add them. They are covered only by the grounded "with AI coding agents" and Langfuse / P@1 facts.

## Final page-fill check

- Page count: 1
- Configured bottom margin: 0.36 in = 25.92 pt (`shared/preamble.tex`)
- Last content bottom: 760.10 pt from the top (`pdftotext -bbox`, page height 792 pt)
- Unused height: 792 − 25.92 − 760.10 = **5.98 pt**, within the 0–12 pt limit
- Visual review at 100 dpi: full page, no empty bottom strip, no clipping or overlap, and no one-word widow lines.
