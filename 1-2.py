#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 1 - Part 2
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
list2 = {i: list2.count(i) for i in list2}

similarity_scores = []
for n in list1:
    if n in list2.keys():
        score = int(n * list2[n])
        similarity_scores.append(score)

print(sum(similarity_scores))
