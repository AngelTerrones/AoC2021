#!/usr/bin/env python3

import sys
import collections

class Polymer:
    def __init__(self, template, comb) -> None:
        self.pair_count = collections.Counter()
        for x in [''.join(z) for z in zip(template, template[1:])]:
            self.pair_count[x] += 1
        self.comb = dict()
        for pair, atom in comb:
            self.comb[pair] = atom
        self.last_atom = template[-1]

    def step(self):
        for pair, amount in [x for x in self.pair_count.items() if x[1] > 0]:
            if pair not in self.comb.keys():
                continue
            atom = self.comb[pair]
            self.pair_count[pair] -= amount # should set to 0?
            self.pair_count[pair[0] + atom] += amount
            self.pair_count[atom + pair[1]] += amount

    def get_freq(self):
        counter = collections.Counter()
        for pair, amount in self.pair_count.items():
            counter[pair[0]] += amount
        counter[self.last_atom] += 1
        return counter

with open(sys.argv[1], 'r') as f:
    data = f.read()
    base, seq = data.split('\n\n')
    seq  = [line.split(' -> ') for line in seq.split('\n')[:-1]]

poly = Polymer(base, seq)
for _ in range(40):
    poly.step()

freq = poly.get_freq().most_common()
print(freq[0][1] - freq[-1][1])
