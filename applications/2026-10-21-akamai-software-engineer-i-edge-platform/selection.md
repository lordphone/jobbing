# Selection — Akamai, Software Engineer I (Edge Platform), Job 4237

## NewsBreak title
**Backend Engineer Intern**. The JD is backend systems: "high-reliability/high-throughput systems", "RDBMS and NoSQL databases", "scalable backend applications". He was the sole backend owner.

## Used
- **nb-fastapi-backend** `believable`: 89 REST endpoints, 7 CronJobs on EKS, ~1,450 offline tests in CI. Matches the "work with testing and SQA" and NoSQL (MongoDB) asks.
- **nb-catalog-cache** `default`: 25–30 requests → 1 call, per-user cache → shared 10.9 MB. Matches "optimizing existing functionality" and performance.
- **nb-eks-standup** `day3`: DNS → TLS → admission-policy chain. TLS is the closest fact to the team's certificate work.
- **nb-third-party-proxy** + **nb-dramabreak-stripe**: zero credentials in the binary, signature-verified webhook, idempotent fulfillment. Secure delivery and correctness under retries.
- **nb-cronjob-outage** + **nb-observability**: reliability and operations.
- **nb-llm-failure** `infra`, plus the Redis Streams fact: reliability debugging in a concurrent worker system.
- **hd-lead-mvp** + **hd-langchain-apis**: schemas and REST APIs. **hd-mentor-process** shortened to one line.
- **za-mock-interview** `with-auth` (PostgreSQL) + **za-demos-contracts** `contracts` with the recruiter fact.
- **cm-psc** `default`: research fill. It also says "safety certificate", but this is a different meaning from TLS certificates. It is here as fill only.
- **pj-cs537-os** `default`, rephrased: C pthreads, mutexes, condition variables, xv6 syscalls. Covers "tens of thousands of concurrent operations" (concurrency basics only, with no throughput claim) and Linux/Unix.
- **ld-ece-fellow**: fill.
- Coursework: CMU Distributed Systems, Foundations of SE, Software Refactoring. UW Operating Systems, Algorithms, Software Engineering, Computer Architecture.
- Skills: Java leads Languages (JD's first ask), then Python and Bash. The second row holds the JD's database and Terraform asks: PostgreSQL, MySQL, MongoDB, Terraform, Linux. Certifications kept.

## Skipped
- Spring / Spring Boot, Angular, C++, Oracle, SQL Server, Elasticsearch, Cassandra: not in inventory. Not added.
- nb-llm-pipeline, nb-agentic-search, nb-retired-detector, nb-morning-digest: LLM product work, less relevant to a certificate and configuration platform.
- nb-server-driven-ui, nb-app-store, nb-live-activities, nb-ads-max, nb-manual-broadcast, nb-dramabreak-ads, nb-coaching-marketplace, nb-swiftui-app: iOS and product.
- nb-ownership, nb-jira-process, nb-cross-dept: weaker than the systems lines.
- cm-nl-safety: an LLM line. PSC is the shorter fill.
- pj-codingplans: tried first. Cut for space; it is less relevant than the OS project.
- pj-my-av, pj-wisconsin-autonomous: ML and embedded.

## Page-fill check
- Draft 1: 2 pages (Projects spilled). Dropped codingplans, shortened the Haddee mentor line, and unwrapped two Skills rows (moved Kubernetes into the backend row and dropped Jenkins, Prometheus, and Grafana from Skills, since all three are in bullets). Result: 1 page, 33.7 pt unused.
- Final: added the ECE fellow line. 1 page. Bottom margin 0.36 in = 25.92 pt. Last content yMax 759.66 pt. Unused 792 − 25.92 − 759.66 = 6.42 pt.
- Rendered at 80 dpi: no empty strip, clipping, overlap, or cramped text. SportsBreak and DramaBreak are hyperlinked.
