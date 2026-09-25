"""Step 2: check every company's own job board (Greenhouse / Lever / Ashby / Workday APIs) for new-grad postings.

Board sources, in order: timeline/sources.csv specs (found by earlier research), board URLs seen in tracker postings,
then slug guesses (Greenhouse guesses must match the board's company name). Writes timeline/data/boards.json.
Takes ~20-30 minutes for all companies.  Usage: probe.py [--only "Company name" ...]
"""
import csv, json, os, re, sys, urllib.request, urllib.error, concurrent.futures as cf, datetime as dt
from common import *

companies = load_companies()
p0 = {o['name']: o for o in json.load(open(f'{DATA}/trackers.json'))}
KIND = {'gh': 'greenhouse', 'lever': 'lever', 'ashby': 'ashby', 'wd': 'workday'}
known_specs = {}
if os.path.exists(f'{TIMELINE}/sources.csv'):
    for row in csv.DictReader(open(f'{TIMELINE}/sources.csv')):
        k, _, v = (row.get('jobs.py spec') or '').partition(':')
        if k in KIND and v:
            known_specs[row['Company']] = f'{KIND[k]}:{v}'

STRONG = re.compile(r'new grad|new college|college grad|university|graduate|early career|entry.level|campus|'
                    r'2027|junior|associate software|engineer,? i\b|engineer,? 1\b|developer i\b|rotational|'
                    r'residency|emerging talent|class of|early in career|recent grad|apprentice|level 1\b|amts|associate member', re.I)


def get(url, data=None, timeout=20):
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data else None,
                                 headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/json',
                                          'Accept': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read())
    except Exception:
        return None


def slugs(c):
    out = []
    for a in c['aliases']:
        n = norm(a)
        if not n:
            continue
        t = n.split()
        # no first-word-only guesses: 'capital' matched the wrong company for Capital Group
        for s in (''.join(t), '-'.join(t), t[0] if len(t) == 1 else None, ''.join(t) + 'hq',
                  ''.join(t) + 'inc', ''.join(t) + 'careers'):
            if s and s not in out:
                out.append(s)
    return out[:10]


def ok_job(title, loc):
    return is_role(title) and STRONG.search(title) and (is_us([loc] if loc else []) or re.search(r'\d+ Locations', loc or '')) and not re.search(
        r'intern|co-op', title, re.I)


def greenhouse(slug):
    j = get(f'https://boards-api.greenhouse.io/v1/boards/{slug}/jobs')
    if not j or 'jobs' not in j:
        return None
    meta = get(f'https://boards-api.greenhouse.io/v1/boards/{slug}') or {}
    jobs = [{'title': x['title'], 'loc': (x.get('location') or {}).get('name', ''), 'url': x.get('absolute_url'),
             'date': (x.get('first_published') or x.get('updated_at') or '')[:10]} for x in j['jobs']]
    return {'board_name': meta.get('name', ''), 'jobs': jobs}


def lever(slug):
    j = get(f'https://api.lever.co/v0/postings/{slug}?mode=json')
    if not isinstance(j, list) or not j:
        return None
    jobs = [{'title': x['text'], 'loc': (x.get('categories') or {}).get('location', ''), 'url': x.get('hostedUrl'),
             'date': dt.date.fromtimestamp(x['createdAt'] / 1000).isoformat() if x.get('createdAt') else ''}
            for x in j]
    return {'board_name': '', 'jobs': jobs}


def ashby(slug):
    j = get(f'https://api.ashbyhq.com/posting-api/job-board/{slug}')
    if not j or not j.get('jobs'):
        return None
    jobs = [{'title': x['title'], 'loc': x.get('location', '') + (' USA' if ((x.get('address') or {}).get(
        'postalAddress') or {}).get('addressCountry') in ('United States', 'USA', 'US') else ''),
             'url': x.get('jobUrl'), 'date': (x.get('publishedAt') or '')[:10]} for x in j['jobs']]
    return {'board_name': '', 'jobs': jobs}


def workday(spec):
    tenant, wd, site = spec.split('/')
    base = f'https://{tenant}.{wd}.myworkdayjobs.com'
    jobs, seen = [], set()
    for q in ('new grad', 'university graduate', 'early career', 'college graduate', 'entry level software',
              '2027', 'associate software engineer', 'software engineer I'):
        j = get(f'{base}/wday/cxs/{tenant}/{site}/jobs', {'appliedFacets': {}, 'limit': 20, 'offset': 0,
                                                         'searchText': q})
        if j is None:
            if not jobs:
                return None
            continue
        for x in j.get('jobPostings', []):
            if x.get('externalPath') in seen:
                continue
            seen.add(x.get('externalPath'))
            jobs.append({'title': x.get('title', ''), 'loc': x.get('locationsText', ''),
                         'url': f"{base}/{site}{x.get('externalPath', '')}", 'posted_on': x.get('postedOn', '')})
    return {'board_name': '', 'jobs': jobs}


def wd_date(s):
    s = s.lower()
    if 'today' in s:
        return TODAY.isoformat(), 'exact'
    if 'yesterday' in s:
        return (TODAY - dt.timedelta(days=1)).isoformat(), 'exact'
    m = re.search(r'(\d+)\+? days', s)
    if m:
        n = int(m.group(1))
        return (TODAY - dt.timedelta(days=n)).isoformat(), 'on or before' if '+' in s else 'exact'
    return '', ''


FN = {'greenhouse': greenhouse, 'lever': lever, 'ashby': ashby, 'workday': workday}


def probe(c):
    known = ([known_specs[c['name']]] if c['name'] in known_specs else []) + (p0.get(c['name']) or {}).get('ats', [])
    tries = [tuple(k.split(':', 1)) for k in known]
    if not any(k in ('greenhouse', 'lever', 'ashby') for k, _ in tries):
        for s in slugs(c):
            tries += [('greenhouse', s), ('ashby', s), ('lever', s)]
    boards = []
    done = set()
    for kind, slug in tries:
        if kind not in FN or (kind, slug.lower()) in done:
            continue
        done.add((kind, slug.lower()))
        if kind in {b['kind'] for b in boards} and kind != 'workday':
            continue
        r = FN[kind](slug)
        if not r:
            continue
        guessed = f'{kind}:{slug}' not in known
        if guessed and kind == 'greenhouse' and r['board_name']:
            if not (set(norm(r['board_name']).split()) & set(' '.join(c['keys']).split())):
                continue
        hits = []
        for x in r['jobs']:
            if not ok_job(x['title'], x['loc']):
                continue
            if kind == 'workday':
                x['date'], x['date_kind'] = wd_date(x.pop('posted_on', ''))
            hits.append(x)
        boards.append({'kind': kind, 'slug': slug, 'guessed': guessed, 'n_jobs': len(r['jobs']),
                       'board_name': r['board_name'], 'hits': hits})
        if len(boards) >= 3:
            break
    return c['name'], boards


if __name__ == '__main__':
    only = [a for a in sys.argv[1:] if a != '--only']
    targets = [c for c in companies if not only or c['name'] in only]
    path = f'{DATA}/boards.json'
    res = {}
    if only and os.path.exists(path):  # keep other companies' results; old files were keyed by list position
        names = [c['name'] for c in companies]
        res = {(names[int(k)] if k.isdigit() else k): v for k, v in json.load(open(path)).items()}
    with cf.ThreadPoolExecutor(24) as ex:
        for i, (name, boards) in enumerate(ex.map(probe, targets)):
            res[name] = boards
            if i % 100 == 0:
                print(i, flush=True)
    json.dump(dict(sorted(res.items())), open(path, 'w'), indent=1)
    print('with board', sum(1 for b in res.values() if b))
    print('with hits', sum(1 for b in res.values() if any(x['hits'] for x in b)))
