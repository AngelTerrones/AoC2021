#!/usr/bin/env python3

import sys

def check_cell(x, y, X, Y, map):
    cell = map[y][x]
    if cell == 0:
        return 1
    if cell == 9:
        return 0

    n = True if y == 0 else cell < map[y - 1][x]
    s = True if y == Y else cell < map[y + 1][x]
    e = True if x == 0 else cell < map[y][x - 1]
    w = True if x == X else cell < map[y][x + 1]

    if n and s and e and w:
        return cell + 1

    return 0


with open(sys.argv[1], 'r') as f:
    data = [[int(x) for x in line if x != '\n'] for line in f]

Y = len(data)
X = len(data[0])
acc = sum(check_cell(i, j, X - 1, Y - 1, data) for j in range(Y) for i in range(X))
print(acc)
