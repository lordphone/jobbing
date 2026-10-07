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

1. **Snapshot.** Run `python3 $FS/changes.py snapshot`. It copies `timeline/status.csv`, `timeline/postings.csv` and `timeline/COMPANY_LIST.md` to `timeline/data/prev/` so the morning report can compare.
2. **Trackers.** Run `python3 $TL/trackers.py` (about 10 seconds).
3. **Company list.** See "Company list review" below.
4. **Job boards.** Run `python3 $TL/probe.py` in the foreground with a 10-minute timeout (a few minutes).
5. **Merge, board check and worklist.** Run `python3 $TL/merge.py`, then `python3 $TL/check_sources.py` (about a minute; it flags saved job boards that error, list 0 jobs or carry another company's name), then `python3 $TL/worklist.py --redo`. That picks every company on the list, and each flagged company's agent confirms or replaces its board.
6. **Research.** Read `timeline/data/workflow_args.json`. Set `approval` to the request that started this run, quoted: the scheduled task's prompt, or his chat message. Then call the Workflow tool with `scriptPath: <repo>/.claude/workflows/new-grad-research.js` and those contents as `args`. It runs 20 companies per agent, 6 agents at a time, for about 2 hours.
7. **Rerun misses.** Rerun the companies in the result's `failed` and `declined` lists, and any company on the list whose `timeline/research/<slug>.json` isn't dated today. To rerun them, use `worklist.py --redo --names "A|B|C"` and run the workflow again. Do this once; if some still fail, list them in the report.
8. **Report.** Run `python3 $TL/merge.py`, then `python3 $FS/changes.py`. It writes `timeline/CHANGES.md`: newly open companies, no longer open, postings that are new (including new roles at companies that were already open), removed, changed (deadline, title, location) or reposted under a new link, other status changes, and company-list edits.
9. **Finish.** Reply with the counts from `changes.py`, the newly open companies, the new postings, and any removed posting he had applied to or any deadline that moved earlier. Don't commit.

## Company list review

The list's rule is about how companies hire. A company gets its own entry if it hires under its own name, whoever owns it. An acquisition or merger alone is never a reason to change the list.

Look at:
- `timeline/data/unmatched_tracker_names.txt`: companies with new-grad postings in the GitHub trackers that aren't on the list, most postings first. Go down the top ~100.
- The last run's `timeline/research/*.json` files, for companies whose `evidence` says they now post only under another name, or have stopped hiring.

Allowed edits:
- **Add** a company that posts US new-grad or entry-level software roles under its own name, in the tier that fits. Skip:
  - staffing and IT-contracting agencies (Artech, TSMG, mthree, Jobsbridge);
  - universities;
  - employers with no US roles (Sainsbury's).
- **Rename** when the company now hires under a new name. Use the list's style: `New Name (formerly Old Name)`. Delete the old `timeline/research/<old-slug>.json`.
- **Merge** only when two entries are the same company, or when the research shows its postings now appear only under the parent's name.
- **Remove** only when the company has shut down or stopped hiring, with evidence from its own site.
- **Move tiers** only when an entry is clearly in the wrong tier.

If an added company's tracker name doesn't match its list name, add the pair to `$TL/overrides.json` (normalized tracker name → exact list name).

After editing, run `python3 $FS/recount.py` to fix the counts. Write one line per edit to `timeline/data/list_notes.md`, overwriting the last run's: what changed and why. `changes.py` puts it in the report.

Keep it to about 20 edits a run. Leave the rest for the next run.

## When it runs unattended

- **Browser approval prompts stall agents.** A site that needs approval can hold an agent for over an hour when nobody answers. The agent eventually gets "denied", marks the company `unknown`, and moves on.
- **Permission prompts stall the whole run.** The scheduled session must be allowed to run Bash, write files and call the Workflow tool without asking.
