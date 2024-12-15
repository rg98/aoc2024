#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 9 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

def find_space_for(space, spaceMap):
    for s in sorted(spaceMap.keys()):
        if spaceMap[s] >= space:
            return s
    return None

def compact_files(blockMap, fileMap, spaceMap):
    # Move files from reversed fileMap into spaceMap spaces
    for file, _len in reversed(fileMap.items()):
        pos = find_space_for(_len, spaceMap)
        if pos:
            blockMap = [None if e == file else e for e in blockMap]
            for i in range(_len):
                blockMap[pos+i] = file

            spaceMap[pos + _len] = spaceMap[pos] - _len
            del spaceMap[pos]
    return blockMap

def get_checksum(filemap):
    block_map = []
    file_map = {}
    space_map = {}
    # Build block map
    for n, c in enumerate(list(filemap)):
        l = int(c)
        if (n % 2) == 0:
            file_map[n//2] = l
            for _ in range(l):
                block_map.append(n//2)
        else:
            space_map[len(block_map)] = l
            for _ in range(l):
                block_map.append(None)

    # Compact files
    block_map = compact_files(block_map, file_map, space_map)

    # Calculate checksum
    checksum = 0
    for i, n in enumerate(block_map):
        if n == None:
            continue
        checksum += i * n

    return checksum

# Read orderes and pages
checksum = 0
with open('9.in.ref', 'r') as fd:
    for line in fd:
        checksum += get_checksum(line[:-1])

print(checksum)
