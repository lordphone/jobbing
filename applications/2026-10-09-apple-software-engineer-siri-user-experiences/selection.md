# Selection — Apple, Software Engineer, Siri User Experiences (200687375)

## NewsBreak title

**Software Engineering Intern** — the posting title is "Software Engineer" and the role is the on-device platform for Siri / Apple Intelligence "across the OS", not an iOS-app role, so the general-SWE default fits. "iOS Engineer Intern" was the close alternative (Swift is listed first; "Experience developing mobile ... software" is preferred). Heading is plain "NewsBreak" (not a new-venture JD).

Header city: Mountain View, CA (posting is Cupertino, Bay Area).

## Items used

- **nb-swiftui-app + nb-app-store** → bullet 1: sole SwiftUI engineer, SportsBreak link, 1.4K ratings, peak DAU 1,119, 43,695 lines / 233 views, Firebase auth with Apple sign-in, 72-event analytics catalog, shipped through three trademark rejections — "mobile ... software", "ship new capabilities".
- **nb-live-activities** → bullet 2: ActivityKit Live Activities + widget extension with shared ScoreboardKit; push-to-start never worked because iOS drops a start push without `aps.alert` while APNs returns 200 — "investigate and resolve software issues", OS-level iOS behavior.
- **nb-server-driven-ui** → bullet 3: 27 widget types, no App Store release for new surfaces, unknown kinds drop — platform software.
- **nb-morning-digest** → bullet 4: Catch Me Up, ~1,341 generations/day, 5,026 users (~81%), source index 10/10 — "software that interfaces with AI-powered systems", LLMs.
- **nb-llm-pipeline** → bullet 5: embed → LLM-score → select → LLM dedupe → APNs, ~2 min, ~1,200 LLM calls/day, filler 34% → 4%, 2/day cap over 11,745 user-days — LLMs reaching the device.
- **nb-catalog-cache** → bullet 6: 25–30 requests → 1 call, home-load copy 9.0 ms → 0.89 ms, 78× smaller shared cache sized for a 512 MiB pod — "performance optimization", "resource-constrained environments".
- **nb-ads-max** → bullet 7: `NSClassFromString` dead-strip root cause, `-ObjC` linker fix proved with +7.5 MB binary delta and 0 → 2 adapter symbols — Objective-C / build-system debugging.
- **nb-fastapi-backend + nb-third-party-proxy** → bullet 8: first commit → 89 endpoints, ~1,450 offline tests, ruff / pyright / pytest gate; nine integrations server-side, zero API keys in the app — "testing", "quality and reliability".
- **hd-lead-mvp (agile) + hd-langchain-apis** → Haddee 2 lines (collaboration, LLM features).
- **za-mock-interview + za-auth-db + za-demos-contracts** → ZenAI 2 lines (second line added as page fill).
- **cm-nl-safety** → research (multi-turn LLMs; kept as fill — "research ... experience" is in preferred quals).
- **pj-cs537-os** → project line: pthread quicksort in C, xv6 syscall entry points and clone wrapper — "operating systems concepts, concurrency".
- Skills: Swift, Python, C first (JD languages; Java also named); iOS row (SwiftUI, ActivityKit, WidgetKit, APNs, Xcode, SwiftPM, App Store Connect); AI & Tools row with Claude Code / AI coding tools ("AI-assisted coding tools"), Git, pytest ("version control", "testing"); backend/infra row; certifications kept.
- Coursework: CMU — LLM Systems, Distributed Systems, Machine Learning; UW — Operating Systems, Mobile Computing Laboratory, Computer Architecture, Algorithms.

## Skipped

- nb-ownership (commit share/PR counts): bullet 1 already says sole SwiftUI engineer; space.
- nb-agentic-search, nb-llm-failure, nb-retired-detector: LLM backend depth; the digest and alert pipeline cover LLMs reaching the device more directly. Space.
- nb-eks-standup, nb-cronjob-outage, nb-observability: infra, lower JD value; space.
- nb-manual-broadcast, nb-dramabreak-ads, nb-dramabreak-stripe, nb-coaching-marketplace, nb-jira-process, nb-cross-dept: space.
- hd-mentor-process, cm-psc: space / off-JD.
- pj-my-av, pj-wisconsin-autonomous, pj-codingplans, ld-ece-fellow: OS coursework fits the preferred quals better; no room for a second project line.

## Constraints almost violated

- Not claimed: C++ (pj-cs537-os notes say C only), Objective-C as a skill (not in skills.md; the bullet only names `NSClassFromString` / `-ObjC` from nb-ads-max), any on-device ML model work, iOS unit tests (inventory says no iOS test target), measured parallel speedup or completed kernel threading from the OS coursework.
- The Live Activity bullet states the finding only; the fix ("raising on the sender") was cut for space, not altered.
- Digest "source index (10/10 linked)" is the citations-version fact; worded as "bullets carry a source index", not "every bullet ever".
- First compile spilled 3 lines to page 2 (three Skills rows wrapped, bullet 1 widow). Trimmed Firebase Auth, Unit Testing, REST APIs from Skills and tightened bullets 1 and 4; that left 33.9 pt, so restored the digest generation count / source-index clause and added the second ZenAI line.

## Page-fill verification (final PDF)

- Pages: 1 (letter, 792 pt tall)
- Bottom margin: 0.36 in = 25.92 pt (from `shared/preamble.tex`)
- Last content bottom (pdftotext -bbox yMax): 759.54 pt
- Unused height: 792 − 25.92 − 759.54 = 6.54 pt (passes 0–12 pt)
- Visual review: rendered at 110 dpi. No empty bottom strip, clipping, overlap, or cramped text; all Skills rows fit on one line.
