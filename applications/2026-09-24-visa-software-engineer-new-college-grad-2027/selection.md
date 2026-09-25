# Selection — Visa, Software Engineer, New College Grad - 2027 (REF088543W)

## NewsBreak title

**Software Engineering Intern** (default). The posting title is "Software Engineer" and the duties are general SWE ("Build end-to-end technology solutions"), not backend-, full-stack-, or AI-specific. It does not say "SWE", so "SWE Intern" was not used.

## Header

Mountain View, CA. The job is in Foster City, CA (SF Bay).

## Items used

### NewsBreak
1. **nb-fastapi-backend + nb-ownership**: first commit, 89 endpoints, ~1,450 offline tests, ruff / pyright / pytest CI gate, 344 PRs (340 merged). Maps to "unit testing, code reviews", "REST APIs", "test frameworks", "version control".
2. **nb-dramabreak-stripe + nb-third-party-proxy**: Stripe web checkout, signature-verified webhook as the only trusted fulfillment path, idempotent fulfillment with stale-pending reclaim; nine integrations server-side, zero third-party API credentials in the iOS app. Maps to "secure" code and payments.
3. **nb-catalog-cache + nb-eks-standup**: 25–30 request fan-out → 1 call, shared cache 78× smaller than the per-user key, 512 MiB pod; production AWS EKS (Helm, Jenkins, Docker) on day 3. Maps to "optimized ... scalable code" and "cloud technologies (AWS)".
4. **nb-cronjob-outage + nb-llm-failure**: 5-day silent CronJob outage (ImagePullBackOff + Forbid concurrency), paired deadlines; 65% failure rate traced via Langfuse to an unbounded reasoning loop. Maps to "Diagnose and resolve software issues using root cause analysis".
5. **nb-llm-pipeline**: ingest → embed → LLM-score → dedupe → push, 4,100+ shadow decisions, prompt ablation, categorical gate, filler 34% → 4% by count. Maps to "Generative AI ... integration, prompt design".
6. **nb-agentic-search**: hybrid retrieval, SSE streaming, server-resolved citations, deterministic entity resolution 0% → 100% P@1 on real logged queries. Maps to "Generative AI tools and concepts (framework usage, integration)".

### Haddee
1. **hd-lead-mvp + hd-mentor-process**: 8-intern team, Agile sprints, React / Next.js / FastAPI / Supabase, 0→1 on GCP App Engine, user stories, PR reviews, mentoring on Git and testing. Maps to "cross-functional teams in an Agile environment", "React", "code reviews".
2. **hd-langchain-apis**: schemas and REST APIs for LangChain LLM features.

### ZenAI
1. **za-mock-interview + za-auth-db**: VC-backed, 0→1, sole engineer, React / Next.js / Supabase / PostgreSQL, auth, session state, DB. Maps to "end-to-end technology solutions".
2. **za-mock-interview + za-auth-db + za-demos-contracts**: worked with recruiters on scoring categories, iterated from user testing and client feedback, demos, contracts with mid-sized companies.

### Projects & leadership
- **pj-my-av** (default wording with the pipeline detail).
- **ld-ece-fellow**.

### Education
- CMU: Distributed Systems, Foundations of Software Engineering, Large Language Model Systems.
- UW–Madison: Algorithms, Operating Systems, Software Engineering, Large Language Models in Practice.

### Skills
Java, Python, JavaScript, and Go moved to the front of Languages; React first in Frameworks; MySQL first in Data & AI; AWS first in Cloud & DevOps; Unit Testing first in Testing & Practices. All are in skills.md.

## Skipped and why

- **nb-jira-process**: first draft included it; the page spilled to two pages, so it was the lowest-value cut.
- **CMU coursework "Software Refactoring"**: dropped because it alone wrapped onto a second line; the line went to nb-agentic-search.
- **cm-psc / cm-nl-safety**: the JD does not ask for research; a Research section does not fit.
- **nb-server-driven-ui, nb-swiftui-app, nb-app-store, nb-live-activities, nb-ads-max, nb-morning-digest, nb-manual-broadcast, nb-dramabreak-ads, nb-coaching-marketplace, nb-retired-detector**: iOS / ads specifics or less relevant to a general payments SWE role; cut for length.
- **pj-wisconsin-autonomous**: embedded work, not relevant.

## Constraints almost violated

- C++, C#, .NET, Angular, Vue.js, Selenium, and Power BI are JD keywords but are not in inventory; none added.
- "Unit tests": inventory says "tests" / "fully offline"; the bullet says "offline tests", and "Unit Testing" appears only in Skills, where it is listed in skills.md.
- "Stale-pending recovery" paraphrases the inventory fact "60s stale-pending reclaim".
- First draft said "authored 344 pull requests across five repositories"; shortened to "344 PRs (340 merged)" for fit. Both are inventory facts.

## Layout adjustment

After content fits were exhausted (one more line overflowed the page; one fewer left 12.9 pt), `\setlist*[itemize]{itemsep=0.7pt}` was added locally (shared default 0.5 pt). Margins and font size are unchanged.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax): **754.79 pt** from top.
- Unused height: 792 − 25.92 − 754.79 = **11.29 pt** (passes the 0–12 pt check).
- Rendered at 90 dpi and inspected the whole page: no clipping, overlap, cramped text, or empty bottom strip.

## Referral notes

`outreach.md`: role shortened to "SWE New Grad". Pitch is the default ("main backend engineer on a 6K-install sports app"), from nb-ownership (~83% of backend commits) and nb-swiftui-app (~6,000 installs). Final: CMU 279, UW 291.
