#!/usr/bin/env python3
"""After a research run: how long each company took, from the agents' transcripts -> timeline/data/company_minutes.json.

  timing.py [<workflow transcript dir> ...]

With no argument it reads the newest new-grad-research run of this repo (the Workflow tool prints its transcript dir).
Pass several dirs to read a run and its rerun.

Each agent starts a company's first Bash command with `: start <slug>;` (the workflow prompt asks for it), so a company
runs from its marker to the next one. Agents that skipped the markers get each tool call's time split among the
companies that call names (slug, company name, board or careers-site host); calls that name none go to the last company
named. Saved per slug with the date and method, merged over the last values, so a rerun only updates its companies.
worklist.py reads this file to balance the next run's batches.
"""
import datetime as dt, glob, json, os, re, sys
from common import *

OUT = f'{DATA}/company_minutes.json'
MARK = re.compile(r'(?<![\w-]):\s+start\s+([a-z0-9-]+)\s*;')


def ts(s):
    return dt.datetime.fromisoformat(s.replace('Z', '+00:00'))


def run_dirs():
    if len(sys.argv) > 1:
        return sys.argv[1:]
    proj = os.path.expanduser('~/.claude/projects/' + re.sub(r'[^A-Za-z0-9]', '-', REPO))
    runs = []
    for d in glob.glob(f'{proj}/*/subagents/workflows/wf_*'):
        first = sorted(glob.glob(f'{d}/agent-*.jsonl'))
        if first and 'new-grad timeline' in open(first[0]).read(20000):
            runs.append(d)
    if not runs:
        sys.exit('no new-grad-research run found; pass its transcript dir')
    return [max(runs, key=os.path.getmtime)]


def tokens(s):
    """Strings that name this company in a tool call: slug, company name, board id, careers-site host."""
    out = {s}
    p = f'{TIMELINE}/research/{s}.json'
    if os.path.exists(p):
        d = json.load(open(p))
        if len(d.get('company', '')) >= 4:
            out.add(d['company'].lower())
        spec = d.get('jobs_spec') or ''
        if ':' in spec and len(spec.split(':', 1)[1].split('/')[0]) >= 4:
            out.add(spec.split(':', 1)[1].split('/')[0].lower())
        host = re.sub(r'^https?://(www\.)?', '', d.get('jobs_page') or '').split('/')[0].lower()
        if host and not re.search(r'greenhouse|lever\.co|ashbyhq|myworkdayjobs|smartrecruiters|icims|workable', host):
            out.add(host)
    return [re.compile(r'(?<![a-z0-9])' + re.escape(t) + r'(?![a-z0-9])') for t in out]


def tool_text(x):
    c = x.get('message', {}).get('content')
    if not isinstance(c, list):
        return ''
    return ' '.join(json.dumps(b.get('input', '')) for b in c if b.get('type') == 'tool_use').lower()


def agent_minutes(path):
    T = [x for x in map(json.loads, open(path)) if x.get('timestamp')]
    if len(T) < 2:
        return {}, None
    slugs = []
    for x in T:
        for m in re.findall(r'timeline/research/([a-z0-9-]+)\.json', json.dumps(x.get('message', {}).get('content', ''))):
            if m not in slugs:
                slugs.append(m)
    gaps = [(ts(T[i + 1]['timestamp']) - ts(T[i]['timestamp'])).total_seconds() / 60 for i in range(len(T) - 1)]
    marks = [(i, m) for i, x in enumerate(T) for m in MARK.findall(tool_text(x))]
    sec = {}
    if len({m for _, m in marks}) >= max(2, len(slugs) // 2):
        # the time before the first marker is the agent reading the skill: shared overhead, left out
        for k, (i, m) in enumerate(marks):
            j = marks[k + 1][0] if k + 1 < len(marks) else len(T) - 1
            sec[m] = sec.get(m, 0) + sum(gaps[i:j])
        return sec, 'marker'
    pats = {s: tokens(s) for s in slugs}
    cur = None
    for i, x in enumerate(T[:-1]):
        text = tool_text(x)
        if text:
            hit = [s for s, ps in pats.items() if any(p.search(text) for p in ps)]
            if 0 < len(hit) <= 3:
                cur = hit
        for s in cur or []:
            sec[s] = sec.get(s, 0) + gaps[i] / len(cur)
    return sec, 'attributed'


old = json.load(open(OUT)) if os.path.exists(OUT) else {}
new, how = {}, {}
for d in run_dirs():
    for f in glob.glob(f'{d}/agent-*.jsonl'):
        mins, method = agent_minutes(f)
        for s, m in mins.items():
            new[s] = new.get(s, 0) + m
            how[s] = method
day = TODAY.isoformat()
for s, m in new.items():
    old[s] = {'minutes': round(m, 2), 'measured': day, 'method': how[s]}
json.dump(dict(sorted(old.items())), open(OUT, 'w'), indent=1)
v = sorted(new.values())
if v:
    q = lambda f: v[min(len(v) - 1, int(len(v) * f))]
    print(f'{len(v)} companies timed ({sum(1 for s in how.values() if s == "marker")} by marker): '
          f'median {q(.5):.1f} min, p90 {q(.9):.1f}, max {v[-1]:.1f}, total {sum(v):.0f} -> {OUT}')
    print('slowest:', ', '.join(f'{s} {m:.0f}' for s, m in sorted(new.items(), key=lambda kv: -kv[1])[:10]))
