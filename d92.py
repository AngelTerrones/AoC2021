#!/usr/bin/env python3

import sys
import math

class Cell():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return '({},{})'.format(self.x, self.y)
    def __str__(self):
        return '({},{})'.format(self.x, self.y)

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

def is_root(cell, SX, SY, map):
    value = map[cell.y][cell.x]
    if value == 0:
        return True
    if value == 9:
        return False

    n = True if cell.y == 0 else value < map[cell.y - 1][cell.x]
    s = True if cell.y == SY - 1 else value < map[cell.y + 1][cell.x]
    e = True if cell.x == 0 else value < map[cell.y][cell.x - 1]
    w = True if cell.x == SX - 1 else value < map[cell.y][cell.x + 1]

    return n and s and e and w

def cell_in_basin(cell, basins):
    for basin in basins:
        if cell in basin:
            return True
    return False

def get_nsew_nodes(cell, SX, SY):
    nsewcoord = [(cell.x + 1, cell.y), (cell.x - 1, cell.y), (cell.x, cell.y + 1), (cell.x, cell.y - 1)]
    return [Cell(x, y) for x, y in nsewcoord if x >= 0 and x < SX and y >= 0 and y < SY]

def expand_root_node(cell, SX, SY, map):
    basin = [cell]

    for node in get_nsew_nodes(cell, SX, SY):
        expand_node(node, basin, SX, SY, map)

    return basin

def expand_node(cell, basin, SX, SY, map):
    if map[cell.y][cell.x] == 9:
        return
    if cell in basin:
        return
    basin.append(cell)
    for node in get_nsew_nodes(cell, SX, SY):
        if node in basin:
            continue
        expand_node(node, basin, SX, SY, map)

def process_map(map):
    SY = len(data)
    SX = len(data[0])

    basins = []
    for j in range(SY):
         for i in range(SX):
            cell = Cell(i, j)
            # check if cell is in one basin
            if cell_in_basin(cell, basins):
                # in basin. Continue to the next cell
                continue
            # check if root node
            if is_root(cell, SX, SY, map):
                basins.append(expand_root_node(cell, SX, SY, map))

    return basins


with open(sys.argv[1], 'r') as f:
    data = [[int(x) for x in line if x != '\n'] for line in f]

sb = [len(x) for x in process_map(data)]
sb.sort(reverse=True)
print(math.prod(sb[:3]))
