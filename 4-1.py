#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 4 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

puzzle = []

# Read memory
with open('4.in', 'r') as fd:
    for line in fd:
        puzzle.append([c for c in list(line[:-1])])

def check_xmas(x, y, puzzle):
    n = 0
    if puzzle[y][x] == 'X':
        # Check up
        if y >= 3:
            if puzzle[y-1][x] == 'M' and \
               puzzle[y-2][x] == 'A' and \
               puzzle[y-3][x] == 'S':
                n += 1
        # Check up-right
        if y >= 3 and x <= len(puzzle[y]) - 4:
            if puzzle[y-1][x+1] == 'M' and \
               puzzle[y-2][x+2] == 'A' and \
               puzzle[y-3][x+3] == 'S':
                n += 1
        # Check right
        if x <= len(puzzle[y]) - 4:
            if puzzle[y][x+1] == 'M' and \
               puzzle[y][x+2] == 'A' and \
               puzzle[y][x+3] == 'S':
                n += 1
        # Check donw-right
        if y <= len(puzzle) - 4 and x <= len(puzzle[y]) - 4:
            if puzzle[y+1][x+1] == 'M' and \
               puzzle[y+2][x+2] == 'A' and \
               puzzle[y+3][x+3] == 'S':
                n += 1
        # Check down
        if y <= len(puzzle) - 4:
            if puzzle[y+1][x] == 'M' and \
               puzzle[y+2][x] == 'A' and \
               puzzle[y+3][x] == 'S':
                n += 1
        # Check down-left
        if y <= len(puzzle) - 4 and x >= 3:
            if puzzle[y+1][x-1] == 'M' and \
               puzzle[y+2][x-2] == 'A' and \
               puzzle[y+3][x-3] == 'S':
                n += 1
        # Check left
        if x >= 3:
            if puzzle[y][x-1] == 'M' and \
               puzzle[y][x-2] == 'A' and \
               puzzle[y][x-3] == 'S':
                n += 1
        # Check up-left
        if y >= 3 and x >= 3:
            if puzzle[y-1][x-1] == 'M' and \
               puzzle[y-2][x-2] == 'A' and \
               puzzle[y-3][x-3] == 'S':
                n += 1
    return n

n_xmas = 0
for y, line in enumerate(puzzle):
    for x, c in enumerate(line):
        n_xmas += check_xmas(x,y,puzzle)

print(n_xmas)
