"""Step 5: merge everything into timeline/status.csv, timeline/postings.csv, timeline/SUMMARY.md and timeline/sources.csv.

status.csv has one row per company (its timeline). postings.csv has one row per open posting, since a company can
have several, and marks each one applied only if a TRACKER.md row matches that posting (link, posting ID, or title).

Priority (highest first): timeline/research/*.json (one first-party check per company, newest)
  > first-pass agent results (timeline/data/first_pass_agents/, 2026-09-24)
  > job-board API check (timeline/data/boards.json)
  > community trackers (timeline/data/trackers.json).
A tracker listing never makes a company "open" by itself. If the company's own board was read and shows no
matching posting, the company is not_yet; if no board could be read, it is tracker_lead (check it first-party).
The listing is kept in the "Tracker lead" column either way.
"""
import json, re, csv, glob, datetime as dt, collections
from common import *

companies = load_companies()
idx = build_index(companies)
# Intermediate files are keyed by company name so edits to COMPANY_LIST.md don't misalign them.
_p0 = json.load(open(f'{DATA}/trackers.json'))
p0 = {o['name']: o for o in _p0}
p1 = {(_p0[int(k)]['name'] if k.isdigit() else k): v for k, v in json.load(open(f'{DATA}/boards.json')).items()}
EMPTY = {'open': [], 'open_count': 0, 'open_restricted_count': 0, 'no_sponsor': False, 'cycle_first_posted': None,
         'last_first_newgrad': None, 'last_first_any': None, 'prev_first': None, 'last_example': None, 'ats': []}
agent = {}
research = {}
for f in glob.glob(f'{TIMELINE}/research/*.json'):
    x = json.load(open(f))
    m = next((c['id'] for c in companies if c['name'] == x.get('company')), None)
    if m is None:
        m = match(idx, x.get('company', ''))
    if m is not None:
        research[m] = x
for f in sorted(glob.glob(f'{DATA}/first_pass_agents/*.jsonl')):
    for line in open(f):
        line = line.strip()
        if not line:
            continue
        try:
            x = json.loads(line)
            agent[x.get('name') or _p0[int(x['id'])]['name']] = x
        except Exception:
            pass

def job_ids(s):
    """Posting IDs in a URL or note: long numbers, UUIDs, and req codes like JR26091743 or R-12345."""
    s = s or ''
    return set(re.findall(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', s, re.I)) | \
        set(re.findall(r'(?<![\w-])(?:[A-Z]{1,3}-?)?\d{5,}(?:-\d+)?', s)) - {''}


def url_id(u):
    """The posting's own ID: the last ID in the URL path (earlier ones are often a site or board ID)."""
    ids = [m.group(0) for m in re.finditer(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|'
                                           r'(?<![\w-])(?:[A-Z]{1,3}-?)?\d{5,}(?:-\d+)?', re.sub(r'[?#].*', '', u or ''), re.I)]
    return {ids[-1]} if ids else set()


def norm_url(u):
    return re.sub(r'^https?://(www\.)?|[?#].*$|/+$', '', (u or '').strip().lower())


def norm_title(t):
    return re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()


# applications from TRACKER.md, a list per company (he may apply to several postings at one company)
applied = collections.defaultdict(list)
for line in open(f'{REPO}/applications/TRACKER.md'):
    p = [x.strip() for x in line.split('|')]
    if len(p) > 6 and re.match(r'\d{4}-', p[1]):
        names = [p[2], re.sub(r'\s*\(.*?\)', '', p[2])] + re.findall(r'\((.*?)\)', p[2])
        for n in names:
            m = match(idx, re.sub(r'^formerly\s+', '', n))
            if m is not None:
                applied[m].append({'date': p[1], 'role': p[3], 'link': p[4], 'status': p[5],
                                   'notes': p[-2] if len(p) > 2 else '', 'ids': url_id(p[4]) | job_ids(p[-2])})
                break


def applied_str(cid):
    return '; '.join(f"{a['status']} ({a['date']}): {a['role']}" for a in applied.get(cid, []))


def application_for(cid, title, url):
    """The tracker row for this exact posting, matched by link, posting ID, or title."""
    for a in applied.get(cid, []):
        if (a['link'] and norm_url(a['link']) == norm_url(url)) or (a['ids'] & url_id(url)) \
                or norm_title(a['role']) == norm_title(title):
            return a
    return None

NOSPON = re.compile(r"no (visa )?sponsor|not (offer |provide )?(visa )?sponsor|won.?t sponsor|does not sponsor|"
                    r"without (visa )?sponsorship|unable to sponsor|permanent (us |u\.s\. )?work auth", re.I)
REFERRAL_HORIZON = TODAY + dt.timedelta(weeks=8)
# he applies with a master's: a title that requires a PhD and names no other degree is not for him
PHD_ONLY = lambda t: bool(re.search(r'\bph\.?d\b', t or '', re.I)) and \
    not re.search(r'\b(b\.?s|m\.?s|bachelor|master|undergrad)', t or '', re.I)


def iso(x):
    return x.isoformat() if isinstance(x, dt.date) else (x or '')


def parse_date(s):
    if not s:
        return None
    m = re.search(r'(\d{4})-(\d{2})(?:-(\d{2}))?', str(s))
    if not m:
        return None
    return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3) or 15))


rows = []
postings = []  # one row per open posting; a company can have several
for c in companies:
    cid = c['id']
    o, boards, a = p0.get(c['name'], EMPTY), p1.get(c['name'], []), agent.get(c['name'])
    r = {'Company': c['name'], 'Tier': c['tier'], 'Industry': c['industry'], 'Status': 'unknown', 'Role': '', 'Link': '', 'Opened': '', 'Deadline': '', 'Areas': '',
         'Last year opened': '', 'Expected open': '', 'Applied': applied_str(cid), 'Sponsorship': '', 'Notes': '',
         'Confidence': '', 'Source': '', 'Job board': '', 'Tracker lead': ''}
    posts_out = []  # (title, url, location, opened, deadline, level, no_sponsorship) for this company's open postings
    notes = []
    api_boards = [b for b in boards if b['kind'] in ('greenhouse', 'lever', 'ashby', 'workday')]
    if api_boards:
        r['Job board'] = '; '.join(f"{b['kind']}:{b['slug']}" for b in api_boards)
    hits = [h for b in api_boards for h in b['hits']]
    hits_ok = [h for h in hits if not CLEAR.search(h['title'])]
    excluded = False
    # 1) API
    if hits_ok:
        h = sorted(hits_ok, key=lambda h: h.get('date') or '9999')[0]
        best = next((x for x in hits_ok if re.search(r'2027|new grad|new college|college grad|university', x['title'], re.I)), h)
        r.update(Status='open', Role=best['title'], Link=best['url'] or '', Source=api_boards[0]['kind'] + ' API',
                 Confidence='high')
        dates = sorted(x['date'] for x in hits_ok if x.get('date'))
        if dates:
            kind = next((x.get('date_kind') for x in hits_ok if x.get('date') == dates[0]), '')
            r['Opened'] = ('on or before ' if kind == 'on or before' else '') + dates[0]
        posts_out = [(h['title'], h.get('url') or '', h.get('loc') or '',
                      (('on or before ' if h.get('date_kind') == 'on or before' else '') + h['date']) if h.get('date') else '', '',
                      'new-grad title', None) for h in hits_ok]
        if len(hits_ok) > 1:
            notes.append(f'{len(hits_ok)} matching postings')
    elif hits and not hits_ok:
        excluded = True
        notes.append('only open roles need clearance/citizenship')
    # 2) trackers: a lead only, never proof of open
    if o['open']:
        t = o['open'][0]
        best = next((x for x in o['open'] if NEWGRAD.search(x['title'])), t)
        more = f" (+{o['open_count'] - 1} more)" if o['open_count'] > 1 else ''
        r['Tracker lead'] = f"{best['title']} | first seen {t['date']} | {best['url']}{more}"
    if r['Status'] != 'open' and o['open']:
        if api_boards:
            notes.append('tracker lists a posting the company board does not show')
        else:
            r.update(Status='tracker_lead', Role=best['title'], Link=best['url'], Opened=t['date'],
                     Source='tracker only (' + ','.join(t['src']) + ')', Confidence='low')
    elif r['Status'] == 'open' and o['cycle_first_posted'] and (
            not r['Opened'] or o['cycle_first_posted'] < r['Opened'].replace('on or before ', '')):
        r['Opened'] = o['cycle_first_posted']
    if r['Status'] != 'open' and not excluded and o['open_restricted_count'] and not o['open_count']:
        excluded = True
        notes.append('tracker postings need US citizenship/clearance')
    if r['Status'] != 'open' and api_boards and not excluded:
        r.update(Status='not_yet', Source=api_boards[0]['kind'] + ' API (no new-grad posting)',
                 Confidence='medium' if not api_boards[0]['guessed'] else 'low')
    # last year
    ly = o['last_first_newgrad'] or o['last_first_any']
    if ly:
        r['Last year opened'] = ly
    elif o['prev_first']:
        r['Last year opened'] = ''
        notes.append(f"2 yrs ago opened {o['prev_first']}")
    # 3) agent
    if a:
        if a.get('excluded'):
            excluded = True
            notes.append(f"requires {a.get('excluded_reason') or 'citizenship/clearance'}")
        if r['Status'] == 'open' and a.get('status') in ('not_yet', 'closed', 'no_program'):
            if a.get('confidence') in ('medium', 'high'):
                notes.append(f"research overrode {r['Source']} open result ({r['Role'][:40]})")
                r.update(Status=a['status'], Role=a.get('role') or '', Link=a.get('link') or '',
                         Opened=a.get('opened') or '', Source='first-pass agent', Confidence=a.get('confidence', ''))
            else:
                notes.append('research doubts this is a new-grad role')
                r['Confidence'] = 'low'
        elif r['Status'] != 'open' and a.get('status') and a['status'] != 'unknown':
            r.update(Status=a['status'], Role=a.get('role') or '', Link=a.get('link') or '',
                     Opened=a.get('opened') or '', Source='first-pass agent', Confidence=a.get('confidence', ''))
        if a.get('last_year_opened') and not r['Last year opened']:
            r['Last year opened'] = a['last_year_opened']
            if a.get('last_year_basis'):
                notes.append('last yr: ' + a['last_year_basis'][:60])
        if a.get('notes'):
            notes.append(a['notes'])
        if a.get('ats') and not r['Job board']:
            r['Job board'] = a['ats']
    if excluded and (r['Status'] != 'open' or (a and a.get('excluded'))):
        r['Status'] = 'excluded'
    # sponsorship flag (kept, not excluded)
    txt = ' '.join([r['Notes'] if isinstance(r['Notes'], str) else '', ' '.join(notes)])
    if o.get('no_sponsor') or NOSPON.search(txt) or any(NOSPON.search(x['notes']) for x in applied.get(cid, [])):
        r['Sponsorship'] = 'no sponsorship'
    # 4) per-company research (first-party, newest) overrides everything above
    rs = research.get(cid)
    if rs:
        st = {'no_program_found': 'no_program', 'leftover_2026': 'not_yet'}.get(rs['status'], rs['status'])
        posts = rs.get('postings') or []
        live = [p for p in posts if rs['status'] == 'open']
        live.sort(key=lambda p: not areas_of(p.get('location')))  # show a posting in his areas first
        p = live[0] if live else None
        r['Areas'] = ', '.join(dict.fromkeys(a for q in live for a in areas_of(q.get('location'))))
        notes = [n for n in notes if not n.startswith('research overrode') and n != 'research doubts this is a new-grad role']
        if rs['status'] == 'leftover_2026':
            notes.append('only 2026-cycle leftover postings live')
        notes.append(rs.get('evidence') or '')
        r.update(Status=st, Role=p['title'] if p else '', Link=p['url'] if p else '', Opened=p.get('opened', '') if p else '',
                 Deadline=(p.get('deadline') or '') if p else '',
                 Source=f"first-party check {rs.get('checked', '')}", Confidence=rs.get('confidence', ''))
        if len(live) > 1:
            notes.append(f'{len(live)} live postings')
        if rs.get('last_cycle_opened'):
            r['Last year opened'] = rs['last_cycle_opened']
        if rs.get('jobs_spec') or rs.get('jobs_page'):
            r['Job board'] = rs.get('jobs_spec') or rs.get('jobs_page')
        r['Sponsorship'] = 'no sponsorship' if rs.get('no_sponsorship') else ''
        r['Notes'] = '; '.join(dict.fromkeys(n for n in notes if n))[:300]
        posts_out = [(q['title'], q.get('url') or '', q.get('location') or '', q.get('opened') or '',
                      q.get('deadline') or '', q.get('level') or '', q.get('no_sponsorship')) for q in live]
    if r['Status'] != 'open':
        posts_out = []
    elif not posts_out:
        posts_out = [(r['Role'], r['Link'], '', iso(r['Opened']), r['Deadline'], '', None)]
    seen = set()
    for title, url, loc, opened, deadline, level, no_spon in posts_out:
        if (url or title) in seen or PHD_ONLY(title):
            continue
        seen.add(url or title)
        ap = application_for(cid, title, url)
        postings.append({'Company': c['name'], 'Tier': c['tier'], 'Role': title, 'Level': level, 'Link': url, 'Location': loc,
                         'Areas': ', '.join(areas_of(loc)) if loc else r['Areas'], 'Opened': iso(opened),
                         'Deadline': deadline, 'Applied': f"{ap['status']} ({ap['date']})" if ap else '',
                         # the posting's own sponsorship line when research recorded one, else the company's
                         'Sponsorship': r['Sponsorship'] if no_spon is None else ('no sponsorship' if no_spon else ''),
                         'Confidence': r['Confidence'], 'Source': r['Source']})
    # expected
    if r['Status'] in ('not_yet', 'unknown', 'closed'):
        ref = parse_date(r['Last year opened'])
        src = 'last year'
        if not ref:
            ref = parse_date(o['prev_first'])
            src = '2 yrs ago'
            if ref:
                ref = ref.replace(year=ref.year + 1)
        if ref:
            try:
                exp = ref.replace(year=ref.year + 1)
            except ValueError:
                exp = ref + dt.timedelta(days=365)
            if exp < TODAY:
                r['Expected open'] = f'overdue (opened {exp.strftime("%b %d")} last cycle)' if src == 'last year' \
                    else f'overdue (~{exp.strftime("%b")} per {src})'
            else:
                r['Expected open'] = exp.isoformat() + ('' if src == 'last year' else f' (from {src})')
    r['Notes'] = '; '.join(dict.fromkeys(n for n in notes if n))[:300]
    r['Last year opened'] = iso(r['Last year opened'])
    r['Opened'] = iso(r['Opened'])
    rows.append(r)

OUT = TIMELINE
cols = list(rows[0].keys())
with open(f'{OUT}/status.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(rows)

with open(f'{OUT}/postings.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['Company', 'Tier', 'Role', 'Level', 'Link', 'Location', 'Areas', 'Opened', 'Deadline',
                                      'Applied', 'Sponsorship', 'Confidence', 'Source'])
    w.writeheader()
    w.writerows(postings)

cnt = collections.Counter(r['Status'] for r in rows)
print(cnt, 'applied at', len(applied), 'companies |', len(postings), 'open postings,',
      sum(1 for p in postings if p['Applied']), 'applied')
json.dump(rows, open(f'{DATA}/merged.json', 'w'), indent=1)


# ---- SUMMARY.md ----
def link(r):
    return f"[{r['Role'] or 'posting'}]({r['Link']})" if r['Link'] else (r['Role'] or '')


def exp_key(r):
    e = r['Expected open']
    if e.startswith('overdue'):
        return '0000'
    return e[:10]


live = [r for r in rows if r['Status'] != 'excluded']
# "Apply now" is per posting: applying to one posting doesn't hide a company's other open postings
company_notes = {r['Company']: r['Notes'] for r in rows}
for p in postings:
    p['Notes'] = company_notes.get(p['Company'], '')
apply_now = sorted([p for p in postings if not p['Applied']],
                   key=lambda r: (r['Tier'], r['Company'], r['Opened'] or '9999'))
applied_rows = [r for r in rows if r['Applied']]
open_left = collections.Counter(p['Company'] for p in apply_now)
for r in applied_rows:
    r['Open, not applied'] = str(open_left.get(r['Company'], 0))
# stated deadlines first, soonest first; "at least" dates are lower bounds and sort by that date
asap = sorted([r for r in apply_now if parse_date(r['Deadline'])], key=lambda r: parse_date(r['Deadline']))
mine = lambda rs: [r for r in rs if r['Areas']]
others = lambda rs: [r for r in rs if not r['Areas']]
for r in asap:
    d = parse_date(r['Deadline'])
    if d >= TODAY:
        r['Days left'] = str((d - TODAY).days)
    else:
        r['Days left'] = 'no end date known' if 'at least' in r['Deadline'] else 'passed — check it is still live'
# Company-level sections keep companies he applied to: one application there doesn't cover its other roles
soon = [r for r in live if r['Status'] in ('not_yet', 'unknown', 'closed') and r['Expected open']
        and (r['Expected open'].startswith('overdue') or r['Expected open'][:10] <= REFERRAL_HORIZON.isoformat())]
soon.sort(key=lambda r: (r['Tier'], exp_key(r)))
later = [r for r in live if r['Status'] in ('not_yet', 'unknown', 'closed') and r not in soon]
nop = [r for r in live if r['Status'] == 'no_program']
leads = sorted([r for r in live if r['Status'] == 'tracker_lead'], key=lambda r: (r['Tier'], r['Opened']))
exc = [r for r in rows if r['Status'] == 'excluded']

L = [f'# 2027 New-Grad Timeline', '',
     f'Checked {TODAY.isoformat()}. {len(rows)} companies in `COMPANY_LIST.md`. Full data: `status.csv` (one row per '
     f'company) and `postings.csv` (one row per open posting).', '',
     f'- **Apply now:** {len(apply_now)} open postings not yet applied to, at {len(open_left)} companies: '
     f'{len(mine(apply_now))} in your areas, {len(others(apply_now))} elsewhere ({len(asap)} with a stated deadline)',
     f'- **Referrals / cold messages now:** {len(soon)} expected to open by {REFERRAL_HORIZON.isoformat()} or overdue vs last year',
     f'- **Tracker leads to confirm:** {len(leads)} listed by a GitHub tracker, company board not checked yet',
     f'- **Later / unknown timing:** {len(later)}',
     f'- **Companies in TRACKER.md:** {len(applied_rows)} ({sum(len(v) for v in applied.values())} applications); '
     'other open postings at these companies still appear under Apply now',
     f'- **No US new-grad SWE track found:** {len(nop)}',
     f'- **Dropped (citizenship, green card, or clearance required):** {len(exc)} — kept in `status.csv` as `excluded`', '',
     '"Apply now" only counts postings seen on the company\'s own job board. GitHub trackers (SimplifyJobs, '
     'speedyapply, vanshb03) are used for leads and last-cycle dates. Workday dates are the latest repost.', '']


def table(rs, cols):
    out = ['| ' + ' | '.join(cols) + ' |', '|' + '---|' * len(cols)]
    for r in rs:
        vals = []
        for c in cols:
            v = link(r) if c == 'Role' else str(r[c])
            vals.append(v.replace('|', '/'))
        out.append('| ' + ' | '.join(vals) + ' |')
    return out


L += ['## Already applied', '',
      '"Open, not applied" counts this company\'s open postings that no TRACKER.md row matches; they are listed under Apply now.', '']
L += table(applied_rows, ['Company', 'Tier', 'Applied', 'Status', 'Open, not applied']) + ['']
L += ['## Apply ASAP: stated deadlines', '',
      'Open, not yet applied, and the posting states a deadline. Soonest first. Most postings state none, '
      'so a missing entry is not a sign of time to spare.', '']
L += ['### In your areas', ''] + table(mine(asap), ['Company', 'Tier', 'Role', 'Areas', 'Deadline', 'Days left', 'Opened',
                                                    'Sponsorship']) + ['']
L += ['### Elsewhere', ''] + table(others(asap), ['Company', 'Tier', 'Role', 'Deadline', 'Days left', 'Opened',
                                                 'Sponsorship']) + ['']
L += ['## 1. Apply now', '',
      'One row per open posting you haven\'t applied to, by tier and company, oldest first. Level "unlabeled" means the '
      'title has no level but the posting reads entry-level (see the research file\'s level_basis); blank means not recorded yet. '
      '"Your areas" are set in `.agents/skills/new-grad-timeline/scripts/areas.json`; '
      'every company is still researched, and the rest are listed under Elsewhere.', '']
L += ['### In your areas', ''] + table(mine(apply_now), ['Company', 'Tier', 'Role', 'Level', 'Location', 'Areas', 'Opened',
                                                        'Deadline', 'Confidence', 'Sponsorship', 'Notes']) + ['']
L += ['### Elsewhere', ''] + table(others(apply_now), ['Company', 'Tier', 'Role', 'Level', 'Location', 'Opened', 'Deadline',
                                                      'Confidence', 'Sponsorship', 'Notes']) + ['']
L += ['## Tracker leads: confirm on the company site', '',
      'A GitHub tracker lists these as open, but no one has checked the company\'s own board yet.', '']
L += table(leads, ['Company', 'Tier', 'Role', 'Opened', 'Applied', 'Notes']) + ['']
L += ['## 2. Start referrals and cold messages now', '',
      '"Overdue" means last year it had opened by this date but nothing is live yet — likely any day.', '']
L += table(soon, ['Company', 'Tier', 'Expected open', 'Last year opened', 'Applied', 'Sponsorship', 'Notes']) + ['']
L += ['## 3. Later or unknown timing', '']
L += table(sorted(later, key=lambda r: (r['Tier'], exp_key(r) or '9999')),
           ['Company', 'Tier', 'Status', 'Expected open', 'Applied', 'Notes']) + ['']
open(f'{OUT}/SUMMARY.md', 'w').write('\n'.join(L) + '\n')
print('summary', len(apply_now), len(soon), len(later), len(nop), len(exc))


# ---- sources.csv: where each company's job list lives ----
def spec_of(raw):
    raw = (raw or '').strip()
    for pat, kind in ((r'(?:greenhouse|gh):([\w-]+)$', 'gh'), (r'lever:([\w.-]+)$', 'lever'),
                      (r'ashby:([\w.%-]+)$', 'ashby'), (r'(?:smartrecruiters|sr):([\w-]+)$', 'sr')):
        m = re.match(pat, raw, re.I)
        if m:
            return f'{kind}:{m.group(1)}'
    m = re.match(r'workday:([\w-]+)/(wd\d+)/([\w-]+)', raw, re.I)
    if m:
        return f'wd:{m.group(1)}/{m.group(2)}/{m.group(3)}'
    m = re.match(r'oracle[\w-]*:([\w.-]+)/([\w-]+)$', raw, re.I)
    if not m:
        return ''
    h = m.group(1)
    if not h.endswith('oraclecloud.com'):  # agents often wrote the short host
        h += '.fa.ocs.oraclecloud.com' if 'saasfaprod' in h else '.oraclecloud.com'
    return f'oracle:{h}/{m.group(2)}'


def page_of(spec, raw=''):
    k, _, v = spec.partition(':')
    if k == 'gh':
        return f'https://job-boards.greenhouse.io/{v}'
    if k in ('lever', 'levereu'):
        return f"https://jobs{'.eu' if k == 'levereu' else ''}.lever.co/{v}"
    if k == 'ashby':
        return f'https://jobs.ashbyhq.com/{v}'
    if k == 'sr':
        return f'https://jobs.smartrecruiters.com/{v}'
    if k == 'wd':
        t, pod, site = v.split('/')
        return f'https://{t}.{pod}.myworkdayjobs.com/{site}'
    if k == 'oracle':
        h, site = v.rsplit('/', 1)
        return f'https://{h}/hcmUI/CandidateExperience/en/sites/{site}/jobs'
    if k == 'pinpoint':
        return f'https://{v}.pinpointhq.com'
    if k == 'eightfold':
        return f"https://{v.split('/')[0]}/careers"
    if k == 'amazon':
        return 'https://www.amazon.jobs'
    m = re.search(r'https?://[^\s,;)]+|[\w-]+(\.[\w-]+)*\.[a-z]{2,}(/[\w./-]*)?', re.sub(r'^[\w -]+:(?!//)', '', raw or ''))
    return (m.group(0) if m.group(0).startswith('http') else 'https://' + m.group(0)) if m else ''


VALID_SPEC = re.compile(r'(gh|lever|levereu|ashby|sr|amazon|pinpoint):[\w.%-]*$|wd:[\w-]+/wd\d+/[\w-]+$|'
                        r'oracle:[\w.-]+/[\w-]+$|eightfold:[\w.-]+/[\w.-]+$')


def spec_from_url(u):
    """A jobs.py spec from a board URL that research wrote where the short spec belongs."""
    for pat, fmt in ((r'(?:boards|job-boards)(?:\.eu)?\.greenhouse\.io/(?:embed/job_board\?for=)?([\w-]+)', 'gh:{}'),
                     (r'jobs\.eu\.lever\.co/([\w.-]+)', 'levereu:{}'), (r'jobs\.lever\.co/([\w.-]+)', 'lever:{}'),
                     (r'jobs\.ashbyhq\.com/([\w.%-]+)', 'ashby:{}'), (r'(?:jobs|careers)\.smartrecruiters\.com/([\w-]+)', 'sr:{}'),
                     (r'([\w-]+)\.(wd\d+)\.myworkdayjobs\.com/(?:[a-z]{2}-[A-Z]{2}/)?([\w-]+)', 'wd:{}/{}/{}')):
        m = re.search(pat, u or '')
        if m:
            return fmt.format(*m.groups())
    return ''


KSHORT = {'greenhouse': 'gh', 'lever': 'lever', 'ashby': 'ashby', 'workday': 'wd'}
ATSNAME = {'gh': 'greenhouse', 'wd': 'workday', 'sr': 'smartrecruiters', 'levereu': 'lever (EU)'}
src_rows = []
for c in companies:
    cid = c['id']
    rs, a, boards, o = research.get(cid) or {}, agent.get(c['name']) or {}, p1.get(c['name'], []), p0.get(c['name'], EMPTY)
    spec = page = by = ''
    trusted = [b for b in boards if not b['guessed']]
    if rs.get('jobs_spec') or rs.get('jobs_page'):
        spec, page, by = rs.get('jobs_spec') or '', rs.get('jobs_page') or '', f"first-party check {rs.get('checked', '')}"
        if spec and not VALID_SPEC.match(spec):  # a URL written where the short spec belongs
            page = page or spec
            spec = spec_from_url(spec)
    elif trusted:
        b = trusted[0]
        spec, by = f"{KSHORT[b['kind']]}:{b['slug']}", 'board URL in tracker postings'
    elif spec_of(a.get('ats')):
        spec, by = spec_of(a['ats']), 'first-pass agent'
    elif boards and boards[0]['kind'] in ('greenhouse', 'workday'):
        spec, by = f"{KSHORT[boards[0]['kind']]}:{boards[0]['slug']}", 'slug guess (name-checked)'
    raw = a.get('ats') or ''
    if not page:
        page = page_of(spec, raw if raw.lower() not in ('none', 'unknown', 'null') else '')
        if page and not by:
            by = 'first-pass agent'
    if not page:
        urls = [x['url'] for x in o['open']] + ([o['last_example']['url']] if o.get('last_example') else [])
        urls = [u for u in urls if u and not re.search(r'simplify\.jobs|linkedin\.com|indeed|builtin|jobright', u)]
        m = re.match(r'https?://[^/?#]+', urls[0]) if urls else None
        if m:
            page, by = m.group(0), 'host of a tracker posting'
    k = spec.split(':')[0] if spec else ''
    ats = ATSNAME.get(k, k) or (re.match(r'[\w-]+', raw).group(0).lower() if raw and raw.lower() not in ('none', 'unknown', 'null') else '')
    src_rows.append({'Company': c['name'], 'Tier': c['tier'], 'ATS': ats, 'Jobs page': page, 'jobs.py spec': spec,
                     'Found by': by})
with open(f'{OUT}/sources.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(src_rows[0]))
    w.writeheader()
    w.writerows(src_rows)
print('sources: api spec', sum(1 for r in src_rows if r['jobs.py spec']), '| page only',
      sum(1 for r in src_rows if r['Jobs page'] and not r['jobs.py spec']), '| none',
      sum(1 for r in src_rows if not r['Jobs page']))
