# Selection — Superhuman, Software Engineer, Early Career

## NewsBreak title

**Software Engineering Intern.** Posting title is "Software Engineer, Early Career" — general SWE across Grammarly, Coda, Mail, and Go. The JD leans AI-native, but AI is one part of a general product-engineering role, so the default title fits better than AI Engineer Intern.

Header: Mountain View, CA (posting allows the San Francisco hub).

## Items used

- **nb-fastapi-backend**: first commit → 89 endpoints, 27 routers, 26 collections (~48 indexes), ~1,450 fully-offline tests (0.17 s; 1:1 with production lines), ruff / pyright / pytest gate; "with AI coding tools" from the NewsBreak header note (intern work written with AI). JD: "AI coding agents", "databases, and back-end architecture", "testing frameworks".
- **nb-agentic-search**: deterministic RAG, hybrid retrieval (keyword, full-text, bge, RRF), bounded tool-use agent, SSE streaming, server-resolved citations, 100% P@1. JD: "AI-native features that leverage large language models".
- **nb-llm-pipeline**: embed → LLM-score → LLM same-story judge → push, production shadow on 4,100+ decisions, filler 34% → 4%. JD: "intelligent automation".
- **nb-catalog-cache + nb-eks-standup**: 25–30 request fan-out → 1 call, shared 10.9 MB cache 78× smaller than per-user key; production AWS EKS (Helm, Jenkins) day 3. JD: "large-scale distributed systems", "scalability", "deployment".
- **nb-llm-failure + nb-cronjob-outage**: 65% LLM failure rate via Langfuse as an unbounded reasoning loop; 5-day silent CronJob outage, paired deadlines. JD: "highly available and reliable".
- **nb-swiftui-app + nb-ownership + nb-jira-process**: sole SwiftUI engineer (SportsBreak hyperlinked), ~6,000 installs, peak DAU 1,119, primary backend author, 344 PRs (340 merged), 34 API specs, ~10,000 lines of docs, onboarded the next engineer. JD: "shipping projects end-to-end", "work independently".
- **hd-lead-mvp (agile) + hd-langchain-apis**, **hd-mentor-process**: React / Next.js, LangChain, Git workflows, PR reviews. JD: React, LangChain, Git.
- **za-mock-interview + za-auth-db**, **za-demos-contracts**: React / Next.js / PostgreSQL LLM web app; recruiter collaboration. JD: modern web frameworks, cross-functional collaboration.
- **pj-codingplans**: AI-native; tests LLM coding plans.
- **pj-my-av (short, + streaming inference)**: PyTorch (JD nice-to-have).
- **ld-ece-fellow**: communication / cross-functional; fill.
- Coursework: CMU Large Language Model Systems, Distributed Systems, Foundations of Software Engineering; UW Algorithms, Data Structure & Programming III, Large Language Models in Practice (data structures + algorithms are JD must-haves).
- Skills: Languages first (Python, TypeScript, JavaScript, Java, Go — the JD's list minus C++, which is not in skills.md); AI & LLMs second, led by Claude Code / AI coding tools (JD names Claude Code), plus LangChain and PyTorch (JD nice-to-haves).

## Items skipped

- **cm-nl-safety / cm-psc (Research)**: first compile with Research spilled to two pages; least relevant to a product SWE role, so cut in favor of my-av (PyTorch) and the ECE Fellow line.
- **nb-third-party-proxy, nb-server-driven-ui, nb-live-activities, nb-app-store, nb-ads-max, nb-retired-detector, nb-manual-broadcast, nb-morning-digest, nb-dramabreak-*, nb-coaching-marketplace**: lower value here or no room.
- **pj-wisconsin-autonomous**: embedded; not relevant.

## Constraints nearly violated

- Node.js, Cursor, Codex, OpenAI, TensorFlow, and C++ appear in the JD but not in skills.md; not added.
- Operating Systems coursework and the extra backend facts each pushed the last line 0.08 pt into the bottom margin; kept the backend facts, dropped Operating Systems, and removed one `\vspace{1pt}` before the ZenAI role (no other spacing changes; margins and font size unchanged).

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**.
- Bottom margin (shared/preamble.tex): 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, ECE Fellow line): **765.17 pt** from the top.
- Unused height: 792 − 25.92 − 765.17 = **0.91 pt** (passes 0–12 pt).
- Visual review at 110 dpi: full page, no empty bottom strip, no clipping, overlap, or cramped text.
