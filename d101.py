#!/usr/bin/env python3

import sys

matches = {'[':']', '{':'}', '(':')', '<':'>'}
score   = {']': 57, '}': 1197, ')': 3, '>': 25137}

def get_score(line):
    stack = []
    for x in line[:-1]:
        if x in ('[', '{', '(', '<'):
            stack.append(x)
        else:
            q = stack.pop()
            if x != matches[q]:
                return score[x]
    return 0

with open(sys.argv[1], 'r') as f:
    data = [line for line in f]

#print([is_corrupted(x) for x in data])
print(sum(get_score(x) for x in data))
