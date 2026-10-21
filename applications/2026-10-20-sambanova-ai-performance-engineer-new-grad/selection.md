# Selection — SambaNova, AI Performance Engineer - New Grad

## NewsBreak title
**AI Engineer Intern** — the JD is AI/ML systems ("bring up and optimize foundation models", "LLM training or inference"). None of the other printed titles fits a performance role better.

## Fit
Weak on the hard requirements: no vLLM / TensorRT / SGLang, no Triton or kernel-level CUDA, no C++, no quantization or kernel-fusion work in inventory. Strong points: Python, PyTorch + CUDA (my-av), LLM inference debugging, memory/latency measurement, Computer Architecture / OS / LLM Systems coursework. Resume leans on measurement and bottleneck-finding.

## Used
- **nb-llm-failure** (`llm`, trimmed): 65% failure rate, Langfuse traces, p95 1,197 vs 16,384 runaways, 2,048-token cap. Profiling LLM execution.
- **nb-catalog-cache**: 512 MiB pod limit, 13.2 MB per-user → 10.9 MB shared, home-load copy 9.0 ms → 0.89 ms. Memory / caching.
- **nb-llm-pipeline**: embeddings + DeepSeek scoring + LLM dedupe, ~1,200 LLM calls/day, ~2 min ingest-to-decision, 11-day production shadow, filler 34% → 4%. LLM inference in production; DeepSeek is named in the JD.
- **nb-agentic-search**: SSE streaming, TTFT 0.85 s, hybrid vector + text retrieval fused by RRF, fixed RAG + capped tool-calling agent (agentic workloads in the JD). Second bullet: entity resolution 0.4 ms, chosen over embeddings after measuring both, 20/20 logged queries.
- **nb-fastapi-backend** + **nb-eks-standup** + **nb-observability**: 89 endpoints, AWS EKS, ~1,450 offline tests gating CI, Prometheus / Grafana. Tracking performance across releases.
- **hd-lead-mvp** + **hd-langchain-apis**: fused, one bullet.
- **za-mock-interview** + **za-demos-contracts**: fused, one bullet.
- **cm-nl-safety**: multi-turn LLMs, Bayesian estimators (numerical computing).
- **pj-codingplans**: KV caching, long context, quantization — closest inventory item to inference optimization.
- **pj-my-av** (`short` + streaming inference): PyTorch, local CUDA, Vertex AI.
- **pj-cs537-os**: C, pthreads, xv6 syscalls — systems depth for a compiler/runtime-adjacent team.
- Coursework: CMU Large Language Model Systems, Machine Learning, Distributed Systems; UW Computer Architecture, Operating Systems, Algorithms.
- Skills: Languages lead with Python and C; second row ML & Inference (PyTorch, CUDA, NumPy). Certifications kept.

## Skipped
- cm-psc: tried; cut for space (cm-nl-safety covers the LLM + numerical angle).
- nb-ownership, nb-jira-process, nb-cross-dept: ownership / process, not performance.
- nb-retired-detector: latency story, but less about systems performance than the cache and LLM-failure lines.
- nb-cronjob-outage, nb-third-party-proxy, nb-dramabreak-*, nb-coaching-marketplace, iOS items: not relevant.
- ld-ece-fellow, pj-wisconsin-autonomous: weaker than the three projects used.
- Skills not printed: OpenCV, bge embeddings, Helm, Redis Streams, GitHub Actions (wrapped rows), mobile and frontend stack.

## Page-fill check
- Draft 1: 2 pages (Skills spilled). Cut cm-psc and the OS line, shortened skills rows, moved Skills before Projects as in the template.
- Draft 2: 2 pages by one line. Shortened nb-llm-failure, nb-llm-pipeline, codingplans, my-av → 1 page, 35.5 pt unused.
- Draft 3: added OS coursework → 8.1 pt unused, but UW coursework wrapped one word ("III").
- Final: dropped Data Structure & Programming III, restored needle-in-a-haystack and the clone-wrapper detail. 1 page; bottom margin 0.36 in = 25.92 pt; last content yMax 757.94 pt; unused 792 − 25.92 − 757.94 = 8.14 pt.
- Rendered at 80 dpi: no empty strip, clipping, overlap, or orphaned words; SportsBreak hyperlinked.
