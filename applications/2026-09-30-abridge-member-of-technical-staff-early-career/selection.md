# Selection — Abridge, Member of Technical Staff, Early Career

## NewsBreak title

**AI Engineer Intern.** The JD says "GenAI is at the center of everything we build" and asks for agentic LLM systems, retrieval pipelines, structured tool use, chained LLM workflows, and evaluation frameworks — AI / LLM / agents as product work. Software Engineering Intern was the alternative (the JD calls the hires "Software Engineers"), but the asks are LLM-specific throughout.

Header: Mountain View, CA (SF on-site 5 days).

## Items used

- **nb-agentic-search** (design / grounded): deterministic RAG turn 1, hybrid retrieval fused with RRF, bounded tool-use agent (≤3 hops, 5 tools), server-resolved citations the model cannot author. JD: "retrieval pipelines, structured tool use"; echoes Linked Evidence / mapping summaries to ground truth.
- **nb-agentic-search** (entities / eval): eval harness on real logged queries, 0% → 100% P@1 at 0.4 ms, embeddings rejected with measurements, 23 problems from a manual grounding spot-check. JD: "evaluation frameworks… automated pipelines and human-in-the-loop review".
- **nb-llm-pipeline**: chained embed → LLM-score → LLM same-story judge → push; hand-graded alerts at ~90 for both filler and real events → categorical gate; 4,100+ shadow decisions, shipped live, filler 34% → 4%. JD: "chained LLM workflows", "failure modes", "where the human in the loop is critical".
- **nb-llm-failure**: 65% failure rate via Langfuse traces, p95 1,197 vs 16,384 runaways, token cap sized to truncate 0% of observed successes. JD: "monitoring and observability… LLM workflows healthy in production".
- **nb-fastapi-backend + nb-ownership + nb-eks-standup + nb-swiftui-app + nb-morning-digest**: fused into one bullet — FastAPI / MongoDB from first commit, 89 endpoints on AWS EKS, ~1,450 offline tests, ruff / pyright / pytest gate, 344 PRs (340 merged); sole SwiftUI engineer for SportsBreak (~6,000 installs, hyperlinked); LLM digest reached 5,026 users. JD: "backend and frontend systems".
- **hd-langchain-apis** (first, since the JD names LangChain), **hd-lead-mvp + hd-mentor-process**.
- **za-mock-interview + za-auth-db**, **za-demos-contracts**: working with recruiters so scoring matched real hiring parallels working with clinicians as domain experts.
- **cm-nl-safety**: multi-turn LLMs mapping natural language to formal specs; kept as fill and LLM-relevant.
- **pj-codingplans**: model evaluation and failure modes (caching nerfs, quantization). JD: "curiosity about model evaluation, failure modes".
- Coursework: CMU Large Language Model Systems, Machine Learning, Data Science for Software Engineering; UW Large Language Models in Practice, Software Engineering, Algorithms.
- Skills: AI & LLMs row first (LangChain, RAG, hybrid retrieval, bge embeddings, Langfuse, DeepSeek / DeepInfra), Languages second.

## Items skipped

- **pj-my-av**: tried; spilled one line onto page 2. Not LLM work.
- **cm-psc**: control theory; less relevant than cm-nl-safety.
- **ld-ece-fellow, pj-wisconsin-autonomous**: no room; not relevant.
- **nb-catalog-cache, nb-cronjob-outage, nb-third-party-proxy, nb-server-driven-ui, nb-live-activities, nb-app-store, nb-ads-max, nb-retired-detector, nb-manual-broadcast, nb-dramabreak-*, nb-jira-process, nb-coaching-marketplace**: lower value for an LLM-product JD.
- Skills dropped: RRF (in a bullet already; unwrapped the AI row), PyTorch, Express, Tailwind, mobile ad stack, Terraform, etc.

## Constraints nearly violated

- First draft ran ~14 lines onto page 2; tightened NB bullets to two lines, fused backend + iOS, then re-added research and filled the last line with shadow-calibration and CI facts.
- Briefly printed "DeepInfra" alone in skills; restored the inventory name "DeepSeek / DeepInfra".
- The "know when to trust AI vs. verify" ask is not claimed on the resume; inventory facts about AI-written code (catalog cache) include a bug that reached production, so it is better left for interview stories.
- No LlamaIndex in inventory; not claimed.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, "models." in codingplans): **758.38 pt** from the top.
- Unused height: 792 − 25.92 − 758.38 = **7.70 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, wrapped skill rows, or empty bottom strip.

## Referral notes

Role shortened to "MTS, Early Career". No job ID in the posting (the Ashby URL UUID is not a printed ID). Pitch swapped to "I shipped LLM search and alerts on a 6K-install sports app." (59 chars, same as the default) because the JD centers on shipped GenAI work. Why-this-team uses the JD's "maps AI-generated summaries to ground truth".
