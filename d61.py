#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
	data = [int(x) for line in f for x in line.split(',')]

NDAY  = 80
days  = [0 for x in range(NDAY)]
total = len(data)
# First round
for fish in data:
    for i in range((NDAY + (6 - fish)) // 7):
        days[fish + i*7] += 1
# offpring
for day, count in enumerate(days):
    if count != 0:
        total += count
        for idx in range(day + 9, NDAY, 7):
            days[idx] += count

print(total)
