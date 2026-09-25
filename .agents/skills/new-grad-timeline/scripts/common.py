import json, re, os, datetime as dt

S = os.path.dirname(os.path.abspath(__file__))  # this scripts/ folder
REPO = os.path.abspath(os.path.join(S, '..', '..', '..', '..'))
TIMELINE = os.path.join(REPO, 'timeline')
DATA = os.path.join(TIMELINE, 'data')  # intermediate files: trackers.json, boards.json, worklist.json, ...
CACHE = os.path.join(os.environ.get('TMPDIR', '/tmp'), 'newgrad-trackers')  # tracker repo clones (re-downloadable)
TODAY = dt.date.fromisoformat(os.environ['NEWGRAD_TODAY']) if os.environ.get('NEWGRAD_TODAY') else dt.date.today()
# Hiring cycle being tracked. For the 2028 cycle, move each date forward one year.
CYCLE_START = dt.date(2026, 7, 1)  # 2027 new-grad cycle
LAST_START, LAST_END = dt.date(2025, 7, 1), dt.date(2026, 1, 31)  # last cycle (2026 grads)
PREV_START, PREV_END = dt.date(2024, 7, 1), dt.date(2025, 1, 31)  # two cycles ago

STOP = {'inc', 'llc', 'ltd', 'corp', 'corporation', 'co', 'company', 'the', 'holdings', 'group',
        'plc', 'lp', 'llp', 'sa', 'ag', 'nv', 'us', 'usa', 'america', 'americas', 'north'}


def norm(s):
    s = s.lower().replace('&', ' and ')
    s = re.sub(r'\.(com|ai|io|dev|co)\b', r' \1', s)
    s = re.sub(r'[^a-z0-9 ]+', ' ', s)
    toks = [t for t in s.split() if t not in STOP]
    return ' '.join(toks)


def load_companies():
    out, tier, tiername = [], None, None
    for line in open(f'{REPO}/timeline/COMPANY_LIST.md'):
        m = re.match(r'## (\d+)\. (.*) \(\d+\)', line)
        if m:
            tier, tiername = int(m.group(1)), m.group(2)
            continue
        if not line.startswith('- '):
            continue
        name = line[2:].strip()
        aliases = set()
        base = re.sub(r'\s*\(.*?\)', '', name).strip()
        for part in re.split(r'\s*/\s*', base):
            aliases.add(part)
        for inner in re.findall(r'\((.*?)\)', name):
            inner = re.sub(r'^(formerly|incl\.|a division of)\s*', '', inner, flags=re.I)
            if 'subsidiary' in inner or 'division' in inner:
                continue
            for part in re.split(r'\s*[/,]\s*', inner):
                aliases.add(part)
        aliases.add(base)
        keys = {norm(a) for a in aliases if norm(a)}
        out.append({'id': len(out), 'tier': tier, 'tier_name': tiername, 'name': name,
                    'aliases': sorted(aliases), 'keys': sorted(keys)})
    return out


NS = {}


def build_index(companies):
    idx = {}
    for c in companies:
        for k in c['keys']:
            idx.setdefault(k, c['id'])
    NS[id(idx)] = {k.replace(' ', ''): v for k, v in idx.items()}
    by_name = {c['name']: c['id'] for c in companies}
    OVR.clear()
    OVR.update({k: by_name[v] for k, v in OVR_NAMES.items() if v in by_name})
    return idx


# overrides.json: normalized tracker company name -> exact name in COMPANY_LIST.md (for names matching can't guess)
OVR_NAMES = json.load(open(os.path.join(S, 'overrides.json'))) if os.path.exists(os.path.join(S, 'overrides.json')) else {}
OVR = {}


def match(idx, name):
    k = norm(name)
    if k in OVR:
        return OVR[k]
    if k.replace(' ', '') in NS.get(id(idx), {}):
        return NS[id(idx)][k.replace(' ', '')]
    if k in idx:
        return idx[k]
    # try dropping trailing generic words
    for suf in (' technologies', ' technology', ' labs', ' ai', ' systems', ' software', ' financial',
                ' bank', ' inc', ' international', ' global', ' services', ' solutions'):
        if k.endswith(suf) and k[: -len(suf)] in idx:
            return idx[k[: -len(suf)]]
    return None


ROLE = re.compile(r'software|\bswe\b|\bsde\b|back.?end|full.?stack|front.?end|machine learning|\bml\b|\bai\b|'
                  r'developer|platform|infrastructure|forward.?deployed|applied|cloud|devops|site reliab|'
                  r'\bsre\b|mobile|ios|android|web|data engineer|systems engineer|programmer|quant(itative)? dev|'
                  r'research engineer|member of technical', re.I)
ENG = re.compile(r'engineer|developer|\bsde\b|\bswe\b|programmer|technical staff|technologist', re.I)
SENIOR = re.compile(r'\b(senior|sr\.?|staff|principal|lead|manager|director|head of|intern|internship|co-?op|'
                    r'ii|iii|iv|2|3)\b', re.I)
EXCL_ROLE = re.compile(r'hardware|electrical|mechanical|analog|asic|fpga|rtl|verification|manufactur|'
                       r'civil|chemical|process engineer|field service|sales engineer|solutions engineer|'
                       r'test technician|physical design|circuit|firmware|embedded|rf ', re.I)
NEWGRAD = re.compile(r'new grad|new college|university|graduate|early career|entry|campus|2026|2027|'
                     r'associate|junior|\bi\b|\b1\b|rotational|residency|fellow|emerging talent|class of', re.I)
CLEAR = re.compile(r'clearance|cleared|\bts/sci\b|top secret|\bsecret\b|polygraph|\bsci\b|u\.?s\.? citizen', re.I)

STATES = set('AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC '
             'ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC'.split())


def is_us(locs):
    if not locs:
        return True
    for l in locs:
        if re.search(r'\b(USA|US|United States|U\.S\.)\b', l) or re.search(r'remote', l, re.I) and not re.search(
                r'canada|uk|india|europe|mexico', l, re.I):
            return True
        m = re.search(r',\s*([A-Z]{2})\b', l)
        if m and m.group(1) in STATES:
            return True
        if re.search(r'alabama|alaska|arizona|arkansas|california|colorado|connecticut|delaware|florida|georgia|hawaii|idaho|illinois|indiana|iowa|kansas|kentucky|louisiana|maine|maryland|massachusetts|michigan|minnesota|mississippi|missouri|montana|nebraska|nevada|new hampshire|new jersey|new mexico|north carolina|north dakota|ohio|oklahoma|oregon|pennsylvania|rhode island|south carolina|south dakota|tennessee|texas|utah|vermont|virginia|washington|wisconsin|wyoming', l, re.I):
            return True
        if re.search(r'new york|san francisco|seattle|boston|chicago|austin|nyc|bay area|los angeles', l, re.I):
            return True
    return False


def is_role(title):
    return bool(ROLE.search(title) and ENG.search(title) and not SENIOR.search(title)
                and not EXCL_ROLE.search(title))


def d(ts):
    return dt.date.fromtimestamp(ts)
