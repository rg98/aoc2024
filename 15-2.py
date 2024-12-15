#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 15 - Part 2
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

from itertools import chain

warehouse = []
moves = []

# Read lists
with open('15.in.simple2', 'r') as fd:
    for line in fd:
        if len(line) > 1:
            warehouse.append(list(line[:-1]))
        else:
            break

    for line in fd:
        moves.append(list(line[:-1]))

replacementMap =  {'#': '##', 'O': '[]', '.': '..', '@': '@.'}

wideWarehouse = []
for row in warehouse:
    wideRow = []
    for e in row:
        wideRow.append(replacementMap[e])
    wideWarehouse.append(list(chain.from_iterable(wideRow)))

warehouse = wideWarehouse

moves = list(chain.from_iterable(moves))

def print_warehouse(warehouose):
    for row in warehouse:
        print(''.join(row))
    print()

def find_robot(warehouse):
    for y, row in enumerate(warehouse):
        print(row)
        if '@' in row:
            x = row.index('@')
            return (x, y)

def move_box_up(box, warehouse):
    if warehouse[box[1]-1][box[0]] == '.':
        warehouse[box[1]-1][box[0]] = 'O'
        warehouse[box[1]][box[0]] = '.'
        return True
    elif warehouse[box[1]-1][box[0]] == '#':
        return False
    elif warehouse[box[1]-1][box[0]] == 'O':
        if move_box_up([box[0], box[1]-1], warehouse):
            warehouse[box[1]-1][box[0]] = 'O'
            warehouse[box[1]][box[0]] = '.'
            return True
        else:
            return False
    else:
        raise RuntimeError(f'Unexpected warehouse content {warehouse[box[1]-1][box[0]]}')

def move_box_right(box, warehouse):
    if warehouse[box[1]][box[0]+1] == '.':
        warehouse[box[1]][box[0]+1] = 'O'
        warehouse[box[1]][box[0]] = '.'
        return True
    elif warehouse[box[1]][box[0]+1] == '#':
        return False
    elif warehouse[box[1]][box[0]+1] == 'O':
        if move_box_right([box[0]+1, box[1]], warehouse):
            warehouse[box[1]][box[0]+1] = 'O'
            warehouse[box[1]][box[0]] = '.'
            return True
        else:
            return False
    else:
        raise RuntimeError(f'Unexpected warehouse content {warehouse[box[1]][box[0]-1]}')

def move_box_down(box, warehouse):
    if warehouse[box[1]+1][box[0]] == '.':
        warehouse[box[1]+1][box[0]] = 'O'
        warehouse[box[1]][box[0]] = '.'
        return True
    elif warehouse[box[1]+1][box[0]] == '#':
        return False
    elif warehouse[box[1]+1][box[0]] == 'O':
        if move_box_down([box[0], box[1]+1], warehouse):
            warehouse[box[1]+1][box[0]] = 'O'
            warehouse[box[1]][box[0]] = '.'
            return True
        else:
            return False
    else:
        raise RuntimeError(f'Unexpected warehouse content {warehouse[box[1]-1][box[0]]}')

def move_box_left(box, warehouse):
    if warehouse[box[1]][box[0]-1] == '.':
        warehouse[box[1]][box[0]-1] = 'O'
        warehouse[box[1]][box[0]] = '.'
        return True
    elif warehouse[box[1]][box[0]-1] == '#':
        return False
    elif warehouse[box[1]][box[0]-1] == 'O':
        if move_box_left([box[0]-1, box[1]], warehouse):
            warehouse[box[1]][box[0]-1] = 'O'
            warehouse[box[1]][box[0]] = '.'
            return True
        else:
            return False
    else:
        raise RuntimeError(f'Unexpected warehouse content {warehouse[box[1]][box[0]-1]}')

print('Initial state:')
print_warehouse(warehouse)

robot = find_robot(warehouse)
print('robot:', robot)
print()

for move in moves:
    print(f"Move '{move}'")
    if move == '^':
        if warehouse[robot[1]-1][robot[0]] == '.':
            warehouse[robot[1]-1][robot[0]] = '@'
            warehouse[robot[1]][robot[0]] = '.'
            robot = [robot[0], robot[1]-1]
        elif warehouse[robot[1]-1][robot[0]] == '#':
            pass
        elif warehouse[robot[1]-1][robot[0]] == 'O':
           if move_box_up([robot[0], robot[1]-1], warehouse):
               warehouse[robot[1]-1][robot[0]] = '@'
               warehouse[robot[1]][robot[0]] = '.'
               robot = [robot[0], robot[1]-1]
    elif move == '>':
        if warehouse[robot[1]][robot[0]+1] == '.':
            warehouse[robot[1]][robot[0]+1] = '@'
            warehouse[robot[1]][robot[0]] = '.'
            robot = [robot[0]+1, robot[1]]
        elif warehouse[robot[1]][robot[0]+1] == '#':
            pass
        elif warehouse[robot[1]][robot[0]+1] == 'O':
            if move_box_right([robot[0]+1, robot[1]], warehouse):
                warehouse[robot[1]][robot[0]+1] = '@'
                warehouse[robot[1]][robot[0]] = '.'
                robot = [robot[0]+1, robot[1]]
    elif move == 'v':
        if warehouse[robot[1]+1][robot[0]] == '.':
            warehouse[robot[1]+1][robot[0]] = '@'
            warehouse[robot[1]][robot[0]] = '.'
            robot = [robot[0], robot[1]+1]
        elif warehouse[robot[1]+1][robot[0]] == '#':
            pass
        elif warehouse[robot[1]+1][robot[0]] == 'O':
           if move_box_down([robot[0], robot[1]+1], warehouse):
               warehouse[robot[1]+1][robot[0]] = '@'
               warehouse[robot[1]][robot[0]] = '.'
               robot = [robot[0], robot[1]+1]
    elif move == '<':
        if warehouse[robot[1]][robot[0]-1] == '.':
            warehouse[robot[1]][robot[0]-1] = '@'
            warehouse[robot[1]][robot[0]] = '.'
            robot = [robot[0]-1, robot[1]]
        elif warehouse[robot[1]][robot[0]-1] == '#':
            pass
        elif warehouse[robot[1]][robot[0]-1] == 'O':
            if move_box_left([robot[0]-1, robot[1]], warehouse):
                warehouse[robot[1]][robot[0]-1] = '@'
                warehouse[robot[1]][robot[0]] = '.'
                robot = [robot[0]-1, robot[1]]
    else:
        raise RuntimeError(f'Unknown direction {move}')
    print_warehouse(warehouse)

def find_boxes(warehouse):
    boxes = []
    for y, row in enumerate(warehouse):
        for x, col in enumerate(list(row)):
            if col == 'O':
                boxes.append([x, y])
    return boxes

def get_gps(x, y):
    return x + 100 * y

boxes = find_boxes(warehouse)

gps = 0
for box in boxes:
    gps += get_gps(box[0], box[1])

print(gps)
