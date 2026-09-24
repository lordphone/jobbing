---
name: new-application
description: >-
  Starts a new application from a job description: tailors a one-page LaTeX
  resume from inventory/, logs it in applications/TRACKER.md, and writes
  LinkedIn referral notes. Use when the user pastes a JD, a job posting URL,
  both, asks to generate or tailor a resume, or wants a new applications/
  folder for a company or role.
---

# New application

## Inputs

1. The job description — pasted text, a posting URL, or both. A URL alone is enough: fetch it. If the page is login-walled, ask for a paste instead of inventing a JD.
2. `inventory/` — source of truth. Read the role files you might pick from.
3. Layout: `shared/preamble.tex` plus the wrapper below. From `applications/<slug>/` the preamble path is `../../shared/preamble`. If an `applications/*/resume.tex` already exists, match its structure. Match the header in the current root `resume.tex` (name left, location right, contact centered).

## Steps

1. Write the JD to `applications/<YYYY-MM-DD>-<company>-<role>/jd.md`. Use today's full date, including the day, for every new application folder (for example, `2026-09-23-singlestore-software-engineer-helios-new-grad-2027`). Put the posting URL at the top of `jd.md` if the paste has one.
2. Score inventory items against the JD. Fuse overlapping facts into one bullet when they are the same work; do not repeat a metric. Otherwise pick and rewrite freely.
3. Pick:
   - NewsBreak title: one of the printed titles in `inventory/newsbreak.md`, from the JD. Official on paper is Engineering Intern. Default print is Software Engineering Intern. iOS / Swift / SwiftUI JD → iOS Engineer Intern. Mobile JD that is not iOS-specific → Mobile Engineer Intern. Full-stack JD → Full-Stack Engineer Intern. Backend / API / services JD → Backend Engineer Intern. AI infra / ML infra / LLM platform / serving JD → AI Infrastructure Intern (print "AI Infra Intern" only if the JD says AI Infra). General infra / cloud / Kubernetes JD that is not AI infra → Infrastructure Engineer Intern. AI / ML / LLM / agents as product work → AI Engineer Intern. JD says intern or engineering intern and is not more specific → Engineering Intern. Print "SWE Intern" only if the JD itself says SWE. Do not invent a title.
   - NewsBreak: 3–4 bullets
   - Haddee / ZenAI: 1–2 each
   - Research: 1–2 if the JD cares; if it does not, keep it as fill before leaving empty space
   - Projects / leadership: 1–2 lines
   - Skills: reorder so JD keywords sit in the first two rows; drop the rest
   - Coursework: 2–4 per school, JD-relevant first
   - The page must be full. An empty strip at the bottom is a failed draft, even when the PDF is one page. Add the next-best unused inventory item or expand a selected bullet with relevant unused facts (second Haddee/ZenAI line, research, project details, extra project). Do not invent facts or repeat claims. Treat the section-length targets above as defaults, not a reason to leave usable space empty. Only after useful inventory content is exhausted may you modestly loosen itemsep / titlespacing. Preserve the shared margins and font size; do not use blank lines, manual vertical padding, or stretched spacing to disguise missing content. If it spills to two pages, cut the lowest-value line and check again.
4. Write 1–2 (or 3–4 for NewsBreak) bullets from the picked facts. `approved` lines are a starting point; new sentences and real fusions are fine. Every printed claim maps to inventory facts. Header is the contact block in `profile.md`. Header city: prefer Mountain View, CA whenever the JD allows the SF Bay (including multi-office postings that list New York or Seattle alongside SF / South San Francisco / Bay). Canada-only → Toronto, ON. New York only if the JD is New York–only with no Bay option. Otherwise Mountain View, CA.
5. Write `selection.md` in the same folder:
   - NewsBreak title chosen and why (JD phrase that picked it)
   - item ids used and which facts went into each bullet
   - item ids skipped and why
   - any constraint you almost violated
6. Write `resume.tex` in that folder. Keep the existing voice and macros (`\role`, `\edu`). Convert numbers to the same LaTeX style (`~`, `\,`, `{,}`). Wrapper:

```latex
\documentclass[11pt, letterpaper]{article}
\input{../../shared/preamble}

\begin{document}

\begin{center}
  {\LARGE\bfseries Name}\\[2pt]
  Location \ $\cdot$ \ email \ $\cdot$ \ phone\\[1pt]
  linkedin \ $\cdot$ \ github
\end{center}

\section{Education}
% \edu{School}{Degree \ $|$ \ GPA: x / 4.0}{Dates}{}
% Selected Coursework: ...\\[1pt]

\section{Work Experience}
% \role{Company}{Title}{Dates}{Location}
% \begin{itemize}...\end{itemize}

\section{Research Experience}
% omit if the JD does not care and space is tight

\section{Skills}
\begin{tabularx}{\textwidth}{@{}l @{\hspace{7pt}} >{\raggedright\arraybackslash}X@{}}
  \textbf{Languages} & ... \\[1pt]
  \textbf{Frameworks \& Tools} & ... \\[1pt]
  \textbf{Data \& ML} & ... \\[1pt]
  \textbf{Cloud \& DevOps} & ... \\[1pt]
  \textbf{Practices} & ... \\[1pt]
  \textbf{Certifications} & ... \\
\end{tabularx}

\section{Leadership \& Activities}
\begin{itemize}
  \item ...
\end{itemize}

\end{document}
```

7. Compile from that folder:

```bash
tectonic resume.tex
mv resume.pdf Lordphone_Wen_Resume.pdf
```

The deliverable PDF is always `Lordphone_Wen_Resume.pdf`. Keep `resume.tex` as the source. If the preamble `\input` path is wrong, fix the path, do not copy the preamble.

### Required page-fill verification before delivery

- Verify the newly compiled deliverable, not a stale PDF from an earlier successful build. A failed compile does not permit delivery of the old PDF as the revision.
- Require exactly one page. Measure the bottom of the last visible content line using PDF text bounding boxes (for example, pdfplumber or PyMuPDF). With coordinates measured from the top, compute `unused_height = page_height - configured_bottom_margin - last_content_bottom`, in points. Require `0 <= unused_height <= 12 pt`. The current shared bottom margin is 0.36 in = 25.92 pt; read the preamble for the actual value. The normal bottom margin is intentional; extra blank space above it is what this check limits.
- Render and inspect the entire final page at a readable resolution. Require no obvious empty bottom strip, clipping, overlap, or cramped text. Passing the numeric check does not override a visible defect, and visual inspection does not replace the measurement.
- If either check fails, revise using the inventory-first rule in step 3, recompile, and repeat both checks. Do not call the resume complete or claim it fills the page while a check fails. If compilation or verification is blocked, report the unresolved check instead of claiming success.
- Record the final page count, bottom margin, last-content position, unused height, and visual-review result in `selection.md`. These measurements must describe the final PDF after the last edit.

8. Prepend a row to `applications/TRACKER.md` (newest first). Date = today (`YYYY-MM-DD`). Company and Role = the JD. Link = posting URL, or empty. Status = `draft`. Folder = the slug. NB title = the printed NewsBreak title. Notes empty unless something is worth one clause. Do not duplicate a row for the same folder.

9. Write LinkedIn referral notes to `outreach.md` in the same folder, and paste them in the reply as two copyable `text` code blocks, one for CMU alumni and one for UW–Madison alumni. Templates:

```text
Hi [Name], CMU MSSE student here (ex-NewsBreak, ZenAI backend). I'm applying for [Role] ([Job ID]) at [Company]. Would you be open to referring me? Resume: [link]. Kept this short to respect your time, but I'd love to chat if you're open to it. Thanks!
```

```text
Hi [Name], fellow Badger, now doing my MSSE at CMU (ex-NewsBreak, ZenAI backend). Applying for [Role] ([Job ID]) at [Company]. Would you be open to referring me? Resume: [link]. Kept this short to respect your time, but happy to chat if you're open to it. Thanks!
```

   - Fill `[Role]`, `[Job ID]`, and `[Company]` from the JD. Leave `[Name]` and `[link]` as placeholders.
   - Use the role's short form if the posting title is long, for example "Backend SWE, New Grad" instead of the full posting title. Keep it recognizable.
   - If the JD has no job ID, drop ` ([Job ID])`. Do not invent one.
   - Keep the note framed around respecting their time. Do not reword the last sentence so it sounds like he is avoiding a call.
   - LinkedIn notes have a hard 300-character limit. Check each note's length with a script, counting `[Name]` as 10 characters and `[link]` as 23. Require 300 or less. If a note is over, cut in this order until it fits: shorten `[Role]`, remove ` (ex-NewsBreak, ZenAI backend)`, then remove ` Resume: [link].` Report each final count in the reply.
