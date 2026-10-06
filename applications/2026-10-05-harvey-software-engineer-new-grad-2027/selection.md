# Selection — Harvey, Software Engineer, New Grad (2027)

## NewsBreak title

**Software Engineering Intern.** The posting is a general "Software Engineer, New Grad" role that ships code "across the stack" with team matching after hire (Frontend, Backend, Full-Stack, Infrastructure, Applied AI). AI Engineer Intern was the alternative given "retrieval, document intelligence", but the role title and team spread favor the default.

Header: Mountain View, CA (SF or NYC office; SF allowed).

## Items used

- **nb-agentic-search** (design / grounded): one SSE endpoint, deterministic RAG over hybrid retrieval (substring + Mongo `$text` + bge vectors, RRF), bounded tool-use agent (≤3 hops, 5 tools, 45 s), server-resolved citations. JD: "retrieval over large document collections", "interfaces for collaborating with AI systems".
- **nb-agentic-search** (entities + eval facts): eval harness on real logged queries, 0% → 100% P@1 at 0.4 ms after measurements ruled out embeddings, 23 grounding problems. JD: "evaluate cutting-edge LLMs", Simplicity (simplest solution that works).
- **nb-llm-pipeline** (gate / shadow, shortened): embed → LLM-score → LLM same-story judge → push, categorical gate after hand-grading, production shadow, live, filler 34% → 4%.
- **nb-fastapi-backend + nb-catalog-cache**: built with AI coding tools; 89 endpoints on EKS, ~1,450 offline tests, ruff / pyright / pytest gate; re-keyed an agent-written cache (78×). JD: "own the quality of everything you ship—AI-generated or not". "With AI coding tools" grounded in newsbreak.md (intern work written with AI; cache written by an AI agent).
- **nb-third-party-proxy + nb-jira-process (audit)**: zero API credentials in the iOS binary; reopened two closed security tickets with line-level evidence. JD: "security standards", "secure systems for sensitive client data", Job's Not Finished.
- **nb-swiftui-app + nb-ownership + nb-morning-digest**: sole SwiftUI engineer (hyperlinked SportsBreak), ~6,000 installs, peak DAU 1,119, primary backend author, 344 PRs (340 merged), digest to 5,026 users. JD: Mobile team, "across the stack".
- **hd-lead-mvp + hd-langchain-apis + hd-mentor-process**: fused into one line (0→1, schemas / REST APIs for LangChain features, PR reviews). JD: code reviews.
- **za-mock-interview + za-auth-db**, **za-demos-contracts**: sole engineer 0→1 at a VC-backed accelerator startup; recruiter-aligned scoring, client iteration, three 200–500-person contracts. JD: "internship experience at an early-stage startup is a plus", cross-functional work.
- **cm-nl-safety**: fill; multi-turn LLMs.
- **pj-codingplans**: JD "experiment with and evaluate cutting-edge LLMs".
- Coursework: CMU Large Language Model Systems, Distributed Systems, Foundations of Software Engineering; UW Large Language Models in Practice, Software Engineering, Algorithms, Operating Systems.
- Skills: Languages first (Python, TypeScript, JavaScript, Go, Java match the JD list); AI row second with "Claude Code / AI coding tools" (JD names Claude Code).

## Items skipped

- **nb-llm-failure**: cut for space (first draft ran to two pages); Langfuse dropped from skills with it.
- **nb-eks-standup, nb-cronjob-outage, nb-server-driven-ui, nb-live-activities, nb-app-store, nb-ads-max, nb-retired-detector, nb-manual-broadcast, nb-dramabreak-*, nb-coaching-marketplace**: lower value for this JD; no room.
- **cm-psc**: control theory, less relevant than cm-nl-safety.
- **pj-my-av, pj-wisconsin-autonomous, ld-ece-fellow**: less relevant; no room.

## Constraints nearly violated

- First compile spilled ~10 lines to page 2. Cut the 65% failure bullet, merged the two Haddee bullets, shortened the alert bullet, and temporarily removed Research; then restored Research to fill a 55 pt gap.
- Skills row printed "Claude Code" alone at one point; changed back to the exact skills.md name "Claude Code / AI coding tools" and dropped Langfuse / LangChain from that row so it stays one line.
- ZenAI line briefly said "early-stage startup"; reverted to inventory's "VC-backed startup".
- Search bullet says "keyword, full-text, and bge vectors" for substring + Mongo `$text` + bge vector legs.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, codingplans line): **759.05 pt** from the top.
- Unused height: 792 − 25.92 − 759.05 = **7.03 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, wrapped skill rows, or empty bottom strip.

## Referral notes

Role shortened to "SWE New Grad". No job ID (Ashby UUID is not a printed ID). Pitch: "I shipped LLM search and alerts on a 6K-install sports app." (same length as the default; Harvey's work is retrieval and LLM product). Why-this-team uses the JD's "retrieval over large document collections".
