#!/usr/bin/env python3
"""Print the recent-postings table for the end-of-run reply: open postings he hasn't applied to, posted (or, with no
posted date, discovered) in the last few days, newest first. Reads timeline/postings.csv, so run it after merge.py.

  recent.py [--days 5] [--max-tier 4]
"""
import csv, os, sys, datetime as dt

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
arg = lambda name, default: int(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default
DAYS, MAX_TIER = arg('--days', 5), arg('--max-tier', 4)
since = (dt.date.today() - dt.timedelta(days=DAYS - 1)).isoformat()  # --days 5 on Oct 20: Oct 16 to Oct 20

when = lambda r: (r['Posted'] or r['Discovered'])[-10:]
rows = [r for r in csv.DictReader(open(f'{REPO}/timeline/postings.csv'))
        if not r['Applied'] and int(r['Tier']) <= MAX_TIER and when(r) >= since]
rows.sort(key=lambda r: (when(r), -int(r['Tier'])), reverse=True)  # newest first, then by tier


def day(v):
    if not v:
        return '—'
    d = dt.date.fromisoformat(v[-10:])
    return ('≤ ' if v.startswith('on or') else '') + f'{d:%b} {d.day}'


cell = lambda s: (s or '').replace('|', '/')
print(f'{len(rows)} postings since {day(since)}, tiers 1–{MAX_TIER}, not applied. Sorted by posted date, or '
      'discovered date when the posting shows none.\n')
print('| Posted | Discovered | Company | Role | Tier | Location | Deadline | Link |')
print('|---|---|---|---|---|---|---|---|')
for r in rows:
    print(f"| {day(r['Posted'])} | {day(r['Discovered'])} | {cell(r['Company'])} | {cell(r['Role'])} | {r['Tier']} | "
          f"{cell(r['Location']) or '—'} | {cell(r['Deadline']) or '—'} | [Apply]({r['Link']}) |")
