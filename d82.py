#!/usr/bin/env python3

import sys

unique = {2:1, 4:4, 3:7, 7:8}

def get_keys(txt):
    tmp   = {unique[l] : set(dat) for dat in txt if (l := len(dat)) in unique.keys()}
    codex = {}

    for d, s in [(dat, set(dat)) for dat in txt if len(dat) == 6]:
        if not tmp[7].issubset(s):
            codex[d] = (6, s)
        elif tmp[4].issubset(s):
            codex[d] = (9, s)
            s9 = s
        else:
            codex[d] = (0, s)
    for d, s in [(dat, set(dat)) for dat in txt if len(dat) == 5]:
        if tmp[1].issubset(s):
            codex[d] = (3, s)
        elif s.issubset(s9):
            codex[d] = (5, s)
        else:
            codex[d] = (2, s)

    return codex

def  get_digit(x, codex):
    if (l := len(x)) in unique.keys():
        return unique[l]
    s = set(x)
    for v, sk in codex.values():
        if s == sk:
            return v

with open(sys.argv[1], 'r') as f:
    data = [(x[0].split(), x[1].split()) for line in f if len(x := line.split('|')) != 0]

acc = 0
for txt, disp in data:
    codex = get_keys(txt)
    acc  += sum([(10 ** idx) * get_digit(x, codex) for idx, x in enumerate(disp[::-1])])

print(acc)
