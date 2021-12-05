#!/usr/bin/env python3

import sys

class Point():
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)

	def __repr__(self):
		return 'Point({},{})'.format(self.x, self.y)
	def __str__(self):
		return '({},{})'.format(self.x, self.y)

class Line():
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __repr__(self):
		return 'Line({} -> {})'.format(self.a, self.b)
	def __str__(self):
		return '({} -> {})'.format(self.a, self.b)

	def maxX(self):
		return self.a.x if self.a.x > self.b.x else self.b.x

	def maxY(self):
		return self.a.y if self.a.y > self.b.y else self.b.y

	def isDiagonal(self):
		return (self.a.x != self.b.x) and (self.a.y != self.b.y)

	def getCoverPoints(self):
		# y
		step = -1 if self.a.y > self.b.y else  1
		y = [i for i in range(self.a.y, self.b.y + step, step)]
		# x
		step = -1 if self.a.x > self.b.x else  1
		x = [i for i in range(self.a.x, self.b.x + step, step)]
		# points
		if self.a.x == self.b.x:
			return [Point(self.a.x, i) for i in y]
		if self.a.y == self.b.y:
			return [Point(i, self.a.y) for i in x]
		return [Point(i, j) for i, j in zip(x, y)]

def print_map(map):
	for line in floor:
		for x in line:
			if x == 0:
				print('.', end='')
			else:
				print(x, end='')
		print()


def update_map(map, line):
	for point in line.getCoverPoints():
		map[point.y][point.x] += 1

def get_map_score(map):
	return len([cell for line in map for cell in line if cell > 1])

with open(sys.argv[1], 'r') as f:
	data = [Line(*[Point(*x.split(',')) for x in line.split() if x != '->']) for line in f]

sizeX = max([line.maxX() for line in data]) + 1
sizeY = max([line.maxY() for line in data]) + 1

floor = [[0 for _ in range(sizeX)] for _ in range(sizeY)]

for line in data:
	update_map(floor, line)

#print(sizeX, sizeY)
print(get_map_score(floor))
#print_map(floor)
