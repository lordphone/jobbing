# Full search 2026-10-01 (cloud trial) — INCOMPLETE

The run stopped before research (step 6). It is not a real report.

## What failed
- `probe.py` reached **0 job boards** (with board 0, with hits 0, across ~1770 companies).
- The cloud proxy answers 403 to CONNECT for job-board hosts (e.g. boards-api.greenhouse.io, api.lever.co, api.ashbyhq.com). The environment's network allowlist blocks them.
- GitHub tracker data (step 2) did work: 24018 listings, 195 open now.
- No browser in cloud run either, so research agents could not have read the boards that need one.

## Decisions
- Did not run the Workflow research, `merge.py`, `worklist.py`, or `changes.py`: they would have produced a misleading report (every company `unknown`).
- Reverted `timeline/data/boards.json` to the committed version, because the probe overwrote it with empty results.
- Company list: no edits this run. The top unmatched tracker names are staffing firms, universities, or non-US/non-software employers, and without research evidence I did not add or remove anything.
- Companies ended `unknown` because no browser was available: 0 (research not run).
- `status.csv` unchanged; counts from `changes.py`: not produced.

## Fix
Allow the job-board hosts (greenhouse, lever, ashby, workday, smartrecruiters, etc.) in the environment's network policy, then rerun.
