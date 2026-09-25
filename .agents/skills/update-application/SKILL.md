---
name: update-application
description: >-
  Finds a job application in applications/TRACKER.md and updates its status
  or outreach. Use when the user pastes a recruiter or ATS email, says they
  applied, reports OA / screen / interview / rejection / offer / withdrawn,
  or reports LinkedIn outreach (sent requests, replies, referrals).
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

Change only `Status`, `Outreach`, and `Notes` (and `Date` if the email has a clear applied/event date and the row is still `draft`). Keep Company, Role, Link, Folder, NB title unless the user corrects them.

Notes: one short clause — subject or event, not the whole email.

Tell the user which row changed and old → new status or outreach.

## Outreach

The tracker's `Outreach` column is the one-glance summary. Values:

`—` not reached out · `sent` requests sent · `talking` someone replied · `referred` someone submitted a referral · `none` looked, found nobody, applied cold

The details go in the Contacts table at the bottom of `applications/<folder>/outreach.md`: `Name | Link | Type | Sent | Status | Notes`.

- Type: `CMU alum` · `UW alum` · `non-alum` · `hiring mgr`
- Sent: the date he sent the request (`MM-DD`), today if he does not say.
- Status: `no reply` · `replied` · `referred MM-DD` · `declined`, plus anything short he mentions.
- Add one row per person he names ("sent to J. Chen and A. Patel at Visa"). Update the existing row when he reports on someone already logged. Record names and links only as he gives them; do not look people up or fill in a link he did not provide.
- If `outreach.md` has no Contacts table, add one at the end. If the application has no folder, keep the details in the tracker Notes instead.

Set the tracker `Outreach` value from the best contact status: any referral → `referred`, else any reply → `talking`, else any sent → `sent`. Set `none` only when he says he found nobody. Never move it backward (a later "no reply" does not undo `referred`).

When there is a referrer, add `ref: <Name>` to Notes, alongside what is already there.

"Who haven't I followed up with?" → read the Contacts tables and list contacts still `no reply` more than a week after Sent, grouped by company.
