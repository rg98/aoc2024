#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 11 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################


# Read input
stones = []
with open('11.in', 'r') as fd:
    for line in fd:
        stones = [int(n) for n in line[:-1].split(' ')]

# Rules
# 0 -> 1 -> 2024 -> 20 24 -> 2 0 2 4 -> 4048 1 4048 8196 -> \
#  40 48 2024 40 48 81 92 -> 4 0 4 8 20 24 4 0 4 8 8 1 9 6
# 1 -> 1 -> 1 -> 2 -> 4 -> 4 -> 7 -> 14 -> 16 
#
# 11 -> 1 1 -> 2024 2024 -> 20 24 20 24 -> 2 0 2 4 2 0 2 4 -> \
#  4048 1 4048 8196 4028 1 4048 8196 -> \
#  40 48 2024 40 48 81 96 40 48 2024 40 48 81 96 -> \
#  4 0 4 8 20 24 4 0 4 8 8 1 9 6 4 0 4 8 20 24 4 0 4 8 8 1 9 6
# 1 -> 2 -> 2 -> 4 -> 8 -> 8 -> 14 -> 28 -> 32 ->
#
# n -> n * 2024 ->  
#
# 111 -> 224664 -> 224 664 -> 453376 1343936 -> 453 376 1376190464 -> \
#  916872 761024 13761 90464 -> 916 872 761 24 27852264 183099136 -> \
#  1853984 1764928 1540264 48576 2785 2264 370592651264
# 1 -> 1 -> 2 -> 2 -> 3 -> 4 -> 6 -> 7

print(stones)
