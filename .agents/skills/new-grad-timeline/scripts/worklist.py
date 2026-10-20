#!/usr/bin/env python3
"""Step 3: pick the companies for a research run and write timeline/data/worklist.json.

Reads timeline/data/merged.json (run merge.py first). Companies that already have a file in timeline/research/
are skipped unless --redo is given. Order is tier, then list order, then (more than 20 companies) regrouped into
balanced batches, the costliest first; see the batching block below.

  worklist.py [--status open,tracker_lead,unknown,...] [--source first-pass,tracker,api,none]
              [--tier 1-5] [--names "A|B|C"] [--limit 100] [--redo] [--blind]

--blind leaves out previous_result, so a second-opinion run (the top-tier check) researches without the last answer.

--source picks by where the current answer came from: first-pass (first-pass agents), tracker (tracker only),
api (job-board API check), research (timeline/research files; implies --redo), none.

Prints a summary and writes timeline/data/workflow_args.json, the `args` for the saved workflow
.claude/workflows/new-grad-research.js. Fill its "approval" field with his request, quoted, before running.
"""
import json, os, re, sys
from common import *


def source_kind(src):
    if src.startswith('first-party'):
        return 'research'
    if 'API' in src:
        return 'api'
    if src.startswith('tracker'):
        return 'tracker'
    if src == 'first-pass agent':
        return 'first-pass'
    return 'none'


def opt(name, default=None):
    if name in sys.argv:
        return sys.argv[sys.argv.index(name) + 1]
    return default


rows = json.load(open(f'{DATA}/merged.json'))
statuses = set(opt('--status', '').split(',')) - {''}
sources = set(opt('--source', '').split(',')) - {''}
tiers = opt('--tier')
if not tiers:
    lo, hi = 1, 11
elif '-' in tiers:
    lo, hi = map(int, tiers.split('-'))
else:
    lo = hi = int(tiers)
names = set(opt('--names', '').split('|')) - {''}
limit = int(opt('--limit', '100000'))
redo = '--redo' in sys.argv or 'research' in sources
done = {os.path.splitext(f)[0] for f in os.listdir(f'{TIMELINE}/research')} if os.path.isdir(f'{TIMELINE}/research') else set()

pick = []
for r in rows:
    if names and r['Company'] not in names:
        continue
    if statuses and r['Status'] not in statuses:
        continue
    if sources and source_kind(r['Source']) not in sources:
        continue
    if not lo <= r['Tier'] <= hi:
        continue
    if not redo and slug(r['Company']) in done:
        continue
    pick.append(r)
pick.sort(key=lambda r: r['Tier'])
pick = pick[:limit]

src = {}
if os.path.exists(f'{TIMELINE}/sources.csv'):
    import csv
    src = {x['Company']: x for x in csv.DictReader(open(f'{TIMELINE}/sources.csv'))}
# doubtful saved boards from check_sources.py; the research agent confirms or replaces each one
flags = json.load(open(f'{DATA}/source_flags.json')) if os.path.exists(f'{DATA}/source_flags.json') else {}
items = []
for r in pick:
    s = src.get(r['Company'], {})
    items.append({'name': r['Company'], 'tier': r['Tier'], 'slug': slug(r['Company']),
                  'jobs_spec': s.get('jobs.py spec') or None, 'jobs_page': s.get('Jobs page') or None,
                  'board_flag': flags.get(r['Company']),
                  'previous_result': None if '--blind' in sys.argv else
                  f"{r['Status']} ({r['Source'] or 'no source'}); {r['Notes'][:200]}",
                  'tracker_lead': r.get('Tracker lead') or None,
                  'tracker_last_cycle': r['Last year opened'] or None})
# Balance the batches so no agent is left running long after the rest (in one full search, two agents of 20 slow
# boards in a row ran 44-48 min while the median agent took 8). Each company's cost is its time from the last run
# (company_minutes.json, written by timing.py) or a guess. Heaviest first, each company goes to the cheapest batch
# that has room, so the slow ones spread one per batch, and light batches take more companies. Batches are written
# in a row, the costliest first, so the workflow starts them first. A rerun of a few companies keeps list order.
PER, MAX_PER = 20, 40
minutes = json.load(open(f'{DATA}/company_minutes.json')) if os.path.exists(f'{DATA}/company_minutes.json') else {}
boards = json.load(open(f'{DATA}/boards.json')) if os.path.exists(f'{DATA}/boards.json') else {}


def cost(x):
    if x['slug'] in minutes:
        return max(minutes[x['slug']]['minutes'], 0.3)
    jobs = max([b.get('n_jobs') or 0 for b in boards.get(x['name'], [])], default=0)
    # no API board means the browser; a big board takes paging; a flagged board needs a new one found
    return 0.3 + (0 if x['jobs_spec'] else 1.0) + min(jobs / 1000, 2) + (1 if x['board_flag'] else 0)


batch_sizes = None
if len(items) > PER:
    n = -(-len(items) // PER)
    bins = [[] for _ in range(n)]
    load = [0.0] * n
    for x in sorted(items, key=cost, reverse=True):
        i = min((i for i in range(n) if len(bins[i]) < MAX_PER), key=lambda i: load[i])
        bins[i].append(x)
        load[i] += cost(x)
    order = sorted(range(n), key=lambda i: -load[i])
    items = [x for i in order for x in bins[i]]
    batch_sizes = [len(bins[i]) for i in order]
    print(f'{n} batches, estimated minutes per batch {load[order[0]]:.0f} max, '
          f'{load[order[n // 2]]:.0f} median, {load[order[-1]]:.0f} min; sizes {min(batch_sizes)}-{max(batch_sizes)}; '
          f'{sum(1 for x in items if x["slug"] in minutes)} of {len(items)} costs measured')

json.dump(items, open(f'{DATA}/worklist.json', 'w'), indent=1)
# small enough to pass inline as the Workflow tool's args; agents read their companies from worklist.json
args = {'approval': 'FILL IN: his request, quoted', 'worklist': f'{DATA}/worklist.json', 'count': len(items)}
if batch_sizes:
    args['batch_sizes'] = batch_sizes
json.dump(args, open(f'{DATA}/workflow_args.json', 'w'), indent=1)
tiers_count = {}
for x in items:
    tiers_count[x['tier']] = tiers_count.get(x['tier'], 0) + 1
print(f'{len(items)} companies -> timeline/data/worklist.json; by tier {dict(sorted(tiers_count.items()))}; '
      f'{sum(1 for x in items if x["board_flag"])} with a board flag')
