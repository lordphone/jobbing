# Story bank

One section per story. Rehearse from the bullets, not a script. `GAP` marks something an interviewer is likely to ask that the inventory does not answer yet — fill it in before the interview.

---

## agent-cache

Agent-built cache that could never hit.

- inventory: `nb-catalog-cache`
- types: working with AI tools, reviewing code, performance, production issue, lesson learned
- used with: (company not recorded, 2026-09-23)

**STAR**
- S: NewsBreak, SportsBreak app. An agent wrote the catalog cache for the main content page; clean code, I wrote tests.
- T: As the app grew, pod memory climbed toward its 512 MiB limit.
- A: Found the cache keyed per user — 13.2 MB per user, near-identical data, hit rate structurally zero. Worked out the ceiling: 10,000-entry cap ≈ 111 GB. Re-keyed on content (`curator_id`). Switched deep copy to shallow copy.
- R: One shared 10.9 MB copy, 78× smaller. Home-load copy 9.0 ms → 0.89 ms (shallow copy 15 µs vs 127 µs deep).
- Lesson: tests prove only what they check; review agent code for cost at real scale.

**Likely follow-ups**
- Why did the agent key it per user? — GAP
- Why didn't your tests catch it? — GAP (draft answer assumes they tested correctness, not hit rate or memory; confirm)
- How did you notice the memory climb — dashboard, alert, restarts? — GAP
- Why is a shallow copy safe here? What stops a caller mutating shared data? — GAP
- What would you do differently? — GAP
- Context: catalog grew 97 → 206 topics; one backend call replaced a 25–30 request client fan-out.

---

## push-to-start

Live Activity push-to-start that had never worked, behind HTTP 200.

- inventory: `nb-live-activities`
- types: hardest bug, working with AI tools, silent failure, mobile
- used with: (company not recorded, 2026-09-23)

**STAR**
- S: NewsBreak, SportsBreak iOS. Live Activity push-to-start had never worked.
- T: Find why, with no signal: APNs returned HTTP 200 on every send; logs and tests showed nothing.
- A: Went down a rabbit hole of irrelevant leads first. Found that iOS silently drops a start push without `aps.alert` even though APNs accepts it. Made the sender raise when a start push is missing `aps.alert`.
- R: Push-to-start works; the failure mode can no longer be silent.
- Lesson: a 200 from APNs does not mean the push reached the phone. Treat an AI's confident diagnosis as a hypothesis.

**Likely follow-ups**
- How did you finally find the real cause? — GAP (the most important one)
- What leads did you chase first, and why were they wrong? — GAP
- How long did it take? — GAP
- How did you verify the fix — real device? — GAP
- Why raise on the sender instead of just adding the field? — GAP
- Context: shipped ActivityKit Live Activities plus a shared ScoreboardKit widget; removed ~380 lines of bespoke scoreboards.
