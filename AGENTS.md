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

Follow `.agents/skills/generate-resume/SKILL.md`. A URL-only paste is enough: fetch the posting, then generate. If he pastes both, use the text and keep the URL as the tracker link. Output goes under `applications/<YYYY-MM-DD>-<company>-<role>/`, using the full creation date including the day. That run also prepends a row to `applications/TRACKER.md`.

## When he pastes an application email or reports a status

Follow `.agents/skills/update-application/SKILL.md`. Find the row in `applications/TRACKER.md` and update status. Do not regenerate the resume.
