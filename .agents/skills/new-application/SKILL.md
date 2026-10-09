---
name: new-application
description: >-
  Starts a new application from a job description: tailors a one-page LaTeX
  resume from inventory/, logs it in applications/TRACKER.md, and writes
  LinkedIn outreach notes. Use when the user pastes a JD, a job posting URL,
  both, asks to generate or tailor a resume, or wants a new applications/
  folder for a company or role.
---

# New application

## Inputs

1. The job description — pasted text, a posting URL, or both. A URL alone is enough: fetch it. If he pastes both, use the text and keep the URL as the link. If the page is login-walled, ask for a paste instead of inventing a JD.
2. The `inventory/` role files you might pick from.
3. The newest `applications/*/resume.tex`, as the template.

## Steps

1. Write the JD to `applications/<YYYY-MM-DD>-<company>-<role>/jd.md`. Use today's full date, including the day, for every new application folder (for example, `2026-09-23-singlestore-software-engineer-helios-new-grad-2027`). Put the posting URL at the top of `jd.md` if the paste has one.
2. Score inventory items against the JD. Fuse overlapping facts into one bullet when they are the same work; do not repeat a metric. Otherwise pick and rewrite freely.
3. Pick:
   - NewsBreak title: pick from the printed-title list in `inventory/newsbreak.md`, using the JD.
   - NewsBreak: 3–4 bullets
   - Haddee / ZenAI: 1–2 each
   - Research: 1–2 if the JD cares; if it does not, keep it as fill before leaving empty space
   - Projects / leadership: 1–2 lines
   - Skills: reorder so JD keywords sit in the first two rows; drop the rest
   - Certifications: strongly recommended. Keep both AWS certifications as their own Skills row (`Certifications`); most employers run on cloud. Cut them only as a last resort to fit the page, and say so in `selection.md`
   - Coursework: 2–4 per school, JD-relevant first
   - Section lengths above are defaults. To fill the page, add the next-best unused inventory item or expand a selected bullet with relevant unused facts (second Haddee/ZenAI line, research, project details, extra project); do not repeat claims. Only after useful inventory content is exhausted may you modestly loosen itemsep / titlespacing. Preserve the shared margins and font size; do not use blank lines, manual vertical padding, or stretched spacing to disguise missing content. If it spills to two pages, cut the lowest-value line.
4. Write the bullets from the picked facts. Header city (`\header{City}`): prefer Mountain View, CA whenever the JD allows the SF Bay (including multi-office postings that list New York or Seattle alongside SF / South San Francisco / Bay). Canada-only → Toronto, ON. New York only if the JD is New York–only with no Bay option. Otherwise Mountain View, CA.
5. Write `selection.md` in the same folder:
   - NewsBreak title chosen and why (JD phrase that picked it)
   - item ids used and which facts went into each bullet
   - item ids skipped and why
   - any constraint you almost violated
6. Write `resume.tex` in that folder from the template. Keep the existing voice and macros (`\header`, `\role`, `\edu`). Convert numbers to the same LaTeX style (`~`, `\,`, `{,}`). The preamble path is `../../shared/preamble`; if it is wrong, fix the path, do not copy the preamble.

7. Compile from that folder:

```bash
tectonic resume.tex
mv resume.pdf Lordphone_Wen_Resume.pdf
```

### Required page-fill verification before delivery

- Verify the newly compiled deliverable, not a stale PDF from an earlier successful build. A failed compile does not permit delivery of the old PDF as the revision.
- Require exactly one page. Measure the bottom of the last visible content line using PDF text bounding boxes (for example, `pdftotext -bbox` yMax). With coordinates measured from the top, compute `unused_height = page_height - configured_bottom_margin - last_content_bottom`, in points. Require `0 <= unused_height <= 12 pt`. Read the bottom margin from the preamble. The normal bottom margin is intentional; extra blank space above it is what this check limits.
- Render and inspect the entire final page at a readable resolution. Require no obvious empty bottom strip, clipping, overlap, or cramped text. Passing the numeric check does not override a visible defect, and visual inspection does not replace the measurement.
- If either check fails, revise using the inventory-first rule in step 3, recompile, and repeat both checks. Do not call the resume complete or claim it fills the page while a check fails. If compilation or verification is blocked, report the unresolved check instead of claiming success.
- Record the final page count, bottom margin, last-content position, unused height, and visual-review result in `selection.md`. These measurements must describe the final PDF after the last edit.

8. Prepend a row to `applications/TRACKER.md` (newest first). Date = today (`YYYY-MM-DD`). Company and Role = the JD. Link = posting URL, or empty. Status = `draft`. Outreach = `—`. Folder = the slug. NB title = the printed NewsBreak title. Notes empty unless something is worth one clause. Do not duplicate a row for the same folder.

9. Write LinkedIn outreach to `outreach.md` in the same folder. He looks for someone at every company, so every run writes all four notes. Each note goes on a connection request; he sends his resume later, so no note has a resume link.

   `outreach.md` has, in this order:
   - **Call:** one line saying which notes to send first and why. Big company (formal referral program, high applicant volume) → alumni referral first, non-alumni as backup, hiring-manager note optional. Startup or small team → hiring-manager note plus any alumni. Consultancy or mass hiring → alumni referral if one is easy to find; otherwise just apply. Referrals are never pointless, so no call says to skip outreach entirely.
   - **Search:** three LinkedIn people-search links, `https://www.linkedin.com/search/results/people/?keywords=<URL-encoded query>`, for `[Company] Carnegie Mellon`, `[Company] University of Wisconsin`, and `[Company] <team or role keyword from the JD>`.
   - **Notes:** the four notes below, recommended ones first, each with its character count. Label any note the call marks optional.
   - **Contacts:** the empty Contacts table from the `update-application` skill, which fills it in as he reaches out.

   CMU alumni:

```text
Hi [Name]! I'm at CMU for my master's and applying for [Company]'s [Role] role. Would you be open to taking a look at my resume, and referring me if it seems like a fit? Kept it short out of respect for your time, but I'd love to chat more if you're open to it. Thanks!
```

   UW–Madison alumni:

```text
Hi [Name]! Fellow Badger, now at CMU for my master's, applying for [Company]'s [Role] role ([Job ID]). [Pitch] Any chance you'd refer me? Kept it short out of respect for your time, but I'd love to chat if you're open to it. Thanks!
```

   Non-alumni referral (someone on the team or in a similar role):

```text
Hi [Name]! I'm a CMU master's student applying for [Company]'s [Role] role ([Job ID]). [Pitch] I know we haven't met, but would you be open to referring me? Happy to send my resume. Thanks!
```

   Hiring manager, eng lead, or founder (no referral ask):

```text
Hi [Name]! I'm a CMU master's student and just applied for [Company]'s [Role] role ([Job ID]). [Pitch] [Why this team] I'd love to chat if you're open to it. Thanks!
```

   - Fill `[Company]`, `[Role]`, and `[Job ID]` from the JD. Leave `[Name]` as a placeholder.
   - `[Why this team]` is one short sentence on what draws him to the team, taken from what the JD says the team builds (for example, "Real-time payments at scale is the backend work I want to do."). Keep it under 70 characters. Do not invent team details the JD does not state.
   - `[Pitch]` default: "I was the main backend engineer on a 6K-install sports app." (inventory: primary backend author, ~6,000 installs). Swap in a different pitch only if it clearly fits the JD better and is no longer than the default. Describe what he built, not where: readers will not recognize NewsBreak or ZenAI, so do not name them.
   - Keep the voice casual and human. Do not add polished filler ("I'd be thrilled", "leverage", "passionate"). Keep the closing sentence as written; it frames the note around respecting their time.
   - Use the role's short form if the posting title is long, for example "SWE New Grad" instead of "Software Engineer, New College Grad - 2027". Keep it recognizable. `[Role]` is followed by the word "role", so do not end it with "role".
   - If the JD has no job ID, drop ` ([Job ID])`. Do not invent one.
   - LinkedIn notes have a hard 300-character limit. Check each note's length with a script, counting `[Name]` as 10 characters. Require 300 or less. The CMU note has no `[Pitch]` and no `[Job ID]`; its fixed text is 258 characters. With the default pitch, the fixed text is 265 (UW), 222 (non-alumni), and 183 (hiring manager, before `[Why this team]`) characters. So company + role get about 42 (CMU), and company + role + job ID get about 35, 78, and 117 minus the why sentence. If a note is over, cut in this order until it fits: shorten `[Role]`, shorten `[Why this team]`, remove ` Thanks!`, then shorten `[Pitch]`. Keep the job ID. Report each final count in the reply.

## Reply format

Every run ends with a reply in this shape. Put the essentials first; detailed resume reasoning stays in `selection.md`, not the reply.

````markdown
## <Company> — <Role short form> (<Job ID>)
Resume: [Lordphone_Wen_Resume.pdf](applications/<slug>/Lordphone_Wen_Resume.pdf) — 1 page, <unused height> pt unused
Tracker: row added (draft)

### Outreach
Call: <the call line from outreach.md>
Search: [CMU alumni](<link>) · [UW alumni](<link>) · [<keyword>](<link>)

**<Note type>** (<count> chars)<, optional if the call says so>
```text
<note>
```
(repeat for all four notes, recommended first)

### Flags
- <anything he should know: no job ID, sponsorship or citizenship language, weak fit, verification problem>
````

- Omit ` (<Job ID>)` in the heading when the JD has none.
- Omit the Flags section when there is nothing to flag.
- If a page-fill check failed or compilation is blocked, say so on the Resume line instead of claiming success.
