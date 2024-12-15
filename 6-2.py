#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 6 - Part 2
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

room = []

# Read orderes and pages
with open('6.in.ref', 'r') as fd:
    for line in fd:
        room.append(list(line[:-1]))

def find_start_pos(room):
    for r, row in enumerate(room):
        if '^' in row:
            return [row.index('^'), r]

def walk(room, start):
    pos = [start[0], start[1]]
    direction = 0
    directions = ['u', 'r', 'd', 'l']
    dirMap = {'u': 'A', 'r': '>', 'd': 'V', 'l' :'<'}
    visited = 1
    room_size = [len(room[0]), len(room)]
    #room[pos[1]][pos[0]] = '&'
    while pos[0] >= 0 and pos[0] < room_size[0] and \
          pos[1] >= 0 and pos[1] < room_size[1]:
        if directions[direction] == 'u':
            if pos[1] - 1 < 0:
                break
            if room[pos[1]-1][pos[0]] == '#':
                direction = (direction + 1) % 4
            else:
                pos[1] -= 1
        elif directions[direction] == 'r':
            if pos[0] + 1 >= room_size[0]:
                break
            if room[pos[1]][pos[0]+1] == '#':
                direction = (direction + 1) % 4
            else:
                pos[0] += 1
        elif directions[direction] == 'd':
            if pos[1] + 1 >= room_size[1]:
                break
            if room[pos[1]+1][pos[0]] == '#':
                direction = (direction + 1) % 4
            else:
                pos[1] += 1
        elif directions[direction] == 'l':
            if pos[0] - 1 < 0:
                break
            if room[pos[1]][pos[0]-1] == '#':
                direction = (direction + 1) % 4
            else:
                pos[0] -= 1
        else:
            raise RuntimeError('Unknown direction')
        if room[pos[1]][pos[0]] == '.':
            room[pos[1]][pos[0]] = dirMap[directions[direction]]
            visited += 1
        else:
            if room[pos[1]][pos[0]] != '^':
                room[pos[1]][pos[0]] = 'X'
    return visited

def find_cycles(room, start):
    # Find all candidates for new endpoints
    # Check all positions on the path
    candidates = []
    for y, row in enumerate(room):
        for x, c in enumerate(row):
            if c ==  '.':
                candidates.append((x, y))
                if y + 1 < len(room) and room[y+1][x] == '.':
                    if (x, y+1) not in candidates:
                        candidates.append((x, y+1))
                if y > 0 and room[y-1][x] == '.':
                    if (x, y-1) not in candidates:
                        candidates.append((x, y-1))
                if x + 1 < len(room[y]) and room[y][x+1] == '.':
                    if (x+1, y) not in candidates:
                        candidates.append((x+1, y))
                if x > 0 and room[y][x-1] == '.':
                    if (x-1, y) not in candidates:
                        candidates.append((x-1, y))
    n = 0

    return n

start = find_start_pos(room)

visited = walk(room, start)
find_cycles(room, start)

print('start:', start)
print(visited)
