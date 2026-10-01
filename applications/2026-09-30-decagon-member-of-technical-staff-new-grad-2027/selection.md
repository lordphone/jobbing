# Selection — Decagon, Member of Technical Staff, New Grad (2027 Start)

## NewsBreak title

**AI Engineer Intern.** Every team "builds the systems behind Decagon's AI agents", and Agent Orchestration "turns workflows, tools and guardrails into a reliable, low-latency" agent runtime — AI agents as product work. Software Engineering Intern was the alternative, since the requirements themselves are general (Python, TypeScript, async, debugging deep stacks).

Header: Mountain View, CA (SF or NYC; SF allowed).

## Items used

- **nb-agentic-search** (design / grounded / entities): one SSE endpoint, deterministic RAG turn 1 over hybrid RRF retrieval, bounded tool-use agent (≤3 hops, 5 tools, 45 s), server-resolved citations, 0% → 100% P@1. JD: Agent Orchestration "workflows, tools and guardrails".
- **nb-llm-pipeline**: embed → LLM-score → LLM same-story judge → APNs as a Kubernetes CronJob, production shadow, live, filler 34% → 4%. JD: "data pipelines, or production infrastructure", shipping products.
- **nb-llm-failure + nb-cronjob-outage + nb-eks-standup (day3)**: fused into one debugging bullet — 65% failure rate in async LLM workers (asyncio.gather batch) via Langfuse, p95 1,197 vs 16,384 runaways; 5-day CronJob outage (ImagePullBackOff + Forbid); DNS → TLS → admission-policy chain. JD: "digging into system failures across deep technology stacks using whatever tool the problem calls for".
- **nb-fastapi-backend + nb-eks-standup + nb-catalog-cache**: async FastAPI / Motor backend from first commit to 89 endpoints on EKS, ~1,450 offline tests, ruff / pyright / pytest gate; AI-agent-written per-user cache re-keyed to shared (78×) as memory neared 512 MiB. "With AI coding agents" grounded in the newsbreak.md note that the intern work was written with AI and the cache fact. JD: "asynchronous programming", "AI coding agents as part of development".
- **nb-swiftui-app + nb-ownership + nb-morning-digest**: sole SwiftUI engineer for SportsBreak (hyperlinked, ~6,000 installs, peak DAU 1,119), 344 PRs (340 merged) across five repos, LLM digest to 5,026 users.
- **hd-lead-mvp + hd-mentor-process**, **hd-langchain-apis** (short): 0→1. JD: "0→1 product-building experience".
- **za-mock-interview + za-auth-db**, **za-demos-contracts**: 0→1 sole engineer; recruiter-aligned scoring, user-testing iteration, contracts. Parallels Agent Engineering's direct customer work.
- **cm-nl-safety**: fill; multi-turn LLMs.
- **pj-my-av** (short + streaming inference): closest inventory item to "multi-modal models" (video model), but not claimed as multimodal.
- Coursework: CMU Distributed Systems, Large Language Model Systems, Machine Learning; UW Operating Systems, Large Language Models in Practice, Algorithms.
- Skills: Languages first (Python, TypeScript lead), Frameworks & Data second with Motor / async MongoDB.

## Items skipped

- **nb-third-party-proxy, nb-server-driven-ui, nb-live-activities, nb-app-store, nb-ads-max, nb-retired-detector, nb-manual-broadcast, nb-dramabreak-*, nb-jira-process, nb-coaching-marketplace**: lower value for an agent-platform JD; no room.
- **cm-psc**: control theory, less relevant.
- **pj-codingplans**: used at Abridge for evaluation; my-av fit "multi-modal" better here and only one project line fits.
- **ld-ece-fellow, pj-wisconsin-autonomous**: not relevant; no room.
- Skills dropped: PyTorch (wrapped the AI row; it is in the my-av bullet), mobile ad stack, Terraform, Express, Tailwind, Jira, etc.

## Constraints nearly violated

- First compile spilled the Projects section onto page 2; shortened the alert bullet (dropped 4,100+ decisions and the gate detail), Haddee API bullet, and ZenAI second bullet.
- The AI & LLMs skills row wrapped with PyTorch; removed it, then restored the fuller ZenAI recruiter / user-testing bullet to fill the freed line.
- No inventory evidence of multi-modal model work; not claimed. No named AI coding tool in skills.md, so no tool name is printed.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, my-av line): **757.66 pt** from the top.
- Unused height: 792 − 25.92 − 757.66 = **8.42 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, wrapped skill rows, or empty bottom strip.

## Referral notes

Role shortened to "MTS New Grad". No job ID (Ashby UUID is not a printed ID). Pitch: "I shipped LLM search and alerts on a 6K-install sports app." (same length as default; JD centers on shipped AI agents). Why-this-team uses Agent Orchestration's "reliable, low-latency" runtime.
