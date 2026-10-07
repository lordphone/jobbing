---
name: top-tier-search
description: >-
  Runs the full search on tier 1–4 companies only (FAANG+, AI labs, unicorns, quant; about 390), from scratch
  and deeper: Opus agents, 20 companies each, that don't see the last answer. Writes timeline/CHANGES.md like the
  full search. On demand only. Use when he asks for the top-tier search or to search the top companies.
---

# Top-tier search

The full search (`.agents/skills/full-search/SKILL.md`), limited to tiers 1–4 of `timeline/COMPANY_LIST.md`. Same steps and outputs, with three differences:

- **Subset:** only tiers 1–4. Every other company keeps its last result.
- **From scratch:** the worklist leaves out the last answer (`--blind`), so each agent researches fresh. It still compares with the saved file afterward, as Procedure step 8 of the research skill says, so a posting the last run found is checked, not silently dropped.
- **Deeper:** Opus agents instead of Sonnet, still 20 companies each.

No company list review: that belongs to the full search.

It may run unattended, so don't ask questions or wait for replies, except the worklist count in step 5 when he asked in chat.

`TL=.agents/skills/new-grad-timeline/scripts` and `FS=.agents/skills/full-search/scripts`, relative to the repo root.

## Steps

1. **Snapshot.** Run `python3 $FS/changes.py snapshot`.
2. **Trackers.** Run `python3 $TL/trackers.py` (about 10 seconds).
3. **Job boards.** Run `python3 $TL/probe.py --tier 1-4` (a minute or two). It redoes only these companies and keeps everyone else's results.
4. **Merge and board check.** Run `python3 $TL/merge.py`, then `python3 $TL/check_sources.py`.
5. **Worklist.** Run `python3 $TL/worklist.py --tier 1-4 --redo --blind`. That picks every tier 1–4 company.
6. **Research.** Read `timeline/data/workflow_args.json`. Set `approval` to his request, quoted, and add `"model": "opus"`. Then call the Workflow tool with `scriptPath: <repo>/.claude/workflows/new-grad-research.js` and those contents as `args`.
7. **Rerun misses.** Rerun the result's `failed` and `declined` companies, and any tier 1–4 company whose research file isn't dated today: `worklist.py --redo --blind --names "A|B|C"`, then the workflow again with the same `model`. Do this once; list any that still fail in the report.
8. **Report.** Run `python3 $TL/merge.py`, then `python3 $FS/changes.py --run "Top-tier search (tiers 1–4)"`. It writes `timeline/CHANGES.md`: newly open, new postings, no longer open and other status changes since the snapshot, which only tier 1–4 companies can have.
9. **Finish.** Reply with the counts from `changes.py`, the newly open companies, and the new postings. Don't commit.
