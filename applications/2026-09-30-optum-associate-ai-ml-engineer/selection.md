# Selection — Optum Associate AI/ML Engineer (2390968)

## NewsBreak title
**AI Engineer Intern** — JD is GenAI / LLM applications / agentic frameworks / RAG as product work ("develop scalable GenAI models, Large Language Model (LLM) applications, agentic frameworks"). Considered AI Infrastructure Intern for "Python inference APIs deployed on Kubernetes", but the JD is mostly model/application work, not serving infra.

## Items used
- **nb-agentic-search** (grounded + design): SSE search API, deterministic RAG turn 1, bounded tool agent (≤3 hops, 5 tools), hybrid retrieval (full-text + bge vector, RRF), server-resolved citations. Hits RAG, embeddings, vector search, agentic frameworks.
- **nb-llm-pipeline** (shadow): Kubernetes CronJob, ingest → embed → LLM-score → LLM dedupe → push, 4,100+ shadow decisions, hand-graded alerts, filler 34% → 4%. Hits model evaluation, LLMs on Kubernetes.
- **nb-agentic-search** (entities): 0% → 100% P@1, entity resolver as query rewriter, rejected embeddings with measurements, eval harness on real catalog. Hits model evaluation.
- **nb-fastapi-backend** + **nb-eks-standup** (fused): FastAPI / MongoDB from first commit, 89 REST endpoints on EKS (Docker via the image, Helm), ~1,450 offline tests, ruff / pyright / pytest gate. Hits Python REST APIs on Kubernetes, containerization.
- **nb-llm-failure** (backend): 65% failure rate, Langfuse traces, 16,384 ceiling, 2,048 cap vs p95 1,197. Hits performance monitoring / root-cause investigations.
- **hd-lead-mvp** + **hd-langchain-apis** (fused into one bullet).
- **za-mock-interview** (with-auth) + **za-demos-contracts** / recruiter-scoring fact.
- **cm-nl-safety** + **cm-psc** (fused, one bullet): multi-turn LLMs, ML research.
- **pj-my-av**, **ld-ece-fellow**.
- Skills: AI & ML row second (RAG, bge embeddings, hybrid retrieval, ...); Cloud & Infra (Kubernetes, Docker) third. Python and SQL lead Languages.
- Coursework: CMU — Machine Learning, LLM Systems, Data Science for SE; UW — LLMs in Practice, Algorithms, Operating Systems.

## Skipped
- nb-swiftui-app, nb-live-activities, nb-ads-max, nb-app-store, nb-server-driven-ui, nb-dramabreak-*: mobile/ads, not in JD.
- nb-catalog-cache, nb-cronjob-outage, nb-third-party-proxy: backend/infra detail; lower value than the LLM items for this JD; space.
- nb-ownership / nb-jira-process: space.
- hd-mentor-process: folded partly into lead bullet originally, cut for space.
- pj-wisconsin-autonomous: embedded, not relevant.
- Second research bullet (Bayesian estimators / PSC detail): cut for space after first compile spilled.

## Constraints almost violated
- Pandas, Scikit-learn, Databricks, vision/speech, MCP, A2A are in the JD but not in `inventory/skills.md` — not added.
- First compile spilled to 2 pages; fused Haddee into one bullet, research into one bullet, dropped CUDA from skills. Then fixed two orphan-word lines (CMU coursework, FastAPI bullet) and re-added the ZenAI recruiter/contracts bullet to fill.

## Verification (final PDF)
- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax): **758.20 pt** from top.
- Unused height: 792 − 25.92 − 758.20 = **7.88 pt** (passes 0–12 pt).
- Rendered at 90 dpi and inspected the whole page: no clipping, overlap, cramped text, orphan lines, or empty bottom strip.

## Referral notes
Default pitch. Role kept full ("Associate AI/ML Engineer") since all notes fit. Why-this-team line from the JD's "LLM applications ... Python inference APIs deployed on Kubernetes".
