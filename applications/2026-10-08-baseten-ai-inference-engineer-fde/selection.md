# Selection — Baseten, AI Inference Engineer (FDE Generalists)

## NewsBreak title

**AI Engineer Intern.** The JD is AI product work ("AI Inference Engineer", "production AI applications", "AI/ML pipelines and the lifecycle of ML model development and deployment"). Heading stays plain "NewsBreak": the JD is customer-facing deployment, not new ventures.

Header city: Mountain View, CA (JD lists San Francisco).

## Items used

- **nb-llm-pipeline** → bullets 1–2: pipeline stages, CronJob, ~1,200 LLM calls/day, 11-day shadow, 4,100+ decisions, filler 34% → 4%, hand-graded median 89 vs 90, categorical gate. Maps to "problem framing → evaluation → production deployment → monitoring".
- **nb-llm-pipeline + nb-retired-detector** → bullet 3: rejected 91%-filler rule that killed the two highest-reach alerts, retired own detector (19 h shadow, 15 h too slow, net −882). Maps to "good judgment on tradeoffs… avoiding unnecessary complexity".
- **nb-agentic-search** → bullet 4: SSE, TTFT 0.85 s, deterministic RAG turn 1, bounded agent ≤3 hops / 5 tools, RRF hybrid retrieval, server-resolved citations, 0% → 100% P@1 at 0.4 ms. Latency outcome for the "quality, latency, and cost" line.
- **nb-llm-failure** → bullet 5: 65% failure, Langfuse, p95 1,197 vs 16,384, Helm env shadowing.
- **nb-eks-standup + nb-observability + nb-cronjob-outage** → bullet 6: EKS day 3 (Docker, Helm, Jenkins), Prometheus/Grafana, 5-day CronJob outage. Maps to "reliable, observable services".
- **nb-fastapi-backend + nb-catalog-cache** → bullet 7: Python FastAPI, first commit, 89 endpoints, ~1,450 offline tests, 25–30 → 1 fan-out, shared cache 78× smaller. Maps to Python in production.
- **nb-swiftui-app + nb-ownership + nb-jira-process** → bullet 8: sole SwiftUI / primary backend author, 1.4K ratings, peak DAU 1,119, 34 contract-first API specs (closest real fact to "specs / PRDs").
- **hd-lead-mvp + hd-langchain-apis** → Haddee bullet.
- **za-mock-interview + za-demos-contracts** → ZenAI bullet (customer demos and client iteration → "pre-sales", "technical customer success").
- **cm-nl-safety** → research bullet (fill, LLM-relevant).
- **pj-codingplans** → project (KV caching, quantization: inference-adjacent).

## Skipped

- nb-third-party-proxy, nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-manual-broadcast, nb-dramabreak-*, nb-coaching-marketplace: mobile/ads, not the JD.
- nb-morning-digest: dropped for space; the LLM pipeline and search cover LLM shipping.
- hd-mentor-process, za-auth-db: space.
- cm-psc: control theory, not the JD.
- pj-my-av: cut for space (first compile was 2 pages).
- ld-ece-fellow, pj-wisconsin-autonomous: not relevant.

## Constraints almost violated

- Not claimed (not in inventory): vLLM, TensorRT-LLM, SGLang, GPU serving or profiling, model training/fine-tuning at the company, Whisper, ComfyUI, Baseten/Truss. The LLM calls go to hosted DeepInfra models, so the resume says "LLM scoring", not inference serving.
- TTFT 0.85 s is a single run, not p95. The resume does not call it p95.
- Prometheus/Grafana are a separate fact from the day-3 EKS standup; the bullet says "set up" separately so it does not imply day 3.
- "Event gate" is the categorical happened / speculative / no_event gate. The 127-alert holdout was cut for space, not reworded.
- No semicolons, per earlier revision preference.
- First compile spilled ~12 lines to page 2. Cut research and my-av, tightened six bullets, which left ~68 pt empty, then restored the research section.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 792 pt tall)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 759.94 pt
- Unused height: 792 − 25.92 − 759.94 = 6.14 pt (passes 0–12 pt)
- Visual review: rendered at 110 dpi. No empty bottom strip, clipping, overlap, or cramped text.
