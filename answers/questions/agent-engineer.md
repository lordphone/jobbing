# What makes a great engineer for this role

"What qualities make someone great at X, and why are you the best candidate?" Name 3–4 qualities from the JD and back each with one inventory fact.

---

## Sierra — Agent Engineer

- question: What qualities do you believe make someone a great Agent Engineer, and how do your skills and experiences make you the best candidate for this role?
- company: Sierra (Software Engineer, Agent (New Grad 2027))
- date: 2026-09-30
- story: `nb-llm-pipeline`, `nb-agentic-search`, `nb-llm-failure`, `nb-fastapi-backend`, `za-demos-contracts`

```text
I think a great Agent Engineer does four things well.

First, they measure the agent on real traffic, not on demos. At NewsBreak, I hand-graded our LLM news alerts and found the model gave filler and real events nearly the same score, around 90. Prompt tweaks alone weren't going to fix that, so I added a categorical gate, calibrated it in production shadow on 4,100+ decisions, and shipped it live. Filler dropped from 34% to 4%.

Second, they don't trust the model's confidence. When I built our LLM search agent, I designed it so the model only emits a citation index and the server resolves the URL, so it can't invent a source. I also built an eval harness on real logged queries that took entity resolution from 0% to 100% P@1.

Third, they own the whole system. I built the backend behind the app from its first commit to 89 endpoints on AWS EKS. When another team's LLM pipeline was failing 65% of the time, I traced it in Langfuse to an unbounded reasoning loop and sized a token cap that cut none of the successful runs.

Fourth, they work directly with customers. At ZenAI I was the sole engineer on an LLM mock-interview app. I worked with recruiters so its scoring matched real hiring, demoed it to clients, iterated on their feedback, and won contracts with mid-sized companies.

That mix of production LLM work, end-to-end ownership, and customer-facing iteration is what this role asks for, and it's what I've been doing.
```
