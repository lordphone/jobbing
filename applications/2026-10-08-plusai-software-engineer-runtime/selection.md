# Selection — PlusAI, Software Engineer, Runtime

## NewsBreak title
**Software Engineering Intern** — JD title is "Software Engineer, Runtime"; not backend/full-stack/iOS/AI product work, so the default fits.

Heading: plain "NewsBreak" (JD is not about new ventures). Header city: Mountain View, CA (Santa Clara, Bay Area).

## Items used
- **nb-fastapi-backend + nb-eks-standup** → bullet 1: Python FastAPI / MongoDB from the first commit, 89 endpoints, 7 CronJobs, EKS, ~1,450 offline tests (0.17 s), ruff/pyright/pytest gate. (Large code base, Python, Linux/K8s.)
- **nb-catalog-cache** → bullet 2: 13.2 MB per-user key, 512 MiB pod, 10.9 MB shared (78×), home-load copy 9.0 ms → 0.89 ms. (Performance troubleshooting / profiling.)
- **nb-cronjob-outage + nb-observability** → bullet 3: fault detection / handling angle.
- **nb-llm-failure** (infra variant) → bullet 4: 65% failure, Langfuse, p95 1,197 vs 16,384, Helm env shadowing.
- **nb-llm-pipeline** → bullet 5: ~2 min, ~1,200 LLM calls/day, 4,100+ shadow decisions, filler 34% → 4%. Framed as validate-in-shadow before going live (validation strategy).
- **nb-ownership + nb-swiftui-app** → bullet 6: sole SwiftUI / primary backend, ~6,000 installs, 1,119 peak DAU, 344 PRs / 340 merged.
- **hd-lead-mvp + hd-langchain-apis + hd-mentor-process** → Haddee bullet.
- **za-mock-interview + za-demos-contracts** → ZenAI bullet.
- **cm-psc** → research bullet 1 (vehicle safety under uncertainty, 3-DOF, LuGre, ice).
- **cm-nl-safety** → research bullet 2 (Bayesian estimators, road-friction adaptation).
- **pj-my-av** (two-line fused) → CV + deep learning + CUDA + streaming inference (JD: CV/DL, CUDA, model inference).
- **pj-wisconsin-autonomous** (encoders) → NVIDIA Jetson, real-time on-vehicle data (JD: Nvidia SoCs, on-vehicle).
- Skills: Languages; ML & Edge (PyTorch, CUDA, OpenCV, NumPy, NVIDIA Jetson, Vertex AI, Bayesian estimation); Infra & Tools (Linux first); Certifications kept.
- Coursework: CMU Distributed Systems, ML, Foundations of SE; UW Operating Systems, Computer Architecture, Algorithms, Mobile Computing Lab.

## Items skipped
- nb-agentic-search, nb-morning-digest, nb-server-driven-ui, nb-live-activities, nb-app-store, nb-ads-max, nb-dramabreak-*, nb-coaching-marketplace, nb-manual-broadcast, nb-retired-detector: product/mobile/search work, not runtime/platform.
- nb-third-party-proxy, nb-jira-process: weaker fit; space.
- za-auth-db second line: space.
- pj-codingplans: LLM-plan benchmarking, off-target.
- ld-ece-fellow: cut — first build spilled 2 lines onto page 2; lowest-value line for this JD.

## Constraints almost violated
- **C++ not in inventory/skills.md** — JD requires "strong C++"; not listed. Also no ROS2, DDS, QNX, OpenCL, IPC/middleware — none added.
- JD asks MS/PhD (in progress, May 2027) and 2+ years professional experience.
- "Profiled a cache" — supported by recorded measurements (15 µs vs 127 µs copy, 9.0 → 0.89 ms, memory sizing); "home-load copy" kept verbatim from inventory rather than "hot path".

## Page-fill verification (final PDF)
- Pages: 1
- Bottom margin: 0.36 in = 25.92 pt (shared/preamble.tex)
- Last content yMax: 759.47 pt (page height 792 pt)
- Unused height: 792 − 25.92 − 759.47 = **6.61 pt** (within 0–12 pt)
- Visual review: rendered at 110 dpi; no empty strip, clipping, or overlap; spacing even.
