#!/usr/bin/env python3

import sys
import heapq as hp

with open(sys.argv[1], 'r') as f:
    data = [[int(x) for x in line if x != '\n'] for line in f]

N       = len(data)
risk    = {(0,0): 0}
visited = set()
heap    = [(0, (0, 0))]
while True:
    dist, piv = hp.heappop(heap)
    if piv == (N-1,N-1):
        break
    visited.add(piv)
    x, y = piv
    n = [] if y == 0     else [(x, y - 1)]
    s = [] if y == N - 1 else [(x, y + 1)]
    w = [] if x == 0     else [(x - 1, y)]
    e = [] if x == N - 1 else [(x + 1, y)]

    for idx, idy in n + s + w + e:
        if (idx, idy) in visited:
            continue
        newrisk = dist + data[idy][idx]
        if newrisk < risk.get((idx, idy), sys.maxsize):
            risk[(idx, idy)] = newrisk
            hp.heappush(heap, (newrisk, (idx, idy)))

print(dist)
