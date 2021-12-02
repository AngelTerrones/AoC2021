#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    data = [line.split(' ') for line in f]

aim = dy = dx = 0
for dir, dist in data:
    dist = int(dist)
    if dir == 'forward':
        dx += dist
        dy += aim * dist
    elif dir == 'up':
        aim -= dist
    else:
        aim += dist

print(dx * dy)
