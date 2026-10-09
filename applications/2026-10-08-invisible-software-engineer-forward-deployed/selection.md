# Selection — Invisible Technologies, Software Engineer, Forward Deployed

## NewsBreak title

**AI Engineer Intern.** The JD calls the role "equal parts AI engineer, software builder, and technical consultant" and centers on "AI-powered workflows using LLMs, embedding models, retrieval systems". Heading stays plain "NewsBreak": client deployment, not new ventures.

Header city: Mountain View, CA (JD lists the SF Bay Area alongside New York).

## Items used

- **nb-llm-pipeline** → bullets 1–3: pipeline stages over a raw news feed (bge embeddings, LLM scoring, LLM dedupe), CronJob, ~2 min ingest-to-decision, ~1,200 LLM calls/day; 11-day shadow, 4,100+ decisions, filler 34% → 4%, median 89 vs 90, categorical event gate; rejected the 91%-filler rule that killed the two highest-reach alerts. Maps to "LLMs, embedding models", "messy real-world constraints", "iterate quickly based on real-time feedback".
- **nb-agentic-search** → bullet 4: retrieval systems, RAG, tool-calling agent, SSE, TTFT 0.85 s, 0% → 100% P@1 at 0.4 ms (latency requirements).
- **nb-llm-failure** → bullet 5: Langfuse, 65% failure, p95 1,197 vs 16,384, Helm env shadowing. Maps to on-call / production debugging.
- **nb-fastapi-backend + nb-catalog-cache** → bullet 6: Python FastAPI, 89 endpoints, ~1,450 offline tests, fan-out 25–30 → 1, shared cache 78×.
- **nb-eks-standup + nb-observability + nb-cronjob-outage** → bullet 7: AWS EKS, Docker, Helm, Jenkins, day 3, Prometheus/Grafana, 5-day CronJob outage. Maps to "production deployment (Docker, FastAPI, GCP/AWS)".
- **nb-swiftui-app + nb-ownership + nb-jira-process** → bullet 8: sole SwiftUI / primary backend author, 1.4K ratings, peak DAU 1,119, 34 contract-first API specs (communication with teams).
- **hd-lead-mvp** → Haddee bullet 1 (FastAPI, GCP App Engine, team lead).
- **hd-langchain-apis** → Haddee bullet 2 (LangChain — a named JD library).
- **za-mock-interview** → ZenAI bullet 1 (sole engineer, worked with recruiters on scoring categories → stakeholder engagement).
- **za-demos-contracts** → ZenAI bullet 2 (demos, fast client iterations, three 200–500-person companies signed → client-facing FDE work).
- **pj-my-av** → project 1 (PyTorch, data pipeline, GCP Vertex AI).
- **pj-codingplans** → project 2 (fill; LLM evaluation).

## Skipped

- nb-retired-detector: first included in bullet 3; cut to fit one page.
- nb-third-party-proxy, nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-manual-broadcast, nb-dramabreak-*, nb-coaching-marketplace: mobile/ads, not the JD.
- nb-morning-digest: the alert pipeline and search already cover LLM shipping.
- hd-mentor-process, za-auth-db: space.
- cm-nl-safety, cm-psc: research section cut when the first compile spilled to page 2; my-av carries PyTorch / data pipelines more directly.
- ld-ece-fellow, pj-wisconsin-autonomous: not relevant.

## Constraints almost violated

- Not claimed (not in inventory): Hugging Face, OpenAI APIs, MLOps model versioning, fine-tuning. LLM calls went to DeepSeek over DeepInfra; the resume does not say OpenAI.
- TTFT 0.85 s is a single run, not p95.
- Prometheus/Grafana are a separate fact from the day-3 EKS standup; the bullet lists "set up" separately.
- Skills: "GCP" and "GCP Vertex AI" are both inventory skill names; GCP App Engine stays in the Haddee bullet.
- Certifications kept.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 792 pt tall)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 755.13 pt
- Unused height: 792 − 25.92 − 755.13 = 10.95 pt (passes 0–12 pt)
- Visual review: rendered at 110 dpi. No empty bottom strip, clipping, overlap, or cramped text; all skill rows fit on one line.
