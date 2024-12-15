#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 9 - Part 2
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

import collections

def exchange(blockMap, a, b):
    tmp = blockMap[a]
    blockMap[a] = blockMap[b]
    blockMap[b] = tmp

def move_file(file_from, file, slot, block_map, free_spaces, used_spaces):
    print('from:', file_from)
    print('file:', file)
    print('slot:', slot)
    print('block_map - before:', block_map)
    print('free_spaces - before:', free_spaces)
    print('used_spaces - before:', used_spaces)
    print('block:', block_map)
    print()
    for i in range(file[1]):
        block_map[slot+i] = file[0]
        block_map[file_from+i] = None
    free_spaces[slot] -= file[1]
    free_spaces[slot+file[1]] = free_spaces[slot]
    del free_spaces[slot]
    if free_spaces[slot+file[1]] == 0:
        del free_spaces[slot+file[1]]
    free_spaces = collections.OrderedDict(sorted(free_spaces.items()))
    print('block_map - after:', block_map)
    print('free_spaces - after:', free_spaces)
    print('used_spaces - after:', used_spaces)
    print()
    return free_spaces

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

    # Find free and used spaces
    free_spaces = {}
    used_spaces = {}
    state = None
    start = None
    file_id = None
    for current, content in enumerate(block_map):
        if state == None:
            start = current
            if content == None:
                state = 'Free'
            else:
                state = 'Used'
        else:
            if state == 'Free' and content != None:
                free_spaces[start] = current - start
                start = current
                file_id = content
                state = 'Used'
            elif state == 'Used' and content == None:
                used_spaces[start] = (block_map[current - 1], current - start)
                start = current
                state = 'Free'
                file_id = None
            elif state == 'Used' and content != file_id:
                used_spaces[start] = (block_map[current - 1], current - start)
                start = current
                file_id = content
    used_spaces[start] = (block_map[current - 1], current - start + 1)
                
    # Compact files
    for n, file in reversed(used_spaces.items()):
        for slot in free_spaces.keys():
            print('check:', file[1], 'vs', free_spaces[slot], 'slot:', slot)
            if free_spaces[slot] >= file[1]:
                free_spaces = move_file(n, file, slot, block_map, free_spaces, used_spaces)
                break

    # Calculate checksum
    checksum = 0
    for i, n in enumerate(block_map):
        if n == None:
            break
        checksum += i * n

    return checksum

# Read orderes and pages
checksum = 0
with open('9.in.ref', 'r') as fd:
    for line in fd:
        checksum += get_checksum(line[:-1])

print(checksum)
