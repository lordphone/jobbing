# Selection — Mixpanel Software Engineer, Growth (8157627)

## NewsBreak title
**Full-Stack Engineer Intern** — JD: "You'll work across the full stack, from frontend UI changes to backend data pipelines" and "2 years of full-stack software engineering experience". Heading is plain "NewsBreak" (growth pod on an existing product, not a new-venture team).

Header city: Mountain View, CA (San Francisco hybrid).

## Used
- **nb-ownership / nb-swiftui-app** (`believable`): primary iOS + sole backend author, ~6,000 installs, 1,119 peak DAU — growth outcome numbers up front.
- **nb-swiftui-app**: 72-event Amplitude catalog, typed emit methods, server-side allowlist (JD: "instrument tracking"); Firebase guest-first anonymous sessions upgraded via `link()` to Google / Apple / email (activation / onboarding friction).
- **nb-dramabreak-ads**: A/B test on DramaBreak menu options, CTR read in Amplitude (JD: "growth experimentation"). Winner, lift, sample size not recorded, so not claimed.
- **nb-morning-digest**: 5,026 users (~81% of base).
- **nb-server-driven-ui + nb-catalog-cache**: 27 widget types, new surface without App Store release (iteration speed); 25–30 → 1 call; per-user-keyed cache that never hit, fixed by sharing one copy near the pod memory limit (debugging).
- **nb-fastapi-backend** (`believable`) + **nb-observability**: 89 endpoints, EKS, ~1,450 offline tests in CI; Prometheus / Grafana (on-call, dashboards).
- **nb-llm-pipeline** (`believable`): 11-day production shadow, per-item decision log, filler 34% → 4% (data-driven mindset).
- **nb-llm-failure** (`infra`, shortened): 65% failure rate root-caused via Langfuse (debugging).
- **hd-lead-mvp + hd-langchain-apis**; **hd-mentor-process**: React / Next.js full stack, PR reviews.
- **za-mock-interview + za-auth-db + za-demos-contracts**: React / Next.js / PostgreSQL 0→1, iterated from user testing and client feedback, three 200–500-person companies signed.
- **pj-codingplans**: data-driven testing of LLM providers; AI interest.
- **ld-ece-fellow**: marketing and outreach (growth-adjacent).
- Skills: TypeScript / React first (bonus points), Amplitude + AI coding tools + MCP (JD mentions MCP-connection experiment). Both AWS certifications kept.
- Coursework: Data Science for Software Engineering, Foundations of SE, Machine Learning; Software Engineering, Algorithms, Mobile Computing Laboratory.

## Skipped
- nb-retired-detector, nb-eks-standup, nb-cronjob-outage, nb-third-party-proxy, nb-ads-max, nb-live-activities, nb-app-store, nb-manual-broadcast, nb-dramabreak-stripe, nb-jira-process, nb-coaching-marketplace, nb-cross-dept: NewsBreak capped at 6 bullets; these are less tied to experimentation / activation.
- nb-agentic-search: strong, but the alert pipeline better shows measurement before launch; good interview story for "agentic onboarding".
- cm-psc, cm-nl-safety: research not relevant to growth.
- pj-my-av, pj-wisconsin-autonomous, pj-cs537-os: not relevant; page already full.
- Django, Mixpanel, Optimizely, LaunchDarkly, Statsig: not in inventory, not claimed.

## Page fill
- Pages: 1
- Bottom margin: 0.36in = 25.92 pt → content limit y = 766.08 pt
- Last content yMax: 761.96 pt
- Unused height: 4.1 pt
- Visual check: no empty strip, no clipping or overlap. First fill left 30.9 pt; filled by adding the cache fix (bullet 4) and the Langfuse root cause (bullet 6).
