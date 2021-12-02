#!/usr/bin/env python3
import sys

with open(sys.argv[1], 'r') as f:
    data = [int(line) for line in f]

countpp = 0
for idx in range(len(data) - 2):
    A = sum(data[idx:idx + 3])
    B = sum(data[idx + 1:idx + 4])
    if B > A:
        countpp += 1

print(countpp)
