#!/usr/bin/env python3
"""Compare the snapshot taken before a run with its results and write timeline/CHANGES.md.

  changes.py snapshot   # before the run: copy status.csv, postings.csv and COMPANY_LIST.md into timeline/data/prev/
  changes.py [--run "Top-tier search (tiers 1–3)"]   # after the run: write timeline/CHANGES.md (--run names the run)
"""
import csv, os, re, shutil, sys, datetime as dt

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
T = os.path.join(REPO, 'timeline')
PREV = os.path.join(T, 'data', 'prev')

RUN = sys.argv[sys.argv.index('--run') + 1] if '--run' in sys.argv else 'Full search'
if sys.argv[1:] == ['snapshot']:
    os.makedirs(PREV, exist_ok=True)
    shutil.copy(f'{T}/status.csv', f'{PREV}/status.csv')
    if os.path.exists(f'{T}/postings.csv'):
        shutil.copy(f'{T}/postings.csv', f'{PREV}/postings.csv')
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

# Postings: compare the open postings before and after, matched by link (a company can have several)
key = lambda r: r['Link'] or f"{r['Company']}|{r['Role']}"
title_key = lambda t: re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()
had_postings = os.path.exists(f'{PREV}/postings.csv')
read = lambda p: {key(r): r for r in csv.DictReader(open(p))} if os.path.exists(p) else {}
old_p, new_p = read(f'{PREV}/postings.csv'), read(f'{T}/postings.csv')
by_company = lambda r: (int(r['Tier']), r['Company'], r['Role'])
gone = {k: r for k, r in old_p.items() if k not in new_p}
fresh = {k: r for k, r in new_p.items() if k not in old_p}


def date_of(s):
    m = re.search(r'\d{4}-\d{2}-\d{2}', s or '')
    return m.group(0) if m else ''


def similar(a, b):
    a, b = set(title_key(a).split()), set(title_key(b).split())
    return len(a & b) / max(1, len(a | b)) >= 0.6


# Same job, new link: a gone posting and a fresh one at the same company. Same title → a repost. A similar title →
# a possible repost; the script can't tell, so it lists both links for him to judge.
reposts, maybe = [], []
for exact in (True, False):
    for ko, o in list(gone.items()):
        cands = [(kn, n) for kn, n in fresh.items() if n['Company'] == o['Company'] and
                 (title_key(n['Role']) == title_key(o['Role']) if exact else similar(n['Role'], o['Role']))]
        if not cands:
            continue
        kn, n = next(((kn, n) for kn, n in cands if n['Location'] == o['Location']), cands[0])
        (reposts if exact else maybe).append((o, n))
        del gone[ko], fresh[kn]

changed = []
for k, n in new_p.items():
    o = old_p.get(k)
    if not o:
        continue
    diffs = []
    if o['Deadline'] != n['Deadline']:
        od, nd = date_of(o['Deadline']), date_of(n['Deadline'])
        diffs.append(f"deadline {o['Deadline'] or 'none'} → {n['Deadline'] or 'none'}"
                     + (' **(earlier)**' if od and nd and nd < od else ''))
    for f in ('Role', 'Location'):
        if o[f] != n[f]:
            diffs.append(f"{f.lower()} {o[f] or 'none'} → {n[f] or 'none'}")
    if diffs:
        changed.append((n, '; '.join(diffs)))


def post(r, extra=''):
    s = f"- **{r['Company']}** (tier {r['Tier']}) · {r['Role'][:80]}" + (f" · {r['Location'][:80]}" if r['Location'] else '')
    return s + (f" · {r['Link']}" if r['Link'] else '') + extra


def tracker(r, label='in TRACKER.md'):
    return f" · **{label}: {r['Applied']}**" if r['Applied'] else ''


if had_postings:
    posting_sections = [
        ('New postings', [post(r, tracker(r)) for r in sorted(fresh.values(), key=by_company)]),
        ('Removed postings', [post(r, tracker(r) or ' · was in Apply now') for r in sorted(gone.values(), key=by_company)]),
        ('Changed postings', [post(n, f" · {d}") for n, d in sorted(changed, key=lambda x: by_company(x[0]))]),
        ('Reposted under a new link', [post(n, f" · was {o['Link']}" + tracker(o))
                                       for o, n in sorted(reposts, key=lambda x: by_company(x[1]))]),
        ('Possible reposts: check', [post(n, f" · maybe the same job as \"{o['Role'][:60]}\" · was {o['Link']}"
                                             + tracker(o, 'old one in TRACKER.md'))
                                     for o, n in sorted(maybe, key=lambda x: by_company(x[1]))]),
    ]
    posting_counts = (f'{len(fresh)} new, {len(gone)} removed, {len(changed)} changed, {len(reposts)} reposted, '
                      f'{len(maybe)} possible reposts')
else:
    posting_sections = [('Postings: no snapshot', ['No postings snapshot from the last run; compared from the next run on.'])]
    posting_counts = 'no postings snapshot'

out = [f'# Changes — {dt.date.today()} ({RUN})', '',
       f"Compared with the snapshot taken before this run. Open now: {sum(r['Status'] == 'open' for r in new.values())} "
       f"companies, {len(new_p)} postings.", '']
for title, items in [('Newly open', newly_open), ('No longer open', closed), ('Other status changes', other)] + \
        posting_sections + [('Added to the company list', [f'- {n}' for n in added]),
                            ('Removed from the company list', [f'- {n}' for n in removed])]:
    out += [f'## {title}' + ('' if title.endswith('no snapshot') else f' ({len(items)})'), ''] + (items or ['None.']) + ['']
notes = f'{T}/data/list_notes.md'  # one line per company-list edit, written by the list review step
if os.path.exists(notes) and os.path.getmtime(notes) >= os.path.getmtime(f'{PREV}/status.csv'):
    out += ['## Company list edits', '', open(notes).read().strip() or 'None.', '']
open(f'{T}/CHANGES.md', 'w').write('\n'.join(out))
print(f'timeline/CHANGES.md: {len(newly_open)} newly open, {len(closed)} no longer open, {len(other)} other | '
      f'postings: {posting_counts} | {len(added)} added, {len(removed)} removed')
