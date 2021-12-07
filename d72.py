#!/usr/bin/env python3

import sys
import math

def cost(a, b):
    d = abs(a-b)
    return (d*(d + 1)) >> 1

with open(sys.argv[1], 'r') as f:
	data = [int(x) for line in f for x in line.split(',')]

d1    = math.ceil(sum(data)/len(data))
d2    = math.floor(sum(data)/len(data))
fuel1 = sum([cost(d1, crab) for crab in data])
fuel2 = sum([cost(d2, crab) for crab in data])
print(min(fuel1, fuel2))
