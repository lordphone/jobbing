---
name: full-search
description: >-
  Runs the job posting search on every company in one pass: tidies timeline/COMPANY_LIST.md,
  re-checks every company's own job board, researches all companies with Sonnet agents (20 per
  agent), and writes timeline/CHANGES.md with what changed since the last run. Use for the
  full search, the job posting search on all companies, or a refresh of all companies,
  whether he asks in chat or a scheduled task runs it.
---

# Full search

Every company, every run. No tiering, no skipping.

It may run unattended (scheduled), so don't ask questions or wait for replies. Where the steps below leave a choice, make the sensible call and write it in `timeline/CHANGES.md`.

The research method, statuses and output format live in `.agents/skills/new-grad-timeline/SKILL.md`. This skill only sets the order.

`TL=.agents/skills/new-grad-timeline/scripts` and `FS=.agents/skills/full-search/scripts`, relative to the repo root.

## Steps

1. **Snapshot.** Run `python3 $FS/changes.py snapshot`. It copies `timeline/status.csv`, `timeline/postings.csv`, `timeline/COMPANY_LIST.md` and `timeline/research/` to `timeline/data/prev/` so the checks and the morning report can compare.
2. **Trackers.** Run `python3 $TL/trackers.py` (about 10 seconds).
3. **Company list.** See "Company list review" below.
4. **Job boards.** Run `python3 $TL/probe.py` in the foreground with a 10-minute timeout (about 6 minutes).
5. **Merge, board check and worklist.** Run `python3 $TL/merge.py`, then `python3 $TL/check_sources.py` (about a minute; it flags saved job boards that error, list 0 jobs or carry another company's name, and lists boards that stayed rate-limited as unchecked), then `python3 $TL/worklist.py --redo`. That picks every company on the list, and each flagged company's agent confirms or replaces its board.
6. **Research.** Read `timeline/data/workflow_args.json`. Set `approval` to the request that started this run, quoted: the scheduled task's prompt, or his chat message. Then call the Workflow tool with `scriptPath: <repo>/.claude/workflows/new-grad-research.js` and those contents as `args` (a few lines: the agents read their companies from `worklist.json`). `worklist.py` groups the companies into balanced batches (about 20 per agent: fewer for slow companies, more for fast ones), the slowest batches first, from the times in `timeline/data/company_minutes.json`. The Workflow runtime runs up to 32 agents at once and starts the next batch as each one finishes; with balanced batches the last run (92 agents, 1,829 companies) took about 55 minutes.
7. **Check and rerun.** Run `python3 $TL/verify_dropped.py` (it puts back postings dropped as gone that the API shows live), then `python3 $TL/validate.py`. It prints a `worklist.py --redo --names "..."` line for every company whose file is missing, not dated today or breaks the format, including the result's `failed` and `declined` companies. Run that line and the workflow again with `"per_agent": 3` added to the args (a rerun is small; 3 per agent runs them side by side), then `verify_dropped.py` and `validate.py` once more. Do this once; `changes.py` lists any that still fail. Then run `python3 $TL/timing.py <run dir> <rerun dir>` with the transcript dirs both Workflow results printed. It saves each company's minutes to `timeline/data/company_minutes.json` for the next run's batches.
8. **Report.** Run `python3 $TL/merge.py`, then `python3 $FS/changes.py`. It writes `timeline/CHANGES.md`: newly open companies, no longer open, postings that are new (including new roles at companies that were already open), removed (split into gone from the board, still live but no longer counted, and no reason recorded), put back by `verify_dropped.py`, changed (deadline, title, location, posted date) or reposted under a new link, other status changes, company-list edits, and `validate.py`'s remaining errors and format warnings.
9. **Finish.** Reply with the counts from `changes.py`, the newly open companies, the new postings, and any removed posting he had applied to or any deadline that moved earlier. Each posting line shows its posted date (when the posting showed one) and its discovered date. End with the table `python3 $FS/recent.py` prints, as it prints it: open postings in every tier he hasn't applied to, located in the New York, Bay Area, Seattle, LA, Austin, Vancouver, Toronto or Quebec areas or remote, posted (or, with no posted date, discovered) in the last 7 days, newest discovered first, with the ones this run found marked **new**. Don't commit.

## Company list review

The list's rule is about how companies hire. A company gets its own entry if it hires under its own name, whoever owns it. An acquisition or merger alone is never a reason to change the list.

Look at:
- `timeline/data/unmatched_tracker_names.txt`: companies with new-grad postings in the GitHub trackers that aren't on the list, most postings first. Go down the top ~100. Names already judged are left out (`$TL/skip_tracker_names.json`).
- The last run's `timeline/research/*.json` files, for companies whose `evidence` says they now post only under another name, or have stopped hiring.

Allowed edits:
- **Add** a company that posts US new-grad or entry-level software roles under its own name, in the tier that fits (the tier rules are at the top of the list), under its industry heading. Skip:
  - staffing and IT-contracting agencies (Artech, TSMG, mthree, Jobsbridge);
  - universities;
  - employers with no US, Toronto or Vancouver roles (Sainsbury's). A Toronto or Vancouver employer (Sun Life, Intact, Konrad Group) is in scope.
- **Rename** when the company now hires under a new name. Use the list's style: `New Name (formerly Old Name)`. Delete the old `timeline/research/<old-slug>.json`.
- **Merge** only when two entries are the same company, or when the research shows its postings now appear only under the parent's name.
- **Remove** only when the company has shut down or stopped hiring, with evidence from its own site.
- **Move tiers** only when an entry is clearly in the wrong tier.

For each name you skip for good, add its normalized name (`common.norm`) and the reason to `$TL/skip_tracker_names.json`, so the next run doesn't review it again. Leave a name out of that file when it might qualify later.

If an added company's tracker name doesn't match its list name, add the pair to `$TL/overrides.json` (normalized tracker name → exact list name).

After editing, run `python3 $FS/recount.py` to fix the counts. Write one line per edit to `timeline/data/list_notes.md`, overwriting the last run's: what changed and why. `changes.py` puts it in the report.

Keep it to about 20 edits a run. Leave the rest for the next run.

## When it runs unattended

- **Browser approval prompts stall agents.** A site that needs approval can hold an agent for over an hour when nobody answers. The agent eventually gets "denied", marks the company `unknown`, and moves on.
- **Permission prompts stall the whole run.** The scheduled session must be allowed to run Bash, write files and call the Workflow tool without asking.
