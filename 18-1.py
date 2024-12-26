#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 18 - Part 1
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

#print(falling)

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

#for row in grid:
#    print(''.join(row))

def gen_id(x, y, width):
    return y * width + x

# Build graph
G = nx.Graph()
width = len(grid[0])
height = len(grid)
#print(f'width: {width}, height: {height}')
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == '.':
            G.add_node(gen_id(x, y, width))
#print(G.nodes())

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if y > 0 and grid[y][x] == '.' and grid[y-1][x] == '.':
            #print(0, gen_id(x, y-1, width), gen_id(x, y, width))
            G.add_edge(gen_id(x, y-1, width), gen_id(x, y, width))
        if x > 0 and grid[y][x] == '.' and grid[y][x-1] == '.':
            #print(1, gen_id(x-1, y, width), gen_id(x, y, width))
            G.add_edge(gen_id(x-1, y, width), gen_id(x, y, width))
        if y < height - 1 and grid[y][x] == '.' and grid[y+1][x] == '.':
            #print(2, gen_id(x, y+1, width), gen_id(x, y, width))
            G.add_edge(gen_id(x, y+1, width), gen_id(x, y, width))
        if x < width - 1 and grid[y][x] == '.' and grid[y][x+1] == '.':
            #print(3, gen_id(x+1, y, width), gen_id(x, y, width))
            G.add_edge(gen_id(x+1, y, width), gen_id(x, y, width))

#print()
#print(G.nodes())
#print()
#print(G.edges())

path = nx.shortest_path(G, 0, width*height-1)
print(len(path)-1)

for row in grid:
    print(''.join(row))
