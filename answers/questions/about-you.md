# A story that represents you

Open-ended "share a story that reflects who you are" prompts (challenge, passion, achievement).

---

## Story that reflects who you are (150–300 words)

- question: In 150–300 words, share a story or experience that reflects who you are as a candidate. Possible topics: a challenge you've faced, a passion of yours, an achievement you're proud of. Pick one of these or another that best represents you.
- company: not recorded
- date: 2026-09-30
- story: [retired-detector](../stories.md#retired-detector)
- words: 258

```text
At NewsBreak, I was building breaking-news push alerts for our sports app. My first detector used corroboration: if several publishers covered a story, it was probably big. It sounded reasonable, so I wrote it, along with a 1,003-line calibration harness and tests, and ran it in production shadow mode before it could send anything.

Nineteen hours of data told a different story. Our pipeline picked up an article in 1.8 minutes, but by the time enough publishers had piled on, the median story was 901 minutes old. Twenty of the 26 alerts it would have sent were more than six hours stale. The most-corroborated item, covered by five publishers, was UFC card filler.

No threshold could fix that. Corroboration only exists after the news is old, so the design itself was too slow. Two days after writing it, I deleted the detector, the harness, and the tests, net −882 lines. I kept corroboration as offline ground truth: useless when a story breaks, useful fifteen hours later for grading.

I rebuilt it to judge each article on arrival. An LLM scores it, and it fires only above a percentile of that topic's rolling 7-day score distribution. After 11 days of shadow review, it went live and cut filler alerts from 34% to 4%.

What this says about me: I get attached to problems, not to my own code. I like putting an idea in front of real data early, and when the numbers say I'm wrong, I'd rather find out in nineteen hours than defend it for a month.
```

---

## A passion of yours (codingplans)

- question: In 150–300 words, share a story or experience that reflects who you are as a candidate. Possible topics: a challenge you've faced, a passion of yours, an achievement you're proud of. Pick one of these or another that best represents you.
- company: not recorded
- date: 2026-09-30
- story: `pj-codingplans` (inventory/projects.md)
- written by Lordphone; minor fixes only
- note: "yesterday" (OpenAI $500 plan) is relative to 2026-09-30; update if reused

```text
I'm super passionate about large language models and how they could improve the flow of information for everyone in this space.

As models evolve, so do the payment plans for them. Now every company that makes and provides models has its own plan to serve tokens, but some of them use drastic and unethical cost-saving measures. I've been building a website to inform the public about which token plans are trustworthy and worth the money. I spent my own money to buy some of these coding/token plans from companies like Z.AI, MiniMax, and Kimi, and tested them with task-specific tests like KV cache, long context, and needle-in-a-haystack. I have results showing which companies nerfed caching or heavily quantized their models, basically using cost-saving measures against users' best interests.

As AI plans get more expensive by the day (OpenAI dropped a $500 plan yesterday), I think someone has to keep them in check, so that we understand the token cost without subsidization and people don't get skunked on what they paid for.
```
