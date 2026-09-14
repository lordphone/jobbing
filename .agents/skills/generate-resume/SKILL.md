---
name: generate-resume
description: >-
  Tailors a one-page LaTeX resume from inventory/ plus a job description.
  Use when the user pastes a JD, a job posting URL, both, asks to generate
  or tailor a resume, or wants a new applications/ folder for a company or role.
---

# Generate a resume

## Inputs

1. The job description — pasted text, a posting URL, or both. A URL alone is enough: fetch it. If the page is login-walled, ask for a paste instead of inventing a JD.
2. `inventory/` — source of truth. Read the role files you might pick from.
3. Layout: `shared/preamble.tex` plus the wrapper below. From `applications/<slug>/` the preamble path is `../../shared/preamble`. If an `applications/*/resume.tex` already exists, match its structure. Match the header in the current root `resume.tex` (name left, location right, contact centered).

## Steps

1. Write the JD to `applications/<YYYY-MM>-<company>-<role>/jd.md`. Use today's date. Put the posting URL at the top of `jd.md` if the paste has one.
2. Score inventory items against the JD. Fuse overlapping facts into one bullet when they are the same work; do not repeat a metric. Otherwise pick and rewrite freely.
3. Pick:
   - NewsBreak title: one of the printed titles in `inventory/newsbreak.md`, from the JD. Official on paper is Engineering Intern. Default print is Software Engineering Intern. iOS / Swift / SwiftUI JD → iOS Engineer Intern. Mobile JD that is not iOS-specific → Mobile Engineer Intern. Full-stack JD → Full-Stack Engineer Intern. Backend / API / services JD → Backend Engineer Intern. AI infra / ML infra / LLM platform / serving JD → AI Infrastructure Intern (print "AI Infra Intern" only if the JD says AI Infra). General infra / cloud / Kubernetes JD that is not AI infra → Infrastructure Engineer Intern. AI / ML / LLM / agents as product work → AI Engineer Intern. JD says intern or engineering intern and is not more specific → Engineering Intern. Print "SWE Intern" only if the JD itself says SWE. Do not invent a title.
   - NewsBreak: 3–4 bullets
   - Haddee / ZenAI: 1–2 each
   - Research: 1–2 if the JD cares; if it does not, keep it as fill before leaving empty space
   - Projects / leadership: 1–2 lines
   - Skills: reorder so JD keywords sit in the first two rows; drop the rest
   - Coursework: 2–4 per school, JD-relevant first
   - The page must be full. If the PDF has an empty strip at the bottom, add the next-best unused inventory item (second Haddee/ZenAI line, research, extra project). Do not invent facts. Loosen itemsep / titlespacing only after inventory is used. If it spills to two pages, cut the lowest-value line. Compile and look at the PDF — not just the page count.
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

8. Prepend a row to `applications/TRACKER.md` (newest first). Date = today (`YYYY-MM-DD`). Company and Role = the JD. Link = posting URL, or empty. Status = `draft`. Folder = the slug. NB title = the printed NewsBreak title. Notes empty unless something is worth one clause. Do not duplicate a row for the same folder.
