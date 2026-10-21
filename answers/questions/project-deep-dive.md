# Project deep dive

Questions that ask for one project or feature end to end: what it does, why, a challenge or tradeoff, and how it was built.

---

## Full-stack feature, challenge, and AI use

- question: Describe one full-stack application or feature you built (internship or personal project). What does it do, and why did you build it? What was one technical challenge or tradeoff you worked through? How did you use AI while building it and how did it help? Add a link (repo, paper, or demo) if you have one.
- company: Quora (Full Stack Software Engineer, New Grad)
- date: 2026-10-20
- story: [agent-cache](../stories.md#agent-cache); inventory `nb-catalog-cache`, `nb-server-driven-ui`, `nb-ownership`

```text
At NewsBreak, I built the World feed for SportsBreak, our sports news app: https://apps.apple.com/app/id6762649287. It's the main browse page, where users find teams and leagues to follow across 200+ topics.

I built it because loading the page took 25–30 requests from the iOS app, and any layout change needed an App Store release. I replaced that with one FastAPI endpoint that returns the whole page as server-driven UI. The backend picks from 27 widget types, and the SwiftUI app renders them. If the app sees a widget kind it doesn't know, it drops that widget instead of failing the page. That means we can ship new catalog sections without an app update.

The hardest part was the cache. An AI agent wrote the catalog cache, and the code was clean and passed the tests I wrote. But as the app grew, the pod's memory climbed toward its 512 MiB limit. The cache was keyed per user, so every user had their own 13.2 MB copy of a nearly identical catalog, and the cache could never hit. I re-keyed it on content, so now every user shares one 10.9 MB copy. I also switched a deep copy to a shallow one, which cut the copy time on home load from 9.0 ms to 0.89 ms.

I wrote most of my internship code with AI coding agents. That's how I could be the only iOS engineer and the main backend author at the same time. The agents handled the volume, and I owned design, review, and tests. The cache taught me where that split needs care: tests only prove what they check. Now when I review agent code, I work out what it costs at real scale, not just whether it returns the right answer.
```
