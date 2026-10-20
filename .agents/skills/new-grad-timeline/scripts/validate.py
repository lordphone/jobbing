#!/usr/bin/env python3
"""Check this run's research files and write timeline/data/validation.json.

Run after the research workflow (and after verify_dropped.py). Checks the companies in timeline/data/worklist.json,
or every company on the list with --all.

Errors mean the company's research has to be rerun: no file, not written during this run (newer than the snapshot
and dated between the snapshot's day and today, so a run that crosses midnight is fine), a status or field outside the skill's
format, an open posting nobody opened, a flagged board with no jobs_spec_basis, or a posting from the previous file
(timeline/data/prev/research/, saved by changes.py snapshot) left out with no `dropped` entry.
Warnings go in the report only: deadline, opened or location values outside the skill's format, and an opened date
later than one an earlier run recorded for the same link (timeline/data/first_seen.json; merge.py keeps the earlier).

Prints the companies with errors as a --names string for worklist.py. Results for companies outside this check are
kept from an earlier check in the same run, so a rerun's check adds to the first one.
  validate.py [--all]
"""
import glob, json, os, re, sys
from common import *

STATUSES = {'open', 'not_yet', 'closed', 'leftover_2026', 'no_program_found', 'excluded', 'unknown'}
DATE = r'\d{4}-\d{2}-\d{2}'
# a title naming a level above entry ("Software Engineer II", "Senior Associate") with no entry-level word beside it;
# "Member of Technical Staff" and MTS are entry level (What counts), so Staff after Technical / Assistant is fine
HIGHER = re.compile(r'\b(II|III|IV|Senior|Sr\.?|Lead|Principal|Manager)\b|(?<!Technical )(?<!Assistant )\bStaff\b(?!/Analyst)')
ENTRY = re.compile(r'\b(I|1|Entry|Junior|Jr\.?|New Grad|Graduate|Grad|Campus|Early Career|University|Associate|20\d\d)\b(?![- ]?Senior)', re.I)
PREV = f'{DATA}/prev/research'
SNAP = f'{DATA}/prev/status.csv'  # changes.py snapshot: the run's start
START = os.path.getmtime(SNAP) if os.path.exists(SNAP) else 0
START_DAY = dt.date.fromtimestamp(START).isoformat() if START else TODAY.isoformat()

files = {}
for f in glob.glob(f'{TIMELINE}/research/*.json'):
    try:
        files[os.path.splitext(os.path.basename(f))[0]] = json.load(open(f))
    except ValueError as e:
        files[os.path.splitext(os.path.basename(f))[0]] = e
flags = json.load(open(f'{DATA}/source_flags.json')) if os.path.exists(f'{DATA}/source_flags.json') else {}
if '--all' in sys.argv:
    scope = [(c['name'], slug(c['name'])) for c in load_companies()]
else:
    scope = [(x['name'], x['slug']) for x in json.load(open(f'{DATA}/worklist.json'))]
tier_of = {c['name']: c['tier'] for c in load_companies()}
first_seen = json.load(open(SEEN_PATH)) if os.path.exists(SEEN_PATH) else {}


def text(v):
    return isinstance(v, str) and v.strip() not in ('', '{}', '[]', 'null')


def check(name, slug):
    errors, warnings = [], []
    d = files.get(slug)
    if d is None:
        return [f'no file timeline/research/{slug}.json'], []
    if isinstance(d, Exception):
        return [f'not valid JSON ({str(d)[:60]})'], []
    if d.get('company') != name:
        errors.append(f'company is {d.get("company")!r}, not the list name')
    if not START_DAY <= str(d.get('checked')) <= TODAY.isoformat() or \
            os.path.getmtime(f'{TIMELINE}/research/{slug}.json') < START:
        errors.append(f'not written in this run (checked {d.get("checked")}; the run started {START_DAY})')
    if d.get('tier') != tier_of.get(name):
        errors.append(f'tier is {d.get("tier")}, the list says {tier_of.get(name)}')
    status = d.get('status')
    if status not in STATUSES:
        errors.append(f'status {status!r} is not one of the skill\'s statuses')
    for k in ('evidence', 'jobs_page'):
        if not text(d.get(k)):
            errors.append(f'{k} is empty or not text: {str(d.get(k))[:40]!r}')
    if status == 'excluded' and not text(d.get('excluded_reason')):
        errors.append('excluded with no excluded_reason')
    if name in flags and not text(d.get('jobs_spec_basis')):
        errors.append('its board was flagged but jobs_spec_basis is missing')
    posts = d.get('postings')
    if not isinstance(posts, list):
        errors.append('postings is not a list')
        posts = []
    if status == 'open' and not posts:
        errors.append('open with no postings')
    for p in posts:
        if not isinstance(p, dict) or not text(p.get('title')) or not text(p.get('url')):
            errors.append(f'a posting has no title or url: {str(p)[:60]}')
            continue
        t = p['title'][:50]
        if p.get('live_verified') not in ('api', 'browser', 'no'):
            errors.append(f'"{t}": live_verified {p.get("live_verified")!r}')
        elif status == 'open' and p['live_verified'] == 'no':
            errors.append(f'"{t}": open but live_verified is "no" (open means you opened the posting)')
        if p.get('level') not in ('new-grad title', 'unlabeled'):
            errors.append(f'"{t}": level {p.get("level")!r}')
        elif p['level'] == 'unlabeled' and not text(p.get('level_basis')):
            errors.append(f'"{t}": unlabeled with no level_basis')
        if HIGHER.search(p['title']) and not ENTRY.search(p['title']):
            warnings.append(f'"{t}": the title names a higher level and no entry level; check it qualifies (What counts)')
        dl = p.get('deadline')
        if dl is not None and not re.fullmatch(rf'(at least )?{DATE}', str(dl)):
            warnings.append(f'"{t}": deadline {str(dl)[:50]!r} (want YYYY-MM-DD, "at least YYYY-MM-DD" or null)')
        if not re.fullmatch(rf'(on or before )?{DATE}', str(p.get('opened'))):
            warnings.append(f'"{t}": opened {str(p.get("opened"))[:50]!r}')
        seen = first_seen.get(p['url'].strip())
        cur = opened_value(p.get('opened'))
        if seen and cur and earliest_opened(cur, seen['opened'], seen['discovered']) != cur:
            warnings.append(f'"{t}": opened {cur} is later than {earliest_opened(cur, seen["opened"], seen["discovered"])}, '
                            'recorded for this link before (keep the earlier date)')
        if re.search(r'\+\d|\d+ locations|multiple', p.get('location') or '', re.I):
            warnings.append(f'"{t}": location {p.get("location", "")[:50]!r} (list every city)')
    dropped = d.get('dropped')
    if not isinstance(dropped, list):
        errors.append('dropped is missing (write [] when nothing was dropped)')
        dropped = []
    old = json.load(open(f'{PREV}/{slug}.json')) if os.path.exists(f'{PREV}/{slug}.json') else {}
    kept = [p.get('url') for p in posts if isinstance(p, dict)] + [x.get('url') for x in dropped if isinstance(x, dict)]
    lost = [p['url'] for p in old.get('postings') or [] if p.get('url') and not any(same_posting(p['url'], k) for k in kept if k)]
    if lost:
        errors.append(f'{len(lost)} posting(s) from the previous file left out with no dropped entry: {lost[0]}')
    return errors, warnings


out_path = f'{DATA}/validation.json'
prior = json.load(open(out_path)) if os.path.exists(out_path) else {}
names = {n for n, _ in scope}
result = {'date': TODAY.isoformat(), 'run_start': START, 'errors': {}, 'warnings': {}}
if START and prior.get('run_start') == START:  # keep this run's earlier results for companies outside this check
    for k in ('errors', 'warnings'):
        result[k] = {c: v for c, v in prior.get(k, {}).items() if c not in names}
for name, slug in scope:
    e, w = check(name, slug)
    if e:
        result['errors'][name] = e
    if w:
        result['warnings'][name] = w
json.dump(result, open(out_path, 'w'), indent=1, ensure_ascii=False)
bad = [n for n, _ in scope if n in result['errors']]
print(f'checked {len(scope)} companies: {len(bad)} with errors, '
      f'{sum(1 for n, _ in scope if n in result["warnings"])} with warnings -> timeline/data/validation.json')
for n in bad[:40]:
    print(f'  {n}: {"; ".join(result["errors"][n])[:200]}')
if bad:
    print('rerun: worklist.py --redo --names "' + '|'.join(bad) + '"')
