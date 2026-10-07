---
name: new-grad-timeline
description: >-
  Researches one company's 2027 new-grad software / backend / full-stack / ML / AI engineer
  hiring in the US (plus Toronto and Vancouver): is the role open now, when it opened, when it opened last cycle, and
  whether it needs citizenship / green card / clearance or won't sponsor. Finds the posting on
  the company's own job board and records where the job list lives. Use for any company in
  timeline/COMPANY_LIST.md, when refreshing timeline/status.csv, or when he asks "is X hiring
  new grads yet".
---

# New-grad timeline research

The answer must come from the company's **own job board** (first party). Community trackers are leads and history, never proof that something is open.

Two uses:

- **One company** ("is X hiring new grads yet"): follow the Procedure below yourself and write its research file. Then run `merge.py`.
- **Many companies:** follow "Full pipeline". It runs Sonnet agents, 20 companies each, through the saved workflow. To search every company, use `.agents/skills/full-search/SKILL.md`.

Files:

- `timeline/COMPANY_LIST.md`: the companies, in 11 tiers.
- `timeline/sources.csv`: where each company's job list lives (`jobs.py spec` and `Jobs page`). Start here.
- `timeline/status.csv`, `timeline/postings.csv`, `timeline/SUMMARY.md`, `timeline/sources.csv`: built by `scripts/merge.py`. Don't edit them by hand.
  - `status.csv` has one row per company (status, last cycle, expected opening). `postings.csv` has one row per open posting, since a company can have several.
  - A posting counts as applied only when a `applications/TRACKER.md` row matches it by link, posting ID (from the link or Notes), or exact title. Applying to one posting never hides a company's other open postings from "Apply now".
  - `CHANGES.md` compares postings by link with the last run: new, removed, changed (deadline, title, location), reposted under a new link (same title), and possible reposts (similar title) for him to check.
- `timeline/research/<company-slug>.json`: one first-party result file per company. The research step writes these, and they beat every other source.
- `timeline/data/`: intermediate files. It holds `trackers.json`, `boards.json`, `worklist.json`, `workflow_args.json` and `merged.json`, plus `first_pass_agents/*.jsonl`, the 2026-09-24 first-pass results kept as a lower-priority source.
  - The full search adds `prev/`, its before-run snapshot of `status.csv` and `COMPANY_LIST.md`, and `list_notes.md`, its company-list edits.
- `timeline/CHANGES.md`: what changed since the last full search. Written by `.agents/skills/full-search/scripts/changes.py`.
- `applications/TRACKER.md`: postings he already applied to (one row per application; a company can have several).
- `.claude/workflows/new-grad-research.js`: the saved workflow, 20 companies per Sonnet agent (`per_agent` in args).
- `scripts/jobs.py` (in this skill folder): the tool for every step below. Run it with no arguments for usage.

## What counts

- **Role:** software, SDE, backend, full-stack, front-end, platform, ML, AI or forward-deployed engineer. Also named programs whose track is software engineering (e.g. Technology Development Program, Engineering Analyst, AMTS, "Software Engineer I", "Associate Software Engineer").
- **Years of experience don't disqualify an entry-level role.** A "1+", "2+" or "3+ years" ask on an entry-level posting is usually not enforced, and he applies with a master's. Judge the level by the title and posting (entry-level, I, Associate, Junior), not the years line.
- **Unlabeled titles count when the posting reads entry-level.** Many entry-level roles are just "Software Engineer" or "AI Engineer", with no level, year or "new grad" in the title. Read each one's posting (`jobs.py screen`) and count it if all of these hold:
  - the **required** qualifications ask for at most 2 years of experience, or say entry-level / recent graduates / early career (preferred qualifications don't count against it);
  - the duties aren't senior: no leading a team, mentoring others, or owning a system's architecture;
  - the title carries no higher level (II, III, Senior, Staff, Lead) and the posting names no higher internal level.
  Pay can back this up (a range starting near the company's new-grad pay), but don't decide on pay alone. Record these with `"level": "unlabeled"` and a `level_basis` quote (e.g. "requires 1+ years; $120K–$195K"). If the requirements are unclear, leave it out and mention it in `evidence`.
- **Not counted:** internships, co-ops, and senior / staff / lead or other clearly non-entry-level roles. "Member of Technical Staff" is a common entry-level title at AI companies, not a staff-level role.
- **PhD-only roles are not counted.** He applies with a master's. Leave out a role whose title or required qualifications need a PhD ("PhD New Grad", "PhD required"). A role open to BS / MS / PhD counts. Also returning-intern-only roles, and hardware / electrical / firmware / test / sales-engineer roles.
- **Location:** anywhere in the US, including US-remote, plus Toronto and Vancouver (Canada). Research every company regardless of city; his preferred areas (`scripts/areas.json`) only decide what `SUMMARY.md` lists first.
- **This cycle** means he can apply to it now as a 2027 grad. Clues: "2027" in the title, a graduation window that includes 2027 (e.g. "Graduating Dec 2026 – Aug 2027"), a 2027 start date, or a first-published date on or after 2026-07-01. These are clues, not requirements: a live posting open to recent or upcoming grads with no class year (evergreen or rolling, like Epic or Infosys) counts too, whenever it was first published.
  - "2026" in the title, or a grad window ending in 2026, means a **last-cycle leftover**. Record it, but not as open.
- **Excluded:** requires US citizenship, a green card / permanent residency, a security clearance, or "U.S. person" / ITAR eligibility. Mark it `excluded`. This applies to most defense, space and national-lab roles.
- **No sponsorship:** "will not sponsor", "permanent work authorization required". **Keep** the role. Set the posting's own `no_sponsorship` (`true` if that posting says it, `false` if it says it sponsors or says nothing), and the company-level `no_sponsorship: true` only when the company says it for all its roles.

## Procedure (cheapest and most first-party first)

1. **Look up the source.** Find the company's row in `timeline/sources.csv`.
   - **The board must be the company's own.** It counts only if the company's careers page sends job seekers to it (its "Search jobs" / "Apply" links go there). Referral-only, freelance / contractor and internal boards don't count. A parent company's board, or a separate campus board, counts when that is where this company's new-grad roles are posted.
   - **If your entry has a `board_flag`**, a script found the saved board doubtful (it errored, lists 0 jobs, or carries another company's name). Open the careers page and see where its job links go. Then either confirm the saved board or switch to the right one (step 2), test it with `jobs.py board <spec>`, and write the reason in `jobs_spec_basis`. If there is no API board, set `jobs_spec` to `null` and keep `jobs_page`. A timeout is not a reason to drop a board; retry it.
   - If `jobs.py spec` is set, run `python3 scripts/jobs.py board <spec>`. It prints **every posting on the board**, each with a hint tag from its title (`new-grad title`, `unlabeled eng`, `senior/intern?`, `other`). The tags never hide anything and can be wrong: read the whole list and decide yourself which postings could be entry-level software roles, including oddly named programs ("Technology Development Program").
   - **Check the Coverage line.** `full` means you have the whole board. Workday, Oracle and Eightfold boards with over 1500 postings, and Amazon, can only be searched with new-grad and role keywords; Coverage then says `SEARCHED, NOT THE FULL BOARD`. In that case also search the careers page (browser pane) with other words the company might use before concluding nothing is open.
   - Then run `python3 scripts/jobs.py screen <spec>`. It opens the postings tagged `new-grad title` or `unlabeled eng` and prints their years, level and pay lines. For any other posting you think could qualify, run `screen <url> <url> ...`. Judge each with "Unlabeled titles" in What counts, and open the full posting with `detail` when the lines don't settle it.
   - **No API (browser boards):** scan the whole US engineering list, not only a "new grad" search. Filter by location (US, Toronto, Vancouver) and by engineering / software category, page through every result, and open each unlabeled title that isn't senior.
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
3. **Read the posting.** Run `python3 scripts/jobs.py detail <url>`. It prints the dates, every location the job board lists (`locations:`), location sentences from the text (`@`), plus every citizenship, clearance, sponsorship, graduation-window and years-of-experience line. For sites without an API, open the posting in the browser pane.
   - **Location: list every real place.** Write each city with its state or country, separated by `; `, e.g. `San Francisco, CA; Seattle, WA; Remote (US)`. Never write `+2`, `6 Locations`, `multiple` or `3 US locations`; board listings cut these short, so take them from `detail` or the posting page. If the text names cities the API doesn't ("San Francisco or Seattle"), include them. Only if the posting itself names no city, write what it says and add `(no city listed)`, e.g. `United States (no city listed)`.
   - **Live means** the posting page shows an Apply button, not "no longer accepting" or a redirect to search. Tracker "active" flags go stale (L3Harris was filled while trackers showed it open).
   - **Closed means** a this-cycle posting existed (from `history` or the previous file) and you opened its posting page and saw it gone: "job not found", "no longer accepting applications", a redirect to search, or no Apply button. This caught AutoZone, Marriott, Domino's, Hulu, Redfin and H-E-B, whose 2027 postings opened in Jul–Aug and have since closed.
   - **A failed lookup is not closed.** `detail` saying `LOOKUP FAILED` (network error, timeout, rate limit, blocked) tells you nothing; retry, then open the page. `NOT ON THE BOARD` means the board answered without it; it may be unlisted (Commure's live new-grad posting was missing from its Ashby list), so open the page before calling it closed. If you can't open the page either, the status is `unknown`, not `closed`.
   - **Excluded needs a quote.** Quote the eligibility sentence from a posting, or from the company's official careers or eligibility page (e.g. "requires DOE Q clearance", "U.S. Person per ITAR"). A company looking like a defense firm isn't evidence. If you can't quote it, use the status you actually found and write the suspicion in `evidence`.
4. **Date it.**
   - Greenhouse: use `first_published`, not `updated_at`.
   - Workday: `postedOn` is the latest *repost*. "Posted 30+ Days Ago" is only a bound, so write "on or before YYYY-MM-DD".
   - If the tracker history has an earlier first-seen date for the same posting, use that.
   - **Deadline.** Record it only if the posting or the company's careers page states one ("apply by", "applications close", "deadline"), or the API gives an end date (Oracle `ends=`, Workday `endDate=`; `jobs.py detail` prints both plus any deadline sentence). "Open until at least Sept 30" is a lower bound, so write "at least YYYY-MM-DD". No stated deadline → `null`. Never guess one from past cycles.
5. **Last cycle.** Run `python3 scripts/jobs.py history '<regex for company name>'`. It gives tracker first-seen dates across past cycles. Last cycle's opening is the first new-grad SWE posting between 2025-07 and 2026-01. If that's empty, use the company's university-recruiting page ("applications open in August") or a dated Reddit / Blind / LinkedIn post.
   - Some companies post in spring (Airbnb and Airtable post Feb–Apr). Record that.
   - If you find nothing, say unknown. Don't guess.
6. **Record every qualifying posting.** A company can have several open new-grad or entry-level roles (different teams, titles, or cities). Put each one in `postings`, not just the best one. Same title in several cities as separate postings → one entry each.
7. **Decide status.**
   - `open`: a live, this-cycle, US / Toronto / Vancouver, qualifying posting that you opened yourself in this run. If you couldn't read the posting or the board, the status is `unknown`, not `open`.
   - `not_yet`: has a new-grad track, nothing live yet.
   - `closed`: a this-cycle posting existed and is gone.
   - `leftover_2026`: only last-cycle postings are live.
   - `no_program_found`: you checked the first-party board and the parent company, and there are no entry-level SWE postings this cycle or last. Say what you checked.
   - `excluded`: see What counts.
   - `unknown`: you couldn't reach or read the board. Say why in `evidence` (blocked, site down, filters didn't apply) so a later run can retry. Wayfair and Williams-Sonoma blocked both WebFetch and the browser pane, and Workday was down for Condé Nast.
8. **Compare with the previous file. Do this only after steps 1–6.** Research fresh first, without reading the old `timeline/research/<slug>.json`. Then read it, if it exists, and compare:
   - **Old posting missing from your findings:** check its URL with `jobs.py detail <url>`, or in the browser pane if there's no API.
     - Still live and it qualifies → add it back.
     - Gone (seen on the posting page, per **Closed means** above), and it was a this-cycle posting → that's `closed` (unless another posting is open). A failed lookup alone is not gone.
   - **Same posting found both times:** keep the earlier `opened` date, and keep the old `deadline` if you didn't find one.
   - **Same job under a new link (a repost):** an old posting is gone and a new one has the same or nearly the same title, team and location. Workday and Oracle often repost this way. Treat it as the same job: keep the old `opened` date and add "reposted from <old URL>" to `evidence`. If you can't tell whether it's the same job, record it as a new posting and say so in `evidence`.
   - **Old `last_cycle_opened` or `excluded_reason` you didn't find this time:** keep it, unless your research contradicts it.
   - **The comparison raises a question:** keep investigating (open more pages, fetch more) until you can reach a real conclusion.
   - **Then rewrite the file** with your final result: everything from the old file that is still true, plus what you found. If the status differs from the old file, say why in `evidence`.

## Output

Write `timeline/research/<company-slug>.json`. Use lowercase with hyphens for the slug: `jpmorgan-chase`, `amazon-aws`. One file per company. Rewrite it after the step 8 comparison; it never keeps history.

```json
{
  "company": "exact name from COMPANY_LIST.md",
  "tier": 5,
  "checked": "YYYY-MM-DD",
  "status": "open | not_yet | closed | leftover_2026 | no_program_found | excluded | unknown",
  "postings": [
    {"title": "...", "url": "first-party posting URL", "location": "every city with state/country, '; '-separated",
     "opened": "YYYY-MM-DD or 'on or before YYYY-MM-DD'", "date_source": "greenhouse first_published | workday postedOn | tracker first seen | page text",
     "deadline": "YYYY-MM-DD, 'at least YYYY-MM-DD', or null if none is stated",
     "grad_window": "e.g. Dec 2026 – Aug 2027, or null", "live_verified": "api | browser | no",
     "level": "new-grad title | unlabeled", "level_basis": "for unlabeled: the quote that makes it entry-level, else null",
     "no_sponsorship": false}
  ],
  "last_cycle_opened": "YYYY-MM-DD, YYYY-MM or null",
  "last_cycle_basis": "short source description, with URL if any",
  "excluded_reason": "citizenship | green card | clearance | us person / itar | null",
  "no_sponsorship": false,
  "jobs_page": "first-party URL where the full job list lives",
  "jobs_spec": "jobs.py spec such as wd:visa/wd5/Visa, or null if no API",
  "jobs_spec_basis": "when you confirmed or changed a flagged or unusual board: <= 20 words on how, e.g. 'careers page Apply links go to gh:thoughtworks'; else omit",
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
3. `merge.py`: builds `status.csv`, `SUMMARY.md`, `sources.csv` and `timeline/data/merged.json`. Then `check_sources.py` (about a minute) tests every saved API board and writes doubtful ones to `timeline/data/source_flags.json`; `worklist.py` hands each flag to that company's research agent.
4. `worklist.py`: picks the companies to research and writes `timeline/data/worklist.json` and `timeline/data/workflow_args.json`. It prints the count; **tell him the count and get his OK before running.** Examples:
   - `worklist.py --status open,tracker_lead --source tracker,first-pass`: confirm open roles that aren't first-party yet.
   - `worklist.py --tier 1-5 --source first-pass --limit 100`: redo weak first-pass results, top tiers first.
   - `worklist.py --names "Google|Meta"`: specific companies.
   - Companies that already have a research file are skipped unless you pass `--redo`.
5. Put his request, quoted, into the `approval` field of `workflow_args.json`. Then call the Workflow tool with `scriptPath: <repo>/.claude/workflows/new-grad-research.js` and those contents as `args`.
   - In a new session it may also run by name as `new-grad-research`. Sessions only pick up saved workflows at startup, so use `scriptPath` if the name isn't found.
   - When it finishes, check `declined` and `failed` in the result, and rerun those companies.
6. `merge.py` again. Then open every `open` posting whose research file says `live_verified: "no"` in the browser pane.

The dates are for the 2027 cycle. For the next cycle, move the dates in `common.py` (`CYCLE_START`, `LAST_*`, `PREV_*`) and the snapshot dates in `trackers.py` forward one year, and update the tracker repo names in `trackers.py` and `jobs.py`.
