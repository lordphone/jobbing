# Selection — Jane Street, Software Engineer (New York)

## NewsBreak title

**Software Engineering Intern** (default). The JD is a general "Software Engineer" posting ("design and build the systems and tools that run the firm") and does not say SWE, backend, or AI.

## Framing

The JD asks for "smart programmers who enjoy solving interesting problems", "how you think", and people "humble and unafraid to ask questions and admit mistakes". It names OCaml (statically typed) and Python. So the NewsBreak bullets lean on Python, typing/testing rigor (pyright, 99.7% annotation coverage), measurement-driven decisions, root-cause debugging, and owning a mistake (retiring my own detector). No OCaml or functional-programming claim: neither is in inventory.

Header: **New York, NY** — the posting is New York only, no Bay option.

## Items used

- **nb-fastapi-backend + nb-ownership + nb-eks-standup**: first commit → 89 endpoints, FastAPI / MongoDB, EKS, ~1,450 fully offline tests, ruff / pyright / pytest gate, 99.7% return-type annotation coverage ("99.7% typed"), 344 PRs authored.
- **nb-llm-pipeline** (`gate` variant): Kubernetes CronJob; hand-graded alerts, filler vs. real both 89–90, categorical gate, filler 34% → 4% by count.
- **nb-retired-detector**: 19 hours production data, 901 min p50 vs. 1.8 min, net −882 lines; "admit mistakes" fit.
- **nb-catalog-cache** (`redesign` + `default`): 13.2 MB per user → 10.9 MB shared, 78×, 512 MiB pod, 25–30 requests → 1 call.
- **nb-agentic-search** (`entities` + hybrid RRF): 0% → 100% P@1, 0.4 ms, 206 entities, rejected embeddings after measuring.
- **nb-llm-failure + nb-cronjob-outage**: 65% failure via Langfuse, p95 1,197 vs. 16,384; 5-day silent CronJob outage, paired deadlines.
- **nb-swiftui-app**: sole SwiftUI engineer, App Store link on "SportsBreak", ~6,000 installs, 1,119 peak DAU.
- **hd-lead-mvp + hd-mentor-process**, **hd-langchain-apis** (`default`, shortened).
- **za-mock-interview + za-auth-db**, **za-demos-contracts**.
- **pj-my-av**, **ld-ece-fellow**, **pj-wisconsin-autonomous**.
- Coursework: CMU Distributed Systems, Foundations of SE, ML, Software Refactoring; UW Algorithms, OS, Computer Architecture.
- Skills: Python first; Data & ML row second (JD: Python for data analysis and ML). Added pyright / ruff / pytest under Practices.

## Items skipped

- **cm-psc / cm-nl-safety**: JD does not ask for research; no room.
- **nb-live-activities**: first draft included the APNs-200 finding in the SwiftUI bullet; cut to fit one page.
- **nb-third-party-proxy, nb-server-driven-ui, nb-app-store, nb-ads-max, nb-morning-digest, nb-manual-broadcast, nb-dramabreak-*, nb-jira-process, nb-coaching-marketplace**: lower value for this JD.
- Dropped to fit: "production", 0.17 s, "(340 merged)", 4,100+ shadow decisions, UW Data Structure & Programming III, OpenCV, Langfuse in skills, the longer Haddee API wording.

## Constraints nearly violated

- First compile ran to two pages; trimmed wording rather than spacing.
- No OCaml / functional programming / open-source contributions in inventory, so none claimed.
- Template's `\setlist*[itemize]{itemsep=0.7pt}` unchanged; margins and font size unchanged.

## Verification (final PDF)

- Compiled fresh with tectonic → Lordphone_Wen_Resume.pdf.
- Page count: **1**, Letter, 792 pt.
- Bottom margin: 0.36 in = **25.92 pt**.
- Last content bottom (pdftotext -bbox yMax, "Jetson." line): **756.79 pt** from the top.
- Unused height: 792 − 25.92 − 756.79 = **9.29 pt** (passes the 0–12 pt check).
- Rendered the whole page at 90 dpi and inspected it: no clipping, overlap, cramped text, or empty bottom strip. CMU coursework wraps with "Refactoring" alone on its second line; kept, since cutting it would leave ~21 pt unused.

## Referral notes

Role shortened to "SWE". No job ID in the posting text. Default pitch. Why-this-team line uses the JD's "systems and tools that run the firm".
