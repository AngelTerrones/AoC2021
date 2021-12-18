#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    p = lines.index('\n')
    data = [[int(x) for x in line.split(",")] for line in lines[:p]]

    finst = lines[p + 1].split('=')
    axis  = 0 if finst[0][-1] == 'x' else 1
    piv   = int(finst[1])

acc = 0
for p in data:
    if p[axis] < piv:
        acc += 1
    else:
        t2 = p.copy()
        t2[axis] = 2*piv - t2[axis]
        if t2 not in data:
            acc += 1

print(acc)
