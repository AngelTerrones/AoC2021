#!/usr/bin/env python3

import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    filedata = f.read()

data = [int(x) for x in filedata.split('\n') if x != '']

countpp = 0
for idx, value in enumerate(data):
    if idx == 0:
        pass
    elif value > data[idx - 1]:
        countpp += 1

print(countpp)
