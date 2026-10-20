# Selection — CoreWeave, Software Engineer, Inference AI/ML

## NewsBreak title

**Software Engineering Intern** (default). The posting title is "Software Engineer"; the work is model-serving services, metrics, on-call, and performance experiments — infra/backend, not AI-as-product, so not "AI Engineer Intern". Heading is plain "NewsBreak" (not new-product work).

Header city: Mountain View, CA (Sunnyvale is Bay Area).

## Items used

- **nb-fastapi-backend + nb-ownership** → bullet 1: first commit, 89 endpoints, ~1,450 offline tests (0.17 s), ruff/pyright/pytest gate; 344 PRs (340 merged). JD: tests, Git/CI basics, deployed microservice.
- **nb-eks-standup + nb-observability** → bullet 2: production EKS day 3, Docker/Helm/Jenkins, 7 CronJobs, HPA min 2 / max 4 at 70% CPU, Prometheus + Grafana on the EKS nodes. JD: containers/Kubernetes, metrics and dashboards, Grafana/Prometheus.
- **nb-catalog-cache** → bullet 3: 25–30 → 1 call, 3 s per-source budget, per-user cache (structurally zero hit) → 10.9 MB shared (78×), 512 MiB pod, copy 9.0 → 0.89 ms. JD: performance experiments (concurrency, caching), cost/latency.
- **nb-llm-failure** → bullet 4: 65% failure rate, Langfuse, unbounded reasoning loop, Helm env shadowing code default, 2,048 cap vs p95 1,197. JD: reliability of LLM serving, incident response.
- **nb-cronjob-outage + nb-eks-standup (day3)** → bullet 5: 5-day silent outage, ImagePullBackOff + Forbid, paired deadlines; DNS → TLS → admission-policy chain. JD: incident response, Linux/networked services.
- **nb-agentic-search** → bullet 6: SSE streaming, TTFT 0.85 s (single run, not p95 — worded as one measurement), hybrid retrieval with RRF, degrades to surviving legs, ≤3 hops / 45 s. JD: streaming, latency, reliability.
- **nb-llm-pipeline** → bullet 7: Kubernetes CronJob, ~1,200 LLM calls/day, ~2 min ingest-to-decision, 4,100+ shadow decision rows, filler 34% → 4%.
- **nb-swiftui-app / nb-ownership / nb-jira-process / nb-third-party-proxy** → bullet 8: primary backend author, SportsBreak link (1.4K ratings), 34 contract-first API specs, ~10,000 lines docs, nine integrations server-side. JD: short design docs.
- **hd-lead-mvp (agile)**, **hd-langchain-apis**, **hd-mentor-process** → Haddee 3 bullets (code reviews from JD).
- **za-mock-interview (with-auth)** + **za-auth-db / za-demos-contracts** → ZenAI 2 bullets.
- **pj-my-av** → PyTorch, CUDA, streaming inference (JD preferred: PyTorch, simple CUDA, ML inference demo).
- **pj-codingplans** → KV caching, long context (JD: curiosity about KV cache).
- **pj-cs537-os** → C, pthreads, xv6 syscalls (JD: Linux fundamentals, C++ a plus — only C is claimed).
- Coursework: CMU LLM Systems, Distributed Systems, Machine Learning; UW Operating Systems, Computer Architecture, Algorithms.
- Skills: Python, Go first (JD names Python/Go); Linux, Docker, Kubernetes, Prometheus, Grafana in row 2. Certifications row kept.

## Items skipped

- nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-manual-broadcast, nb-dramabreak-ads, nb-dramabreak-stripe, nb-coaching-marketplace, nb-morning-digest: mobile/product, off-JD.
- nb-retired-detector: no room; pipeline bullet covers the measurement story.
- nb-cross-dept: off-JD.
- cm-psc, cm-nl-safety (research): off-JD; the page is full with projects closer to inference (my-av, codingplans).
- ld-ece-fellow, pj-wisconsin-autonomous: less relevant; no room.

## Constraints almost violated

- C++, Triton, vLLM, TensorRT-LLM, Ray Serve, OpenTelemetry, TensorFlow, micro-batching: not in inventory; not claimed. Only C is listed (OS coursework supports C, not C++).
- Go is in skills.md but no inventory bullet shows Go work; listed in Skills only.
- No alarms/alerting claimed for Prometheus/Grafana (inventory says alerts not recorded); no CronJob success metrics claimed.
- TTFT 0.85 s is a single run; not phrased as p50/p95.
- Page fill: after inventory edits the page sat at −0.53 pt (one line too many) or 12.88 pt (one line short). Since a full line could not fit, loosened itemize itemsep 0.5 → 0.6 pt in this resume only (margins and font size unchanged).

## Page-fill verification (final PDF)

- Pages: 1 (letter, 792 pt tall)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 754.39 pt
- Unused height: 792 − 25.92 − 754.39 = 11.69 pt (passes 0–12 pt)
- Visual review: rendered at 100 dpi. No empty bottom strip, clipping, overlap, or cramped text; skill rows fit on one line.
