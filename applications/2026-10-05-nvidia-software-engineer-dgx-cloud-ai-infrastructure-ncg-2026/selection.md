# Selection — NVIDIA, Software Engineer, DGX Cloud AI Infrastructure - New College Grad 2026 (JR2026477)

## NewsBreak title

**Engineering Intern** (official title). First printed as "AI Infrastructure Intern." Lordphone then cut the printed-title list down to Software Engineering Intern, Engineering Intern, and AI Engineer Intern. This JD is infra and failure triage, not general SWE and not AI as product work, so it gets the official title.

## Header

Mountain View, CA (Santa Clara is one of the listed locations).

## Items used

| Bullet | Item ids | Facts |
|---|---|---|
| NB 1 — EKS bring-up | nb-eks-standup | production EKS on day 3, Helm, Jenkins, Docker, 7 CronJobs, DNS → TLS → admission-policy chain blocking iOS on public networks |
| NB 2 — 65% LLM failure | nb-llm-failure | another team's LLM workers, Langfuse traces, unbounded reasoning loop, p95 1,197 vs 16,384 runaways, 2,048-token cap truncates 0% of observed successes |
| NB 3 — CronJob outage | nb-cronjob-outage | 5-day silent outage, non-terminal ImagePullBackOff + Forbid concurrency, paired job/scheduler deadlines |
| NB 4 — backend + regression gate | nb-fastapi-backend | first commit, 89 endpoints, ~1,450 offline tests, 0.17 s, ruff / pyright / pytest gate, Motor fake reproducing the production cluster failure as the regression guard |
| NB 5 — LLM pipeline | nb-llm-pipeline | Kubernetes CronJob, embed → LLM-score → dedupe → push, ~1,200 LLM calls/day, 11 days of production shadow, 4,100+ decision rows, filler 34% → 4% |
| NB 6 — retired detector | nb-retired-detector | 19 hours of production shadow, 901 min p50 vs 1.8 min pipeline, ~15 h too slow, net −882 lines (data-driven recommendation) |
| NB 7 — cache / memory | nb-catalog-cache | 13.2 MB per-user key, pod memory toward 512 MiB, 10.9 MB shared, 78×, 9.0 ms → 0.89 ms copy |
| NB 8 — SportsBreak | nb-ownership, nb-swiftui-app, nb-live-activities | sole SwiftUI engineer, primary backend author, ~6,000 installs, peak DAU 1,119, App Store link; start push with no `aps.alert` silently dropped while APNs returns 200 |
| Haddee | hd-lead-mvp, hd-langchain-apis | 8 interns, Agile, React / Next.js / FastAPI / Supabase, 0→1, GCP App Engine, schemas and REST APIs for LangChain features |
| ZenAI | za-mock-interview, za-demos-contracts | VC-backed, sole engineer, 0→1, React / Next.js / Supabase / PostgreSQL, three 200–500-person companies signed |
| Projects | pj-my-av, pj-codingplans, ld-ece-fellow, pj-wisconsin-autonomous | my-av: PyTorch CNN-GRU, local CUDA, Vertex AI, streaming inference. codingplans: KV-cache / long-context / needle-in-a-haystack benchmarking of LLM providers, quantization. Wisconsin Autonomous: NVIDIA Jetson. |

Coursework: CMU — Distributed Systems, Large Language Model Systems, Machine Learning. UW — Computer Architecture, Operating Systems, Algorithms (the JD asks for debugging "toward the hardware").

Skills: Python and C lead the first row; PyTorch, CUDA, NVIDIA Jetson, and Linux lead the second. Cluster tooling (Kubernetes, Docker, Helm, CronJobs) is in row three.

## Skipped

- cm-psc, cm-nl-safety (research): this JD does not ask for it. It was in the first draft, but the page spilled to two, so it was the first cut.
- nb-third-party-proxy, nb-server-driven-ui, nb-app-store, nb-ads-max, nb-morning-digest, nb-manual-broadcast, nb-dramabreak-*, nb-coaching-marketplace, nb-jira-process: product/mobile work with no cluster or debugging angle that beats the items chosen.
- nb-agentic-search: strong LLM work, but the JD is about infra and failure triage, not retrieval.
- hd-mentor-process, za-auth-db: kept each older role to one bullet so the infra content had room.

## Near-violations

- **C++** is in the JD's requirements but not in `inventory/skills.md`. Only C is listed. Not added.
- **NCCL, multi-GPU / multi-node, CUDA-aware distributed execution, RDMA, MLPerf, NeMo, TensorRT-LLM** are not in inventory. None are claimed. CUDA appears only as single-machine training (my-av).
- The first draft called the 65% failure pipeline "distributed LLM workers." The inventory says "another team's LLM workers" (Redis streams, `asyncio.gather`), so "distributed" was removed.
- Cut "a Helm env shadowing the code default" from NB 2 for space. It is still true and available in nb-llm-failure.

## Page-fill verification (final PDF)

- Pages: 1
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`); page height 792 pt
- Last content bottom (pdftotext -bbox max yMax): 755.80 pt
- Unused height: 792 − 25.92 − 755.80 = **10.28 pt** (within 0–12 pt)
- Visual review: rendered the whole page at 110 dpi. No empty strip at the bottom, and no clipping, overlap, or cramped lines. Spacing is the shared preamble with the template's `itemsep=0.7pt`.

## Revision — removed AI-infra framing

Lordphone confirmed none of the internship was AI infra (no GPUs, training, or serving). Changes:
- "Brought up" (NVIDIA's hardware bring-up term) → "Stood up" (approved nb-eks-standup wording).
- "Profiled a cache" → "Redesigned a cache" (inventory records the memory climb and measured copies, not a profiling pass).
- Skills row "AI & Systems" → "ML & Systems".

Final PDF after this edit: 1 page, last content at 755.80 pt, unused 10.28 pt. Re-rendered and checked: no defects.
