# Selection — HP, AI Software Engineer - HP IQ (3163597)

## NewsBreak title

**AI Engineer Intern.** The posting title is "AI Software Engineer" and the core asks are "LLM integration into multi-agent systems", "agent orchestration, tool use, and memory/context management", and "structured outputs". Heading is "NewsBreak (Venture Team)": HP IQ is "HP's new AI innovation lab" with "startup agility" — an incubation-style new-products team.

Header city: Mountain View, CA (JD is San Francisco).

## Items used

- **nb-agentic-search** → bullets 1–2: SSE, deterministic RAG turn 1, bounded tool-calling agent (≤3 hops, 5 tools, 45 s), client-held conversation state / no PII at rest (memory/context management, privacy), server-resolved citations; substring + `$text` + bge vector fused by RRF, degrade to surviving legs, entity resolver as query rewriter, 0% → 100% P@1 at 0.4 ms. Maps to "agent orchestration runtime … tool use, memory management, and multi-step reasoning".
- **nb-llm-pipeline** → bullet 3: ingest → embed → LLM score (categorical happened/speculative/no_event + 0–100) → percentile gate → LLM dedupe → push; CronJob, ~2 min, ~1,200 LLM calls/day, 11-day shadow, filler 34% → 4%. Maps to "task decomposition", "structured outputs", "data pipelines … for real-time AI inference".
- **nb-llm-failure** → bullet 4: Redis Streams (JD "data streaming technologies"), Langfuse, 65% failure, p95 1,197 vs 16,384, Helm env shadowing.
- **nb-fastapi-backend + nb-catalog-cache** → bullet 5: Python FastAPI / MongoDB (NoSQL), 89 endpoints, ~1,450 offline tests, fan-out 25–30 → 1, shared cache 78×. Maps to "APIs and microservices", "scalability and performance".
- **nb-eks-standup + nb-observability + nb-cronjob-outage** → bullet 6: AWS EKS, Docker, Helm, Jenkins, HPA min 2 / max 4, day 3, Prometheus/Grafana, 5-day CronJob outage.
- **nb-ownership + nb-swiftui-app + nb-third-party-proxy** → bullet 7: primary backend author, 1.4K ratings; nine integrations (incl. DeepInfra LLM + embeddings) moved server-side, iOS ships zero third-party API keys. Maps to "integration between cloud-based AI models and edge devices" and "security and privacy best practices".
- **hd-lead-mvp** → Haddee 1 (Agile — JD "agile environment"; FastAPI, GCP).
- **hd-langchain-apis** → Haddee 2 (LLM integration into backend services, REST APIs).
- **za-mock-interview / za-auth-db** → ZenAI 1 (sole engineer, auth / sessions / database).
- **za-demos-contracts + za-mock-interview** → ZenAI 2 (recruiters on scoring, three 200–500-person companies).
- **cm-nl-safety** → research (multi-turn LLMs → formal specs ≈ structured outputs; real-time estimation).
- **pj-my-av** → project 1 (PyTorch — JD's on-device framework list; streaming inference; GCP Vertex AI).
- **pj-wisconsin-autonomous** → project 2 (edge device: real-time data to an onboard NVIDIA Jetson; JD "edge devices").

## Skipped

- nb-retired-detector, nb-morning-digest: alert pipeline and search already cover LLM shipping.
- nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-manual-broadcast, nb-dramabreak-*, nb-coaching-marketplace, nb-jira-process: mobile/ads/process, not the JD.
- hd-mentor-process: space.
- cm-psc: control theory, not the JD.
- pj-codingplans: space; my-av and Wisconsin Autonomous map to on-device / edge.
- ld-ece-fellow: not relevant.

## Constraints almost violated

- **C++ is required by the JD and is not in `inventory/skills.md`** — not added. Java and C are listed instead.
- Not claimed (not in inventory): TensorFlow Lite, ONNX Runtime, CoreML, multi-agent systems, microservices as a word, Kafka. The agent is a single bounded tool-calling agent; the resume does not say multi-agent.
- "keyword, full-text" paraphrases substring + Mongo `$text`. "autoscaling 2–4 pods" is HPA min 2 / max 4.
- "Structured" stayed implicit ("categorical LLM scoring"); the inventory records categorical labels + 0–100 scores, not a JSON-schema output feature.
- First compile spilled to page 2 by ~12 lines; cut research and Wisconsin, then overshot (80 pt empty) and added both back with shorter Haddee/ZenAI lines. Dropped "1,119 peak DAU" and "Sole SwiftUI engineer" from bullet 7 and "bge embeddings", "asyncio", "Langfuse" from Skills rows to keep each row on one line.
- Certifications kept.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 792 pt tall)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 760.62 pt
- Unused height: 792 − 25.92 − 760.62 = 5.46 pt (passes 0–12 pt)
- Visual review: rendered at 110 dpi. No empty bottom strip, clipping, overlap, or cramped text; all skill rows fit on one line.
