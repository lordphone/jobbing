"""Check every saved job-board spec in timeline/sources.csv and flag the doubtful ones for research.

Run after merge.py and before worklist.py. worklist.py passes each flag to that company's research agent, which
confirms the board (from the company's own careers page) or replaces it. Writes timeline/data/source_flags.json:
{company: reason}. Only API specs (gh, lever, levereu, ashby, wd, sr) can be checked here.

Flags:
  - the board doesn't answer, or answers with an error (bad tenant/site/slug)
  - a Greenhouse or SmartRecruiters board whose own name doesn't match the company
  - a board that answers with 0 jobs
A name or 0-jobs flag is skipped once a research file has confirmed that same spec (jobs_spec_basis), so a
parent-company board (Weights & Biases on CoreWeave's) is flagged once, not every run. Errors are always flagged.
Usage: check_sources.py [--only "Company" ...]
"""
import csv, glob, json, re, sys, time, urllib.request, concurrent.futures as cf
from common import *

companies = load_companies()
idx = build_index(companies)
cid_of = {c['name']: c['id'] for c in companies}
basis = {}  # company -> spec that research confirmed, with its reason
for f in glob.glob(f'{TIMELINE}/research/*.json'):
    x = json.load(open(f))
    if x.get('jobs_spec') and x.get('jobs_spec_basis'):
        basis[x.get('company')] = x['jobs_spec']


def get(url, data=None):
    """JSON, or ('error', message). Retries once on network trouble, not on an HTTP error."""
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data else None,
                                 headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/json',
                                          'Accept': 'application/json'})
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            return ('error', f'HTTP {e.code}')
        except Exception as e:
            err = str(e)[:60]
            time.sleep(3)
    return ('error', f'no answer ({err})')


def board(spec):
    """(jobs count or None, board name or None, error or None)."""
    k, _, v = spec.partition(':')
    if k == 'gh':
        j = get(f'https://boards-api.greenhouse.io/v1/boards/{v}')
        if isinstance(j, tuple):
            return None, None, j[1]
        jobs = get(f'https://boards-api.greenhouse.io/v1/boards/{v}/jobs')
        return (len(jobs['jobs']) if isinstance(jobs, dict) and 'jobs' in jobs else None), j.get('name'), None
    if k in ('lever', 'levereu'):
        j = get(f"https://api{'.eu' if k == 'levereu' else ''}.lever.co/v0/postings/{v}?mode=json")
        return (len(j), None, None) if isinstance(j, list) else (None, None, j[1] if isinstance(j, tuple) else 'bad answer')
    if k == 'ashby':
        j = get(f'https://api.ashbyhq.com/posting-api/job-board/{v}')
        return (len(j['jobs']), None, None) if isinstance(j, dict) and 'jobs' in j else \
            (None, None, j[1] if isinstance(j, tuple) else 'bad answer')
    if k == 'wd':
        t, pod, site = v.split('/')
        j = get(f'https://{t}.{pod}.myworkdayjobs.com/wday/cxs/{t}/{site}/jobs',
                {'appliedFacets': {}, 'limit': 1, 'offset': 0, 'searchText': ''})
        return (j.get('total', 0), None, None) if isinstance(j, dict) else (None, None, j[1])
    if k == 'sr':
        j = get(f'https://api.smartrecruiters.com/v1/companies/{v}/postings?limit=1')
        if isinstance(j, tuple):
            return None, None, j[1]
        name = ((j.get('content') or [{}])[0].get('company') or {}).get('name')
        return j.get('totalFound', 0), name, None
    return None, None, None


def name_ok(company, board_name):
    if not board_name:
        return True
    if match(idx, board_name) == cid_of.get(company):
        return True
    b = norm(board_name).replace(' ', '')
    names = [re.sub(r'\s*\(.*?\)', '', company)] + re.findall(r'\((?:formerly )?(.*?)\)', company)
    if any(n and (n in b or b in n) for n in (norm(x).replace(' ', '') for x in names)):
        return True
    # a shared distinctive word: "DiDi Labs" for DiDi Global, "The Allen Institute ..." for Ai2 (Allen Institute for AI)
    words = lambda t: {w for w in norm(t).split() if len(w) >= 4 and w not in GENERIC}
    return bool(words(board_name) & set().union(*(words(x) for x in names)))


GENERIC = {'global', 'labs', 'technology', 'technologies', 'solutions', 'entertainment', 'careers', 'career', 'jobs',
           'board', 'early', 'institute', 'international', 'systems', 'software', 'services', 'health', 'financial',
           'interactive', 'digital', 'network', 'networks', 'america', 'americas', 'company', 'referrals', 'only'}


def check(row):
    c, spec = row['Company'], row['jobs.py spec']
    n, name, err = board(spec)
    if err:
        return f'saved board {spec} did not work ({err}); find the right board or confirm it from the careers page'
    if basis.get(c) == spec:
        return None
    if not name_ok(c, name):
        return (f'saved board {spec} is named "{name}", not {c}; confirm it is where {c} posts its jobs '
                f'(careers page links to it; not a referral-only, freelance or internal board) or replace it')
    if n == 0:
        return f'saved board {spec} lists 0 jobs; confirm it is still the board the careers page uses, or replace it'
    return None


rows = [r for r in csv.DictReader(open(f'{TIMELINE}/sources.csv'))
        if r['jobs.py spec'].split(':')[0] in ('gh', 'lever', 'levereu', 'ashby', 'wd', 'sr')]
only = sys.argv[sys.argv.index('--only') + 1:] if '--only' in sys.argv else None
if only:
    rows = [r for r in rows if r['Company'] in only]
with cf.ThreadPoolExecutor(16) as ex:
    flags = {r['Company']: f for r, f in zip(rows, ex.map(check, rows)) if f}
path = f'{DATA}/source_flags.json'
if only:  # keep the other companies' flags from the last full check
    old = json.load(open(path)) if os.path.exists(path) else {}
    flags = {**{k: v for k, v in old.items() if k not in only}, **flags}
json.dump(dict(sorted(flags.items())), open(path, 'w'), indent=1)
print(f'checked {len(rows)} board specs, {len(flags)} flagged -> timeline/data/source_flags.json')
for k, v in sorted(flags.items()):
    print(f'  {k}: {v}')
