#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 8 - Part 2
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

def get_antennas(grid):
    antennas = {}
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c != '.':
                if c in antennas.keys():
                    antennas[c].append((x, y))
                else:
                    antennas[c] = [(x, y)]
    return antennas

def get_antinodes(frequency, positions, grid_size):
    antinodes = []
    for i, p1 in enumerate(positions[:-1]):
        for j, p2 in enumerate(positions[i+1:]):
           print(p1, p2)
           d = (p2[0] - p1[0], p2[1] - p1[1])
           n = 0
           while True:
               a1 = (p1[0] - n * d[0], p1[1] - n * d[1])
               if a1[0] >= 0 and a1[0] < grid_size[0] \
                  and a1[1] >= 0 and a1[1] < grid_size[1]:
                   print(a1)
                   antinodes.append(a1)
                   n += 1
               else:
                   break
           n = 0
           while True:
               a2 = (p2[0] + n * d[0], p2[1] + n * d[1])
               if a2[0] >= 0 and a2[0] < grid_size[0] \
                  and a2[1] >= 0 and a2[1] < grid_size[1]:
                   print(a2)
                   antinodes.append(a2)
                   n += 1
               else:
                   break
    return antinodes

# Read orderes and pages
grid = []
with open('8.in', 'r') as fd:
    for line in fd:
        grid.append(list(line[:-1]))

grid_size = (len(grid), len(grid[0]))

antennas = get_antennas(grid)

antinodes = []
for frequency, positions in antennas.items():
    antinodes.append(get_antinodes(frequency, positions, grid_size))

antinodes = [x for xs in antinodes for x in xs]
print(set(antinodes))
print()
print(len(set(antinodes)))
