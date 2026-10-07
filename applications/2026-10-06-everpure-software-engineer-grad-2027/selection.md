# Selection — Everpure (formerly Pure Storage), Software Engineer Grad 2027 (8249851)

## NewsBreak title

**Software Engineering Intern** — the JD is a general "Software Engineer Grad" role spanning "low-level hardware to large-scale cloud systems"; no backend-only, full-stack, iOS, or AI framing. Heading is plain "NewsBreak" (not new products / ventures).

## Items used

NewsBreak (8 bullets, to fill the page with the most systems-relevant facts):
1. **nb-catalog-cache** — 13.2 MB per-user key → 10.9 MB shared (78×), 512 MiB pod, 9.0 → 0.89 ms copy. JD: "data efficiency", "performance".
2. **nb-catalog-cache** — 25–30 request fan-out → 1 call, 3-second per-source budget, first page 2.8 MB (~4.7 s) → ~0.27 MB, 206 topics. JD: "scales effectively with ever-increasing data volumes".
3. **nb-fastapi-backend** — first commit → 89 endpoints, MongoDB, ~1,450 offline tests (0.17 s), ruff / pyright / pytest gate, Motor fake as regression guard. JD: "extensive automated testing".
4. **nb-llm-pipeline** — embedding-cosine near-duplicate shortlist + LLM same-story dedupe, 4,100+ decisions, filler 34% → 4%. JD: "data deduplication" (honest analog: content dedupe, not block-level).
5. **nb-cronjob-outage** — 5-day silent outage, ImagePullBackOff + Forbid concurrency, paired deadlines. JD: "concurrency", reliability.
6. **nb-llm-failure** — 65% failure rate, Redis-stream `read_article` stall killing an `asyncio.gather` batch, 16,384-token runaways, 2,048-token cap. JD: "concurrency", problem solving.
7. **nb-agentic-search** — substring + `$text` + vector fused by RRF, degrade-to-survivors, 0% → 100% P@1, 0.4 ms per resolve. JD: reliability, performance.
8. **nb-ownership** + **nb-swiftui-app** — sole SwiftUI / primary backend, ~6,000 installs, 1,119 peak DAU, 344 PRs / 340 merged; SportsBreak hyperlinked per inventory.

Other roles:
- **hd-lead-mvp** + **hd-langchain-apis** (schemas / REST APIs) + **hd-mentor-process** (PR reviews, Git workflows and testing protocols) fused into one bullet. JD: "collaborate", "code quality".
- **za-mock-interview** + **za-demos-contracts** fused into one bullet.

Projects: **pj-codingplans** (KV-cache / quantization testing), **pj-wisconsin-autonomous** ("low-level hardware"), **ld-ece-fellow**.

Coursework: CMU — Distributed Systems, Foundations of Software Engineering, Software Refactoring. UW — Operating Systems, Computer Architecture, Data Structure & Programming III, Algorithms (fundamentals + low-level first).

Skills: C first (closest inventory match to C++), systems/testing row second (asyncio, Unit Testing, TDD, pytest, CI/CD).

## Skipped

- **pj-my-av** — cut to get back to one page; ML is the least relevant project for storage.
- **nb-eks-standup, nb-third-party-proxy** — infra / security; less relevant than cache and concurrency items.
- **nb-retired-detector, nb-morning-digest, nb-jira-process** — LLM product or process; lower JD fit.
- **iOS items** (nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-dramabreak-*) — mobile; only the SportsBreak ownership line kept.
- **Research (cm-psc, cm-nl-safety)** — JD does not care; page was full without it.

## Near-violations

- **C++** is the JD's core requirement and is not in `inventory/skills.md`. Only C is listed. Not added.
- **Deduplication / reclamation / WAN replication** — inventory has only content-level near-duplicate detection in the news pipeline. Bullet 4 says "near-duplicates" and "same-story dedupe"; it does not claim storage or block dedupe.
- Bullet 6 first draft said the cap "truncates 0% of successes" (inventory: of observed successes); shortened to "sized a 2,048-token cap" for space rather than drop "observed".
- First compile was two pages (four lines over). Tightened four bullets and cut my-av, then restored the Haddee mentoring clause to fill.

## Page-fill verification (final PDF)

- Pages: 1
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`); page height 792 pt
- Last content bottom (pdftotext -bbox max yMax): 755.10 pt
- Unused height: 792 − 25.92 − 755.10 = **10.98 pt** (within 0–12 pt)
- Visual review: rendered the whole page at 110 dpi. No empty bottom strip, clipping, overlap, or cramped lines. UW coursework wraps "Algorithms" onto its own line; acceptable. Spacing is the shared preamble with the template's `itemsep=0.7pt`.
