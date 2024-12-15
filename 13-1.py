#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 13 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

import re

a=None
b=None
c=None
d=None
e=None
f=None

def solve(A, B, C, D, E, F):
    m = (B * C - D * A)/(F * C - D * E)
    n = (A - E * m)/C
    if (n - int(n)) == 0 and (m - int(m)) == 0:
        #print(int(n), int(m), '->', 3 * int(n) + int(m))
        return 3 * int(n) + int(m)
    else:
        #print("Could not win the prize")
        return 0

result = 0
# Read lists
with open('13.in', 'r') as fd:
    for line in fd:
        if line.startswith('Button A:'):
            m = re.fullmatch(r'Button A: X\+(\d+), Y\+(\d+)', line[:-1])
            if m:
                c, d = m.group(1,2)
        elif line.startswith('Button B:'):
            m = re.fullmatch(r'Button B: X\+(\d+), Y\+(\d+)', line[:-1])
            if m:
                e, f = m.group(1,2)
        elif line.startswith('Prize:'):
            m = re.fullmatch(r'Prize: X=(\d+), Y=(\d+)', line[:-1])
            if m:
                a, b = m.group(1,2)
                result += solve(int(a), int(b), int(c), int(d), int(e), int(f))

print(result)
