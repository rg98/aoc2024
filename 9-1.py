#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 9 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

def exchange(blockMap, a, b):
    tmp = blockMap[a]
    blockMap[a] = blockMap[b]
    blockMap[b] = tmp

def get_checksum(filemap):
    block_map = []
    # Build block map
    for n, c in enumerate(list(filemap)):
        l = int(c)
        if (n % 2) == 0:
            for _ in range(l):
                block_map.append(n//2)
        else:
            for _ in range(l):
                block_map.append(None)

    # Compact files
    for i in range(len(block_map)-1, 0, -1):
        if block_map != None:
            idx = block_map.index(None)
            if idx < i:
                exchange(block_map, i, idx)

    # Calculate checksum
    checksum = 0
    for i, n in enumerate(block_map):
        if n == None:
            break
        checksum += i * n

    return checksum

# Read orderes and pages
checksum = 0
with open('9.in', 'r') as fd:
    for line in fd:
        checksum += get_checksum(line[:-1])

print(checksum)
