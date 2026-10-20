# Working with non-technical domain experts

"Tell us about working with operations / legal / support / product. How did you turn their knowledge into reliable system behavior?" Lead with NewsBreak legal (`nb-cross-dept`: FIFA trademark launch, live chat stripped without monitoring tools), then how decisions were enforced in code (flagged coaching marketplace, alert rules + decision log). ZenAI recruiters (`za-mock-interview`) is the backup story. What legal specifically advised is not recorded; do not invent it.

---

## Figure — Associate AI Engineer

- question: Tell us about your experience working with non-technical domain experts (e.g., operations, legal, customer support, or product managers). How did you translate their domain knowledge into reliable system behavior without depending on them for day-to-day execution?
- company: Figure (Associate AI Engineer)
- date: 2026-10-09
- story: `nb-cross-dept`, `nb-app-store`, `nb-coaching-marketplace`, `nb-llm-pipeline`

```text
At NewsBreak, we moved fast in a startup-style environment. My title was Engineering Intern, but I was the primary engineer on the SportsBreak app's backend and iOS client, and I worked with several departments, especially legal when the app needed best-practice guidance.

The clearest case was our World Cup launch. Apple rejected the app three times over FIFA and World Cup trademarks. Legal guided us through it, and we cut the hero World Cup feature so the app could launch at all. It went live on June 17. Another time, we stripped live chat out of the app because we didn't have the monitoring tools for it yet, rather than ship something nobody could watch. In both cases the right answer was a product change, not more code.

To make decisions like these hold, I put them into the system itself. When our coaching marketplace had to be disabled for App Store submission, I kept it behind a flag and verified that no deep link or notification could open it. For breaking-news alerts, where "is this worth a push?" is a judgment call, I turned the judgment into rules the system enforces: a happened / speculative / no-event gate, a per-topic bar, a cap of 2 alerts a day and 1 per topic, and quiet hours. Every item writes a log row saying why it fired or didn't, and the daily cap held across 11,745 user-days with zero violations.

The pattern I follow: experts decide what "correct" means, and the system enforces it with code, tests, and logs, so they don't have to watch it day to day.
```
