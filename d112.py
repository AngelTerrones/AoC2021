#!/usr/bin/env python3

import sys

N = 10

def update(map):
    tmp = []
    for y in range(N):
        for x in range(N):
            map[y][x] += 1
            if map[y][x] > 9:
                map[y][x] = 0
                tmp.append((x, y))
    return tmp

def flash(map, fp):
    while fp:
        tmp = []
        for x, y in fp:
            tmp.extend(update_surround(x, y, map))
        fp = tmp

def update_surround(x, y, map):
    back = []
    startx = 0 if x == 0 else x - 1
    starty = 0 if y == 0 else y - 1
    endx   = N if x == N - 1 else x + 2
    endy   = N if y == N - 1 else y + 2
    for idy in range(starty, endy):
        for idx in range(startx, endx):
            if map[idy][idx] == 0:
                continue
            map[idy][idx] += 1
            if map[idy][idx] > 9:
                map[idy][idx] = 0
                back.append((idx, idy))
    return back

def check_sync(map):
    ref = map[0][0]
    for y in range(N):
        for x in range(N):
            if map[y][x] != ref:
                return False
    return True

with open(sys.argv[1], 'r') as f:
    data = [[int(x) for x in line if x != '\n'] for line in f]

idx = 0
while True:
    idx += 1
    flash(data, update(data))
    if check_sync(data):
        print(idx)
        for l in data: print(l)
        break
