# Agent Instructions

This repo generates one-page LaTeX resumes from an experience bank.

## Source of truth

- `inventory/` is the only source of truth. If Lordphone adds or corrects a fact there, that is the fact.
- Never invent a metric, tool, title, or outcome. New sentences and fusions are fine if every claim maps to inventory facts.

## Standing rules

- One page. Fill it — no obvious empty strip at the bottom. Same layout as `shared/preamble.tex`.
- Output PDF is always `Lordphone_Wen_Resume.pdf`. Keep `resume.tex` as the source.
- `approved` lines are a starting point, not a lock. Rewrite or fuse freely as long as the facts stay real.
- Do not add a skill that is not in `inventory/skills.md`.
- When asked for bullet points, put them in copyable `text` code blocks with literal `•` bullets. Keep company/role headings outside the blocks, with a separate block for each role. For copy-paste resume text, also give the company, job title, and location each in its own `text` block above that role's bullets.

## Skills

- He pastes a job description, a posting URL, or both → `.agents/skills/new-application/SKILL.md`
- He pastes an application email or reports a status or outreach → `.agents/skills/update-application/SKILL.md`
- He asks about new-grad hiring timelines ("is X hiring new grads yet", refreshing `timeline/`) → `.agents/skills/new-grad-timeline/SKILL.md`
- He pastes an application question or asks for interview prep → `.agents/skills/answers/SKILL.md`
- He asks for the full search (the job posting search on all companies, or refreshing all companies), or a scheduled task runs it → `.agents/skills/full-search/SKILL.md`
- He asks for the top-tier search (the full search on tier 1–4 companies only) → `.agents/skills/top-tier-search/SKILL.md`
