---
name: update-application
description: >-
  Finds a job application in applications/TRACKER.md and updates its status.
  Use when the user pastes a recruiter or ATS email, says they applied,
  or reports OA / screen / interview / rejection / offer / withdrawn.
---

# Update an application

`applications/TRACKER.md` is the log. Each new-application run adds a row. This skill only edits the matching row.

## Statuses

`draft` · `applied` · `oa` · `screen` · `interview` · `rejected` · `offer` · `withdrawn`

Map from the email or message:

- application received / "thank you for applying" / submitted → `applied`
- CodeSignal / HackerRank / Karat / OA / take-home → `oa`
- recruiter screen / phone screen → `screen`
- interview / onsite / loop / hiring manager → `interview`
- not moving forward / unfortunately / other candidates → `rejected`
- offer / compensation / start date → `offer`
- withdrew / not pursuing → `withdrawn`

If the user states a status, use that.

## Find the row

Read `applications/TRACKER.md`. Extract company, role, and any posting/ATS URL from the paste (From, subject, body, Greenhouse / Lever / Ashby / Workday links).

Match in this order:

1. Link column equals the URL in the email
2. Company + role
3. Company, if only one open row for that company
4. Folder name / `applications/*/jd.md`

Prefer the newest row when two still match. If two companies or two roles still fit, ask. Do not guess.

If nothing matches, add a row (date = today or the email date, status from the email, link if present, folder empty, notes = subject). Do not invent a resume folder.

## Edit

Change only `Status` and `Notes` (and `Date` if the email has a clear applied/event date and the row is still `draft`). Keep Company, Role, Link, Folder, NB title unless the user corrects them.

Notes: one short clause — subject or event, not the whole email.

Tell the user which row changed and old → new status.
