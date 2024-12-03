#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 3 - Part 2
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

import re

# Read memory
with open('3.in', 'r') as fd:
    memory = fd.read()

result = 0

cmds = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", memory)

active = 1
for cmd in cmds:
    if cmd.startswith("mul("):
        if active == 1:
            n, m = cmd[4:-1].split(',')
            result += int(n) * int(m)
    elif cmd == "do()":
        active = 1
    elif cmd == "don't()":
        active = 0
    else:
        raise RuntimeError(f"Unexpected command: {cmd}")

print(result)
