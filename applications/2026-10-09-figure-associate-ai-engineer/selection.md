# Selection — Figure, Associate AI Engineer

## NewsBreak title

**AI Engineer Intern** — JD is "Associate AI Engineer" operating conversational AI / agent workflows, retrieval, evaluation. Heading is plain "NewsBreak" (not a new-venture JD).

Header city: Mountain View, CA (posting is Remote).

## Items used

- **nb-agentic-search** → bullets 1–2. Bullet 1: deterministic RAG on turn 1 vs bounded tool agent (≤3 hops, 5 whitelisted tools, 45 s), question-shaped gate (bare lookups skip LLM) — JD "determine whether problems are best solved through … deterministic code, retrieval, an LLM". Bullet 2: server-resolved citations (model cannot author a URL — "deterministic validation instead of model judgment"), rejected embeddings with measurements, 0% → 100% P@1 at 0.4 ms.
- **nb-llm-pipeline** → bullets 3–4. CronJob, ~1,200 LLM calls/day, 4,100+ decision rows, 11 days production shadow, hand-graded alerts, 127-alert holdout, prompt ablation, filler 34% → 4%, 2/day cap held over 11,745 user-days (hard caps). Bullet 4: rejected the 91%-filler rule because it killed the two highest-reach real alerts; decision log reasons (`sent` / `below_bar` / `not_event`) — JD "evaluation", "auditability", "accept model outputs without evaluation".
- **nb-llm-failure** → bullet 5. Langfuse, 65% failure, unbounded reasoning loop, 2,048 cap vs p95 1,197, binomial 49–66% vs 65% — "reading unfamiliar code", "statistics".
- **nb-fastapi-backend + nb-eks-standup + nb-observability** → bullet 6. 89 endpoints, ~1,450 offline tests, ruff / pyright / pytest gate, EKS / Docker / Helm, Prometheus / Grafana — "Python services and APIs", "CI/CD, containerization, monitoring".
- **nb-ownership + nb-third-party-proxy + nb-swiftui-app** → bullet 7. Primary backend author, SportsBreak link, 1.4K ratings, nine integrations server-side incl. DeepInfra LLM → zero API keys ("inventory tools that access third-party APIs", credentials), 72-event analytics catalog ("tagging … analytics").
- **nb-jira-process (audit) + nb-dramabreak-stripe** → bullet 8. Reopened SPR-13/15 with line-level evidence; Stripe signature-verified idempotent webhook as only trusted fulfillment — "security and governance", payments/regulated.
- **hd-lead-mvp (agile) + hd-langchain-apis** → Haddee 2 lines.
- **za-mock-interview + za-demos-contracts** → ZenAI: sole engineer 0→1; worked with recruiters so scoring matched real hiring, three 200–500-person companies signed — JD "partner with domain experts".
- **cm-nl-safety** → research (natural language → formal specs ≈ translating policy into system behavior; Bayesian estimators ≈ statistics).
- **pj-codingplans** → project (LLM evaluation of providers: KV cache, long context, needle-in-a-haystack).
- Skills: Python and SQL first (must-haves); RAG, agents, retrieval, Langfuse, pytest; TypeScript / React (nice-to-have); Terraform (IaC nice-to-have); certifications kept.
- Coursework: CMU — LLM Systems, Data Science for SE, ML, Distributed Systems; UW — LLMs in Practice, Software Engineering, Algorithms.

## Skipped

- nb-catalog-cache, nb-cronjob-outage, nb-retired-detector: space; bullets already cover backend and measurement-driven decisions.
- nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-manual-broadcast, nb-dramabreak-ads, nb-coaching-marketplace, nb-morning-digest: mobile/ads, not the JD.
- hd-mentor-process: space.
- cm-psc: control theory, off-JD.
- pj-my-av, pj-wisconsin-autonomous, ld-ece-fellow, pj-cs537-os: less relevant than codingplans; no room.

## Constraints almost violated

- Not claimed (not in inventory): voice AI, contact-center systems, A/B experiment results, causal inference, econometrics, lending domain. The DramaBreak A/B test has no recorded result and was left out. The 5% rollout hash was left out because the cohort was pre-set to 100% (not a real incremental rollout).
- SQL is in skills.md but no inventory bullet shows SQL work; only listed in Skills. Supabase/PostgreSQL appear via Haddee/ZenAI.
- "hard caps holding over 11,745 user-days" = 2/day cap with zero violations.
- First compile spilled 3 lines onto page 2; shortened bullets 1, 2, 6, the ZenAI scoring line, and the project line.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 792 pt tall)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 757.27 pt
- Unused height: 792 − 25.92 − 757.27 = 8.81 pt (passes 0–12 pt)
- Visual review: rendered at 100 dpi. No empty bottom strip, clipping, overlap, or cramped text; skill rows fit on one line.
