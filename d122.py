#!/usr/bin/env python3

import sys

class Node:
    def __init__(self, name) -> None:
        self.name  = name
        self.small = name.islower()
        self.big   = name.isupper()
        self.start = name == 'start'
        self.end   = name == 'end'
        self.links = []

    def add_link(self, other):
        self.links.append(other)

    def __repr__(self):
        return 'Node({})'.format(self.name)
    def __str__(self):
        return 'Node({})'.format(self.name)

class Graph:
    def __init__(self, data) -> None:
        self.nodes  = {}
        self.paths  = []
        self.enable = False
        self.cave   = None
        for a, b in data:
            a = self.insert_node(a)
            b = self.insert_node(b)
            a.add_link(b)
            b.add_link(a)

    def __repr__(self):
        return 'Graph({})'.format(self.nodes)
    def __str__(self):
        return 'Graph({})'.format(self.nodes)

    def insert_node(self, name):
        if name in self.nodes:
            return self.nodes[name]
        t = self.nodes[name] = Node(name)
        return t

    def visit_root(self, root: Node, visited: list):
        if root is None:
            raise ValueError("Invalid root node")

        if root.end:
            self.paths.append(visited.copy())
            return

        for node in root.links:
            if node.start:
                continue
            if node.small and (node in visited):
                if self.enable:
                    continue
                else:
                    self.enable = True
                    self.cave   = node
            visited.append(node)
            self.visit_root(node, visited)
            if visited.pop() == self.cave:
                self.enable = False
                self.cave   = None

    def get_paths(self):
        start = None
        for node in self.nodes.values():
            if node.start:
                start = node
                break
        visited = [start]
        self.visit_root(start, visited)
        return self.paths

with open(sys.argv[1], 'r') as f:
    data = [line[:-1].split('-') for line in f]

print(len(Graph(data).get_paths()))
