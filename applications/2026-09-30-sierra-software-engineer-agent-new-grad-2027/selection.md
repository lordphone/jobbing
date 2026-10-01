# Selection — Sierra, Software Engineer, Agent (New Grad 2027)

## NewsBreak title

**AI Engineer Intern.** The JD is "design and deliver production-grade AI agents" and asks for "eval frameworks, agent tooling, RAG pipelines, and prompt engineering" — AI / LLM / agents as product work. Software Engineer Intern was the alternative (the title says Software Engineer), but every responsibility is agent work.

Header: Mountain View, CA (SF or NY on-site; SF is an option).

## Items used

- **nb-agentic-search** (grounded / design): deterministic RAG turn 1, hybrid retrieval fused with RRF, bounded tool-use agent (≤3 hops, 5 tools), server-resolved citations. JD: "agent tooling, RAG pipelines", "production-grade AI agents".
- **nb-agentic-search** (entities / eval): eval harness on real logged queries, P@1 0% → 100% at 0.4 ms, embeddings ruled out with measurements, 23 problems from a grounding spot-check. JD: "eval frameworks".
- **nb-llm-pipeline**: embed → LLM-score → LLM same-story judge → push; hand-grading → categorical gate; 4,100+ shadow decisions, shipped live, filler 34% → 4%. JD: "building, tuning, and evolving AI agents in production", "prompt engineering".
- **nb-llm-failure**: 65% failure rate via Langfuse, p95 1,197 vs 16,384 runaways, cap cuts 0% of successes. JD: "reliable" agents, problem-solving in ambiguous environments.
- **nb-fastapi-backend + nb-ownership + nb-eks-standup + nb-swiftui-app + nb-morning-digest**: fused end-to-end bullet. JD: "building and scaling end-to-end production systems".
- **hd-langchain-apis**, **hd-lead-mvp + hd-mentor-process**: leading technical projects; React / Next.js stack.
- **za-mock-interview + za-auth-db**: sole engineer, 0→1 at a VC-backed startup — closest inventory fact to "founding engineer" (not claimed as founder). React stack.
- **za-demos-contracts**: demos to clients, fast iterations on feedback, contracts with mid-sized companies. JD: "comfort working directly with customers", "interfaced with customers".
- **cm-nl-safety**: multi-turn LLMs; fill.
- **pj-codingplans**: model evaluation across providers; tinkerer mindset.
- Coursework: CMU Large Language Model Systems, Distributed Systems, Machine Learning; UW Large Language Models in Practice, Software Engineering, Algorithms.
- Skills: AI & LLMs row first (RAG, hybrid retrieval, LangChain, Langfuse, bge embeddings, DeepSeek / DeepInfra); Languages second with Python, TypeScript, Go up front; React and Next.js lead the frameworks row. JD: "React, TypeScript, and/or Go".

## Items skipped

- **pj-my-av, cm-psc, pj-wisconsin-autonomous, ld-ece-fellow**: no room; not agent work.
- **nb-catalog-cache, nb-cronjob-outage, nb-third-party-proxy, nb-server-driven-ui, nb-live-activities, nb-app-store, nb-ads-max, nb-retired-detector, nb-manual-broadcast, nb-dramabreak-*, nb-jira-process, nb-coaching-marketplace**: less relevant than the LLM/agent items.
- Voice models: no inventory facts; not claimed.

## Constraints nearly violated

- First draft added "45 s" and "streamed over SSE" to the search bullet and spilled the Projects section onto page 2; trimmed the bullet back to two lines.
- First draft put ZenAI (2023) above Haddee (2025); restored reverse-chronological order.
- "Prompt engineering" is not in `inventory/skills.md`, so it is not listed as a skill; the categorical-gate fact sits in the bullet.
- Go and TypeScript are in skills.md but have no supporting bullet; kept in the Languages row only.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, codingplans line): **758.38 pt** from the top.
- Unused height: 792 − 25.92 − 758.38 = **7.70 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, wrapped skill rows, or empty bottom strip.

## Referral notes

Role shortened to "SWE, Agent (New Grad)". No job ID in the posting. Pitch swapped to "I shipped an LLM search agent on a 6K-install sports app." (57 chars, shorter than the default) because the role is agent engineering. Why-this-team draws on the JD's "production-grade AI agents" and direct customer work.
