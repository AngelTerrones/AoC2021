#!/usr/bin/env python3

import sys

def draw(paper):
    x, y = list(zip(*paper))
    mx = max(x) + 1
    my = max(y) + 1

    map = [["." for _ in range(mx)] for _ in range(my)]

    for x, y in paper:
        map[y][x] = '#'

    for line in map:
        for x in line:
            print(x, end='')
        print()


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    p = lines.index('\n')
    data = [[int(x) for x in line.split(",")] for line in lines[:p]]

    finst = []
    for line in lines[p + 1:]:
        axis, value = line.split("=")
        finst.append([axis[-1], int(value)])


for axis, piv in finst:
    axis = 0 if axis == 'x' else 1
    folded = []
    minaxis = sys.maxsize
    for p in data:
        if p[axis] < piv:
            folded.append(p)
        else:
            tmp = p.copy()
            tx = tmp[axis] = 2*piv - tmp[axis]
            if tmp not in data:
                folded.append(tmp)
            if tx < minaxis:
                minaxis = tx

    # fix the data for negative values
    if minaxis < 0:
        minaxis = abs(minaxis)
        for p in folded:
            p[axis] += minaxis

    data = folded

draw(data)
