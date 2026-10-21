# Project deep dive

Questions that ask for one project or feature end to end: what it does, why, a challenge or tradeoff, and how it was built.

---

## Full-stack feature, challenge, and AI use

- question: Describe one full-stack application or feature you built (internship or personal project). What does it do, and why did you build it? What was one technical challenge or tradeoff you worked through? How did you use AI while building it and how did it help? Add a link (repo, paper, or demo) if you have one.
- company: Quora (Full Stack Software Engineer, New Grad)
- date: 2026-10-20
- story: [agent-cache](../stories.md#agent-cache); inventory `nb-catalog-cache`, `nb-server-driven-ui`, `nb-ownership`

```text
I built the World tab for SportsBreak, a sports news app I worked on during my internship at NewsBreak (https://apps.apple.com/app/id6762649287). It's the page where you browse teams and leagues to follow.

When I started on it, the iOS app was making 25 to 30 separate requests just to load that one page, and any layout change meant going through App Store review again. So I moved the work to the backend. The app now makes one call to a FastAPI endpoint, the response describes the whole page, and the SwiftUI side just renders it. If the app gets a section type it doesn't know yet, it skips it instead of breaking, so we could add new sections without shipping an app update.

The problem I remember most was the cache. I had an AI agent write it, the code looked fine, and my tests passed. But as we got more users, the server's memory kept creeping toward its limit. The agent had keyed the cache by user, so every user got their own 13 MB copy of basically the same catalog and nothing was ever reused. I changed the key to the content instead, so everyone shares one copy of about 11 MB and it doesn't grow with every new user.

I used coding agents for most of the code I wrote there. I was the only iOS engineer on the team and the main person on the backend, and the agents are a big part of how I kept up on both sides. The cache did change how I review what they give me, though. The tests passed and it was still wrong, so now I also ask what the code will cost once real traffic hits it.
```
