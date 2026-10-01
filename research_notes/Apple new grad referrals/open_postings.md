# Open Apple New-Grad / Early-Career SWE Postings (US), as of 2026-09-29

Method: I pulled the full US index on jobs.apple.com (4,503 location rows, 3,408 unique role numbers). The search page embeds its results as JSON, so all 239 pages could be read directly. I then loaded the detail page for every non-senior engineer, developer or scientist role (1,839 roles). Each detail page gives Apple's internal level (`highJobTitle`, e.g. "Software Engineering Applications ICT2"), the minimum qualifications, the posting date and the pay band. Every role number below came back as a live detail page on jobs.apple.com on 2026-09-29. For contrast, the closed 2025 posting 200611793 now returns "no longer available". "Verified live" here means the posting is in Apple's current search index and its detail page loads. I did not click through to the Submit Resume flow.

## 1. Which postings are open now for 0-2 years of experience / new grads?

### Takeaway
Apple has no postings titled "new grad" or "university graduate". Exact-phrase searches for "new grad", "university graduate", "recent graduate(s)", "new graduate" and "graduating" all return 0 US results. Early-career SWE demand shows up in two ways. The first is a small set of titles marked "IS&T Early Career", currently 2 in Austin. The second is roles leveled ICT2 (Apple's entry level) or roles that ask for "0 years" or "0-2 years" of experience. I found about 20 software-flavored roles of this kind; the full ICT2 list has 128 roles, but most are silicon or hardware.

### Cited Findings

**A. Explicitly early-career SWE (best fit, IS&T org, Austin)**
| Role # | Title | Level | Location | Posted | Notes |
|---|---|---|---|---|---|
| 200677645 | Software Engineer - AiDP Reliability Engineering, IS&T, Early Career Opportunities | Software Engineering Applications ICT2 | Austin, TX | 2026-08-12 | Min quals: BS CS/CE, Python/Java/Go, OS/networking/security basics, "Relevant Internship experience". ML/big-data/platform reliability. — [posting](https://jobs.apple.com/en-us/details/200677645/software-engineer-aidp-reliability-engineering-is-t-early-career-opportunities) |
| 200676168 | Frontend Engineer, EE&P - IS&T Early Career | Software Engineering Applications ICT2 | Austin, TX | 2026-08-10 | Min quals: Java/Python server-side, JS/HTML/CSS, or iOS; CS fundamentals; BS. Mentions the IS&T "Early Career community". — [posting](https://jobs.apple.com/en-us/details/200676168/frontend-engineer-ee-p-is-t-early-career) |

Neither posting names a graduation class year. Texas postings show no pay band.

**B. ICT2 software / SDET / ML / data roles (entry level by Apple's own leveling)**
| Role # | Title | Level | Location | Posted | Key min qual / pay |
|---|---|---|---|---|---|
| 200686221 | Safety & Contextual Algorithms Validation Engineer, Sensing & Connectivity | SDET ICT2 | Cupertino | 2026-09-28 | BS/MS CS/EE/ME; Python/Matlab; AI model validation. $129,300–$194,700 — [posting](https://jobs.apple.com/en-us/details/200686221/safety-contextual-algorithms-validation-engineer-sensing-connectivity) |
| 200686216 | Safety & Contextual Algorithms Validation Engineer, Sensing & Connectivity (2nd req) | SDET ICT2 | Cupertino | 2026-09-28 | same — [posting](https://jobs.apple.com/en-us/details/200686216/safety-contextual-algorithms-validation-engineer-sensing-connectivity) |
| 200685871 | CAD Engineer - Signoff Infrastructure | Software Development Engineering ICT2 | Austin; San Jose | 2026-09-25 | "BS in Computer Science"; Python or JS/TS. $129,300–$194,700 — [posting](https://jobs.apple.com/en-us/details/200685871/cad-engineer-signoff-infrastructure) |
| 200684964 | Data Engineer, Apple Ads | Software Development Engineering ICT2 | Cupertino | 2026-09-22 | "Minimum 1+ years" cloud data engineering. $129,300–$194,700 — [posting](https://jobs.apple.com/en-us/details/200684964/data-engineer-apple-ads) |
| 200680151 | Graphics Verification Software Engineer | Silicon Prototype Eng ICT2 | Austin | 2026-08-26 | BS; C/C++/Python; HW verification — [posting](https://jobs.apple.com/en-us/details/200680151/graphics-verification-software-engineer) |
| 200678150 | Quality Engineer | SDET ICT2 | San Diego | 2026-08-21 | BS CS/CE/EE only. $122,700–$184,800 — [posting](https://jobs.apple.com/en-us/details/200678150/quality-engineer) |
| 200665258 | Software Quality Engineer | SDET ICT2 | Sunnyvale | 2026-08-07 | BS; Python + ObjC/Swift/Java; UI testing. $129,300–$194,700 — [posting](https://jobs.apple.com/en-us/details/200665258/software-quality-engineer) |
| 200673967 | Database Systems Engineer | Software Engineering Applications ICT2 | Austin | 2026-07-23 | Scripting, Oracle/NoSQL, Git — [posting](https://jobs.apple.com/en-us/details/200673967/database-systems-engineer) |
| 200673991 | SRE Software Engineer | Software Engineering Applications ICT2 | Austin | 2026-07-23 | Linux admin, Python/Go — [posting](https://jobs.apple.com/en-us/details/200673991/sre-software-engineer) |
| 200673652 | Big Data Systems Engineer | Software Engineering Applications ICT2 | Austin | 2026-07-23 | Linux admin, Bash — [posting](https://jobs.apple.com/en-us/details/200673652/big-data-systems-engineer) |
| 200669452 | Graphics Software Content Engineer | Perf & Modeling ICT2 | Orlando | 2026-06-23 | "B.S. degree and 0 years of experience"; C/C++, Metal/Vulkan/CUDA — [posting](https://jobs.apple.com/en-us/details/200669452/graphics-software-content-engineer) |
| 200667874 | FE RTL Infrastructure - CAD Engineer | Software Development Engineering ICT2 | Beaverton; Cupertino | 2026-06-11 | BS; Python/Perl; Verilog — [posting](https://jobs.apple.com/en-us/details/200667874/fe-rtl-infrastructure-cad-engineer) |
| 200660621 | Silicon Validation Software Engineer - GPU IP Validation and Integration | Software Development Engineering ICT2 | Cupertino | 2026-04-28 | BS EE/CE — [posting](https://jobs.apple.com/en-us/details/200660621/silicon-validation-software-engineer-gpu-ip-validation-and-integration) |
| 200657285 | SoC Systems Software Engineer | Silicon Test Engineer ICT2 | Cupertino | 2026-04-10 | "Bachelor's degree". $123,700–$186,900 — [posting](https://jobs.apple.com/en-us/details/200657285/soc-systems-software-engineer) |
| 200656978 | SoC Firmware Engineer | SDE - Firmware ICT2 | Cupertino | 2026-04-09 | "Minimum of BS + 0 years relevant industry experience". $129,300–$194,700 — [posting](https://jobs.apple.com/en-us/details/200656978/soc-firmware-engineer) |
| 200652693 | Machine Learning Video Processing Engineer | Machine Learning ICT2 | Cupertino | 2026-03-20 | BS; PyTorch/TF; video/CV — [posting](https://jobs.apple.com/en-us/details/200652693/machine-learning-video-processing-engineer) |
| 200632595 | Silicon Validation Software Engineer - IO and Thermal Control Validation | Software Development Engineering ICT2 | Cupertino | 2025-11-17 | "Minimum BS Degree" (old req, still live) — [posting](https://jobs.apple.com/en-us/details/200632595/silicon-validation-software-engineer-io-and-thermal-control-validation) |
| 200621483 | Camera Simulation Software Engineer | Software Development Engineering ICT2 | San Diego | 2025-09-17 | BS CS; Python, React, C++/GPU (old req, still live) — [posting](https://jobs.apple.com/en-us/details/200621483/camera-simulation-software-engineer) |
| 200584872 | Machine Learning Video Processing Engineer | Software Engineering Systems ICT2 | Cupertino | 2024-12-23 | MS required (very old req, still live) — [posting](https://jobs.apple.com/en-us/details/200584872/machine-learning-video-processing-engineer) |

**C. ICT3 (or unleveled) SWE roles that still accept 0-2 years of experience**
| Role # | Title | Level | Location | Posted | Key min qual / pay |
|---|---|---|---|---|---|
| 200683808 | Systems Software Engineer | Software Engineering Systems ICT3 | San Diego | 2026-09-15 | "BS in CS/CE/EE and 0-2+ years"; C++/ObjC/Swift; drivers. $122,700–$214,300 — [posting](https://jobs.apple.com/en-us/details/200683808/systems-software-engineer) |
| 200657382 | Cellular Power Optimization Software Engineer, Wireless Technologies & Ecosystems | Software Engineering Systems ICT3 | San Diego | 2026-07-30 | "0-2 years" SWE; C/C++, Python. $122,700–$214,300 — [posting](https://jobs.apple.com/en-us/details/200657382/cellular-power-optimization-software-engineer-wireless-technologies-ecosystems) |
| 200662330 | Darwin Runtime Engineer, Core OS | (level not shown) | Cupertino | 2026-08-20 | "0-3+ years" low-level systems, C, UNIX — [posting](https://jobs.apple.com/en-us/details/200662330/darwin-runtime-engineer-core-os) |
| 200682437 | Software Quality Engineer - Media | Tools & Automation ICT3 | San Diego | 2026-09-10 | "1+ years" — [posting](https://jobs.apple.com/en-us/details/200682437/software-quality-engineer-media) |
| 200681256 | Software Engineer, Commerce Segments and Platform, ASE | Software Engineering Applications ICT3 | Cupertino | 2026-09-01 | "1+ years" — [posting](https://jobs.apple.com/en-us/details/200681256/software-engineer-commerce-segments-and-platform-ase) |

**D. Not SWE, but a large entry-level ICT2 silicon pool.** About 100 ICT2 hardware roles are open: CPU/GPU design verification, physical design, DFT, silicon validation and CAD. They are in Santa Clara, Austin, Cupertino, Beaverton, San Jose, Orlando, Waltham, Seattle and San Diego. Many of these list "0 years" of experience, e.g. [PLL Design Engineer 200658806](https://jobs.apple.com/en-us/details/200658806/pll-design-engineer) ("BSEE with 0 years"). These are relevant only if the candidate has an RTL/verification background.

**E. Students-team postings.** They are all internships (e.g. "Software Undergrad Engineering Internships" 200664785, "Software Engineering Masters Internships" 200664320, posted 2026-05-21) or retail roles. There is also "Applied Data Solutions Program, Internships – Summer 2027" (200673612, Austin/Cupertino, 2026-08-27). The Students team has no full-time new-grad program posting. — [jobs.apple.com search](https://jobs.apple.com/en-us/search?location=united-states-USA)

### Inferences
- By title and explicit early-career framing, the two Austin IS&T "Early Career" roles (200677645, 200676168) fit a 2026/2027 new grad best. After those, the fits are SDET/SWE ICT2 roles in Cupertino/Sunnyvale (200686221/216, 200665258), the 0-2-year San Diego systems roles (200683808, 200657382) and CAD Signoff Infrastructure (200685871, which asks only for a BS CS plus Python/JS).
- Apple's two big SWE orgs, "Software and Services" and "Machine Learning and AI", post almost all their SWE roles at ICT3 and above. Only the IS&T and Apple Ads subgroups of Software and Services currently show ICT2 postings. The ICT2 list leans heavily toward Hardware Technologies.
- No Seattle or NYC SWE ICT2 role is open. The only NYC entry-adjacent role is Data Engineer, Apple Ads 200681997, which is ICT3 and asks for "1+ years".

### Gaps
- I did not click into each posting's application flow to confirm "Submit Resume" is active. "Live" means indexed in search and the detail page loads.
- Roles with non-engineer titles (e.g., "Analyst", "Specialist") were not checked for ICT2 level. Postings whose `highJobTitle` was blank (44) could not be leveled.
- None of the open postings names a class year (2026 or 2027). Whether they target December 2026 or May 2027 graduates is unknown.

## 2. Which teams/orgs and locations?

### Takeaway
Early-career SWE openings are concentrated in IS&T and infrastructure (Austin), Hardware Technologies' software, CAD and validation teams (Cupertino, Austin, San Jose, Beaverton, Santa Clara), Wireless and Sensing & Connectivity (Cupertino, San Diego) and Apple Ads (Cupertino). See the tables above; all data is from [jobs.apple.com](https://jobs.apple.com/en-us/search?location=united-states-USA).

### Cited Findings
- Austin: both IS&T Early Career roles plus the Database, SRE and Big Data ICT2 roles.
- Cupertino/Sunnyvale: SDET, SoC firmware, ML video and silicon-validation SW roles.
- San Diego: Quality Engineer, Camera Simulation SWE and 0-2-year systems/cellular SW roles.
- Orlando: Graphics Software Content Engineer.

### Inferences
- If the candidate is location-flexible, Austin IS&T is the most explicitly new-grad-friendly pipeline.

### Gaps
- There are no open ICT2 SWE roles in Seattle or NYC, so I could not characterize those orgs.

## 3. Formal program vs team-by-team, and timeline

### Takeaway
Apple has no formal new-grad rotation or program. New grads are hired team by team into ICT2 (sometimes ICT3) reqs. The IS&T "Early Career" label, with its "Early Career community", is the closest thing to a program. The students page offers internships only, and interns can convert to full-time.

### Cited Findings
- The students page describes internships and co-ops for enrolled students and has no recent-grad program. It links to the internship search `team=Internships-STDNT-INTRN`. — [Apple Students](https://www.apple.com/careers/us/students.html)
- IS&T Early Career postings mention an "Early Career community" with educational and social events. — [200676168](https://jobs.apple.com/en-us/details/200676168/frontend-engineer-ee-p-is-t-early-career)
- A 2025/2026-cycle IS&T Early Career posting (aggregator copy) listed "0-2 years" of experience and "graduating in the year 2025 or 2026", with pay of $121,900–$183,600. Its team list included Enterprise Technology Services, Global Business Intelligence, SAP, Retail Engineering, Infrastructure Services and Corporate Systems Engineering. — [AnitaB mirror](https://jobs.anitab.org/companies/apple/jobs/89662346-software-engineer-is-t-early-career-opportunities) (secondary source; not re-verified on Apple)
- A third-party guide says new grads join as ICT2 and that Apple "hires through individual teams rather than a highly centralized engineering process". It adds that reqs "post on a rolling, team-by-team basis starting in the fall" and that the process takes 4–7 weeks. — [Simplify guide](https://simplify.jobs/blog/apple-new-grad-software-engineer-2027) (no sources cited; treat as anecdotal)
- Candidate reports describe varying loops: a hiring-manager screen, a LeetCode-medium technical screen, then a 5–6 round onsite. — [search summary of Glassdoor/LeetCode reports](https://static.glassdoor.nl/Interview/Apple-Interview-E1138-RVW5671850.htm) (anecdotal)
- The ICT2 pay band on current postings is $129,300–$194,700 base in the Bay Area and $122,700–$184,800 in San Diego. The ICT3 bands are $129,300–$225,300 (Cupertino) and $122,700–$214,300 (San Diego). — postings above.

### Inferences
- Timeline: last cycle's IS&T early-career SWE posting (200611793) was first seen on 2025-07-05, per repo history, and is now closed. This cycle's IS&T early-career postings went up on 2026-08-10 and 2026-08-12. That suggests IS&T posts early-career reqs in mid-summer, and the rest of Apple posts ICT2 reqs year-round as teams need them.

### Gaps
- I did not read Reddit or Blind threads directly within the tool budget. The process details above come from secondary summaries.

## 4. Comparison with repo file timeline/research/apple.json (checked 2026-09-28)

### Takeaway
The prior file lists one posting, 200657382 (Cellular Power Optimization SWE, San Diego, posted 2026-07-30). That posting is still live and unchanged. The prior research missed the two explicit IS&T Early Career postings and the ICT2 SWE/SDET roles.

### Cited Findings
- 200657382 is still live, leveled ICT3, and asks for "0-2 years". — [posting](https://jobs.apple.com/en-us/details/200657382/cellular-power-optimization-software-engineer-wireless-technologies-ecosystems)
- The prior `last_cycle_basis` posting 200611793 now shows "no longer available". — [URL](https://jobs.apple.com/en-us/details/200611793/software-engineer-is-t-early-career)
- New since the prior file: 200677645 and 200676168, both explicitly "IS&T Early Career" and ICT2, posted Aug 2026. Also 200683808 (0-2 years, San Diego, posted 2026-09-15) and 200686221/200686216 (ICT2, posted 2026-09-28).

### Inferences
- The prior file's evidence line, "Apple has no labeled 2027 new-grad program", still holds. However, "IS&T Early Career" postings do exist and should be recorded as the most direct new-grad reqs.

### Gaps
- None.
