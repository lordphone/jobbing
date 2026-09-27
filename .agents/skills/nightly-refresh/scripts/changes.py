#!/usr/bin/env python3
"""Compare last night's snapshot with tonight's results and write timeline/CHANGES.md.

  changes.py snapshot   # before the run: copy status.csv and COMPANY_LIST.md into timeline/data/prev/
  changes.py            # after the run: write timeline/CHANGES.md
"""
import csv, os, re, shutil, sys, datetime as dt

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
T = os.path.join(REPO, 'timeline')
PREV = os.path.join(T, 'data', 'prev')

if sys.argv[1:] == ['snapshot']:
    os.makedirs(PREV, exist_ok=True)
    shutil.copy(f'{T}/status.csv', f'{PREV}/status.csv')
    shutil.copy(f'{T}/COMPANY_LIST.md', f'{PREV}/COMPANY_LIST.md')
    print('snapshot saved to timeline/data/prev/')
    sys.exit()


def rows(p):
    return {r['Company']: r for r in csv.DictReader(open(p))} if os.path.exists(p) else {}


def names(p):
    return {l[2:].strip() for l in open(p) if l.startswith('- ')} if os.path.exists(p) else set()


old, new = rows(f'{PREV}/status.csv'), rows(f'{T}/status.csv')
added, removed = sorted(names(f'{T}/COMPANY_LIST.md') - names(f'{PREV}/COMPANY_LIST.md')), \
    sorted(names(f'{PREV}/COMPANY_LIST.md') - names(f'{T}/COMPANY_LIST.md'))


def line(c, r, was=None):
    s = f"- **{c}** (tier {r['Tier']})"
    if was:
        s += f": {was} → {r['Status']}"
    if r.get('Role'):
        s += f" · {r['Role'][:80]}"
    if r.get('Link'):
        s += f" · {r['Link']}"
    return s


newly_open, closed, other = [], [], []
for c, r in sorted(new.items(), key=lambda x: (int(x[1]['Tier']), x[0])):
    o = old.get(c)
    if not o or o['Status'] == r['Status']:
        continue
    if r['Status'] == 'open':
        newly_open.append(line(c, r, o['Status']))
    elif o['Status'] == 'open':
        closed.append(line(c, r, o['Status']))
    else:
        other.append(line(c, r, o['Status']))

out = [f'# Changes — {dt.date.today()}', '',
       f"Compared with the snapshot taken before this run. Open now: {sum(r['Status'] == 'open' for r in new.values())}.", '']
for title, items in [('Newly open', newly_open), ('No longer open', closed), ('Other status changes', other),
                     ('Added to the company list', [f'- {n}' for n in added]),
                     ('Removed from the company list', [f'- {n}' for n in removed])]:
    out += [f'## {title} ({len(items)})', ''] + (items or ['None.']) + ['']
notes = f'{T}/data/list_notes.md'  # one line per company-list edit, written by the list review step
if os.path.exists(notes) and os.path.getmtime(notes) >= os.path.getmtime(f'{PREV}/status.csv'):
    out += ['## Company list edits', '', open(notes).read().strip() or 'None.', '']
open(f'{T}/CHANGES.md', 'w').write('\n'.join(out))
print(f'timeline/CHANGES.md: {len(newly_open)} newly open, {len(closed)} no longer open, {len(other)} other, '
      f'{len(added)} added, {len(removed)} removed')
