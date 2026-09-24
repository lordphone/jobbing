# NewsBreak (ParticleMedia)

- official title: Engineering Intern
- printed title: pick one from the list below to match the JD; do not invent another
  - Software Engineering Intern — default; general SWE / "software engineer" JDs. Print "SWE Intern" only if the JD itself says SWE.
  - Engineering Intern — official title; use when the JD says intern / engineering intern and is not more specific
  - Backend Engineer Intern — JD is backend, APIs, or services; he was the sole backend owner and most of the work was backend
  - Full-Stack Engineer Intern — JD is full-stack / fullstack; iOS + FastAPI from the first commit, primary on both
  - iOS Engineer Intern — JD is iOS / Swift / SwiftUI; sole SwiftUI engineer, ~69% of iOS commits, App Store, Live Activities
  - Mobile Engineer Intern — JD is mobile and not iOS-specific; same grounding as iOS
  - Infrastructure Engineer Intern — JD is general infra / cloud / Kubernetes and is not AI infra; EKS, Helm, Jenkins, CronJobs
  - AI Engineer Intern — JD is AI / ML / LLM / agents as product work; the intern work was written with AI
  - AI Infrastructure Intern — JD is AI infra / ML infra / LLM platform / serving. Grounded in EKS+Helm LLM CronJobs, DeepInfra embed+LLM, Langfuse, RAG retrieval. Print "AI Infra Intern" only if the JD itself says AI Infra.
- default printed title: Software Engineering Intern
- team: Venture / NexBreak
- dates: May 11, 2026 -- August 14, 2026
- location: Mountain View, CA (in-office)
- primary: SportsBreak iOS + `sportsbreak-service`
- secondary: DramaBreak (iOS + `aigc-service`), `nbot-curator-server`, newsletter tool
- stack: Python 3.12, FastAPI, MongoDB/Motor, Pydantic, Swift/SwiftUI, Firebase, APNs, Amplitude, AppLovin MAX, Kubernetes/EKS, Helm, Jenkins, Docker, GitHub Actions, Langfuse, RAG
- grew the app with the team

---

# Ownership

## nb-ownership

tags: leadership, fullstack
facts:
- sole full-time engineer on SportsBreak iOS + backend from ~2026-06-12 (Vivek last activity) until Khalil joined ~2026-07-01; onboarded Khalil
- pretty much the sole SwiftUI engineer; teammates only made the iOS init commit
- ~69% of iOS commits (429/621); ~83% of backend (397/475)
- team of ~6
- authored 344 PRs across 5 repos, 340 merged
- opened backend repo with first commit on 2026-05-12
- iOS 43,695 lines / 222 Swift files; backend 61,661 lines / 257 py files
approved:
- default: Sole SwiftUI engineer (teammates made the iOS init commit) and primary backend author (69% of iOS commits; opened the backend with its first commit); authored 344 pull requests across five repositories (340 merged).
- window: Sole full-time engineer on SportsBreak iOS + backend between one engineer rolling off and the next joining, whom I onboarded.

---

# Backend

## nb-fastapi-backend

tags: backend, api, testing
facts:
- first commit 2026-05-12
- Python 3.12 / FastAPI / MongoDB (Motor)
- 89 endpoints (53 GET, 18 POST, 10 DELETE, 8 PUT) across 27 routers
- 129 Pydantic models, 29 repositories, 26 collections, ~48 indexes
- 7 Kubernetes CronJobs
- 10 runtime dependencies; no ORM, no Redis, no Celery
- ~62k lines backend; `app/` 29,680 vs `tests/` 29,628 (1:1 line ratio)
- test suite grew 25 → ~1,450 (his last commit; later main includes others' tests)
- fully offline in 0.17s — no Mongo, no Firebase, no network
- hand-written Motor fake deliberately reproduces the production cluster's pre-4.4 `$meta` failure (that mismatch silently killed a search leg behind HTTP 200 on 2026-07-22)
- the raise is the regression guard
- ruff + pyright (pinned 1.1.410) + pytest CI gate
- 99.7% return-type / 99.5% parameter annotation coverage
approved:
- default: Built the FastAPI backend from the first commit to 89 MongoDB endpoints on EKS, with ~1,450 fully-offline tests (1:1 vs. production lines).
- detailed: Opened a production FastAPI service with its first commit and grew it to 89 endpoints across 27 routers, ~62k lines, and ~1,450 fully-offline tests (0.17s) behind a ruff / pyright / pytest gate.
- with-cache: Built the FastAPI / MongoDB backend from the first commit to 89 endpoints, with ~1,450 fully-offline tests, and replaced a 25–30 request client fan-out with one backend call.
- regression: Grew the suite to ~1,450 fully-offline tests (0.17s) against a Motor fake that reproduces the production cluster's pre-4.4 `$meta` failure — the raise is the regression guard.

## nb-eks-standup

tags: infra, kubernetes, ci
facts:
- production EKS on day 3 (Helm, Jenkins, corp-internal ingress)
- diagnosed DNS → TLS → admission-policy chain blocking iOS on public networks; real fix was a public domain (`api.sportsbreak.ai` live 2026-05-22)
- found stale ArgoCD app pinning `v0.1.0` with `prune: true, selfHeal: true` that would have wiped Jenkins deploys
- 7 CronJobs; HPA min 2 / max 4 at 70% CPU
- two-stage amd64 image (pymongo bson C extension SIGILLs on arm64)
- ruff / pyright / pytest GitHub Actions gate added after two tests had been red on `main` (Jenkins previously only built the image)
- Helm 689-line values against an external org chart
approved:
- default: Stood up production EKS (Helm, Jenkins) on day 3: 7 CronJobs, a two-stage amd64 image, and a ruff / pyright / pytest gate.
- day3: Stood up the service on production EKS on day 3, then diagnosed a DNS → TLS → admission-policy chain that blocked iOS clients on public networks and drove a public-domain fix.

## nb-third-party-proxy

tags: backend, mobile, security
facts:
- migrated nine third-party integrations server-side (SportsDataIO ×3, YouTube Data v3, SerpApi, DeepInfra LLM + embeddings, NBot public + internal, internal comment classifier, APNs)
- iOS binary ships zero third-party API credentials
- ESPN proxy rolled back 2.5 hours later — ESPN public API has no key, so the proxy added latency and a health dependency for nothing
approved:
- default: Migrated nine third-party integrations server-side so the iOS binary ships zero third-party API credentials.

## nb-catalog-cache

tags: backend, infra, performance
facts:
- World tab ~25–30 client requests → 1 backend call (day 5); 3-second per-source budget
- cache was 13.2 MB per user keyed per user (hit rate structurally zero)
- re-keyed on content / `curator_id` → 10.9 MB shared, 78× smaller
- 15 µs shallow vs 127 µs deep copy (8.6×); home-load copy 9.0 ms → 0.89 ms
- 512 MiB pod; uncapped catalog would OOM (CACHE_MAX_ENTRIES 10,000 implied ~111 GB)
- catalog 97 → 206 topics; section ~53 KB resident / ~9 KB serialized; full catalog ~11 MB resident / ~1.9 MB JSON
- first-page payload 2.8 MB / ~4.7 s → 20 sections ≈ 0.27 MB
- 168 of 206 topics previously unreachable without paging
- cache code was written by an AI agent; the code was clean and he wrote tests for it
- found the per-user key after the pod's memory climbed toward the 512 MiB limit as the app grew (not caught before production)
approved:
- default: Replaced a 25–30 request client fan-out with one backend call and a shared 10.9 MB catalog cache — 78× smaller than a per-user key — sized for a 512 MiB pod.
- redesign: Redesigned a cache that could not hit: 13.2 MB per user (structurally-zero hit rate) → 10.9 MB shared (78×), after pod memory climbed toward its 512 MiB limit.

## nb-cronjob-outage

tags: infra, kubernetes, debugging
facts:
- 5-day silent outage of the `push-live-activities` CronJob
- empty image tag → ImagePullBackOff (non-terminal) → Job stayed Active → Forbid concurrency skipped every later run
- fixed with paired Job `activeDeadlineSeconds` and scheduler `startingDeadlineSeconds` (SVC#93)
- fixed the mechanism, not the detection (no cron success/duration metrics)
approved:
- default: Diagnosed a 5-day silent Live Activity CronJob outage (non-terminal ImagePullBackOff + Forbid concurrency) and fixed it with paired job and scheduler deadlines.

---

# iOS / mobile

## nb-swiftui-app

tags: mobile, frontend, fullstack
facts:
- pretty much the sole SwiftUI engineer
- primary iOS author (~69% of commits)
- 43,695 lines, 233 views, 12 view models, 26 service types, 196 previews
- iOS 18+, iPhone-only, 28 SwiftPM pins, no CocoaPods
- Firebase auth: Google + Apple + email/password; guest-first anonymous sessions upgraded via `link()`
- analytics catalog: ~50 custom events at first ship; 72 names; 76 queryable in Amplitude by Aug 2026
- 74 typed emit methods, server-side allowlist
- binary with zero third-party API keys (after proxy migration)
- the app reached peak DAU 1,119 (2026-08-10) and 5,999 installs by 2026-08-11 (Amplitude)
- grew the app with the team
- no iOS test target and no CI
approved:
- default: Sole SwiftUI engineer for a consumer sports app (peak DAU 1,119; ~6,000 installs by 2026-08-11); shipped Firebase auth, a 72-event analytics catalog, and a binary with zero third-party API keys.
- scale: Shipped a 43,695-line SwiftUI app (233 views, 196 previews) to the App Store; iOS has no test target — 196 previews and a device/simulator protocol were the substitutes.

## nb-server-driven-ui

tags: mobile, frontend
facts:
- built the server-driven UI
- backend registry has 27 widget types; iOS has 31 widget renderer files
- World feed paging, topics catalog, search sections, region bucketing
- unknown widget/section kinds dropped rather than failing a page
- a new catalog surface does not require an App Store release
approved:
- default: Built server-driven UI over 27 widget types so a new catalog surface ships without an App Store release; unknown kinds drop instead of failing a page.
- paging: Built World-feed paging and search sections so unknown kinds drop instead of failing a page — a new catalog surface does not require an App Store release.

## nb-app-store

tags: mobile
facts:
- launched 2026-06-17 after 3+ FIFA/World Cup trademark rejections (06-10, 06-12, 06-15)
- cut the hero World Cup feature to launch at all
- ATT rejection: SwiftUI `.onChange` does not fire for its initial value, so cold launch skipped the prompt; moved to `didBecomeActive`
- custom product page ASO approved 2026-07-15 after one rejection
- #129 App Store Sports chart
approved:
- default: Shipped to the App Store on 2026-06-17 through three trademark rejections, cutting the hero World Cup feature to launch at all.

## nb-live-activities

tags: mobile
facts:
- ActivityKit Live Activities + widget extension
- shared ScoreboardKit compiled into both targets; removed ~380 lines of bespoke scoreboards
- Live Activity push-to-start had never worked: iOS drops a start push with no `aps.alert` while APNs returns HTTP 200; fixed by raising on the sender
- went down a rabbit hole of irrelevant leads before finding the real cause (APNs 200 meant logs showed no problem)
- general, across his debugging: AI tools have repeatedly claimed with confidence to have found a bug's cause, then contradicted themselves one turn later after reading log output
approved:
- default: Shipped ActivityKit Live Activities and a shared scoreboard widget; found that iOS drops a start push with no `aps.alert` while APNs returns 200.

## nb-ads-max

tags: mobile, ads
facts:
- migrated SportsBreak (and DramaBreak) to AppLovin MAX with Liftoff/Mintegral mediation
- root cause: `NSClassFromString` adapter instantiation → linker dead-stripped static archives
- proved `-ObjC` fix: binary 28.36 → 36.19 MB (+7.5 MB) and adapter symbols 0 → 2
- native fill 1/3 → 5/0 in one session
- `app-ads.txt` SportsBreak 62 → 1,332 records, recovering three days of silently discarded Liftoff bids
approved:
- default: Migrated the ad stack to AppLovin MAX; root-caused dead-stripped mediation adapters to `NSClassFromString` and proved the `-ObjC` fix with a +7.5 MB binary delta and 0 → 2 adapter symbols.
- app-ads: Expanded `app-ads.txt` from 62 → 1,332 records, recovering three days of silently discarded bids.

## nb-morning-digest

tags: llm, mobile, frontend
facts:
- Catch Me Up personalized morning digest — live 2026-07-14
- ~1,341 generations/day
- 5,026 unique users via `catch_me_up_digest_view` ≈ 81% of 6,215 lifetime users
- digest bullets use a cluster `source` index (10/10 bullets linked vs 0/6 → 5/6 on the old sourceless markdown)
- SWR caching on the digest path
approved:
- llm: Shipped a personalized LLM morning digest to 5,026 users (~81% of the base).
- mobile: Shipped a personalized morning digest to 5,026 users (~81% of the base), plus ActivityKit Live Activities and a shared scoreboard widget.
- citations: Re-sourced the morning digest onto nbot highlight clusters so bullets carry a source index (10/10 linked); reached 5,026 users (~81% of the base).

## nb-manual-broadcast

tags: mobile, backend
facts:
- manual segment-broadcast tool, live
- World Cup notifications were faster than other sports apps (Real Sports) and arrived a minute before FOX broadcasted a goal
- LeBron-to-76ers 2026-07-24: 117 people, 90 phones buzzed
approved:
- default: Built a live manual segment-broadcast tool used during the World Cup; notifications beat other sports apps and arrived a minute before FOX broadcasted a goal.

---

# LLM / search / alerts

## nb-retired-detector

tags: llm, backend
facts:
- first breaking-news detector used corroboration (how many publishers covered a story)
- 19 hours of production shadow: pipeline 1.8 min p50 vs 901 min (15 h) from the story's first article
- 20 of 26 would-be alerts >6 h old; 35 fires = 21 distinct stories; 12 UFC vs 1 NFL
- most-corroborated item (5 publishers) was UFC card-filler
- deleted the detector, 1,003-line calibration harness, and tests — net −882 lines — 2 days 1 hour after writing them
- kept corroboration as offline ground truth ("useless at t=0, useful at t+15h")
approved:
- default: Retired my own corroboration-based detector after 19 hours of production data showed it was structurally 15 hours too slow (901 min p50 from a story's first article vs 1.8 min pipeline latency), net −882 lines.

## nb-llm-pipeline

tags: llm, backend, infra
facts:
- designed ingest → embed → LLM-score → select → LLM same-story dedupe → APNs in the same CronJob run (~2 min ingest-to-decision)
- embed: DeepInfra `BAAI/bge-base-en-v1.5` (not an LLM), L2-normalized; cosine shortlists near-duplicates against that user's last 3 days — not corpus clustering
- score: DeepSeek-V4-Flash, one call per article, temperature 0; categorical `happened / speculative / no_event` + 0–100 importance; model never sees topic or season
- select: percentile vs that topic's rolling 7-day score distribution (not article/publisher count), plus an absolute score floor so a quiet topic cannot promote its least-bad item
- low-water bar: 90th percentile if that user has been quiet 20h, else 98th
- quiet hours: UTC 07:00–12:00; alerts in the window are dropped, not deferred
- final LLM same-story judge so a user does not get two notifications for the same event; cosine >= 0.84 same / < 0.70 different / 0.70–0.84 one LLM call per pair
- notifications are personalized to topic followers
- caps: 2/day and 1/topic per user — 1/topic sits on top of the daily cap
- trending path for users who follow nothing: national curator only, best-scoring item of the run, absolute score >= 65, 1/day
- 5% rollout hash (`sha1(uid) % 100`) is a blast-radius control, not an A/B; cohort was pre-set to 100% so flipping dry_run could not half-apply
- deliver: APNs fan-out plus an in-app inbox row per user
- decision log: one row per item with why it fired or did not (`sent` / `below_bar` / `not_event` / `no_audience` / `all_suppressed`)
- Kubernetes CronJob; ~1,200 LLM calls/day; DeepSeek-V4-Flash; `bge-base-en-v1.5`
- production shadow: 11 consecutive days of formal reviews (2026-07-31 → 08-10)
- 4,100+ decision rows in the shadow window
- `NEWS_ALERTS_DRY_RUN` flipped to false — shipped, live sends
- filler by count: 34% → 4%
- filler device-weighted: 29% → 3%
- hand-graded alerts: nothing-happened scored median 89 vs 90 for confirmed events, so added a categorical `happened / speculative / no_event` gate
- 13% of good alerts blocked by the gate
- 127-alert holdout: 36% blocked vs 37% on the tuned day
- prompt ablation: category block alone catches 52% of filler
- rejected a "multi-event = roundup" rule that caught 91% of filler but killed the day's two highest-reach real alerts (218 and 123 devices) to remove ~40 devices of filler
- temp 0 re-score: most scores identical; 4 crossed the alert line
- live send rate: 1.8 median/day, cap 2/day and 1/topic, all users
- 2/day cap held over 11,745 user-days with zero violations
- quiet hours shipped 2026-08-10 (`SVC#152`); dedupe threshold stayed 0.78
approved:
- llm: Designed and shipped a personalized breaking-news pipeline: embed with bge, LLM-score each article on arrival, gate on per-topic 7-day percentile, then an LLM same-story judge so users do not get two alerts for one event; cut filler 34% → 4% by count, 29% → 3% device-weighted.
- design: Designed ingest → embed → LLM-score → select → LLM same-story dedupe → APNs in one CronJob (~2 min): bge shortlists near-duplicates, DeepSeek scores (model never sees topic), percentile vs the topic's 7-day distribution (90th if a user has been quiet 20h), quiet hours that drop not defer, a trending path for users who follow nothing, then a final LLM judge so a user does not see two of the same notification.
- backend: Built a personalized LLM alert pipeline as a Kubernetes CronJob, calibrated it in production shadow, then shipped it live at 1.8 median sends/day (cap 2/day and 1/topic); filler 29% → 3% of devices.
- cut: Built a personalized breaking-news scorer, calibrated it in production shadow, and shipped it; cut filler 29% → 3% after corroboration lagged 15h.
- shadow: Designed a personalized LLM-judged breaking-news pipeline, calibrated it in production shadow on 4,100+ decision rows, then shipped it live at 1.8 median sends/day (cap 2/day and 1/topic); filler 34% → 4% by count, 29% → 3% device-weighted.
- gate: Hand-graded alerts and found filler and fact both scored 89–90, so added a categorical gate; filler 34% → 4% by count, 29% → 3% device-weighted.

## nb-agentic-search

tags: llm, search, backend
facts:
- shipped 2026-08-07 — `POST /api/v1/search/answer`, one SSE endpoint, two modes, split on who decides how many retrievals
- turn 1 (committed search): deterministic RAG — code plans retrieval; zero model-initiated retrievals; 1 streaming answer + 1 concurrent suggestion, neither given `tools`
- turn 2+ (in-chat follow-up): the model picks tools; ≤3 hops, ≤4 calls/hop, 45s wall clock
- 5 whitelisted tools: `search_articles`, `find_games`, `scores_on_day`, `standings`, `resolve_entities`
- hybrid retrieval underneath: substring + Mongo `$text` + `BAAI/bge-base-en-v1.5` vector, fused by RRF (k=60), 7-day half-life recency floored at 0.2, cosine floor 0.62
- any retrieval leg failing degrades to the survivors; only all legs failing is a 500
- entity resolver is the query rewriter: pass catalog display names to the index, not the question words — raw "how did the dodgers do last night" retrieved WNBA / Godzilla noise; "Los Angeles Dodgers" did not
- question-shaped gate: bare entity lookups skip the LLM (most real `search_submit` traffic)
- evidence floor before answering, re-applied on turn 2+
- server-resolved citations by index — model emits `[n]` only, cannot author a URL; unresolvable index dropped
- DeepSeek-V4-Flash over DeepInfra (not Claude); native tool calling verified against the live gateway before the loop was fixed
- SSE streaming; conversation state client-held (no PII at rest); 20 req/min per uid
- TTFT 0.85s vs 2.53s full answer — single-run, not p95
- 23 problems found by manual grounding spot-check
- ~62% of corpus invisible to in-process vector index (20,000 of 53,639 docs)
- Amplitude: 187 unique search users lifetime
- multi-turn conversations with suggested follow-ups
- deterministic span-based entity resolution over 206-entity catalog
- 0% → 100% P@1 on real logged queries that previously returned nothing
- 28/28 recall, 20/20 P@1, 0/10 zero-result
- 0.4 ms per resolve
- rejected embeddings: cosine returns one blurry neighbour where span matching returns both teams
- eval harness runs against the real committed catalog, not a fixture
approved:
- default: Shipped agentic search with hybrid retrieval and server-resolved citations; entity resolution hit 100% P@1 on real logged queries.
- with-followups: Shipped an LLM search agent with server-resolved citations and entity resolution; achieved 100% P@1 on real logged queries and enabled multi-turn conversations with suggested follow-ups.
- grounded: Built agentic search — one endpoint, two modes — with server-resolved citations (the model emits only an index, so it cannot author a URL), a bounded tool loop (≤3 hops, 45s), and SSE streaming.
- design: Designed one SSE search-answer endpoint with two modes: turn 1 is deterministic RAG (code retrieves, model never gets tools), turn 2+ is a bounded agent (≤3 hops, 5 tools); hybrid RRF retrieval, entity resolver as the query rewriter, a question-shaped gate so bare lookups skip the LLM, and server-resolved `[n]` citations the model cannot author.
- entities: Took real logged search queries from 0% to 100% P@1 with deterministic entity resolution at 0.4 ms over a 206-entity catalog, after rejecting embeddings with measurements.

## nb-llm-failure

tags: llm, infra, debugging
facts:
- another team's LLM pipeline (`nbot-curator-server`, 1,661-commit repo); helped debug it
- 10 commits / 7 PRs
- earlier outage: DeepInfra HTTP 402 ($0 balance) swallowed by bare `except:`; PR #250 model-id fallback across 4 call sites
- ~65% run-failure rate
- Redis streams: one `read_article` stall killed an `asyncio.gather` batch
- Langfuse: unbounded reasoning loop, `enable_thinking`, no `max_tokens`, runaways at 16,384; one trace 701 s / 16,384 tokens / empty JSON
- successful reads: min 354 / p50 684 / p95 1,197 / max 1,197
- sized 2048-token cap (truncates 0% of observed successes)
- binomial predicted 49–66% vs observed 65%
- Helm env shadowed the code default
- timeout raise labeled a band-aid in the PR body with a pre-registered falsification test
- no post-deploy confirmation that the failure rate dropped
approved:
- llm: Diagnosed a 65% failure rate in a shared LLM pipeline, via Langfuse traces, as an unbounded reasoning loop (p95 1,197 tokens vs runaways at 16,384).
- backend: Diagnosed a 65% failure rate in another team's LLM pipeline, via Langfuse traces, as an unbounded reasoning loop hitting a 16,384-token ceiling.
- infra: Root-caused a 65% failure rate in another team's LLM workers via Langfuse traces and a Helm env shadowing the code default; scoped the token cap to the failing call path.
- honest: Diagnosed a 65% failure rate in a shared LLM pipeline as an unbounded reasoning loop at a 16,384-token ceiling, sized a 2048-token cap against p95 1,197, and modeled 49–66% vs observed 65%. No post-deploy confirmation — I left before the follow-up.

---

# Cross-team / process

## nb-dramabreak-ads

tags: mobile, ads
facts:
- minority contributor on a mature codebase: 43 of 565 iOS commits (7.6%), 13 of 1,049 backend
- 20 PRs, 19 merged; 20/20 targeted the correct base branch
- rewarded/interstitial unlock, per-drama `iaa`/`iap`/`iaap` contract (default `iap`)
- promo-code redemption with atomic `max_uses`
- MSP dummy bid tokens until `bidLoaderProvider` registered — verified with mitmproxy
- invalid `Package.resolved` for 6 weeks; −3 lines unblocked SPM for the team
- black screen after rewarded ads: AVPlayer resource contention
- notification-driven rewarded-ad preload removed ~10 s cold-auction wait
- native feed ads stayed on MSP after the MAX migration
approved:
- default: On DramaBreak, migrated ads to AppLovin MAX and diagnosed a post-rewarded-ad black screen as AVPlayer resource contention in a mature two-repo codebase.

## nb-dramabreak-stripe

tags: backend, mobile
facts:
- Stripe web checkout shipped (backend +389, iOS +194)
- signature-verified webhook as only trusted fulfillment; idempotent with 60s stale-pending reclaim; US-gated
approved:
- default: Shipped a Stripe web-checkout path (signature-verified webhook, idempotent fulfillment).

## nb-jira-process

tags: leadership
facts:
- built the SPR Jira board unprompted when asked for "a running list"; it became the canonical backlog
- 145 issues on the board; 75 reported / 46 assigned / 56 closed
- SPR-13 / SPR-15: he closed both himself in a June tidy-up, then reopened on 2026-08-05 with line-level evidence that the security fixes were absent
- 34–35 contract-first API wire specs; ~10,180 lines of documentation he authored
- onboarded the team's second engineer (Khalil Ibrahim) end to end
approved:
- default: Introduced the team's Jira backlog unprompted, wrote 34 contract-first API specs and ~10,000 lines of engineering docs, and onboarded the second engineer.
- audit: Spot-checked two closed security tickets against the code, found the fixes absent, reopened them with evidence, and wrote "a status field is not evidence of a code change" into the team doc.

## nb-coaching-marketplace

tags: fullstack
facts:
- coaching marketplace built for SportsBreak: profiles, reviews, booking; ~5,500 lines across both repos
- flag-disabled for App Store submission and never turned back on
- verified no deep link or notification could open a coaching screen behind the flag
approved:
- default: Built a coaching marketplace (~5,500 lines) and left it behind a flag with no leak via deep link or notification.