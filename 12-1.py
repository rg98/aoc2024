#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 12 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

from itertools import chain

garden = []

# Read lists
with open('12.in.simple', 'r') as fd:
    for line in fd:
        garden.append(list(line[:-1]))

for row in garden:
    print(row)
print()

plants = sorted(list(set(chain.from_iterable(garden))))
print(plants)
print()

regions = {}

def get_coords(plant, garden):
    coords = []
    for y, row in enumerate(garden):
        for x, p in enumerate(row):
            if p == plant:
                coords.append((x, y))
    return coords

for plant in plants:
    # Find all coordinates of the plant
    coords = get_coords(plant, garden)
    print(plant, coords)

