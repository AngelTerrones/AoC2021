#!/usr/bin/env python3

import sys

def update_boards(boards, value):
    for line in boards:
        for idx, cell in enumerate(line):
            if cell == value:
                line[idx] = -1

def check_boards(boards):
    # first pass:
    for idx, line in enumerate(boards):
        if sum(line) == -5:
            return True, (idx//5) * 5
    #second pass
    tmp = zip(*boards)
    for line in tmp:
        for idx in range(0, len(line), 5):
            if sum(line[idx:idx + 5]) == -5:
                return True, idx
    return False, -1

with open(sys.argv[1], 'r') as f:
    inputs = [int(x) for x in f.readline().split(',')]
    boards   = [[int(x) for x in line.split()] for line in f if line != '\n']

for value in inputs:
    update_boards(boards, value)
    done, idx = check_boards(boards)
    if done:
        winval = value
        break

score = sum([x for row in boards[idx:idx+5] for x in row if x != -1]) * winval
print(score)
