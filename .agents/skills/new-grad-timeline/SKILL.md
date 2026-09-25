---
name: new-grad-timeline
description: >-
  Researches one company's 2027 new-grad software / backend / full-stack / ML / AI engineer
  hiring in the US: is the role open now, when it opened, when it opened last cycle, and
  whether it needs citizenship / green card / clearance or won't sponsor. Finds the posting on
  the company's own job board and records where the job list lives. Use for any company in
  timeline/COMPANY_LIST.md, when refreshing timeline/status.csv, or when he asks "is X hiring
  new grads yet".
---

# New-grad timeline research

The answer must come from the company's **own job board** (first party). Community trackers are leads and history, never proof that something is open.

Two uses:

- **One company** ("is X hiring new grads yet"): follow the Procedure below yourself and write its research file. Then run `merge.py`.
- **Many companies:** follow "Full pipeline". It runs one Sonnet agent per company through the saved workflow.

Files:

- `timeline/COMPANY_LIST.md`: the companies, in 11 tiers.
- `timeline/sources.csv`: where each company's job list lives (`jobs.py spec` and `Jobs page`). Start here.
- `timeline/status.csv`, `timeline/SUMMARY.md`, `timeline/sources.csv`: built by `scripts/merge.py`. Don't edit them by hand.
- `timeline/research/<company-slug>.json`: one first-party result file per company. The research step writes these, and they beat every other source.
- `timeline/data/`: intermediate files. It holds `trackers.json`, `boards.json`, `worklist.json`, `workflow_args.json` and `merged.json`, plus `first_pass_agents/*.jsonl`, the 2026-09-24 first-pass results kept as a lower-priority source.
- `applications/TRACKER.md`: companies he already applied to.
- `.claude/workflows/new-grad-research.js`: the saved workflow, one Sonnet agent per company.
- `scripts/jobs.py` (in this skill folder): the tool for every step below. Run it with no arguments for usage.

## What counts

- **Role:** software, SDE, backend, full-stack, front-end, platform, ML, AI or forward-deployed engineer. Also named programs whose track is software engineering (e.g. Technology Development Program, Engineering Analyst, AMTS, "Software Engineer I" or "Associate Software Engineer" when the posting asks for 0–1 years).
- **Not counted:** internships, co-ops, and roles asking for 1+ years of experience. Also returning-intern-only roles, and hardware / electrical / firmware / test / sales-engineer roles.
- **Location:** the US, including US-remote.
- **This cycle** means the posting is for 2027 grads. Look for: "2027" in the title, a graduation window that includes 2027 (e.g. "Graduating Dec 2026 – Aug 2027"), a 2027 start date, or a first-published date on or after 2026-07-01 with no 2026 grad window.
  - "2026" in the title, or a grad window ending in 2026, means a **last-cycle leftover**. Record it, but not as open.
- **Excluded:** requires US citizenship, a green card / permanent residency, a security clearance, or "U.S. person" / ITAR eligibility. Mark it `excluded`. This applies to most defense, space and national-lab roles.
- **No sponsorship:** "will not sponsor", "permanent work authorization required". **Keep** the role and set `no_sponsorship: true`.

## Procedure (cheapest and most first-party first)

1. **Look up the source.** Find the company's row in `timeline/sources.csv`.
   - If `jobs.py spec` is set, run `python3 scripts/jobs.py board <spec>`. Use `--all` to see every title when the filter might miss a program name.
   - Specs: `gh:`, `lever:`, `levereu:`, `ashby:`, `sr:`, `wd:TENANT/wdN/SITE`, `oracle:HOST/SITE`, `pinpoint:SUBDOMAIN`, `eightfold:HOST/DOMAIN`, `amazon:`.
2. **No spec? Find the job board.**
   - Open the careers page (browser pane or WebFetch) and follow the "Search jobs" / "Early careers" link. The URL tells you the job-board software:
     - `*.myworkdayjobs.com/SITE` → Workday
     - `boards.greenhouse.io` / `job-boards.greenhouse.io` / `?gh_jid=` → Greenhouse
     - `jobs.lever.co`, `jobs.ashbyhq.com`, `jobs.smartrecruiters.com` → Lever, Ashby, SmartRecruiters
     - `jobs.eu.lever.co` → Lever's EU region (`levereu:`). US roles can still be listed there (Quantinuum).
     - `*.pinpointhq.com` → Pinpoint (`pinpoint:`)
     - A careers site whose job URLs look like `/careers/job/<long number>` is Eightfold. Try `eightfold:HOST/DOMAIN` (it worked for careers.lamresearch.com/lamresearch.com).
     - `*.oraclecloud.com/hcmUI/CandidateExperience/.../sites/SITE` → Oracle Cloud
     - `*.icims.com`, `*.avature.net`, `*.taleo.net`, SuccessFactors, Phenom, Jobvite, Workable, Comeet, BrassRing, AcquireTM → no API; read them in the browser pane. Jobvite and Avature listing pages worked with WebFetch (Nutanix, Lenovo).
   - `python3 scripts/jobs.py workday <tenant>` brute-forces Workday pods and site names.
   - `python3 scripts/jobs.py guess "<Company>"` tries Greenhouse, Lever, Ashby and SmartRecruiters slugs. **Check that the board is really this company.** Short slugs hit other companies: "capital" is not Capital Group, "analog" is not Analog Devices, "constellation" covers two companies.
   - Custom sites: Amazon (`amazon:`), Google (careers.google.com), Apple (jobs.apple.com), Microsoft (apply.careers.microsoft.com), Meta (metacareers.com), Netflix (explore.jobs.netflix.net) and Tesla. Use the browser pane; it renders JavaScript and got through sites that blocked plain requests (Citadel, Tesla).
   - Subsidiaries often post under the parent. MuleSoft and Slack post under Salesforce, Juniper under HPE (`wd:hpe/wd5/Jobsathpe`), Hulu under Disney (`wd:disney/wd5/disneycareer`), Splunk under Cisco, W&B under CoreWeave, and Electrify America under Volkswagen Group. Check the parent before concluding "no program".
   - Only use web search if none of that works: `"<company>" new grad software engineer 2027`, `"<company>" university graduate software engineer`, `site:<careers-domain> graduate`.
3. **Read the posting.** Run `python3 scripts/jobs.py detail <url>`. It prints the dates plus every citizenship, clearance, sponsorship, graduation-window and years-of-experience line. For sites without an API, open the posting in the browser pane.
   - **Live means** the posting page shows an Apply button, not "no longer accepting" or a redirect to search. Tracker "active" flags go stale (L3Harris was filled while trackers showed it open).
   - **Closed means** `history` shows a this-cycle posting but it's missing from the live board or `detail` can't find it. This caught AutoZone, Marriott, Domino's, Hulu, Redfin and H-E-B, whose 2027 postings opened in Jul–Aug and have since closed.
   - **Excluded needs a quote.** Quote the eligibility sentence from a posting, or from the company's official careers or eligibility page (e.g. "requires DOE Q clearance", "U.S. Person per ITAR"). A company looking like a defense firm isn't evidence. If you can't quote it, use the status you actually found and write the suspicion in `evidence`.
4. **Date it.**
   - Greenhouse: use `first_published`, not `updated_at`.
   - Workday: `postedOn` is the latest *repost*. "Posted 30+ Days Ago" is only a bound, so write "on or before YYYY-MM-DD".
   - If the tracker history has an earlier first-seen date for the same posting, use that.
5. **Last cycle.** Run `python3 scripts/jobs.py history '<regex for company name>'`. It gives tracker first-seen dates across past cycles. Last cycle's opening is the first new-grad SWE posting between 2025-07 and 2026-01. If that's empty, use the company's university-recruiting page ("applications open in August") or a dated Reddit / Blind / LinkedIn post.
   - Some companies post in spring (Airbnb and Airtable post Feb–Apr). Record that.
   - If you find nothing, say unknown. Don't guess.
6. **Decide status.**
   - `open`: a live, this-cycle, US, qualifying posting.
   - `not_yet`: has a new-grad track, nothing live yet.
   - `closed`: a this-cycle posting existed and is gone.
   - `leftover_2026`: only last-cycle postings are live.
   - `no_program_found`: you checked the first-party board and the parent company, and there are no entry-level SWE postings this cycle or last. Say what you checked.
   - `excluded`: see What counts.
   - `unknown`: you couldn't reach or read the board. Say why in `evidence` (blocked, site down, filters didn't apply) so a later run can retry. Wayfair and Williams-Sonoma blocked both WebFetch and the browser pane, and Workday was down for Condé Nast. Don't spend more than 2–3 calls fighting a blocked site.

Budget: about 10 tool calls per company. If the board works through the API, 3–4 calls is normal.

## Output

Write `timeline/research/<company-slug>.json`. Use lowercase with hyphens for the slug: `jpmorgan-chase`, `amazon-aws`. Overwrite any older file for that company.

```json
{
  "company": "exact name from COMPANY_LIST.md",
  "tier": 5,
  "checked": "YYYY-MM-DD",
  "status": "open | not_yet | closed | leftover_2026 | no_program_found | excluded | unknown",
  "postings": [
    {"title": "...", "url": "first-party posting URL", "location": "...",
     "opened": "YYYY-MM-DD or 'on or before YYYY-MM-DD'", "date_source": "greenhouse first_published | workday postedOn | tracker first seen | page text",
     "grad_window": "e.g. Dec 2026 – Aug 2027, or null", "live_verified": "api | browser | no"}
  ],
  "last_cycle_opened": "YYYY-MM-DD, YYYY-MM or null",
  "last_cycle_basis": "short source description, with URL if any",
  "excluded_reason": "citizenship | green card | clearance | us person / itar | null",
  "no_sponsorship": false,
  "jobs_page": "first-party URL where the full job list lives",
  "jobs_spec": "jobs.py spec such as wd:visa/wd5/Visa, or null if no API",
  "evidence": "<= 40 words: what you checked and why this status",
  "confidence": "high | medium | low"
}
```

Always fill `jobs_page`, even for `unknown` or `excluded`. It lets the next run go straight to the job board.

## Full pipeline

All scripts are in this skill's `scripts/` folder. Run them with `python3` from that folder. They use only the standard library.

1. `trackers.py`: clones the GitHub trackers into `$TMPDIR/newgrad-trackers` and writes `timeline/data/trackers.json`. Takes about a minute.
   - Check `timeline/data/unmatched_tracker_names.txt` for big companies that didn't match a list name. Add real matches to `scripts/overrides.json` as tracker name (normalized) → exact list name.
2. `probe.py`: checks every company's own Greenhouse / Lever / Ashby / Workday board and writes `timeline/data/boards.json`. Takes 20–30 minutes; run it in the background. Use `probe.py --only "Name" ...` to redo a few companies.
3. `merge.py`: builds `status.csv`, `SUMMARY.md`, `sources.csv` and `timeline/data/merged.json`.
4. `worklist.py`: picks the companies to research and writes `timeline/data/worklist.json` and `timeline/data/workflow_args.json`. It prints the count and a token estimate (~58K per company on Sonnet); **tell him the estimate and get his OK before running.** Examples:
   - `worklist.py --status open,tracker_lead --source tracker,first-pass`: confirm open roles that aren't first-party yet.
   - `worklist.py --tier 1-5 --source first-pass --limit 100`: redo weak first-pass results, top tiers first.
   - `worklist.py --names "Google|Meta"`: specific companies.
   - Companies that already have a research file are skipped unless you pass `--redo`.
5. Put his request, quoted, into the `approval` field of `workflow_args.json`. Then call the Workflow tool with `scriptPath: <repo>/.claude/workflows/new-grad-research.js` and those contents as `args`.
   - In a new session it may also run by name as `new-grad-research`. Sessions only pick up saved workflows at startup, so use `scriptPath` if the name isn't found.
   - When it finishes, check `declined` and `failed` in the result, and rerun those companies.
6. `merge.py` again. Then open every `open` posting whose research file says `live_verified: "no"` in the browser pane.

The dates are for the 2027 cycle. For the next cycle, move the dates in `common.py` (`CYCLE_START`, `LAST_*`, `PREV_*`) and the snapshot dates in `trackers.py` forward one year, and update the tracker repo names in `trackers.py` and `jobs.py`.

## Running it across many companies

These lessons come from the runs on 2026-09-24 and 2026-09-25:

- **Say in each agent's prompt that he approved the run, and quote his words.** Agents see his latest chat message, and his AGENTS.md rule says an opinion isn't a request. When his latest message was "i think we can use sonnet for the subagents", 75 of 89 agents declined my instructions as unauthorized. Adding an approval line with his quotes fixed it.
- **Sonnet is enough.** With this skill, Sonnet agents averaged about 58K tokens and 0–4 web searches per company. 95 of 100 results were high or medium confidence.
- **The workflow runs at most min(16, CPU cores − 2) agents at once.** That's 6 on his 8-core Mac.

- **Keep each agent's list short.** Each agent session can make 200 web searches. When one agent had ~290 companies, four of the five agents ran out 13 minutes in, and about 850 companies were researched without web search. Use one agent per company (or at most ~10 per agent), and use the API steps before web search.
- **Agents must not spawn sub-agents.** One agent split its batch into 11 more agents and broke the agent cap.
- **One result file per company.** Agents appending to a shared file raced each other and overwrote shared helper files.
- **Work top tiers first,** so the results that matter most get done first.
- **Never let a tracker make a company "open".** The first merge did, and 82 of 225 "open" companies rested on a GitHub tracker alone. `merge.py` now keeps a tracker listing in the `Tracker lead` column. If the company's own board shows nothing, the status is `not_yet`. If nobody has read the board yet, it's `tracker_lead`.
