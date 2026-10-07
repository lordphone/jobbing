# Selection — LinkedIn, Software Engineer - AI Platform

## NewsBreak title

**Engineering Intern.** The JD is AI *infrastructure* (training infra, feature platform, model serving, MLOps / observability), not AI as product work, so not "AI Engineer Intern". The inventory says to use the official title for infra JDs; this matches the NVIDIA DGX Cloud AI Infrastructure resume.

## Framing

JD keywords: "observability and understandability of various systems", "Ramping to Observability", orchestration, containers / Kubernetes, "LLM serving", "search systems or similar large-scale distributed systems", performance optimization, Python / Java / Go, PyTorch, CUDA, Distributed Systems.

- Observability / ramping: alert pipeline decision log, 11-day production shadow behind a dry-run flag, Langfuse root-cause.
- Containers / orchestration: EKS, Docker, Helm, HPA, CronJobs, two-stage image, CronJob outage.
- Search / IR: hybrid retrieval, RRF, bounded tool-calling agent, P@1.
- Performance: cache 78×, 512 MiB pod.
- PyTorch / CUDA / data pipeline: my-av.

Header: **Mountain View, CA** (JD location).

## Items used

- **nb-llm-pipeline** (two bullets): bge → LLM scoring → per-topic 7-day percentile → LLM dedupe → push as a CronJob, ~1,200 LLM calls/day, decision log; 11 days of shadow, 4,100+ decisions, `NEWS_ALERTS_DRY_RUN` flag, filler 34% → 4% by count, 2/day cap over 11,745 user-days.
- **nb-llm-failure**: 65%, Langfuse, p95 1,197 vs 16,384, Helm env shadowing the code default.
- **nb-agentic-search**: Mongo `$text` + bge vectors, RRF, bounded tool loop, SSE, 0% → 100% P@1, 0.4 ms.
- **nb-eks-standup + nb-cronjob-outage** (fused): EKS day 3, Docker / Helm / Jenkins, HPA, two-stage amd64 image (bson C extension SIGILLs on arm64), 5-day outage (non-terminal ImagePullBackOff + Forbid), paired deadlines.
- **nb-fastapi-backend + nb-catalog-cache** (fused): first commit → 89 endpoints, ~1,450 offline tests (0.17 s), 13.2 MB per-user → 10.9 MB shared (78×), 512 MiB pod.
- **nb-ownership + nb-swiftui-app + nb-morning-digest** (fused): SportsBreak link, 1.4K ratings, 1,119 peak DAU, digest to 5,026 users.
- **hd-lead-mvp + hd-langchain-apis**; **za-mock-interview + za-auth-db + za-demos-contracts**.
- **cm-nl-safety + cm-psc**: both research bullets, as ML fill.
- **pj-my-av** (`pipeline` + `training` merged into one bullet).

## Items skipped

- **nb-retired-detector, nb-third-party-proxy, nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-manual-broadcast, nb-dramabreak-*, nb-coaching-marketplace, nb-jira-process**: product / mobile, not platform.
- **hd-mentor-process, ld-ece-fellow, pj-codingplans, pj-wisconsin-autonomous**: no room.
- Skills dropped: frontend / mobile, NumPy, Grafana (wrapped a row), certifications.
- UW Algorithms dropped from coursework (it wrapped onto its own line).

## Constraints almost violated

- Not in inventory, not claimed: Spark / Beam / Flink, feature stores, distributed / multi-GPU training, GPU serving, model or tensor parallelism, TensorFlow, Ray, vLLM, Hugging Face, DeepSpeed, Kubeflow, MLFlow, C++, Rust, Scala, recommender model training.
- The LLM calls go to hosted DeepInfra models; the resume says "LLM scoring", not GPU inference or LLM serving infra.
- "Ramped" refers to the shadow → dry-run-off rollout; the 5% hash was a blast-radius control, not an A/B, so no experiment is claimed.
- First compile was 2 pages (my-av split across two bullets). Merged my-av, trimmed two skill rows; that left 20.7 pt unused, so added the PSC research bullet and then the HPA / amd64-image facts to the EKS bullet.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 792 pt tall)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 759.50 pt
- Unused height: 792 − 25.92 − 759.50 = 6.58 pt (passes 0–12 pt)
- Visual review: rendered at 110 dpi; no empty bottom strip, clipping, overlap, or orphan lines.

## Revision — no semicolons

Rewrote every bullet without semicolons (commas, "and", or a sentence break). Line breaks unchanged. Final PDF after this edit: 1 page, last content at 759.50 pt, unused 6.58 pt. Re-rendered and checked: no defects.
