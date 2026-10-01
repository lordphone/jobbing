# Selection — Citadel, Software Engineer – University Graduate (US)

## NewsBreak title

**Software Engineering Intern** (default). The JD is a general "Software Engineer" posting and does not say SWE, backend, or AI.

## Framing

JD asks for Python (C++ also preferred), "probability and statistics", "high-performance, large data research platforms", distributed computing, NLP, and ML. Bullets lean on Python, measurement-driven decisions, statistical calibration (percentile vs. a rolling 7-day distribution, binomial failure model), performance (cache 78×, 0.4 ms resolver), and research with probabilistic / Bayesian methods. No C++ claim: it is not in inventory.

Header: **Mountain View, CA**. The posting lists New York, Miami, Greenwich, and Houston. The skill's header rule uses New York only for New York-only postings, so the default applies.

## Items used

- **nb-fastapi-backend + nb-ownership + nb-eks-standup**: first commit → 89 endpoints, FastAPI / MongoDB on EKS, ~1,450 fully offline tests, ruff / pyright / pytest gate, 99.7% annotation coverage, 344 PRs.
- **nb-llm-pipeline**: score on arrival, percentile vs. the topic's rolling 7-day score distribution, 4,100+ shadow decision rows, filler 34% → 4% by count.
- **nb-swiftui-app**: sole SwiftUI engineer, App Store link on "SportsBreak", ~6,000 installs, 1,119 peak DAU.
- **nb-retired-detector**: 19 h production data, 901 min p50 vs. 1.8 min, net −882 lines.
- **nb-catalog-cache**: 13.2 MB per user → 10.9 MB shared, 78×, 512 MiB pod, 25–30 requests → 1 call.
- **nb-agentic-search**: 0% → 100% P@1, 0.4 ms, 206 entities, rejected embeddings after measuring, hybrid RRF.
- **nb-llm-failure**: 65% failure via Langfuse, p95 1,197 vs. 16,384, binomial model 49–66% vs. 65% observed.
- **hd-lead-mvp + hd-langchain-apis** (fused into one bullet).
- **za-mock-interview + za-demos-contracts** (fused into one bullet).
- **cm-psc + cm-nl-safety**: probabilistic safety certificate for stochastic systems, outperformed Adaptive MPC; Bayesian estimators, LuGre, multi-turn LLM to formal specs. Kept for "probability and statistics" and NLP.
- **pj-my-av**, **pj-wisconsin-autonomous**.
- Coursework: CMU Distributed Systems, Machine Learning, Data Science for SE; UW Algorithms, Operating Systems, Computer Architecture.
- Skills: Python and C first; Data & ML second. Dropped HTML, CSS, Firebase, Jira, and certifications.

## Items skipped

- **nb-cronjob-outage, nb-live-activities, nb-third-party-proxy, nb-server-driven-ui, nb-app-store, nb-ads-max, nb-morning-digest, nb-manual-broadcast, nb-dramabreak-*, nb-jira-process, nb-coaching-marketplace**: lower value for a trading-tech JD.
- **hd-mentor-process, za-auth-db**: cut to one bullet per role to make room for research.
- **ld-ece-fellow**: lower value than the two technical projects; section renamed "Projects".
- UW Data Structure & Programming III: dropped because it wrapped onto its own line.

## Constraints nearly violated

- C++ is the JD's first language, but it is not in `inventory/skills.md`, so it is not listed.
- First compile spilled onto two pages; cut the SwiftUI line and a skills row, then restored both after tightening three one-word orphan lines.
- Spacing (`itemsep=0.7pt`), margins, and font size are unchanged from the template.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, "Jetson." line): **761.86 pt** from the top.
- Unused height: 792 − 25.92 − 761.86 = **4.22 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, orphan words, or empty bottom strip.

## Referral notes

Role shortened to "SWE University Grad". No job ID. Default pitch. The why-this-team line uses the JD's "high-performance, large data research platforms".
