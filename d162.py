#!/usr/bin/env python3

import sys
import math

def operation(op, values):
    if op == 0:
        return sum(values)
    if op == 1:
        return math.prod(values)
    if op == 2:
        return min(values)
    if op == 3:
        return max(values)
    if op == 5:
        return values[0] > values[1]
    if op == 6:
        return values[0] < values[1]
    if op == 7:
        return values[0] == values[1]

def proc_packet(packet, level=0):
    version = int(packet[:3],  base=2)
    id      = int(packet[3:6], base=2)
    # print(f"{' '*4*level}New packet. Version {version}, ID: {id}")
    if id == 4:
        v, subpack = proc_litval(packet, level + 1)
    else:
        if packet[6] == '1':
            v, subpack = proc_id1(packet, level + 1)
        else:
            v, subpack = proc_id0(packet, level + 1)
        v = operation(id, v)
    return v, subpack

def proc_litval(packet, level=0):
    fields = []
    for i in range(6, len(packet), 5):
        fields.append(packet[i + 1:i + 5])
        if packet[i] == '0':
            break
    payload = int(''.join(fields), base=2)
    snp     = i + 5
    # print(f"{' '*4*level}Payload: {payload}. Final scan index: {snp}")
    return payload, packet[snp:]

def proc_id0(packet, level=0):
    values = []
    size    = int(packet[7:22], base=2)
    subpack = packet[22:22 + size]
    # print(f"{' '*4*level}Length Type ID 0. Size: {size}")
    while subpack != '':
        v, subpack = proc_packet(subpack, level)
        values.append(v)
    return values, packet[22 + size:]

def proc_id1(packet, level=0):
    values = []
    npack   = int(packet[7:18], base=2)
    subpack = packet[18:]
    # print(f"{' '*4*level}Length Type ID 1. Npack: {npack}")
    while npack > 0:
        v, subpack = proc_packet(subpack, level)
        values.append(v)
        npack -= 1
    return values, subpack

# ----------------------------------------------------------------------------------------
with open(sys.argv[1], 'r') as f:
    data = [f'{int(line, base=16):0{4*(len(line) - 1)}b}' for line in f if line != '\n']

print([proc_packet(transmission)[0] for transmission in data])
