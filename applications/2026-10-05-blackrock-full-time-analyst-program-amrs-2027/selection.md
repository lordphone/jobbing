# Selection — BlackRock, 2027 Full-Time Analyst Program - AMRS

Target function: **Technology**, with Analytics & Risk / modeling as the likely second choice. The JD lists no stack, so this leans on what BlackRock tech hires for: Python/Java, data, reliability, and measured, quantitative decisions.

## NewsBreak title

**Software Engineering Intern**: the default. The JD is a general analyst program with no backend, full-stack, or AI focus to match a more specific title.

## Header

Mountain View, CA. The posting lists San Francisco, Santa Monica, Sausalito, and Seattle alongside New York, so a Bay option exists.

## Items used

- **nb-fastapi-backend + nb-eks-standup**: bullet 1, covering the backend from its first commit, 89 REST endpoints, EKS, ~1,450 offline tests, and the ruff / pyright / pytest gate.
- **nb-llm-pipeline**: bullet 2, covering production-shadow calibration on 4,100+ decision rows, filler 34% → 4% by count, and zero cap violations over 11,745 user-days. This is the quantitative, data-driven bullet ("passionate about performance").
- **nb-dramabreak-stripe + nb-third-party-proxy**: bullet 3, the signature-verified idempotent payment webhook and zero third-party keys. These are payments and security, the closest fit to a fiduciary/fintech reader.
- **nb-catalog-cache**: bullet 4, covering 25–30 requests → 1 call and a cache that could never hit becoming a shared 10.9 MB one, 78× smaller.
- **nb-llm-failure + nb-cronjob-outage**: bullet 5, covering the 65% failure rate traced via Langfuse, a token cap sized against p95 output, and the 5-day CronJob outage fixed with paired deadlines.
- **nb-ownership + nb-swiftui-app + nb-jira-process (incl. audit)**: bullet 6, covering sole SwiftUI, ~6,000 installs, peak DAU 1,119, 344 PRs (340 merged), the Jira backlog, two security tickets reopened with evidence, and onboarding ("emotional ownership").
- **hd-lead-mvp + hd-langchain-apis**: one Haddee line.
- **za-mock-interview + za-demos-contracts**: one ZenAI line.
- **cm-psc + cm-nl-safety (Bayesian estimators only)**: one research line. Probabilistic and Bayesian work fits Analytics & Risk.
- **ld-ece-fellow**: leadership line.
- Skills: Python, Java, SQL lead. The Data & ML row comes second.
- Coursework: Distributed Systems, Machine Learning, Data Science for SE, Foundations of SE (CMU); Algorithms, OS, Software Engineering, LLMs in Practice (UW).

## Skipped

- nb-agentic-search: strong, but AI-search-specific and space was short. The LLM pipeline bullet carries the data story better for this reader.
- hd-mentor-process, za-auth-db (beyond the one line), the second research fact (NL → specs): cut to fit one page.
- pj-codingplans: cut to fit one page.
- nb-server-driven-ui, nb-live-activities, nb-ads-max, nb-app-store, nb-morning-digest, nb-manual-broadcast, nb-dramabreak-ads, nb-coaching-marketplace, nb-retired-detector: mobile, ads, or covered elsewhere.
- pj-my-av, pj-wisconsin-autonomous: off JD.

## Constraints nearly violated

- The first draft ran to two pages (skills and projects spilled). It was cut to one page by trimming the lowest-value lines and then refilled with the cache bullet and a Practices skills row.
- Skills use only inventory names. Nothing finance-specific (e.g., Aladdin, Excel) was added because none is in inventory.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, ECE Fellow line): **759.16 pt** from the top.
- Unused height: 792 − 25.92 − 759.16 = **6.92 pt** (passes 0–12 pt).
- Rendered at 90 dpi and inspected: no clipping, overlap, cramped text, or empty bottom strip.
