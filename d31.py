#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    data = [''.join(x) for x in list(zip(*[line for line in f]))[:-1]]

gamma = epsilon = 0

for bits in data:
    isBit1 = bits.count('1') > bits.count('0')
    gamma = gamma << 1
    gamma += 1 if isBit1 else 0
    epsilon = epsilon << 1
    epsilon += 0 if isBit1 else 1

print(gamma * epsilon)
