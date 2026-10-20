# Selection — Palantir, Software Engineer, New Grad - Query Engines

## NewsBreak title
**Software Engineering Intern** (default). The JD title is "Software Engineer" and the work is query engines / data infrastructure; no listed title fits better (not backend services, not AI). Heading plain "NewsBreak" (not a new-venture team).

## Header city
Mountain View, CA. The posting is New York–only, so the skill's rule would print New York, NY; he asked for Mountain View.

## Used
- **nb-fastapi-backend + nb-eks-standup** (bullet 1): first commit, 89 endpoints, 26 collections, ~48 indexes, ~1,450 offline tests (0.17 s), ruff / pyright / pytest gate; production EKS (Helm, Jenkins) on day 3, 7 CronJobs. JD: "design, code review, testing, and release".
- **nb-fastapi-backend** (bullet 2): Motor fake reproducing the pre-4.4 `$meta` failure that silently killed a search leg behind HTTP 200; the raise is the regression guard. JD: "high bar for correctness", "dig until you understand why".
- **nb-agentic-search** (bullet 3): hybrid retrieval (substring + `$text` + bge vector, RRF), failing leg degrades to survivors; entity resolution 0% → 100% P@1 at 0.4 ms. JD: how data is read efficiently, operators / query execution.
- **nb-catalog-cache** (bullet 4): 13.2 MB per-user key (zero hit rate) → 10.9 MB shared, 78×, 512 MiB pod; 9.0 → 0.89 ms copy, 15 vs 127 µs shallow vs deep. JD: "performance, grounded in measurement rather than intuition".
- **nb-llm-failure** (bullet 5): 65% failure rate, Redis Streams stall killing an `asyncio.gather` batch, Langfuse unbounded reasoning loop, 2,048 cap vs p95 1,197, binomial 49–66% vs 65%. JD: concurrency, measurement, following a problem across services.
- **nb-ownership / nb-swiftui-app + nb-ads-max** (bullet 6): sole SwiftUI engineer, SportsBreak hyperlinked, 1.4K ratings; linker dead-stripped adapters, `-ObjC` fix proved by +7.5 MB delta. JD: "following a problem across languages ... and layers of the stack".
- **hd-lead-mvp + hd-langchain-apis**, **hd-mentor-process** (Haddee, 2 bullets): database schemas, code review, mentoring. JD: communication, code review.
- **za-mock-interview + za-auth-db + za-demos-contracts** (ZenAI, 1 bullet, fused).
- **cm-psc** (research, 1 bullet): fill; stochastic systems reads closer to "Mathematics / Physics" rigor than the LLM-spec line.
- **pj-cs537-os**: pthread quicksort (mutexes, condition variables), xv6 syscall entry points + clone wrapper. JD requires concurrency and OS coursework/projects. No speedup, kernel `clone`, or `join` claimed.
- **ld-ece-fellow**.
- Coursework: CMU Distributed Systems, Data Science for SE; UW Operating Systems, Algorithms, Data Structure & Programming III (JD: algorithms, data structures, OS, distributed systems). LLM Systems and Computer Architecture dropped to stop each line wrapping.
- Skills: Java and C first (JD language list); Data & Systems row second. Certifications kept.

## Skipped
- nb-llm-pipeline, nb-retired-detector, nb-morning-digest: LLM product work, not data systems; no room at the 6-bullet cap.
- nb-cronjob-outage, nb-observability, nb-third-party-proxy, nb-server-driven-ui, nb-live-activities, nb-app-store, nb-manual-broadcast, nb-jira-process, nb-cross-dept, nb-dramabreak-*, nb-coaching-marketplace: lower fit than the six chosen.
- cm-nl-safety: one research line is enough; LLM-to-spec is less relevant.
- pj-my-av, pj-wisconsin-autonomous, pj-codingplans: OS project fits the JD better.

## Gaps (not in inventory)
No Rust, Scala, C++, Spark, Arrow, Parquet, Iceberg, or open-source contributions. The JD lists open-source contributions under "What We Require".

## Page-fill check
First compile spilled to 2 pages; trimmed coursework, bullets 3/5/6, and a skills widow, then re-expanded bullets 1 and 5 to fill.
Final: 1 page; bottom margin 0.36 in = 25.92 pt; last content yMax 758.47 pt; unused 792 − 25.92 − 758.47 = 7.61 pt. Rendered at 90 dpi: no empty strip, clipping, overlap, or cramped text; SportsBreak hyperlinked.
