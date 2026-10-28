#!/usr/bin/env python3
"""Print the recent-postings table for the end-of-run reply: open postings he hasn't applied to, posted (or, with no
posted date, discovered) in the last few days, newest discovered first. Postings this run found (not in the
snapshot at timeline/data/prev/postings.csv) are marked new. Reads timeline/postings.csv, so run it after merge.py.
Only postings in the New York, Bay Area, Seattle, LA, Austin, Vancouver, Toronto or Quebec areas, or remote, are kept (--any-location keeps
all). Each role links to its posting.

  recent.py [--days 7] [--max-tier 5] [--any-location]
"""
import csv, os, re, sys, datetime as dt

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(REPO, '.agents', 'skills', 'new-grad-timeline', 'scripts'))
from common import norm_url

arg = lambda name, default: int(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default
DAYS, MAX_TIER = arg('--days', 7), arg('--max-tier', 5)
since = (dt.date.today() - dt.timedelta(days=DAYS - 1)).isoformat()  # --days 7 on Oct 20: Oct 14 to Oct 20

# Metro areas, not just the city: the New York area takes in New Jersey, Long Island, Westchester and Fairfield County
# CT; Seattle the Puget Sound (Bellevue, Redmond, Bothell...); LA the whole region (Orange County, Ventura County, the
# Inland Empire); Austin its suburbs (Round Rock, Cedar Park...). Vancouver is BC, not Vancouver, WA; Quebec is the
# whole province. Any remote role counts, US or Canada or anywhere. Names other states share need the state code.
AREAS = {
    'NY': (r'new york|\bnyc\b|brooklyn|manhattan|queens|bronx|staten island|long island|westchester|white plains|'
           r'new jersey|\bnj\b|stamford|greenwich|norwalk|rowayton|westport|darien|danbury|bridgeport|'
           r'(melville|hauppauge|garden city|purchase|armonk|yonkers|tarrytown),? ny'),
    'Bay Area': (r'san francisco|\bsf\b|bay area|silicon valley|san mateo|mountain view|sunnyvale|cupertino|san jose|'
                 r'palo alto|menlo park|redwood city|redwood shores|santa clara|oakland|fremont|milpitas|foster city|'
                 r'berkeley|emeryville|burlingame|san carlos|los gatos|pleasanton|san bruno|san ramon|walnut creek|'
                 r'livermore|hayward|(belmont|campbell|newark|dublin|union city|alameda|richmond|concord),? ca'),
    'Seattle': (r'seattle|bellevue|redmond|kirkland|bothell|issaquah|renton|tukwila|lynnwood|sammamish|woodinville|'
                r'mercer island|tacoma|bremerton|puyallup|federal way|(everett|kent|auburn|kenmore|shoreline),? wa'),
    'LA': (r'los angeles|\bla\b|santa monica|culver city|playa vista|el segundo|burbank|pasadena|glendale|hawthorne|'
           r'torrance|long beach|venice|marina del rey|west hollywood|beverly hills|manhattan beach|redondo beach|'
           r'inglewood|calabasas|woodland hills|van nuys|northridge|santa clarita|valencia|thousand oaks|'
           r'westlake village|simi valley|camarillo|oxnard|ventura|irvine|costa mesa|santa ana|anaheim|newport beach|'
           r'huntington beach|aliso viejo|mission viejo|lake forest|tustin|fullerton|riverside|san bernardino|'
           r'rancho cucamonga|redlands|(carson|downey|cerritos|orange|brea|ontario|lakewood|san pedro|el monte|torrance),? ca'),
    'Austin': (r'austin|round rock|cedar park|pflugerville|san marcos|bee cave|lakeway|'
               r'(georgetown|leander|kyle|buda|hutto|manor|dripping springs),? tx'),
    'Canada': r'vancouver(?!,? wa)|burnaby|richmond,? bc|toronto|mississauga|markham|quebec|\bqc\b|montr[eé]al|laval',
    'Remote': r'remote|virtual|work from home|anywhere',
}
PLACES = re.compile('|'.join(f'(?:{v})' for v in AREAS.values()), re.I)
wanted = lambda loc: '--any-location' in sys.argv or bool(PLACES.search(loc))

when = lambda r: (r['Posted'] or r['Discovered'])[-10:]
rows = [r for r in csv.DictReader(open(f'{REPO}/timeline/postings.csv'))
        if not r['Applied'] and int(r['Tier']) <= MAX_TIER and when(r) >= since and wanted(r['Location'])]
PREV = f'{REPO}/timeline/data/prev/postings.csv'
seen = {norm_url(r['Link']) for r in csv.DictReader(open(PREV))} if os.path.exists(PREV) else None
is_new = lambda r: seen is not None and norm_url(r['Link']) not in seen
rows.sort(key=lambda r: (r['Discovered'][-10:], -int(r['Tier'])), reverse=True)  # newest discovered first, then by tier


def day(v):
    if not v:
        return '—'
    d = dt.date.fromisoformat(v[-10:])
    return ('≤ ' if v.startswith('on or') else '') + f'{d:%b} {d.day}'


cell = lambda s: (s or '').replace('|', '/')
where = 'any location' if '--any-location' in sys.argv else 'NY, Bay Area, Seattle, LA, Austin, Vancouver, Toronto or Quebec areas, or remote'
print(f'{len(rows)} postings since {day(since)}, tiers 1–{MAX_TIER}, {where}, not applied, posted (or, with no posted date, '
      'discovered) since then. Sorted by discovered date. '
      '**new** = found by this run.\n')
print('| Posted | Discovered | Company | Role | Tier | Location | Deadline |')
print('|---|---|---|---|---|---|---|')
for r in rows:
    print(f"| {day(r['Posted'])} | {day(r['Discovered'])}{' **new**' if is_new(r) else ''} | {cell(r['Company'])} | [{cell(r['Role']).replace('[', '(').replace(']', ')')}]({r['Link']}) | {r['Tier']} | "
          f"{cell(r['Location']) or '—'} | {cell(r['Deadline']) or '—'} |")
