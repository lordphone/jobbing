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

---

## Most complex project

- question: Please describe your most complex project.
- company: Formlabs (Software Engineer, API & Automation)
- date: 2026-10-23
- story: [retired-detector](../stories.md#retired-detector); inventory `nb-llm-pipeline`, `nb-retired-detector`

```text
My most complex project was the personalized breaking-news alert system I designed and shipped for SportsBreak during my internship at NewsBreak. The goal was to send a push notification within minutes when something actually happened to a team a user follows, without spamming them with filler.

My first version ranked stories by how many publishers covered them. I ran it in shadow on production traffic for 19 hours and found it was about 15 hours too slow, because by the time several outlets cover a story, it's old news. So I deleted it and rebuilt the system as a Kubernetes CronJob that ingests articles, embeds them, scores each one with an LLM, selects, removes duplicates, and sends push notifications, all in about two minutes. Each score is compared against that topic's own 7-day score history instead of one global threshold, so a quiet topic can't promote its least-bad story. An embedding check plus a final LLM judge keeps a user from getting two alerts about the same event, and hard caps of 2 alerts a day and 1 per topic sit on top.

The hardest part was trusting it before it reached real phones. I ran it in shadow for 11 days and logged a row for every decision explaining why it fired or didn't, over 4,100 rows in all. Hand-grading those showed the model gave filler and real events almost the same score (89 vs 90), so I added a separate check for whether anything had actually happened. That cut filler from 34% to 4% of alerts. I also turned down a rule that caught 91% of filler, because it would have blocked the day's two biggest real alerts. The system is live now, sending a median of 1.8 alerts a day, and the 2-a-day cap held across 11,745 user-days with no violations.
```
