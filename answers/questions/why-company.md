# Why this company

"Why do you want to work at X?" Ground it in one real piece of his work plus what the JD says the company builds. Do not claim he uses the product unless inventory says so.

---

## Notion

- question: Why do you want to work at Notion?
- company: Notion (Software Engineer, Early Career)
- date: 2026-09-30
- story: `nb-morning-digest` (inventory/newsbreak.md)

```text
At my internship I built an LLM morning digest that about 81% of our users ended up viewing, and it taught me I like AI features most when they quietly save people time instead of showing off. Notion is putting AI right next to the work people already do there, and I want to be on the team figuring out what actually helps.
```

---

## Sierra

- question: Why are you excited to join us at Sierra?
- company: Sierra (Software Engineer, Agent (New Grad 2027))
- date: 2026-09-30
- story: `nb-agentic-search`, `nb-llm-pipeline` (inventory/newsbreak.md); `za-demos-contracts` (inventory/zenai.md)

```text
This summer I shipped an LLM search agent and a personalized news-alert pipeline to real users, and the part I enjoyed most wasn't getting the model to answer. It was everything after: building evals on real logged queries, making citations the model can't make up, and running the alert pipeline in production shadow for 11 days before it sent a single push. That loop of build, measure, tune, and ship again is what Sierra calls the Agent Development Life Cycle, and I want to do it full-time.

Sierra's agents also talk to the customers of companies like SoFi and Sutter Health, where a confident wrong answer costs real trust. That raises the bar on reliability in a way I find exciting. And I like that Agent Engineers work directly with customers. At ZenAI I demoed our product to clients and iterated on their feedback until we won contracts, and I'd love to pair that with production agent work.
```

---

## Perplexity

- question: What are the most interesting aspects of Perplexity that you're excited to work on?
- company: Perplexity (Member of Technical Staff (New Grad) - CMU 2026-2027)
- date: 2026-10-01
- story: profile.md personal (uses Perplexity instead of Googling)

```text
Perplexity changed a habit that is very hard to break for me: Googling. I think that is a very hard feat, and I'd love to improve the experience that made my life better. I think the pipeline's latency is the number one thing to optimize in this age of short attention spans, and that's what I would love to work on the most.
```

---

## LinkedIn

- question: Include a message with your application (short pitch: why this job is a top choice and why I'm a good fit)
- company: LinkedIn (AI Engineer)
- date: 2026-10-02
- story: `nb-llm-pipeline`, `nb-agentic-search`, `nb-llm-failure`, `nb-dramabreak-ads` (A/B test) (inventory/newsbreak.md)

```text
This summer I built a couple of LLM-backed systems that I'm really proud of, from the first design and hand-grading outputs to putting them in production. That's the part of the job I enjoyed the most, and I'd love to do it at LinkedIn's scale.
```

---

## Harvey

- question: Why are you interested in working at Harvey?
- company: Harvey (Software Engineer, New Grad (2027))
- date: 2026-10-05
- story: `nb-agentic-search` (server-resolved citations) (inventory/newsbreak.md)

```text
This summer I built an LLM search feature, and the part I cared about most was making sure every answer pointed to a real source. I think that matters even more in legal work, where a wrong citation can actually hurt someone. That's the kind of problem I'd love to work on, and Harvey is working on it every day.
```

---

## Fireworks AI

- question: Why are you interested in Fireworks AI?
- company: Fireworks AI (Member of Technical Staff, New Grad (BS/MS))
- date: 2026-10-05
- story: `pj-codingplans` (inventory/projects.md); `nb-llm-pipeline`, `nb-agentic-search` (DeepSeek over DeepInfra) (inventory/newsbreak.md)

```text
On the side, I've been buying LLM coding plans out of pocket from Z.AI, MiniMax, and Kimi and testing them on KV caching, long context, and needle-in-a-haystack to see which providers quietly nerfed caching or heavily quantized their models to save money. That taught me how much of a model's real quality comes down to how it's served, not just the weights. Fireworks' whole job is serving open models fast and well at scale, and that's the problem I want to work on. This summer I also shipped production LLM features on DeepSeek through an inference API, so I've felt the latency and reliability side as a customer too.
```

---

## EvenUp

- question: In your own words, what is the core product that EvenUp builds, and how do you see Machine Learning playing a role in it?
- company: EvenUp (Machine Learning Engineer)
- date: 2026-10-22
- story: `nb-agentic-search` (server-resolved citations, eval on logged queries), `nb-llm-pipeline` (hand-graded outputs, shadow mode) (inventory/newsbreak.md)

```text
EvenUp builds AI for personal injury law firms. A firm sends over a case, which is mostly a pile of medical records, bills, and accident details, and EvenUp's platform, Piai, turns it into the work a firm needs to win a fair settlement: what happened, what the injuries and treatments were, what they cost, and what the claim is worth. The goal is that an injured person gets a faster and fairer outcome, whether or not their firm can afford a big team to go through every page.

ML sits at almost every step. Document understanding has to read messy, scanned, inconsistent medical records and pull out the facts that matter. NLP and LLMs turn those facts into a clear case narrative. Retrieval keeps every claim tied to the exact page it came from, because in legal work a confident wrong sentence can hurt the client. And models trained on past outcomes can help estimate what a case should settle for.

The part I find most interesting is the evaluation. This summer I built an LLM search feature where the model can only cite sources by index and the server attaches the real link, so it can't make one up, and I measured it on real logged queries instead of a fixture. I also hand-graded outputs for an alert pipeline and ran it in shadow on production traffic before it sent anything. I'd want to work the same way at EvenUp, with legal experts defining what "correct" means and the models measured against it.
```
