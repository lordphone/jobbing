# Project deep dive

Questions that ask for one project or feature end to end: what it does, why, a challenge or tradeoff, and how it was built.

---

## Full-stack feature, challenge, and AI use

- question: Describe one full-stack application or feature you built (internship or personal project). What does it do, and why did you build it? What was one technical challenge or tradeoff you worked through? How did you use AI while building it and how did it help? Add a link (repo, paper, or demo) if you have one.
- company: Quora (Full Stack Software Engineer, New Grad)
- date: 2026-10-20
- story: [agent-cache](../stories.md#agent-cache); inventory `nb-catalog-cache`, `nb-server-driven-ui`, `nb-ownership`

```text
I built the World tab for SportsBreak (along with most of the rest of the app), a sports news app I worked on during my internship at NewsBreak (https://apps.apple.com/app/id6762649287). It's the app's landing page, giving users direct access to the sports news relevant to them.

When I started on the project, the mostly frontend iOS app was making 25 to 30 separate requests just to load that one page, and every layout change needed another App Store review. I moved the work to the backend with a backend-for-frontend design, so the app now makes one call to a single FastAPI endpoint to render the page. The response also describes the layout, so we could add new sections without shipping an app update.

A challenge I ran into was caching. As our user base grew, the Kubernetes pod's memory kept creeping toward its limit. It turned out the original cache was keyed by user, so every user had their own 13 MB copy of basically the same catalog and nothing was ever reused. I re-keyed it on the content instead, so everyone shares one copy of about 11 MB and memory no longer grows with every new user.

That cache was written by an AI agent. The code looked clean and my tests passed, which is why it got through. I used coding agents for most of what I wrote at NewsBreak, and they're how I kept up as the only iOS engineer and the main backend author. But the cache changed how I review their output. Now I also ask what the code will cost once real traffic hits it, not just whether it works.
```
