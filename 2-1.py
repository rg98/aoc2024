#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 2 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

def check_save(l):
    if l[0] > 0:
        for n in l:
            if n < 1 or n > 3:
                return 0
        return 1
    elif l[0] < 0:
        for n in l:
            if n < -3 or n > -1:
                return 0
        return 1
    else:
        return 0

lists = []

# Read lists
with open('2.in', 'r') as fd:
    for line in fd:
        lists.append(line[:-1].split(' '))


save_reports = 0
for l in lists:
    d = [(int(b) - int(a)) for a, b in zip(l[1:], l[:-1])]
    save_reports += check_save(d)

print(save_reports)
