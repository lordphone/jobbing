#!/usr/bin/env python3
"""First-party job-board lookups for new-grad research. Standard library only.

  jobs.py board SPEC [--all]     list new-grad-looking postings (title | location | date | url)
  jobs.py guess NAME [SLUG...]   try Greenhouse / Lever / Ashby / SmartRecruiters slugs for a company
  jobs.py workday TENANT [SITE...]   find a Workday board (tries wd1..wd503 and common site names)
  jobs.py detail URL             fetch one posting's text; print dates and citizenship / clearance /
                                 sponsorship / graduation lines
  jobs.py history REGEX          SimplifyJobs + vanshb03 tracker history for a company (last-year dates)

SPEC forms:
  gh:SLUG   lever:SLUG   levereu:SLUG   ashby:SLUG   sr:COMPANY_ID   wd:TENANT/wdN/SITE   oracle:HOST/SITE_NUMBER
  pinpoint:SUBDOMAIN   eightfold:HOST/DOMAIN (careers sites with /api/pcsx/search)   amazon:
"""
import datetime as dt, html, json, os, re, subprocess, sys, urllib.parse, urllib.request

NEWGRAD = re.compile(r'new grad|new college|college grad|university|graduate|early career|early in career|entry.level|'
                     r'campus|2027|junior|associate|engineer,? i\b|engineer,? 1\b|developer,? i\b|level 1\b|rotation|'
                     r'residen|apprentice|emerging talent|class of|amts|analyst program|development program', re.I)
ROLE = re.compile(r'software|engineer|developer|\bsde\b|\bswe\b|machine learning|\bml\b|\bai\b|full.?stack|back.?end|'
                  r'platform|technolog|programmer|member of technical', re.I)
SKIP = re.compile(r'\bintern\b|internship|co-?op|senior|\bsr\b|staff|principal|\blead\b|manager|director', re.I)
FLAGS = re.compile(r'[^.]{0,140}(u\.?s\.? citizen|citizenship|security clearance|clearance|green card|permanent resident|'
                   r'u\.?s\.? person|itar|export control|sponsor|work authori[sz]ation|graduat|years of experience)'
                   r'[^.]{0,140}', re.I)
WD_SITES = ['External', 'Careers', 'careers', 'External_Careers', 'ExternalCareers', 'External_Career_Site', 'Jobs',
            'jobs', 'Search', 'University', 'Campus', 'EarlyCareers', 'Early_Careers', 'en-US']
WD_PODS = ['wd1', 'wd3', 'wd5', 'wd12', 'wd103', 'wd108', 'wd501', 'wd503', 'wd504']


def get(url, data=None, timeout=25):
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data is not None else None,
                                 headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/json',
                                          'Accept': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read())
    except Exception:
        return None


def text(h):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', html.unescape(h or ''))))


def ms(t):
    return dt.date.fromtimestamp(t / 1000).isoformat() if t else ''


# ---- boards: each returns list of (title, location, date, url) or None ----
def b_gh(slug):
    d = get(f'https://boards-api.greenhouse.io/v1/boards/{slug}/jobs')
    if not d or 'jobs' not in d:
        return None
    return [(j['title'], (j.get('location') or {}).get('name', ''),
             'first ' + (j.get('first_published') or '')[:10] if j.get('first_published') else 'upd ' + j.get('updated_at', '')[:10],
             j['absolute_url']) for j in d['jobs']]


def b_lever(slug, host='api.lever.co'):
    d = get(f'https://{host}/v0/postings/{slug}?mode=json')
    if not isinstance(d, list) or not d:
        return None
    return [(j['text'], (j.get('categories') or {}).get('location', ''), ms(j.get('createdAt')), j['hostedUrl']) for j in d]


def b_ashby(slug):
    d = get(f'https://api.ashbyhq.com/posting-api/job-board/{slug}')
    if not d or not d.get('jobs'):
        return None
    return [(j['title'], j.get('location', ''), (j.get('publishedAt') or '')[:10], j.get('jobUrl')) for j in d['jobs']]


def b_sr(cid, q=''):
    out, off = [], 0
    while True:
        d = get(f'https://api.smartrecruiters.com/v1/companies/{cid}/postings?limit=100&offset={off}&q={urllib.parse.quote(q)}')
        if not d or not d.get('content'):
            break
        for j in d['content']:
            loc = j.get('location') or {}
            out.append((j['name'], f"{loc.get('city', '')}, {loc.get('region', '')}, {loc.get('country', '')}",
                        (j.get('releasedDate') or '')[:10], f"https://jobs.smartrecruiters.com/{cid}/{j['id']}"))
        off += 100
        if off >= d.get('totalFound', 0) or off > 1000:
            break
    return out or None


def b_wd(spec, queries=('new grad', 'university', 'early career', 'college graduate', 'entry level', 'graduate',
                        '2027', 'associate software', 'software engineer I', 'junior')):
    tenant, pod, site = spec.split('/')
    base = f'https://{tenant}.{pod}.myworkdayjobs.com'
    out, seen, ok = [], set(), False
    for q in queries:
        d = get(f'{base}/wday/cxs/{tenant}/{site}/jobs', {'appliedFacets': {}, 'limit': 20, 'offset': 0, 'searchText': q})
        if d is None:
            continue
        ok = True
        for j in d.get('jobPostings', []):
            p = j.get('externalPath', '')
            if p in seen:
                continue
            seen.add(p)
            out.append((j.get('title', ''), j.get('locationsText', ''), j.get('postedOn', ''), f'{base}/{site}{p}'))
    return out if ok else None


def b_oracle(spec, queries=('graduate', 'new grad', 'university', 'entry level', 'early career', 'associate', 'software engineer')):
    host, site = spec.rsplit('/', 1)
    out, seen, ok = [], set(), False
    for q in queries:
        u = (f'https://{host}/hcmRestApi/resources/latest/recruitingCEJobRequisitions?onlyData=true'
             f'&expand=requisitionList.secondaryLocations&finder=findReqs;siteNumber={site},limit=50,'
             f'keyword={urllib.parse.quote(q)},sortBy=POSTING_DATES_DESC')
        d = get(u)
        if not d or not d.get('items'):
            continue
        ok = True
        for r in d['items'][0].get('requisitionList', []):
            if r['Id'] in seen:
                continue
            seen.add(r['Id'])
            out.append((r['Title'], r.get('PrimaryLocation', ''), r.get('PostedDate', ''),
                        f'https://{host}/hcmUI/CandidateExperience/en/sites/{site}/job/{r["Id"]}'))
    return out if ok else None


def b_amazon(_=''):
    out, seen = [], set()
    for q in ('new grad', 'university graduate', 'early career', '2027', 'software development engineer I'):
        d = get(f'https://www.amazon.jobs/en/search.json?base_query={urllib.parse.quote(q)}&country=USA&result_limit=100')
        for j in (d or {}).get('jobs', []):
            if j['id_icims'] in seen:
                continue
            seen.add(j['id_icims'])
            out.append((j['title'], j.get('normalized_location', ''), j.get('posted_date', ''),
                        'https://www.amazon.jobs' + j['job_path']))
    return out or None


def b_pinpoint(sub):
    d = get(f'https://{sub}.pinpointhq.com/postings.json')
    if not d or not d.get('data'):
        return None
    return [(j['title'], (j.get('location') or {}).get('name', ''), '', f"https://{sub}.pinpointhq.com{j.get('path', '')}")
            for j in d['data']]


def b_eightfold(spec, queries=('graduate', 'new grad', 'university', 'early career', 'entry level', 'associate', 'software engineer')):
    host, domain = spec.split('/')
    out, seen, ok = [], set(), False
    for q in queries:
        d = get(f'https://{host}/api/pcsx/search?domain={domain}&query={urllib.parse.quote(q)}'
                f'&location=United%20States&start=0')
        if not d or not isinstance(d.get('data'), dict):
            continue
        ok = True
        for p in d['data'].get('positions', []):
            if p['id'] in seen:
                continue
            seen.add(p['id'])
            ts = p.get('postedTs') or p.get('creationTs')
            out.append((p['name'], ';'.join(p.get('standardizedLocations') or p.get('locations') or []),
                        dt.date.fromtimestamp(ts).isoformat() if ts else '', f"https://{host}{p.get('positionUrl', '')}"))
    return out if ok else None


BOARDS = {'amazon': b_amazon, 'levereu': lambda s: b_lever(s, 'api.eu.lever.co'), 'pinpoint': b_pinpoint,
          'eightfold': b_eightfold, 'gh': b_gh, 'lever': b_lever, 'ashby': b_ashby, 'sr': b_sr, 'wd': b_wd, 'oracle': b_oracle}


def board(spec, show_all=False):
    kind, _, rest = spec.partition(':')
    jobs = BOARDS[kind](rest)
    if jobs is None:
        print(f'{spec}: not found / no response')
        return None
    hits = [j for j in jobs if show_all or (NEWGRAD.search(j[0]) and ROLE.search(j[0]) and not SKIP.search(j[0]))]
    print(f'{spec}: {len(jobs)} postings fetched, {len(hits)} shown')
    for j in hits:
        print('  ' + ' | '.join(str(x) for x in j))
    return jobs


def guess(name, extra):
    base = re.sub(r'[^a-z0-9 ]', '', name.lower().replace('&', 'and')).split()
    slugs = list(dict.fromkeys(extra + [''.join(base), '-'.join(base), ''.join(base) + 'hq', ''.join(base) + 'inc',
                                        ''.join(base) + 'careers', ''.join(base) + 'ai']))
    for s in slugs:
        for kind in ('gh', 'ashby', 'lever', 'sr'):
            jobs = BOARDS[kind](s)
            if jobs:
                extra_info = ''
                if kind == 'gh':
                    extra_info = ' name=' + str((get(f'https://boards-api.greenhouse.io/v1/boards/{s}') or {}).get('name'))
                print(f'{kind}:{s}  {len(jobs)} postings{extra_info}  e.g. {jobs[0][0]} | {jobs[0][1]}')
    print('Check the board name / sample titles really belong to this company before using it.')


def workday(tenant, sites):
    for pod in WD_PODS:
        for s in list(dict.fromkeys(sites + WD_SITES + [tenant, tenant.capitalize(), tenant.upper(), tenant + '_careers',
                                                         tenant + 'careers', tenant.capitalize() + '_Careers'])):
            d = get(f'https://{tenant}.{pod}.myworkdayjobs.com/wday/cxs/{tenant}/{s}/jobs',
                    {'appliedFacets': {}, 'limit': 1, 'offset': 0, 'searchText': ''}, timeout=10)
            if d and 'total' in d:
                print(f'wd:{tenant}/{pod}/{s}  total={d["total"]}')
                return
    print('not found — get the exact URL from the careers page ("Search jobs" link) or a search result')


def detail(url):
    u = urllib.parse.urlparse(url)
    t, title, dates = '', '', ''
    m = re.search(r'greenhouse\.io/(?:embed/job_app\?for=)?([\w-]+)/jobs/(\d+)', url) or \
        (re.search(r'gh_jid=(\d+)', url) and None)
    if m:
        j = get(f'https://boards-api.greenhouse.io/v1/boards/{m.group(1)}/jobs/{m.group(2)}?content=true') or {}
        title, t = j.get('title', ''), text(j.get('content'))
        dates = f"first_published={j.get('first_published')} updated={j.get('updated_at')}"
    elif 'myworkdayjobs.com' in u.netloc:
        tenant = u.netloc.split('.')[0]
        parts = [p for p in u.path.split('/') if p]
        if re.match(r'[a-z]{2}-[A-Z]{2}$', parts[0]):
            parts = parts[1:]
        site, path = parts[0], '/'.join(parts[1:])
        j = (get(f'https://{u.netloc}/wday/cxs/{tenant}/{site}/{path}') or {}).get('jobPostingInfo', {})
        title, t = j.get('title', ''), text(j.get('jobDescription'))
        dates = f"postedOn={j.get('postedOn')} startDate={j.get('startDate')} timeType={j.get('timeType')}"
    elif 'lever.co' in u.netloc:
        slug, jid = [p for p in u.path.split('/') if p][:2]
        api = 'api.eu.lever.co' if '.eu.' in u.netloc else 'api.lever.co'
        j = get(f'https://{api}/v0/postings/{slug}/{jid}') or {}
        title = j.get('text', '')
        t = text(j.get('description', '') + ' '.join(x.get('content', '') for x in j.get('lists', [])) + j.get('additional', ''))
        dates = f"createdAt={ms(j.get('createdAt'))}"
    elif 'ashbyhq.com' in u.netloc:
        slug, jid = [p for p in u.path.split('/') if p][:2]
        for j in (get(f'https://api.ashbyhq.com/posting-api/job-board/{slug}') or {}).get('jobs', []):
            if jid in (j.get('jobUrl') or '') or j.get('id') == jid:
                title, t, dates = j['title'], j.get('descriptionPlain', ''), f"publishedAt={j.get('publishedAt')}"
    elif 'smartrecruiters.com' in u.netloc:
        cid, jid = [p for p in u.path.split('/') if p][:2]
        jid = jid.split('-')[0]
        j = get(f'https://api.smartrecruiters.com/v1/companies/{cid}/postings/{jid}') or {}
        title = j.get('name', '')
        t = text(' '.join(s.get('text', '') for s in ((j.get('jobAd') or {}).get('sections') or {}).values()))
        dates = f"releasedDate={j.get('releasedDate')}"
    elif '/hcmUI/CandidateExperience' in url:
        site = re.search(r'/sites/([^/]+)/', url).group(1)
        jid = re.search(r'/job/(\d+)', url).group(1)
        d = get(f'https://{u.netloc}/hcmRestApi/resources/latest/recruitingCEJobRequisitionDetails?expand=all'
                f'&onlyData=true&finder=ById;Id=%22{jid}%22,siteNumber={site}') or {}
        j = (d.get('items') or [{}])[0]
        title = j.get('Title', '')
        t = text(''.join(j.get(k) or '' for k in ('ExternalDescriptionStr', 'ExternalQualificationsStr',
                                                  'ExternalResponsibilitiesStr')))
        dates = f"posted={j.get('ExternalPostedStartDate')}"
    else:
        print('No API for this host. Open it in the browser pane (it renders JavaScript) or WebFetch it.')
        return
    if not title:
        print('Posting not found via API — it may be closed. Confirm in the browser pane.')
        return
    print(title, '|', dates)
    for s in list(dict.fromkeys(m.group(0).strip() for m in FLAGS.finditer(t)))[:8]:
        print('  >', s[:300])


CACHE = os.path.join(os.environ.get('TMPDIR', '/tmp'), 'newgrad-trackers')


def history(rx):
    """Company postings from tracker history, with first-seen dates. Clones the trackers once into $TMPDIR."""
    os.makedirs(CACHE, exist_ok=True)
    repos = {'SimplifyJobs/New-Grad-Positions': '.github/scripts/listings.json',
             'vanshb03/New-Grad-2027': '.github/scripts/listings.json'}
    files = []
    for r, path in repos.items():
        d = os.path.join(CACHE, r.split('/')[1])
        if not os.path.isdir(d):
            subprocess.run(['git', 'clone', '-q', '--filter=blob:none', f'https://github.com/{r}.git', d], check=True)
        files.append(os.path.join(d, path))
        if r.startswith('SimplifyJobs'):  # the file is reset each cycle; keep monthly snapshots of past cycles
            for day in ('2025-05-25', '2025-09-15', '2025-12-15', '2026-01-26'):
                snap = os.path.join(CACHE, f'simplify_{day}.json')
                if not os.path.exists(snap):
                    h = subprocess.run(['git', '-C', d, 'log', '--format=%h', f'--until={day}', '-1', '--', path],
                                       capture_output=True, text=True).stdout.strip()
                    if h:
                        with open(snap, 'w') as f:
                            subprocess.run(['git', '-C', d, 'show', f'{h}:{path}'], stdout=f, check=True)
                files.append(snap)
    arch = os.path.join(CACHE, 'New-Grad-2027', 'archived', '2025', 'listings.json')
    if os.path.exists(arch):
        files.append(arch)
    seen, rows = set(), []
    for fn in files:
        if not os.path.exists(fn):
            continue
        for x in json.load(open(fn)):
            if re.search(rx, x.get('company_name', ''), re.I) and x.get('category') not in ('Hardware', 'Product'):
                if x['id'] in seen:
                    continue
                seen.add(x['id'])
                rows.append((dt.date.fromtimestamp(x['date_posted']).isoformat(), 'active' if x.get('active') else 'closed',
                             (x.get('sponsorship') or '')[:14], x['title'][:70], ';'.join(x.get('locations') or [])[:40],
                             x.get('url', '')[:110]))
    for r in sorted(rows):
        print(' | '.join(r))
    print(f'{len(rows)} postings. Last cycle = first new-grad SWE posting between 2025-07 and 2026-01.')


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        print(__doc__)
    elif a[0] == 'board':
        board(a[1], '--all' in a)
    elif a[0] == 'guess':
        guess(a[1], a[2:])
    elif a[0] == 'workday':
        workday(a[1], a[2:])
    elif a[0] == 'detail':
        detail(a[1])
    elif a[0] == 'history':
        history(a[1])
    else:
        print(__doc__)
