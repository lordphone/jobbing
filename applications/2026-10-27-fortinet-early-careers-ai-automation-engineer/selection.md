# Selection — Fortinet Early Careers: AI Automation Engineer (24771)

## NewsBreak title
**AI Engineer Intern**: the JD is LLM pipelines as product work ("design prompts and pipelines for summarization, classification, retrieval, and scoring", "calibrate against human-graded samples", "built with AI models, not just used AI products").

Heading: plain "NewsBreak" (internal automation team, not 0→1 ventures).

## Used
- nb-llm-pipeline → NB 1 (pipeline as CronJob, decision log, 11-day production shadow, 4,100+ decisions, filler 34% → 4%). Matches "auditable workflows", "ship only when it meets the quality bar".
- nb-llm-pipeline (hand-grading facts) → NB 2 (median 89 vs 90, categorical gate, 127-alert holdout, rejected the 91% roundup rule that killed the two highest-reach real alerts). Matches "calibrate against human-graded samples", "catch the ways these systems get things wrong".
- nb-agentic-search → NB 3 (deterministic RAG turn 1, capped tool agent, 5 tools / ≤3 hops, server-resolved citations, 20/20, eval harness on the real catalog). Matches retrieval, "keep deterministic logic where possible", "measure against ground truth".
- nb-fastapi-backend + nb-ownership → NB 4 (sole backend author, SportsBreak link, ~6,000 installs, 89 endpoints on EKS, ~1,450 offline tests, ruff/pyright/pytest CI, Motor fake reproducing production failure as regression guard). Matches FastAPI, testing/fixtures/regression coverage, CI.
- nb-third-party-proxy + nb-observability + nb-cronjob-outage → NB 5 (nine integrations server-side, zero API keys in binary; Prometheus/Grafana; 5-day CronJob outage). Matches secrets management, observability, cron jobs, API integrations.
- nb-llm-failure (backend variant + p95 sizing) → NB 6. Matches debugging LLM pipelines via logs/traces.
- hd-langchain-apis → Haddee 1 (schemas, REST APIs, LangChain features, reviewed API structure).
- hd-lead-mvp + hd-mentor-process → Haddee 2 (8 interns, stack, user stories, PR reviews, Git/testing). Matches Git, code review.
- za-mock-interview + za-demos-contracts → ZenAI (sole engineer, recruiters shaped AI scoring, mid-sized companies signed). Matches "define what well-scored means".
- cm-nl-safety → Research (LLMs → formal safety specs).
- pj-codingplans → Projects 1 (LLM evaluation: KV cache, long context, needle-in-a-haystack).
- pj-my-av (pipeline facts) → Projects 2 (data pipeline).
- Coursework: CMU LLM Systems, Machine Learning, Data Science for SE; UW LLMs in Practice, Software Engineering, Operating Systems.
- Skills: Python / TypeScript / JavaScript / SQL first; AI & Evaluation row second; both AWS certifications kept.

## Skipped
- nb-swiftui-app, nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-manual-broadcast, nb-dramabreak-ads, nb-coaching-marketplace: mobile/product, off-JD.
- nb-dramabreak-stripe: idempotent webhook fits "idempotency" but no room; good interview example.
- nb-morning-digest: LLM summarization fits, but space; cut for the evaluation-heavy lines.
- nb-eks-standup, nb-catalog-cache: infra/perf, lower value than eval lines.
- nb-retired-detector: good "measured and retired my own thing" story; space. Interview material.
- nb-jira-process (34 API specs, ~10,000 lines of docs, security-ticket audit): fits "define the contract", "documentation", but space. Interview material.
- nb-cross-dept: space.
- cm-psc: one research line is enough.
- pj-cs537-os, pj-wisconsin-autonomous, ld-ece-fellow: off-JD.
- No OpenAI/Anthropic API, GitLab, fairness/bias, or redaction claims: not in inventory.

## Page fill
- Pages: 1
- Bottom margin: 0.36 in = 25.92 pt → content limit 766.08 pt
- Last content yMax: 763.21 pt
- Unused height: 2.9 pt
- Visual check: rendered at 80 dpi; no empty strip, clipping, overlap, or orphan lines.
