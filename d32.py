#!/usr/bin/env python3

import sys

def task(data, size, common):
    for idx in range(size):
        onedata  = [x for x in data if x[idx] == '1']
        zerodata = [x for x in data if x[idx] == '0']
        data = onedata if not ((len(onedata) >= len(zerodata)) ^ common) else zerodata
        if len(data) == 1:
            return data[0]

with open(sys.argv[1], 'r') as f:
    data = [line for line in f]

o2  = int(task(data, len(data[0]) - 1, True), base=2)
co2 = int(task(data, len(data[0]) - 1, False), base=2)
print(o2 * co2)
