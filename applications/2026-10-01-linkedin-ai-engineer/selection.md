# Selection — LinkedIn, AI Engineer

## NewsBreak title

**AI Engineer Intern.** The JD is AI / ML as product work: "own end-to-end machine learning systems that run in production", "recommender and classification system", and basic qualifications in "information retrieval or natural language processing". Not AI Infrastructure: the GPU-fleet line is one clause, and the rest is models, experiments, and measured member impact.

## Framing

JD keywords: production ML systems, recommender / classification, information retrieval / NLP, experiments that prove efficacy, measured member impact, efficiency or quality improvement backed by data, root-causing a production regression, PyTorch, AI code tools (Claude Code), data mining.

- Classification / ranking: alert pipeline (LLM scoring, categorical gate, per-topic percentile, LLM same-story judge).
- Experiments / data-backed: production shadow on 4,100+ rows, hand-grading, 127-alert holdout, rejected rule with reach evidence.
- IR: hybrid retrieval, RRF, P@1.
- Regression root-cause: Langfuse 65% failure.
- Efficiency: cache 78×.
- Member impact: digest 5,026 users (~81%), ~6,000 installs, 1,119 peak DAU.
- PyTorch: my-av (two lines).

Header: **Mountain View, CA**. The body lists Sunnyvale / San Francisco / New York City; Bay is allowed.

## Items used

- **nb-llm-pipeline** (three bullets): design (bge, LLM scoring, per-topic 7-day percentile, LLM same-story judge, ~1,200 calls/day); shadow 4,100+ rows, filler 34% → 4% / 29% → 3%, 2/day cap over 11,745 user-days; hand-graded 89 vs 90 → categorical gate, rejected the 91% roundup rule that killed the two highest-reach alerts. "Classifier" describes the `happened / speculative / no_event` categorical scoring.
- **nb-agentic-search**: hybrid Mongo `$text` + bge vector, RRF, bounded tool-calling agent, 0% → 100% P@1, 0.4 ms.
- **nb-llm-failure**: 65%, Langfuse traces, p95 1,197 vs 16,384, binomial 49–66% vs 65%.
- **nb-fastapi-backend + nb-eks-standup + nb-catalog-cache** (fused): first commit → 89 endpoints on EKS, ~1,450 offline tests, cache 78× (13.2 → 10.9 MB shared), 512 MiB pod.
- **nb-swiftui-app + nb-morning-digest** (fused): App Store link, 1.4K App Store ratings (replaces ~6,000 installs, per the updated approved line), 1,119 peak DAU; LLM digest to 5,026 users (~81%).
- **nb-dramabreak-ads** (A/B fact only): "DramaBreak" hyperlinked to its App Store page; A/B test of menu options, click-through rate in Amplitude. No winner, lift, or sample size is recorded, so none is claimed.
- **hd-lead-mvp + hd-langchain-apis** (fused): REST APIs for LangChain resume parsing and AI job matching.
- **za-mock-interview + za-auth-db**: LLM mock-interview app, sole engineer, iterated AI scoring from user testing and with recruiters.
- **cm-nl-safety + cm-psc**: both research bullets (NLP / LLM + Bayesian estimation).
- **pj-my-av** (`pipeline` + `training`, merged into one bullet so it reads as one project): PyTorch, data pipeline, CUDA, Vertex AI, streaming inference.

## Items skipped

- **nb-retired-detector**: strong data story but no room; the holdout / rejected-rule bullet carries that signal.
- **nb-cronjob-outage, nb-third-party-proxy, nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-manual-broadcast, nb-dramabreak-*, nb-coaching-marketplace, nb-jira-process**: not ML.
- **za-demos-contracts, hd-mentor-process, ld-ece-fellow, pj-codingplans, pj-wisconsin-autonomous**: no room.
- Skills dropped: OpenCV, DeepSeek / DeepInfra, frontend / mobile, most infra, certifications.

## Constraints almost violated

- Spark, fine-tuning, student–teacher distillation, recommender model training, GPU fleets, and publications are in the JD but not in inventory; not claimed. The 5% rollout is a blast-radius control, not an A/B test, so it is not described as one.
- First compile was 2 pages (~5 lines over). Cut the scoring detail, the holdout, recency, the Haddee feature list, OpenCV, DeepSeek / DeepInfra, and the my-av frame details. That left 20 pt unused, so I restored the 127-alert holdout clause. Revision (10-02): added the DramaBreak A/B test bullet (newly in inventory) and cut the holdout clause again to make room. "A/B testing" is not in `skills.md`, so it is in a bullet only.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 792 pt tall)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 759.53 pt
- Unused height: 792 − 25.92 − 759.53 = 6.55 pt (passes 0–12 pt)
- Visual review: rendered at 110 dpi; no empty bottom strip, clipping, or overlap; spacing even.
