#!/usr/bin/env python3
"""Re-check every posting this run's research dropped as gone, and put back the ones that are still live.

Run after the research workflow, before validate.py. For each company in timeline/data/worklist.json, it looks at the
research file's `dropped` entries whose reason starts with "gone" and asks the job board's API (jobs.py posting()).
If the API returns the posting as live, the agent was wrong (Bank of America's live Quantitative Engineer req was
dropped as "page doesn't exist"): the posting goes back into `postings` from the previous file
(timeline/data/prev/research/), the status becomes open if it wasn't, and evidence says so. Postings with no API,
failed lookups and "ruled out" drops are left alone.

Writes timeline/data/restored.json ({company: [url, ...]}) for changes.py.
  verify_dropped.py
"""
import json, os, concurrent.futures as cf
from common import *
from jobs import posting

PREV = f'{DATA}/prev/research'
work = json.load(open(f'{DATA}/worklist.json'))
todo = []  # (slug, dropped entry)
for x in work:
    f = f'{TIMELINE}/research/{x["slug"]}.json'
    try:
        d = json.load(open(f))
    except (OSError, ValueError):
        continue
    for e in d.get('dropped') or []:
        if isinstance(e, dict) and e.get('url') and str(e.get('reason', '')).lower().startswith('gone'):
            todo.append((x['slug'], e))

with cf.ThreadPoolExecutor(8) as ex:
    states = list(ex.map(lambda t: posting(t[1]['url']), todo))

restored, counts = {}, {}
for (slug, e), p in zip(todo, states):
    k = 'live' if isinstance(p, dict) else p
    counts[k] = counts.get(k, 0) + 1
    if k != 'live':
        continue
    f = f'{TIMELINE}/research/{slug}.json'
    d = json.load(open(f))
    old = json.load(open(f'{PREV}/{slug}.json')) if os.path.exists(f'{PREV}/{slug}.json') else {}
    back = next((q for q in old.get('postings') or [] if same_posting(q.get('url'), e['url'])), None)
    if d.get('status') == 'excluded':
        print(f'  {d["company"]}: {e["url"]} is live, but the company is excluded; left for the report')
        continue
    if not back:
        print(f'  {d["company"]}: {e["url"]} is live but not in the previous file; left for the report')
        continue
    d['postings'] = (d.get('postings') or []) + [{**back, 'live_verified': 'api'}]
    d['dropped'] = [x for x in d['dropped'] if x is not e]
    if d.get('status') != 'open':
        d['status'] = 'open'
    d['evidence'] = (d.get('evidence') or '') + f' verify_dropped: put back "{back.get("title")}", its API shows it live.'
    json.dump(d, open(f, 'w'), indent=2, ensure_ascii=False)
    restored.setdefault(d['company'], []).append(e['url'])

# keep this run's earlier restores (the main pass) when a rerun's check writes the file again
path, snap = f'{DATA}/restored.json', f'{DATA}/prev/status.csv'
if os.path.exists(path) and os.path.exists(snap) and os.path.getmtime(path) >= os.path.getmtime(snap):
    for c, us in json.load(open(path)).items():
        restored.setdefault(c, []).extend(u for u in us if u not in restored.get(c, []))
json.dump(restored, open(path, 'w'), indent=1)
print(f'checked {len(todo)} postings dropped as gone: {counts}; put back {sum(map(len, restored.values()))} '
      f'at {len(restored)} companies -> timeline/data/restored.json')
for c, us in restored.items():
    print(f'  {c}: {", ".join(us)}')
