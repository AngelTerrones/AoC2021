#!/usr/bin/env python3

import sys
from statistics import median

with open(sys.argv[1], 'r') as f:
	data = [int(x) for line in f for x in line.split(',')]

pivot = int(median(data))
fuel = sum([abs(pivot - crab) for crab in data])
print(fuel)
