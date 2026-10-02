# Selection — Goldman Sachs, 2027 Engineering New Analyst (New York)

## NewsBreak title

**Software Engineering Intern** (default). The JD is a general Engineering Division analyst program ("build massively scalable software and systems"); it does not say SWE, backend, or AI specifically.

## Framing

The JD names scalable software and systems, low-latency infrastructure, guarding against cyber threats, machine learning, risk management, big data, and mobile. Bullets lean on the scalable backend, the production EKS service, credentials removed from the client (security), cache/latency work, ML/LLM work with statistical calibration, and the shipped iOS app (mobile). Built from the Citadel resume (closest finance-tech template).

Header: **New York, NY**. The posting is New York only with no Bay option.

## Items used

- **nb-fastapi-backend + nb-ownership**: first commit → 89 endpoints, FastAPI / MongoDB, ~1,450 fully offline tests, ruff / pyright / pytest gate, 99.7% annotation coverage, 344 PRs.
- **nb-eks-standup + nb-third-party-proxy** (fused): production EKS (Helm, Jenkins) on day 3; nine integrations moved server-side, zero third-party API credentials in the iOS binary. Picked for "infrastructure" and "guard against cyber threats".
- **nb-catalog-cache**: 13.2 MB per user → 10.9 MB shared, 78×, 512 MiB pod, 25–30 requests → 1 call. Picked for "low latency" / "scalable".
- **nb-llm-pipeline**: score on arrival, percentile vs. the topic's rolling 7-day distribution, 4,100+ shadow decisions, filler 34% → 4%. Picked for "machine learning … turn data into action".
- **nb-swiftui-app**: sole SwiftUI engineer, App Store link on "SportsBreak", ~6,000 installs, 1,119 peak DAU. Picked for "mobile".
- **nb-agentic-search**: 0% → 100% P@1, 0.4 ms, 206 entities, rejected embeddings after measuring, hybrid RRF.
- **nb-llm-failure**: 65% failure via Langfuse, p95 1,197 vs. 16,384, binomial model 49–66% vs. 65% observed.
- **hd-lead-mvp + hd-langchain-apis** (fused).
- **za-mock-interview + za-demos-contracts** (fused).
- **cm-psc + cm-nl-safety**: probabilistic safety / Bayesian estimation — kept as risk-adjacent fill.
- **pj-my-av**, **pj-wisconsin-autonomous**.
- Coursework: CMU Distributed Systems, Machine Learning, Data Science for SE; UW Algorithms, Operating Systems, Computer Architecture.
- Skills: Languages (Java moved up for bank stacks) and Cloud & Infra in the first two rows; added Langfuse, SwiftUI. Dropped HTML, CSS, OpenCV, Firebase, Jira, certifications.

## Items skipped

- **nb-retired-detector**: swapped out for the EKS + credentials bullet, which maps to infra and cyber language in the JD.
- **nb-cronjob-outage, nb-live-activities, nb-server-driven-ui, nb-app-store, nb-ads-max, nb-morning-digest, nb-manual-broadcast, nb-dramabreak-*, nb-jira-process, nb-coaching-marketplace**: lower value for this JD; no room.
- **hd-mentor-process, za-auth-db**: one bullet per role to keep research.
- **ld-ece-fellow, pj-codingplans**: lower value than the two technical projects.

## Constraints nearly violated

- The JD mentions "financial engineering" and "risk management"; no finance experience is in inventory, so none is claimed.
- Spacing (`itemsep=0.7pt`), margins, and font size unchanged from the template.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, "Jetson." line): **761.86 pt** from the top.
- Unused height: 792 − 25.92 − 761.86 = **4.22 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, or empty bottom strip.

## Referral notes

Role shortened to "Engineering New Analyst" ("Eng New Analyst" in the UW note, which was 303 otherwise). Job ID 171569 from the apply URL. Default pitch. Why-this-team line uses the JD's "massively scalable" and "low latency".
