#!/usr/bin/env python3

import sys
from statistics import median

matches = {'[':']', '{':'}', '(':')', '<':'>'}
score   = {'[': 2, '{': 3, '(': 1, '<': 4}

def get_score(line):
    stack = []
    for x in line[:-1]:
        if x in ('[', '{', '(', '<'):
            stack.append(x)
        else:
            q = stack.pop()
            if x != matches[q]:
                return 0

    acc = 0
    for x in stack[::-1]:
        acc = (5 * acc) + score[x]
    return acc

with open(sys.argv[1], 'r') as f:
    data = [line for line in f]

r = [v for x in data if (v := get_score(x)) != 0]
r.sort()
print(median(r))
