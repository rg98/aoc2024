#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 1 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

list1 = []
list2 = []

# Read lists
with open('1.in', 'r') as fd:
    for line in fd:
        l1, l2 = line[:-1].split('   ')
        list1.append(int(l1))
        list2.append(int(l2))

# Sort lists
list1 = sorted(list1)
list2 = sorted(list2)

difference_list = [abs(a - b) for a, b in zip(list1, list2)]

print(sum(difference_list))
