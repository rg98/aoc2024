#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 6 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

room = []

# Read orderes and pages
with open('6.in', 'r') as fd:
    for line in fd:
        room.append(list(line[:-1]))

def find_start_pos(room):
    for r, row in enumerate(room):
        if '^' in row:
            return [row.index('^'), r]

def walk(room, start):
    pos = start
    direction = 0
    directions = ['u', 'r', 'd', 'l']
    visited = 1
    room_size = [len(room[0]), len(room)]
    room[pos[1]][pos[0]] = 'X'
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
        if room[pos[1]][pos[0]] != 'X':
            room[pos[1]][pos[0]] = 'X'
            visited += 1
    return visited

visited = walk(room, find_start_pos(room))

print(visited)
