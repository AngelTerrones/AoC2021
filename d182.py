#!/usr/bin/env python3
import sys
import copy
import itertools as itt

class Node:
    def __init__(self, data, parent) -> None:
        self.parent = parent
        if data is None or len(data) == 0:
            self.left = self.right = None
        else:
            if type(data[0]) is Node:
                self.left = copy.deepcopy(data[0])
                self.left.parent = self
            else:
                self.left = data[0] if type(data[0]) is int else Node(data[0], self)
            if type(data[1]) is Node:
                self.right = copy.deepcopy(data[1])
                self.right.parent = self
            else:
                self.right = data[1] if type(data[1]) is int else Node(data[1], self)

    def isEmpty(self):
        return self.right is None or self.left is None

    def need2explode(self):
        if type(self.left) is Node:
            return type(self.left.left) is int and type(self.left.right) is int
        if type(self.right) is Node:
            return type(self.right.left) is int and type(self.right.right) is int
        return False

    def left2left(self, value):
        parent = self
        node   = parent.left
        while True:
            if parent is None:
                break
            if parent.left is node:
                node, parent = parent, parent.parent
            elif type(parent.left) is int:
                parent.left += value
                break
            else:
                parent.rigth2left(value)
                break

    def left2right(self, value):
        parent = self
        while True:
            if parent is None:
                raise ValueError(f'Parent should not be None for this case: {self}')
            if type(parent.right) is Node:
                # go deep
                parent = parent.right
                while True:
                    if type(parent.left) is Node:
                        parent = parent.left
                    else:
                        parent.left += value
                        break
                break
            elif type(parent.right) is int:
                # Node at the right is an int. Done
                parent.right += value
                break
            else:
                raise ValueError(f'Impossible: {parent}')

    def right2right(self, value):
        parent = self
        node   = parent.right
        while True:
            if parent is None:
                break
            if parent.right is node:
                node, parent = parent, parent.parent
            elif type(parent.right) is int:
                parent.right += value
                break
            else:
                parent.left2right(value)
                break

    def rigth2left(self, value):
        parent = self
        while True:
            if parent is None:
                raise ValueError(f'Parent should not be None for this case: {self}')
            if type(parent.left) is Node:
                parent = parent.left
                while True:
                    if type(parent.right) is Node:
                        parent = parent.right
                    else:
                        parent.right += value
                        break
                break
            elif type(parent.left) is int:
                parent.left += value
                break
            else:
                raise ValueError(f'Impossible: {parent}')

    def explode(self, lvl):
        if lvl >= 4 and self.need2explode():
            if type(self.left) is Node:
                self.left2left(self.left.left)
                self.left2right(self.left.right)
                self.left  = 0
                return False
            if type(self.right) is Node:
                self.right2right(self.right.right)
                self.rigth2left(self.right.left)
                self.right = 0
                return False
            return True
        else:
            ok = True
            if type(self.left) == Node:
                ok &= self.left.explode(lvl + 1)
            if ok and type(self.right) == Node:
                ok &= self.right.explode(lvl + 1)
            return ok

    def split(self):
        ok = True
        if type(self.left) is int:
            if self.left > 9:
                self.left = Node([self.left//2, (self.left + 1)//2], self)
                return False
        else:
            ok &= self.left.split()

        if ok:
            if type(self.right) is int:
                if self.right > 9:
                    self.right = Node([self.right//2, (self.right + 1)//2], self)
                    return False
            else:
                ok &= self.right.split()
        return ok

    def magnitude(self):
        if type(self.left) is int:
            left = self.left
        else:
            left = self.left.magnitude()

        if type(self.right) is int:
            right = self.right
        else:
            right = self.right.magnitude()
        return (3* left) + (2 * right)

    def __repr__(self) -> str:
        return f'[{self.left}, {self.right}]'

    def __str__(self) -> str:
        return f'[{self.left}, {self.right}]'

class Tree:
    def __init__(self, data) -> None:
        self.root = Node(data, None)

    def collapse(self):
        doneExplode = False
        doneSplit   = False
        while not (doneExplode and doneSplit):
            doneExplode = self.root.explode(1)
            if doneExplode:
                doneSplit = self.root.split()

    def magnitude(self):
        return self.root.magnitude()

    def __repr__(self) -> str:
        return f'{self.root}'

    def __str__(self) -> str:
        return f'{self.root}'

    def __add__(self, x):
        if x.root.isEmpty():
            return self
        if self.root.isEmpty():
            return x
        newtree = Tree([self.root, x.root])
        newtree.collapse()
        return newtree

# ----------------------------------------------------------------------------------------
with open(sys.argv[1], 'r') as f:
    data = [Tree(eval(line)) for line in f if f != '\n']

print(max([(a + b).magnitude() for a, b in itt.permutations(data, 2)]))
