#!/usr/bin/env python3

import sys
# ----------------------------------------------------------------------------------------
with open(sys.argv[1], 'r') as f:
    data = [[int(z) for z in x.split('=')[1].split('..')] for x in f.readline().split(',')]

x0 = data[0][0]
x1 = data[0][1]
y0 = data[1][0]
y1 = data[1][1]

Vy = abs(y0) - 1  # max velocity in Y is when the probe reaches the most negative Y value after cossing Y=0 in one step
print(Vy*(Vy + 1)//2) # and the max velocity is an arithmetic progression with d=1.
