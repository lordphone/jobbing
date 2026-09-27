#!/usr/bin/env python3
"""Rewrite the counts in timeline/COMPANY_LIST.md ("N companies." and each "## k. Tier (n)") after editing the list."""
import os, re

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
P = os.path.join(REPO, 'timeline', 'COMPANY_LIST.md')
lines = open(P).read().split('\n')
heads, total, cur = {}, 0, None
for i, l in enumerate(lines):
    if re.match(r'## \d+\. .* \(\d+\)$', l):
        cur = i
        heads[i] = 0
    elif l.startswith('- ') and cur is not None:
        heads[cur] += 1
        total += 1
for i, n in heads.items():
    lines[i] = re.sub(r'\(\d+\)$', f'({n})', lines[i])
lines = [re.sub(r'^\d+ companies\.$', f'{total} companies.', l) for l in lines]
open(P, 'w').write('\n'.join(lines))
print(f'{total} companies in {len(heads)} tiers')
