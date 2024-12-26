#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 24 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

gates = {}
logic = []

# Read lists
with open('24.in', 'r') as fd:
    for line in fd:
        if len(line) == 1:
            break
        values = line[:-1].split(": ")
        gates[values[0]] = int(values[1])
    for line in fd:
        logic.append([x for x in list(line[:-1].split(' '))])

def find_all_gates(logic):
    _gates = set(gates.keys())
    for step in logic:
        _gates |= {step[0], step[2], step[4]}
    return _gates

all_gates = find_all_gates(logic)

for gate in all_gates:
    if gate not in gates.keys():
        gates[gate] = None

while sum(x is None for x in gates.values()) > 0:
    for step in logic:
        if gates[step[0]] != None and gates[step[2]] != None:
            if step[1] == 'AND':
                if gates[step[4]] == None:
                    gates[step[4]] = gates[step[0]] & gates[step[2]]
            elif step[1] == 'OR':
                if gates[step[4]] == None:
                    gates[step[4]] = gates[step[0]] | gates[step[2]]
            elif step[1] == 'XOR':
                if gates[step[4]] == None:
                    gates[step[4]] = gates[step[0]] ^ gates[step[2]]

n = 0
for i, gate in enumerate(tuple(filter(lambda x: x[0] == 'z' , sorted(gates)))):
    n += gates[gate] << i

print(n)
