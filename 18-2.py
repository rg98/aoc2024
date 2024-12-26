#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 18 - Part 2
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

import networkx as nx
import re

falling = []
size = 71
part = 1024

# Read registers and instructions
with open('18.in', 'r') as fd:
    for line in fd:
        falling.append([int(n) for n in line[:-1].split(',')])

def build_grid(n, part, falling):
    g = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append('.')
        g.append(row)
    # Mark korruptions
    for o in falling[:part]:
        g[o[1]][o[0]] = '#'
    return g

grid = build_grid(size, part, falling[:part])

def gen_id(x, y, width):
    return y * width + x

# Build graph
G = nx.Graph()
width = len(grid[0])
height = len(grid)
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == '.':
            G.add_node(gen_id(x, y, width))

# Add edges
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if y > 0 and grid[y][x] == '.' and grid[y-1][x] == '.':
            G.add_edge(gen_id(x, y-1, width), gen_id(x, y, width))
        if x > 0 and grid[y][x] == '.' and grid[y][x-1] == '.':
            G.add_edge(gen_id(x-1, y, width), gen_id(x, y, width))
        if y < height - 1 and grid[y][x] == '.' and grid[y+1][x] == '.':
            G.add_edge(gen_id(x, y+1, width), gen_id(x, y, width))
        if x < width - 1 and grid[y][x] == '.' and grid[y][x+1] == '.':
            G.add_edge(gen_id(x+1, y, width), gen_id(x, y, width))

path = nx.shortest_path(G, 0, width*height-1)

def remove_node(byte, G):
    G.remove_node(byte[0] + width * byte[1])

for byte in falling[1024:]:
    remove_node(byte, G)
    try:
        path = nx.shortest_path(G, 0, width*height-1)
    except nx.exception.NetworkXNoPath as e:
        print(e)
        print(byte)
        break

#print(len(path)-1)

#for row in grid:
#    print(''.join(row))
