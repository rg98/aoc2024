#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 1 - Part 2a
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

import pandas as pd

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
df = pd.DataFrame({'l2': list2})
df2 = df.groupby(['l2']).size()

similarity_scores = []
for n in list1:
    if n in list(df2.index.values):
        score = int(n * df2[n])
        similarity_scores.append(score)

print(sum(similarity_scores))
