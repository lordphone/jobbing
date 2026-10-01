# Selection — Google, Software Engineer, Early Career, Campus

Base: `2026-09-24-visa-software-engineer-new-college-grad-2027/resume.tex` (closest general-SWE new-grad version), re-aimed at Google's qualifications.

## NewsBreak title

**Software Engineering Intern** — the JD is "Software Engineer, Early Career"; general SWE with no single specialty.

## JD targets and where they land

- Min qual "AI productivity tools to streamline development workflows" → nb-catalog-cache fact: "cache code was written by an AI agent; the code was clean and he wrote tests for it" → "had an AI coding agent write the cache and verified it with my own tests."
- Min qual "data structures or algorithms" → UW Algorithms, Data Structure & Programming III; cache re-keying; RRF fusion.
- Min qual languages (Python, C, C++, Java, JavaScript) → Languages row reordered Python, Java, C, JavaScript first. C++ is not in inventory; not added.
- Preferred "information retrieval / NLP" → nb-agentic-search (hybrid retrieval, RRF, entity resolution P@1) and nb-llm-pipeline; new "ML & Retrieval" skills row.
- Preferred "Unix/Linux" → Linux, Bash lead the "Systems & Cloud" row.
- Preferred "distributed and parallel systems / large software systems" → CMU Distributed Systems; EKS backend; CronJob outage.
- Preferred "mobile application development" → nb-swiftui-app.
- Preferred "security software development" → nb-third-party-proxy (zero third-party API credentials in the binary).
- Preferred "machine learning" → CMU Machine Learning; my-av.
- Preferred "accessible technologies" → nothing in inventory; not claimed.

## Items used

- nb-fastapi-backend + nb-ownership (344 PRs, 340 merged) + nb-eks-standup (EKS, CI gate)
- nb-swiftui-app (sole SwiftUI, ~6,000 installs, 1,119 peak DAU) + nb-third-party-proxy
- nb-agentic-search (hybrid substring / full-text / vector with RRF, ≤3 hops / 45 s tool loop, SSE, server-resolved citations, 0% → 100% P@1)
- nb-llm-pipeline (shadow variant: 4,100+ decisions, filler 34% → 4%)
- nb-catalog-cache (25–30 → 1 call, 78×, 512 MiB pod, AI-agent-written code verified with his tests)
- nb-cronjob-outage + nb-llm-failure (backend variant)
- hd-lead-mvp + hd-mentor-process fused; hd-langchain-apis
- za-mock-interview; za-demos-contracts fused with the iteration bullet
- pj-my-av, ld-ece-fellow, pj-wisconsin-autonomous (default wording)
- Coursework: CMU Distributed Systems, Machine Learning, Large Language Model Systems; UW Algorithms, Data Structure & Programming III, Operating Systems

## Items skipped

- nb-dramabreak-stripe — payments are Visa-specific; mobile + security bullet fits Google better.
- nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-dramabreak-ads — lower value than the picks; no room.
- nb-jira-process, nb-coaching-marketplace, nb-morning-digest, nb-manual-broadcast, nb-retired-detector — no room.
- cm-psc, cm-nl-safety (research) — Research section costs ~5 lines; the page is full with work bullets that hit more JD targets.
- Mobile Computing Laboratory (UW) — wrapped to an orphan line; cut.
- Jenkins, MySQL, and non-JD skills — cut to keep skill rows on one line.

## Constraints nearly violated

- First draft spilled one line onto page 2 → trimmed UW coursework and the search bullet.
- Next draft ran 1 pt past the bottom margin (Wisconsin line wrapped) → shortened the CronJob bullet to two lines.
- 12.38 pt unused after content was exhausted → local `\setlist*[itemize]{itemsep=0.7pt}` (shared default 0.5 pt), same as the Visa resume. Margins and font size unchanged.
- "bge" dropped from the search bullet for length; "vector" is still true.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax): **755.49 pt** from top.
- Unused height: 792 − 25.92 − 755.49 = **10.59 pt** (passes the 0–12 pt check).
- Rendered at 90 dpi and inspected the whole page: no clipping, overlap, cramped text, or empty bottom strip.

## Referral notes

Role shortened to "SWE Early Career". Posting shows no job ID, so it was dropped. Default pitch. Why-this-team line is about his interest (search/retrieval, from the JD's preferred areas), not an invented team detail.
