#!/usr/bin/env python3

import sys
from math import sqrt
import itertools as itt

# ----------------------------------------------------------------------------------------
with open(sys.argv[1], 'r') as f:
    data = [[int(z) for z in x.split('=')[1].split('..')] for x in f.readline().split(',')]

x0 = data[0][0]
x1 = data[0][1]
y0 = data[1][0]
y1 = data[1][1]

vxmin = int(sqrt(2 * x0))
vxmax = x1
vymin = y0
vymax = -(y0 + 1)

vtest = list(itt.product([i for i in range(vxmin, vxmax + 1)], [i for i in range(vymin, vymax + 1)]))

count = 0
for vx, vy in vtest:
    # launch
    px, py = 0, 0
    while True:
        # move
        px += vx
        py += vy
        # update velocity
        if vx > 0:
            vx -= 1
        vy -= 1
        # check for exit:
        if px > x1 or py < y0:
            break
        if px < x0 and (vx == 0 or py < y0):
            break
        # check for hit
        if px >= x0 and px <= x1 and py >= y0 and py <= y1:
            count += 1
            break

print(count)
