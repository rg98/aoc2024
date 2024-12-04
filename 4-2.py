#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 4 - Part 2
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
    if puzzle[y][x] == 'A':
        # Check
        if y >= 1 and y <= len(puzzle) - 2 and \
           x >= 1 and x <= len(puzzle[y]) - 2:
            # Check (MSSM)
            if puzzle[y-1][x-1] == 'M' and \
               puzzle[y-1][x+1] == 'S' and \
               puzzle[y+1][x+1] == 'S' and \
               puzzle[y+1][x-1] == 'M':
                n += 1
            # Check (MMSS)
            if puzzle[y-1][x-1] == 'M' and \
               puzzle[y-1][x+1] == 'M' and \
               puzzle[y+1][x+1] == 'S' and \
               puzzle[y+1][x-1] == 'S':
                n += 1
            # Check (SMMS)
            if puzzle[y-1][x-1] == 'S' and \
               puzzle[y-1][x+1] == 'M' and \
               puzzle[y+1][x+1] == 'M' and \
               puzzle[y+1][x-1] == 'S':
                n += 1
            # Check (SSMM)
            if puzzle[y-1][x-1] == 'S' and \
               puzzle[y-1][x+1] == 'S' and \
               puzzle[y+1][x+1] == 'M' and \
               puzzle[y+1][x-1] == 'M':
                n += 1
    return n

n_xmas = 0
for y, line in enumerate(puzzle):
    for x, c in enumerate(line):
        n_xmas += check_xmas(x,y,puzzle)

print(n_xmas)
