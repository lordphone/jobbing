# Coverage

Common behavioral question types and the inventory stories that fit. **Bold** = written up in `stories.md`. Plain = candidate from inventory, not written up yet.

| Type | Common wording | Stories |
|---|---|---|
| Working with AI tools | "An agent gave you code that was wrong", "What are AI tools bad at" | **agent-cache**, **push-to-start**; `pj-badminton-courts` (personal tool built with AI; day-to-day use, `questions/ai-tools.md`) |
| Hardest bug | "Toughest bug you've debugged" | **push-to-start**; `nb-cronjob-outage` (5-day silent CronJob outage); `nb-llm-failure` (65% failure rate, another team's pipeline); `nb-ads-max` (dead-stripped ad adapters); `nb-eks-standup` (DNS → TLS → admission-policy chain) |
| Failure / mistake | "A time you were wrong", "A decision you reversed" | **retired-detector** (deleted own detector after 19 h of data, net −882 lines); `nb-third-party-proxy` (ESPN proxy rolled back in 2.5 h); **agent-cache** |
| Data-driven decision / tradeoff | "A decision you made with data", "A tradeoff you made" | `nb-llm-pipeline` (hand-graded alerts, added a gate; rejected a rule that killed the top real alerts); `nb-agentic-search` (rejected embeddings for entity resolution with measurements); `nb-retired-detector` |
| Ownership / initiative | "Went beyond your role", "Took ownership" | `nb-ownership` (sole engineer between hires); `nb-jira-process` (built the backlog unprompted; reopened closed security tickets with evidence); `nb-eks-standup` (found the stale ArgoCD app) |
| Deadline / scope cut | "Shipped under pressure", "Had to cut scope" | `nb-app-store` (three trademark rejections, cut the hero World Cup feature) |
| Ambiguity / 0→1 | "Built something from scratch", "Unclear requirements" | `nb-fastapi-backend` (first commit → 89 endpoints); `za-mock-interview` (sole engineer, 0→1); `hd-lead-mvp` |
| Leadership / mentoring | "Led a team", "Helped someone grow" | `hd-lead-mvp` + `hd-mentor-process` (8-intern team, PR reviews); `nb-jira-process` (onboarded Khalil) |
| Helping another team | "Worked across teams" | `nb-llm-failure`; `nb-dramabreak-ads` (unblocked SPM for the team) |
| User impact | "Something you're proud of", "Impact on users" | `nb-manual-broadcast` (alerts beat FOX by a minute); `nb-morning-digest` (5,026 users, ~81%); `nb-llm-pipeline` |
| Customers / stakeholders | "Worked with a customer" | `za-demos-contracts` (demos, contracts, client iteration; recruiters shaped scoring) |
| Conflict / disagreement | "Disagreed with a teammate or manager" | none in inventory — GAP |
| Relevant skills | "3 relevant skills", "Top skills for this role" | `questions/relevant-skills.md` — pick from `inventory/skills.md` by JD; back each with `nb-fastapi-backend`, `hd-lead-mvp` / `za-mock-interview`, `nb-agentic-search` / `nb-llm-pipeline` |
| Qualities for the role | "What makes someone great at X, and why you?" | `questions/agent-engineer.md`; `nb-llm-pipeline` (measured on real traffic), `nb-agentic-search` (citations the model can't author, evals), `nb-llm-failure` + `nb-fastapi-backend` (ownership), `za-demos-contracts` (customers) |
| Why this company | "Why do you want to work at X?" | `questions/why-company.md`; `nb-morning-digest` (AI that saves users time) + what the JD says the company builds; personal product use if inventory has it (Perplexity) |
| Tell me about yourself | — | not written — GAP |
| Story that represents you / passion | "Share a story that reflects who you are", "A passion of yours" | `questions/about-you.md`; **retired-detector**; `pj-codingplans` (LLM plan-testing website) |
