# Agent Instructions

This repo generates one-page LaTeX resumes from an experience bank.

## Source of truth

- `inventory/` is the only source of truth. If Lordphone adds or corrects a fact there, that is the fact.
- `INTERNSHIP_RECORD` is leftover input. Do not treat it as current.
- Never invent a metric, tool, title, or outcome. New sentences and fusions are fine if every claim maps to inventory facts.

## Standing rules

- One page. Fill it — no obvious empty strip at the bottom. Same layout as `shared/preamble.tex`.
- Output PDF is always `Lordphone_Wen_Resume.pdf`. Keep `resume.tex` as the source.
- `approved` lines are a starting point, not a lock. Rewrite or fuse freely as long as the facts stay real.
- Do not add a skill that is not in `inventory/skills.md`.
- When asked for bullet points, put them in copyable `text` code blocks with literal `•` bullets. Keep company/role headings outside the blocks, with a separate block for each role.

## When he pastes a job description, a posting URL, or both

Follow `.agents/skills/new-application/SKILL.md`. A URL-only paste is enough: fetch the posting, then generate. If he pastes both, use the text and keep the URL as the tracker link. Output goes under `applications/<YYYY-MM-DD>-<company>-<role>/`, using the full creation date including the day. That run also prepends a row to `applications/TRACKER.md`.

## When he pastes an application email or reports a status

Follow `.agents/skills/update-application/SKILL.md`. Find the row in `applications/TRACKER.md` and update status. Do not regenerate the resume.

## When he asks about new-grad hiring timelines

Follow `.agents/skills/new-grad-timeline/SKILL.md`. That covers questions like "is X hiring new grads yet", refreshing `timeline/status.csv` / `timeline/SUMMARY.md`, and researching many companies with one Sonnet agent each. Trust the company's own job board first; GitHub trackers are leads only.

## When working on the company list

`timeline/COMPANY_LIST.md` is a plain list of company names in 11 tiers. A company owned by another company gets its own entry if it hires under its own name, like Tinder, Slack, Twitch, X, or Hulu. Only merge entries that are the same company listed twice.
