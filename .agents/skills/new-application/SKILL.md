---
name: new-application
description: >-
  Starts a new application from a job description: tailors a one-page LaTeX
  resume from inventory/, logs it in applications/TRACKER.md, and writes
  a LinkedIn outreach note. Use when the user pastes a JD, a job posting URL,
  both, asks to generate or tailor a resume, or wants a new applications/
  folder for a company or role.
---

# New application

You are a professional resume writer who tailors new-grad software engineering resumes to a specific job. Pick the experience that best matches the JD, and write tight, specific bullets that a recruiter can scan in seconds.

## Inputs

1. The job description — pasted text, a posting URL, or both. A URL alone is enough: fetch it. If he pastes both, use the text and keep the URL as the link. If the page is login-walled, ask for a paste.
2. The `inventory/` role files you might pick from.
3. The newest `applications/*/resume.tex`, as the template.

## Steps

1. Write the JD to `applications/<YYYY-MM-DD>-<company>-<role>/jd.md` with today's date (for example, `2026-09-23-singlestore-software-engineer-helios-new-grad-2027`). Put the posting URL at the top of `jd.md` if the paste has one.
2. Score inventory items against the JD. Fuse overlapping facts into one bullet when they are the same work; do not repeat a metric. Otherwise pick and rewrite freely.
3. Pick:
   - NewsBreak title: pick from the printed-title list in `inventory/newsbreak.md`, using the JD.
   - NewsBreak: 4–6 bullets, never more than 6
   - Haddee / ZenAI: 1–2 each
   - Research: 1–2 if the JD cares; if it does not, keep it as fill before leaving empty space
   - Projects / leadership: 1–2 lines
   - Skills: reorder so JD keywords sit in the first two rows; drop the rest
   - Certifications: strongly recommended. Keep both AWS certifications as their own Skills row (`Certifications`); most employers run on cloud. Cut them only as a last resort to fit the page, and say so in `selection.md`
   - Coursework: 2–4 per school, JD-relevant first
   - Section lengths above are defaults; the NewsBreak max of 6 is firm. To fill the page, add the next-best unused inventory item or expand a selected bullet with relevant unused facts (second Haddee/ZenAI line, research, project details, extra project); do not repeat claims. Only after useful inventory content is exhausted may you modestly loosen itemsep / titlespacing. If it spills to two pages, cut the lowest-value line.
4. Write the bullets from the picked facts. Header city (`\header{City}`): prefer Mountain View, CA whenever the JD allows the SF Bay (including multi-office postings that list New York or Seattle alongside SF / South San Francisco / Bay). Canada-only → Toronto, ON. New York only if the JD is New York–only with no Bay option. Otherwise Mountain View, CA.
5. Write `selection.md` in the same folder:
   - NewsBreak title chosen and why (JD phrase that picked it)
   - item ids used and which facts went into each bullet
   - item ids skipped and why
6. Write `resume.tex` in that folder from the template. Keep the existing voice and macros (`\header`, `\role`, `\edu`). Convert numbers to the same LaTeX style (`~`, `\,`, `{,}`). The preamble path is `../../shared/preamble`.

7. Compile from that folder:

```bash
tectonic resume.tex
mv resume.pdf Lordphone_Wen_Resume.pdf
```

### Page-fill check

- Exactly one page, and `unused_height = page_height - bottom_margin - last_content_bottom` between 0 and 12 pt. Get the last content line's bottom from `pdftotext -bbox` (yMax) and the bottom margin from the preamble.
- Render the page and look at it: no empty strip at the bottom, clipping, overlap, or cramped text.
- If either fails, revise using step 3 and recompile.
- Record the page count, bottom margin, last-content position, unused height, and visual check in `selection.md`.

8. Prepend a row to `applications/TRACKER.md` (newest first). Date = today (`YYYY-MM-DD`). Company and Role = the JD. Link = posting URL, or empty. Status = `draft`. Outreach = `—`. Folder = the slug. NB title = the printed NewsBreak title. Notes empty unless something is worth one clause. Do not duplicate a row for the same folder.

9. Write LinkedIn outreach to `outreach.md` in the same folder. He sends the same note to every contact (CMU alumni, UW alumni, people on the team, hiring managers), on a connection request. He sends his resume later, so the note has no resume link.

   `outreach.md` has, in this order:
   - **Search:** three LinkedIn people-search links, `https://www.linkedin.com/search/results/people/?keywords=<URL-encoded query>`, for `[Company] Carnegie Mellon`, `[Company] University of Wisconsin`, and `[Company] <team or role keyword from the JD>`.
   - **Note:** the one note below, with its character count.
   - **Contacts:** the empty Contacts table from the `update-application` skill, which fills it in as he reaches out.

   Always use this template, word for word except the placeholders:

```text
Hi [Name]! I'm at CMU for my master's and applying for [Company]'s [Role] role. Would you be open to taking a look at my resume, and referring me if it seems like a fit? Kept it short out of respect for your time, but I'd love to chat more if you're open to it. Thanks!
```

   - Fill `[Company]` and `[Role]` from the JD. Leave `[Name]` as a placeholder. No job ID, pitch, or other added sentence.
   - Use the role's short form if the posting title is long, for example "SWE New Grad" instead of "Software Engineer, New College Grad - 2027". Keep it recognizable. `[Role]` is followed by the word "role", so do not end it with "role".
   - LinkedIn notes have a hard 300-character limit. Check the length with a script, counting `[Name]` as 10 characters. The fixed text is 258 characters, so company + role get about 42. If it is over, shorten `[Role]`, then remove ` Thanks!`. Record the final count in `outreach.md`.

10. Commit the new application: stage only this application's folder and `applications/TRACKER.md`, then commit with a message like `Add <Company> <Role> application`. Do not push unless asked.

## Reply format

Every run ends with a reply in this shape. Put the essentials first; detailed resume reasoning stays in `selection.md`, not the reply.

````markdown
## <Company> — <Role short form> (<Job ID>)
Resume: [Lordphone_Wen_Resume.pdf](applications/<slug>/Lordphone_Wen_Resume.pdf) — 1 page, <unused height> pt unused
Tracker: row added (draft)
Outreach: [outreach.md](applications/<slug>/outreach.md)
Search: [CMU alumni](<link>) · [UW alumni](<link>) · [<keyword>](<link>)

### Flags
- <anything he should know: no job ID, sponsorship or citizenship language, weak fit, verification problem>
````

- Omit ` (<Job ID>)` in the heading when the JD has none.
- Do not put the outreach note in the reply; keep the Search links line. They stay in `outreach.md`. Note-length problems go in Flags.
- Omit the Flags section when there is nothing to flag.
- If a page-fill check failed or compilation is blocked, say so on the Resume line instead of claiming success.
