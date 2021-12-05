#!/usr/bin/env python3

import sys

def update_boards(boards, value):
    for line in boards:
        for idx, cell in enumerate(line):
            if cell == value:
                line[idx] = -1

def check_boards(boards, winners):
    finalboard = -1
    if winners.count(False) == 1:
        finalboard = winners.index(False)
    # first pass:
    for idx, line in enumerate(boards):
        if sum(line) == -5:
            _idx = idx//5
            winners[_idx] = True
            if _idx == finalboard:
                return True, finalboard * 5
    #second pass
    tmp = zip(*boards)
    for line in tmp:
        for idx in range(0, len(line), 5):
            if sum(line[idx:idx + 5]) == -5:
                _idx = idx//5
                winners[_idx] = True
                if _idx == finalboard:
                    return True, finalboard * 5

    return False, -1

with open(sys.argv[1], 'r') as f:
    inputs = [int(x) for x in f.readline().split(',')]
    boards   = [[int(x) for x in line.split()] for line in f if line != '\n']

winners = [False for _ in range(len(boards)//5)]
for value in inputs:
    update_boards(boards, value)
    done, idx = check_boards(boards, winners)
    if done:
        winval = value
        break

score = sum([x for row in boards[idx:idx+5] for x in row if x != -1]) * winval
print(score)
