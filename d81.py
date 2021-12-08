#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    data = [(x[0].split(), x[1].split()) for line in f if len(x := line.split('|')) != 0]

unique = sum([1 for _, disp in data for i in disp if len(i) in [2, 4, 3, 7]])
print(unique)
