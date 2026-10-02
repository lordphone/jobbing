# Selection — Perplexity, Member of Technical Staff (New Grad) - CMU 2026-2027

## NewsBreak title

**AI Engineer Intern.** New grads "work across the stack, from Perplexity's agent harnesses to our AI inference and training systems": AI and agents as product work at an answer-engine company. I considered AI Infrastructure Intern for "inference and training systems", but the JD leads with agent harnesses, and his strongest match is the agentic search product work.

Header: Mountain View, CA (San Francisco role).

## Base

Built from the Decagon MTS resume (2026-09-30). It's also an AI-agent MTS posting, and its bullets already lead with agentic search, which is the closest work to Perplexity's product (cited LLM answers over retrieval).

## Items used

- **nb-agentic-search** (design / grounded / entities): one SSE endpoint, deterministic RAG on turn 1 over hybrid RRF retrieval, a bounded tool-use agent (≤3 hops, 5 tools, 45 s), server-resolved citations, 0% → 100% P@1. JD: "agent harnesses". It also matches Perplexity's cited-answer product directly.
- **nb-llm-pipeline**: embed → LLM-score → LLM same-story judge → APNs as a Kubernetes CronJob, shadowed in production and shipped live; filler 34% → 4%.
- **nb-llm-failure + nb-cronjob-outage + nb-eks-standup (day3)**: fused debugging bullet. JD: "Depth: dive deep into whatever problem domains you work on".
- **nb-fastapi-backend + nb-eks-standup + nb-catalog-cache**: backend from its first commit to 89 endpoints on EKS, ~1,450 offline tests, cache re-keyed 78× smaller.
- **nb-swiftui-app + nb-ownership + nb-morning-digest**: SportsBreak (hyperlinked), 344 PRs, LLM digest to 5,026 users. JD: "Breadth: work across the stack".
- **hd-lead-mvp + hd-mentor-process**, **hd-langchain-apis**; **za-mock-interview + za-auth-db**, **za-demos-contracts**: same as the Decagon base.
- **cm-nl-safety**: multi-turn LLMs; the JD welcomes "advanced coursework in ... AI/ML" and rigor.
- **pj-codingplans** (rewritten shorter): KV caching, long context, needle-in-a-haystack, quantization. These are the closest inventory facts to "AI inference ... systems". It replaces my-av from the base.
- Coursework: CMU Distributed Systems, Large Language Model Systems, Machine Learning (systems + AI/ML, which the JD names); UW Algorithms moved first (the JD's qualifying courses are all algorithms), then Operating Systems and Large Language Models in Practice.
- Skills: unchanged from the base. The JD names no specific tools, so Languages and Frameworks & Data stay in the first two rows.

## Items skipped

- **pj-my-av**: training-side work, but only one project line fits and codingplans speaks to inference. I'd swap it back if Perplexity's training team is the target.
- **nb-third-party-proxy, nb-server-driven-ui, nb-live-activities, nb-app-store, nb-ads-max, nb-retired-detector, nb-manual-broadcast, nb-dramabreak-*, nb-jira-process, nb-coaching-marketplace**: lower value here; no room.
- **cm-psc, ld-ece-fellow, pj-wisconsin-autonomous**: less relevant; no room.
- UW Computer Architecture: adding it pushed the page to 2.

## Constraints nearly violated

- The first compile spilled to page 2: adding Computer Architecture wrapped the UW coursework line, and the codingplans approved line runs to 3 lines. I dropped Computer Architecture and rewrote codingplans to fit 2 lines with the same facts.
- There's no 15-451/651/750/850 grade in inventory, so none is claimed. The resume does not address the qualification criteria; that belongs in the form's "Anything Else" answer.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, codingplans line): **757.77 pt** from the top.
- Unused height: 792 − 25.92 − 757.77 = **8.31 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, wrapped skill rows, or empty bottom strip.

## Referral notes

The role is shortened to "MTS New Grad". There's no job ID (the Ashby UUID is not a printed ID). Pitch: "I shipped cited LLM search on a 6K-install sports app." (shorter than the default; Perplexity is a cited-answer search product). Why-this-team uses the JD's "agent harnesses" and "inference" systems.
