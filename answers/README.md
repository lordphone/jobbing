# Answers

Interview and application-question prep. Built from `inventory/`, like the resumes. Facts live in `inventory/`; if an answer needs a new fact, add it there first.

## How interviews use this

Behavioral interviews ask many questions but reuse the same handful of stories. The interviewer picks a question type (a hard bug, a failure, a conflict), hears one story, then spends most of the time on follow-ups: what exactly *you* did, the numbers, what you tried first, what you would do differently.

So the unit of prep is the **story**, not the answer:

- Know 8–10 stories cold as bullets, not scripts. Scripts sound recited and fall apart on the first follow-up.
- Each story should answer several question types, told from a different angle.
- Prepare the follow-ups. A gap in a story is exactly where an interviewer will push.
- Spoken answers run ~1.5–2 minutes: situation and task in two sentences, most of the time on what you did, a result with a number, one line on what you took from it. Say "I", not "we", for your own part.
- Do not tell the same story twice to one company, across rounds. Check `used with` before an interview loop.

Written application questions are different: the exact wording matters, and they get saved as finished prose.

## Layout

- [`stories.md`](stories.md) — the story bank. One section per story: STAR bullets, which question types it answers, likely follow-ups, gaps, and where it has been used.
- [`coverage.md`](coverage.md) — question type → best stories. Shows which types are strong and which have no story yet.
- [`questions/`](questions/) — written answers, one file per question type. Each answer keeps the exact question wording, the company, and the date.

## Workflow

1. **Written question comes in:** find its type in `coverage.md`, check `questions/<type>.md` for an answer to adapt, write it from the story in `stories.md`, save it under that type, and add the company to the story's `used with`.
2. **Interview coming up:** check `coverage.md` against the role, pick stories per type, rehearse from the STAR bullets, and drill the follow-ups and gaps.

## Question types

| Type | File |
|---|---|
| Working with AI tools | [questions/ai-tools.md](questions/ai-tools.md) |
