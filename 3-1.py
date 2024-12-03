#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 3 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

import re

# Read memory
with open('3.in', 'r') as fd:
    memory = fd.read()

result = 0

cmds = re.findall(r'mul\(\d{1,3},\d{1,3}\)', memory)
for cmd in cmds:
    n, m = cmd[4:-1].split(',')
    result += int(n) * int(m)

print(result)
