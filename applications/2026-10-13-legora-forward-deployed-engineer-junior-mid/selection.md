# Selection — Legora, Junior/Mid-level Forward Deployed Engineer

## NewsBreak title

**Software Engineering Intern** (default) — JD asks for "strong software engineering fundamentals" and integrations plus core-product work; it is not framed as backend-only, full-stack, or AI-product. Heading is plain "NewsBreak" (not a new-venture JD).

Header city: New York, NY (posting is NYC on-site 5 days/week, no Bay option).

## Items used

- **nb-ownership + nb-swiftui-app** → bullet 1: sole SwiftUI engineer, primary backend author, SportsBreak link, 1.4K ratings, peak DAU 1,119, Firebase auth, 344 PRs / 340 merged — "taking a feature through delivery", "authentication".
- **nb-fastapi-backend + nb-eks-standup + nb-observability** → bullet 2: 89 endpoints, ~1,450 offline tests, EKS on day 3, Prometheus / Grafana — "write, test, and debug reliable code", "production delivery".
- **nb-third-party-proxy + nb-dramabreak-stripe** → bullet 3: nine third-party integrations moved server-side, zero credentials in the binary; Stripe checkout with signature-verified, idempotent webhooks — "APIs, authentication, integrations, and data flows across systems".
- **nb-agentic-search** → bullet 4: RAG, bounded tool loop, server-resolved citations, 0% → 100% P@1 — Legora is an AI product; "AI tools".
- **nb-cronjob-outage + nb-llm-failure** → bullet 5: "Debug issues across Legora and customer systems, using logs, tests, and systematic investigation"; another team's system ≈ working in an existing codebase.
- **nb-jira-process + nb-cross-dept** → bullet 6: 34 API specs, ~10,000 lines of docs, Jira backlog, onboarding, legal — "explain technical decisions clearly", "keep teammates informed", nontechnical stakeholders (legal; on-theme for a legal-tech company). Legal wording kept generic per inventory ("what legal advised … not recorded").
- **hd-lead-mvp + hd-langchain-apis + hd-mentor-process** → Haddee 3 lines (React / Next.js stack; scoping user stories ≈ "translate customer needs into engineering tasks").
- **za-mock-interview + za-auth-db + za-demos-contracts** → ZenAI: sole engineer 0→1, auth / DB; demos, client and recruiter iteration, three 200–500-person companies signed — "working directly with customers", "B2B", "bring customer feedback into product".
- **cm-nl-safety** → one research bullet (natural language → formal specs with LLMs; fill).
- **pj-codingplans** → project (practical AI-tool evaluation; "practical experience using AI tools").
- **ld-ece-fellow** → leadership line; outreach and events fit a customer-facing role.
- Skills: TypeScript and JavaScript first (JD: "We use it extensively"); APIs row with REST APIs, Firebase Auth / Sign in with Apple, Stripe (auth + integrations); Data & AI row with Claude Code / AI coding tools; Cloud; certifications kept.
- Coursework: CMU — Distributed Systems, LLM Systems, Foundations of Software Engineering; UW — Software Engineering, Algorithms, LLMs in Practice.

## Skipped

- nb-llm-pipeline: strong item, but the JD is integrations / customer delivery; the 6th slot went to communication (nb-jira-process).
- nb-catalog-cache, nb-retired-detector: performance / AI depth, less JD-relevant.
- nb-server-driven-ui, nb-app-store, nb-live-activities, nb-manual-broadcast, nb-ads-max, nb-dramabreak-ads, nb-coaching-marketplace: mobile-specific.
- cm-psc: control-theory research, irrelevant; no room.
- pj-my-av, pj-wisconsin-autonomous, pj-cs537-os: less relevant than codingplans.

## Constraints almost violated

- TypeScript is in skills.md, but no inventory bullet shows TypeScript work explicitly (React / Next.js work implies JS/TS but is not stated); listed only in Skills.
- JD asks 2–3+ years; he has internships plus ZenAI / Haddee. Not stretched on the page.
- ZenAI company line printed as "F23" per inventory (the C3 template still said "2023 Fall Batch").
- First compile spilled ~4 lines; shortened bullet 1, Haddee line 1, codingplans, and ZenAI, then added the Haddee mentoring line, rebalanced Skills into one-line rows, and restored the ZenAI recruiter fact to fill.

## Page-fill verification (final PDF)

- Pages: 1
- Bottom margin: 0.36 in = 25.92 pt (from shared/preamble.tex)
- Last content line bottom (pdftotext -bbox yMax): 758.94 pt of 792 pt
- Unused height: 792 − 25.92 − 758.94 = 7.14 pt (within 0–12 pt)
- Visual review at 90 dpi: no empty bottom strip, clipping, overlap, or cramped text.
