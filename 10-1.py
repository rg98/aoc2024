#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 10 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

def count_trailheads(loc, area):
    

def locate_start_locations(area):
    locations = []
    for y, row in enumerate(area):
        for x, n in enumerate(row):
            if n == 0:
                locations.append((x, y))
    return locations

# Read orderes and pages
area = []
with open('10.in.ref', 'r') as fd:
    for line in fd:
        area.append([int(n) for n in list(line[:-1])])

# Get locations of zeros
locations = locate_start_locations(area)

# Get all trailheads
trailheads = 0
for location in locactions:
    trailheads += count_trails(location, area)

print(trailheads)
