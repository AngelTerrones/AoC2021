#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    data = [line.split(' ') for line in f]

dx = dy = 0
for dir, dist in data:
    dist = int(dist)
    if dir == 'forward':
        dx += dist
    elif dir == 'up':
        dy -= dist
    else:
        dy += dist

print(dx * dy)
