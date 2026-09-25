"""Step 1: pull the community new-grad trackers and summarize them per company.

Clones SimplifyJobs/New-Grad-Positions, vanshb03/New-Grad-2027 and speedyapply/2027-SWE-College-Jobs into
$TMPDIR/newgrad-trackers (re-downloadable), extracts SimplifyJobs snapshots from past cycles out of git history,
and writes timeline/data/trackers.json. Tracker data is a lead and last-cycle history only, never proof of "open".
Unmatched tracker company names go to timeline/data/unmatched_tracker_names.txt; add real matches to overrides.json.
"""
import json, re, os, subprocess, collections, datetime as dt, html
from common import *

R = CACHE
REPOS = ['SimplifyJobs/New-Grad-Positions', 'vanshb03/New-Grad-2027', 'speedyapply/2027-SWE-College-Jobs']
LISTINGS = '.github/scripts/listings.json'


def fetch():
    os.makedirs(R, exist_ok=True)
    for repo in REPOS:
        d = os.path.join(R, repo.split('/')[1])
        if os.path.isdir(d):
            subprocess.run(['git', '-C', d, 'pull', '-q'], check=False)
        else:
            subprocess.run(['git', 'clone', '-q', '--filter=blob:none', f'https://github.com/{repo}.git', d], check=True)
    # SimplifyJobs resets listings.json each cycle; keep the last snapshot of each past cycle.
    simp = os.path.join(R, 'New-Grad-Positions')
    for name, until in (('simplify_2025cycle.json', '2025-05-25'), ('simplify_2026cycle.json', '2026-01-26')):
        out = os.path.join(R, name)
        if not os.path.exists(out):
            h = subprocess.run(['git', '-C', simp, 'log', '--format=%h', f'--until={until}', '-1', '--', LISTINGS],
                               capture_output=True, text=True, check=True).stdout.strip()
            with open(out, 'w') as f:
                subprocess.run(['git', '-C', simp, 'show', f'{h}:{LISTINGS}'], stdout=f, check=True)


fetch()
companies = load_companies()
idx = build_index(companies)

recs = {}


def add(company, title, url, locs, date, active, spons, src):
    key = url or f'{company}|{title}|{date}'
    if key in recs:
        r = recs[key]
        r['active'] = r['active'] or active
        r['date'] = min(r['date'], date)
        r['src'].add(src)
        return
    recs[key] = dict(company=company, title=title, url=url, locs=locs, date=date, active=active,
                     spons=spons or '', src={src})


for f, src in [(f'{R}/simplify_2025cycle.json', 'simplify'), (f'{R}/simplify_2026cycle.json', 'simplify'),
               (f'{R}/New-Grad-Positions/.github/scripts/listings.json', 'simplify'),
               (f'{R}/New-Grad-2027/archived/2025/listings.json', 'vanshb03'),
               (f'{R}/New-Grad-2027/.github/scripts/listings.json', 'vanshb03')]:
    for x in json.load(open(f)):
        if x.get('category') in ('Hardware', 'Product', 'Product Management'):
            continue
        if not x.get('is_visible', True):
            continue
        add(x['company_name'], x['title'], x.get('url', ''), x.get('locations') or [], d(x['date_posted']),
            bool(x.get('active')), x.get('sponsorship'), src)

# speedyapply: current open USA new-grad listings with age
row = re.compile(r'^\| (.*?) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \| (\d+)d \|$')
for line in open(f'{R}/2027-SWE-College-Jobs/NEW_GRAD_USA.md'):
    m = row.match(line.strip())
    if not m:
        continue
    comp = html.unescape(re.sub(r'<.*?>', '', m.group(1))).strip()
    title = html.unescape(re.sub(r'<.*?>', '', m.group(2))).strip()
    loc = re.sub(r'<.*?>', ' ', m.group(3)).strip()
    url = (re.findall(r'href="(.*?)"', m.group(5)) or [''])[0]
    age = int(m.group(6))
    add(comp, title, url, [l.strip() for l in re.split(r'<br>|;', m.group(3))] or [loc],
        TODAY - dt.timedelta(days=age), True, '', 'speedyapply')

# ATS harvest from every URL (any role)
ATS = [(r'(?:boards|job-boards)(?:\.eu)?\.greenhouse\.io/(?:embed/job_board\?for=)?([\w-]+)', 'greenhouse'),
       (r'[?&]for=([\w-]+)', 'greenhouse'),
       (r'jobs\.lever\.co/([\w.-]+)', 'lever'),
       (r'jobs\.ashbyhq\.com/([\w.%-]+)', 'ashby'),
       (r'([\w-]+)\.(wd\d+)\.myworkdayjobs\.com/(?:[a-z]{2}-[A-Z]{2}/)?([\w-]+)', 'workday'),
       (r'jobs\.smartrecruiters\.com/([\w-]+)', 'smartrecruiters')]

by_c = collections.defaultdict(list)
unmatched = collections.Counter()
ats = collections.defaultdict(collections.Counter)
for r in recs.values():
    cid = match(idx, r['company'])
    if cid is None:
        unmatched[r['company']] += 1
        continue
    r['cid'] = cid
    by_c[cid].append(r)
    for pat, kind in ATS:
        m = re.search(pat, r['url'] or '')
        if m:
            val = '/'.join(m.groups()) if kind == 'workday' else m.group(1)
            if val not in ('embed', 'jobs'):
                ats[cid][f'{kind}:{val}'] += 1
            break

out = []
for c in companies:
    L = [r for r in by_c.get(c['id'], []) if is_us(r['locs']) and is_role(r['title'])]
    cur = [r for r in L if r['date'] >= CYCLE_START]
    cur_open = [r for r in cur if r['active']]
    last = [r for r in L if LAST_START <= r['date'] <= LAST_END]
    last_ng = [r for r in last if NEWGRAD.search(r['title'])]
    prev = [r for r in L if PREV_START <= r['date'] <= PREV_END]
    prev_ng = [r for r in prev if NEWGRAD.search(r['title'])]

    def restricted(r):
        return 'Citizenship' in r['spons'] or bool(CLEAR.search(r['title']))

    def brief(r):
        return {'title': r['title'], 'url': r['url'], 'date': r['date'].isoformat(), 'active': r['active'],
                'restricted': restricted(r), 'src': sorted(r['src'])}

    open_ok = sorted([r for r in cur_open if not restricted(r)], key=lambda r: r['date'])
    open_restricted = [r for r in cur_open if restricted(r)]
    out.append({**{k: c[k] for k in ('id', 'tier', 'name')},
                'tracker_listings_total': len(by_c.get(c['id'], [])),
                'open': [brief(r) for r in open_ok][:8],
                'open_count': len(open_ok),
                'open_restricted_count': len(open_restricted),
                'no_sponsor': any('Does Not Offer' in r['spons'] for r in cur),
                'cycle_first_posted': min((r['date'] for r in cur if not restricted(r)), default=None),
                'last_first_newgrad': min((r['date'] for r in last_ng), default=None),
                'last_first_any': min((r['date'] for r in last), default=None),
                'prev_first': min((r['date'] for r in (prev_ng or prev)), default=None),
                'last_example': brief(min(last_ng or last, key=lambda r: r['date'])) if (last_ng or last) else None,
                'last_all_restricted': bool(last) and all(restricted(r) for r in last),
                'ats': [k for k, _ in ats[c['id']].most_common()]})

os.makedirs(DATA, exist_ok=True)
json.dump(out, open(f'{DATA}/trackers.json', 'w'), default=str, indent=1)
with open(f'{DATA}/unmatched_tracker_names.txt', 'w') as f:
    f.writelines(f'{n}\t{name}\n' for name, n in unmatched.most_common())
print('listings', len(recs))
print('companies with any tracker data', sum(1 for o in out if o['tracker_listings_total']))
print('open now', sum(1 for o in out if o['open_count']))
print('last-year date', sum(1 for o in out if o['last_first_any']))
print('ats known', sum(1 for o in out if o['ats']))
print('top unmatched (full list in timeline/data/unmatched_tracker_names.txt):', unmatched.most_common(20))
