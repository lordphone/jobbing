#!/usr/bin/env python3
"""Step 3: pick the companies for a research run and write timeline/data/worklist.json.

Reads timeline/data/merged.json (run merge.py first). Companies that already have a file in timeline/research/
are skipped unless --redo is given. Order is tier, then list order.

  worklist.py [--status open,tracker_lead,unknown,...] [--source first-pass,tracker,api,none]
              [--tier 1-5] [--names "A|B|C"] [--limit 100] [--redo]

--source picks by where the current answer came from: first-pass (first-pass agents), tracker (tracker only),
api (job-board API check), research (timeline/research files; implies --redo), none.

Prints a summary and writes timeline/data/workflow_args.json, the `args` for the saved workflow
.claude/workflows/new-grad-research.js. Fill its "approval" field with his request, quoted, before running.
"""
import json, os, re, sys
from common import *


def slug(name):
    s = re.sub(r'\s*\(.*?\)', '', name.lower().replace('&', ' and '))
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', s)).strip('-')


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
items = []
for r in pick:
    s = src.get(r['Company'], {})
    items.append({'name': r['Company'], 'tier': r['Tier'], 'slug': slug(r['Company']),
                  'jobs_spec': s.get('jobs.py spec') or None, 'jobs_page': s.get('Jobs page') or None,
                  'previous_result': f"{r['Status']} ({r['Source'] or 'no source'}); {r['Notes'][:200]}",
                  'tracker_lead': r.get('Tracker lead') or None,
                  'tracker_last_cycle': r['Last year opened'] or None})
json.dump(items, open(f'{DATA}/worklist.json', 'w'), indent=1)
args = {'approval': 'FILL IN: his request, quoted', 'worklist': f'{DATA}/worklist.json',
        'companies': [[x['name'], i] for i, x in enumerate(items)]}
json.dump(args, open(f'{DATA}/workflow_args.json', 'w'), indent=1)
tiers_count = {}
for x in items:
    tiers_count[x['tier']] = tiers_count.get(x['tier'], 0) + 1
print(f'{len(items)} companies -> timeline/data/worklist.json; by tier {dict(sorted(tiers_count.items()))}')
print('Estimated cost on Sonnet: ~58K tokens per company =', f'~{len(items) * 58 / 1000:.1f}M tokens')
