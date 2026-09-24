# Working with AI tools

Questions about coding with agents, reviewing AI output, and where AI tools fall short.

---

## Agent code that looked right but wasn't

- question: Tell us about a time an agent handed you code that looked right but wasn't. How did you catch it?
- company: not recorded
- date: 2026-09-23
- story: [agent-cache](../stories.md#agent-cache)

```text
At NewsBreak, I used an agent to build a catalog cache for the main content page in our sports app. The code was clean and I wrote tests for it. However, as the app grew and things shifted around, the pod's memory started climbing toward its 512 MiB limit. When I dug in, I found the agent had keyed the cache per user. Every user got their own 13.2 MB copy of a catalog that was almost identical for everyone, so the hit rate was structurally zero. Memory just grew with the number of users. The tests passed because they checked that the cache returned the right data, not whether it ever hit or how much memory it used.

I worked out how bad it could get. At the 10,000-entry cap, that's about 111 GB of cache on a 512 MiB pod. I re-keyed the cache on content (curator_id) so every user shares one 10.9 MB copy, 78× smaller. I also switched a deep copy to a shallow one, which cut home-load copy time from 9.0 ms to 0.89 ms.

What I took from it: passing tests only prove what they check. Now when I review agent code, I work out what it costs at real scale, not just whether it returns the right answer.
```

---

## What AI coding tools are still bad at

- question: What's one thing AI coding tools are still bad at, in your experience?
- company: not recorded
- date: 2026-09-23
- story: [push-to-start](../stories.md#push-to-start)

```text
My one grudge with AI coding tools is that they get overconfident with limited information, especially when debugging.

I've had it happen many times: I'm chasing a bug, the AI confidently says it found the cause, and one turn later it reads a log output and contradicts itself.

At NewsBreak, our iOS Live Activity push-to-start had never worked. The code looked correct and APNs returned HTTP 200 on every send, so nothing in our logs or tests showed a problem. With the AI confidently proposing one cause after another, I went down a rabbit hole of irrelevant leads.

The real cause was that iOS silently drops a start push with no aps.alert field, even though APNs has already accepted it. The status code said success, so every theory built on the logs was starting from the wrong place. I fixed it by making the sender raise an error when a start push is missing aps.alert, so it can't fail silently again.

Now when an AI tells me it has found the bug, I treat that as a hypothesis, not an answer. I ask what evidence would prove it wrong, and I check that before I change any code.
```
