# Selection - Commure Software Engineer, Scribe AI

Date: 2026-09-24

## Title and priorities

- NewsBreak title: **Full-Stack Engineer Intern**. The JD says "looking for innovative Full Stack Engineers" and asks for "development for both web and mobile, specifically iOS". NewsBreak was iOS + FastAPI from the first commit, so it fits full-stack better than iOS-only.
- Header: Mountain View, CA. The role is in the Mountain View office.
- What matters most in the JD: LLMs producing "accurate, structured clinical notes"; web + iOS UX; Python, TypeScript, React/Next.js, Node.js/Express, Swift; cloud infra and integrations; zero-to-one; working directly with customers and turning feedback into product.
- Not in inventory, so not claimed: React Native, Node.js (Express is listed and is used instead), audio processing, EHR/healthcare.
- Coursework: CMU LLM Systems, Distributed Systems, Foundations of SE; UW Mobile Computing Laboratory, LLMs in Practice, Software Engineering.
- Skills: Python/TypeScript/JavaScript/Swift lead Languages; React/Next.js/Express/SwiftUI lead Frameworks; LLM tooling leads the Data & AI row. All are from inventory/skills.md.

## Selected items and facts

### NewsBreak
1. **nb-ownership + nb-swiftui-app + nb-fastapi-backend**: sole SwiftUI engineer, primary backend author, ~6,000 installs, 1,119 peak DAU; backend from first commit to 89 FastAPI/MongoDB endpoints, ~1,450 tests.
2. **nb-app-store + nb-swiftui-app + nb-live-activities + nb-server-driven-ui**: shipped through three App Store rejections; Firebase auth; Live Activities; server-driven UI over 27 widget types, with no App Store release needed for new surfaces. Maps to polished iOS UX.
3. **nb-llm-pipeline**: per-article categorical label + 0–100 importance (structured LLM output), LLM same-story judge, 4,100+ shadow decisions, filler 34% → 4%. Maps to "accurate, structured" LLM output.
4. **nb-agentic-search**: hybrid retrieval, SSE streaming, server-resolved citations (the model cannot author a URL), 0% → 100% P@1. Maps to LLM accuracy and grounding.
5. **nb-eks-standup + nb-cronjob-outage**: production EKS on day 3 (Helm, Jenkins); 5-day silent CronJob outage fixed with paired deadlines. Maps to cloud infrastructure and "calm under pressure".
6. **nb-morning-digest + nb-third-party-proxy**: LLM digest to 5,026 users (~81%); nine integrations moved server-side, so the binary ships zero third-party credentials. Maps to integrations.

### Haddee
1. **hd-lead-mvp + hd-mentor-process**: 8 interns, React/Next.js/FastAPI/Supabase 0→1 on GCP App Engine, user stories, PR reviews, mentoring.
2. **hd-langchain-apis** (llm): schemas and REST APIs for LangChain resume parsing, suggestions, and job matching.

### ZenAI
1. **za-mock-interview + za-auth-db**: VC-backed, 0→1, sole engineer, React/Next.js/Supabase/PostgreSQL, auth/session/DB.
2. **za-mock-interview + za-demos-contracts**: iterated AI scoring and UI with recruiters and clients; demos; contracts with mid-sized companies. Maps to "work directly with customers". No claim about the company's lasting direction.

### Research / projects
- **cm-nl-safety**: multi-turn LLMs mapping natural language to formal specs, the closest research match to LLM → structured output.
- **pj-my-av** (default wording): fills the page and shows ML with streaming inference.

## Skipped and why

- **cm-psc**: control-theory research, not relevant here; cut for length.
- **ld-ece-fellow**, **pj-wisconsin-autonomous**: cut for length; my-av was the better fill.
- **nb-catalog-cache**, **nb-llm-failure**, **nb-retired-detector**: strong, but backend/LLM depth is already covered; cut for length.
- **nb-ads-max**, **nb-dramabreak-***, **nb-manual-broadcast**, **nb-coaching-marketplace**, **nb-jira-process**: less relevant to scribe/clinical work; cut for length.

## Constraints almost violated

- React Native and Node.js are JD keywords but are not in inventory. Neither was added; Express covers the Node side.
- "three App Store rejections" is the three FIFA/World Cup trademark rejections in nb-app-store. The ATT and ASO rejections are separate and are not counted.
- The first draft spilled about 180 pt onto page 2. I tightened bullets and dropped the PSC research bullet, ECE fellow, and Tailwind. That left 81 pt empty, so I added the EKS/CronJob bullet and my-av to fill it.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax): **759.49 pt** from top.
- Unused height: 792 − 25.92 − 759.49 = **6.59 pt** (passes the 0–12 pt check).
- Rendered at 110 dpi and inspected the whole page: no clipping, overlap, cramped text, or empty bottom strip.
