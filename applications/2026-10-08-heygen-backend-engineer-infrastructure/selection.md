# Selection — HeyGen, Backend Engineer - Infrastructure

## NewsBreak title

**Backend Engineer Intern** — JD title is "Backend Engineer (Infrastructure)" and asks for "scalable, reliable, and efficient backend systems" and "API design and development"; he was the sole backend owner. Heading plain "NewsBreak" (not a new-venture JD).

Header city: Mountain View, CA (JD lists San Francisco / Palo Alto alongside LA and Toronto → Bay rule).

## Items used

- **nb-fastapi-backend** + **nb-eks-standup** (CronJobs, gate) → bullet 1 (89 endpoints, 27 routers, 7 CronJobs, ~1,450 offline tests 0.17 s, ruff/pyright/pytest) — JD: API design, MongoDB, "unit and integration tests".
- **nb-jira-process** (34 contract-first API specs) + **nb-third-party-proxy** → bullet 2 (nine integrations server-side, zero API keys) — JD: API design. Integrations named by category from the inventory list (SportsDataIO, DeepInfra LLM + embeddings, APNs).
- **nb-eks-standup** → bullet 3 (EKS day 3, Docker/Helm/Jenkins, DNS → TLS → admission-policy chain) — JD: cloud (AWS), Kubernetes.
- **nb-llm-pipeline** → bullet 4 (ingest → embed → LLM-score → dedupe as a CronJob, ~2 min, ~1,200 LLM calls/day, 4,100+ shadow decision rows, filler 34% → 4% by count) — JD: data / ML infrastructure.
- **nb-llm-failure** → bullet 5 (65%, Langfuse, p95 1,197 vs 16,384, Helm env shadowing) — JD: "monitor … errors, and anomalies. Implement fixes". Says "root-caused"; no post-deploy outcome claimed.
- **nb-observability** + **nb-cronjob-outage** → bullet 6 (Prometheus/Grafana; 5-day outage, paired deadlines) — JD: performance monitoring. No dashboard/metric counts invented.
- **nb-catalog-cache** + **nb-eks-standup** (HPA 2–4) → bullet 7 (13.2 MB → 10.9 MB, 78×, 512 MiB) — JD: efficient / performant systems.
- **nb-ownership** + **nb-swiftui-app** → bullet 8 (~6,000 installs, peak DAU 1,119, 344 PRs / 340 merged).
- **hd-lead-mvp** + **hd-langchain-apis** + **hd-mentor-process** → Haddee (Agile, GCP App Engine, database schemas and REST APIs, PR reviews) — JD: API design, code reviews, GCP.
- **za-mock-interview** + **za-demos-contracts** → ZenAI line 1 (PostgreSQL; startup — JD prefers startup experience). **za-auth-db** → ZenAI line 2 (database interactions) — added as page fill after trimming coursework.
- **pj-my-av** (pipeline + training facts, one 3-line bullet) — JD preferred: "ML Infrastructure especially computer vision", training infra, inference.
- **pj-codingplans** — inference (KV cache, quantization).
- **ld-ece-fellow** — fill.
- Skills: Languages lead with Python, C (JD: "python or c++"; no C++ in inventory, not claimed). Backend & Data row carries PostgreSQL, MySQL, MongoDB, REST APIs. Cloud & Infra: AWS, GCP, Kubernetes. ML & Observability: PyTorch, CUDA, OpenCV, Vertex AI, Prometheus, Grafana, Langfuse. Certifications row kept.
- Coursework: CMU Distributed Systems, Machine Learning, Large Language Model Systems; UW Operating Systems, Computer Architecture, Algorithms.

## Items skipped

- nb-agentic-search, nb-retired-detector, nb-morning-digest — LLM product work; less infra than the pipeline bullet.
- nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-dramabreak-*, nb-coaching-marketplace, nb-manual-broadcast — mobile/product.
- ArgoCD stale-app / amd64 image detail (nb-eks-standup) — cut for space; Kubernetes is already covered.
- cm-psc, cm-nl-safety — research off JD; page full without it.
- pj-wisconsin-autonomous — embedded; less relevant than my-av.
- CMU Foundations of Software Engineering — dropped; it wrapped to a 2-word second line. Freed line went to za-auth-db.
- Skills Pydantic, asyncio, ArgoCD, GitHub Actions — dropped to stop skill rows wrapping (first build spilled to two pages).

## Constraints nearly violated

- JD asks for C++ — not in inventory; only C listed.
- JD mentions GPU capacity scheduling and Azure — no inventory facts; not claimed. CUDA appears only via my-av training.
- Did not call the nbot workers "inference workers"; inventory says LLM workers / pipeline.
- JD asks 2+ years of experience — flagged in reply.
- First compile spilled ~1 line to page 2; fixed by trimming skill rows and shortening my-av, then re-expanded my-av with the data-pipeline facts to refill.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, ECE Fellow line): **754.80 pt** from the top.
- Unused height: 792 − 25.92 − 754.80 = **11.28 pt** (passes 0–12 pt).
- Rendered at 90 dpi and inspected: no clipping, overlap, orphan wraps, or empty bottom strip.
