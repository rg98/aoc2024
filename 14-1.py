#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 14 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

import re

robots = []
restroom = []
restroom_size = (101, 103)

# Read lists
with open('14.in', 'r') as fd:
    for line in fd:
        m = re.fullmatch(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line[:-1])
        px, py, vx, vy = m.group(1, 2, 3, 4)
        robots.append((int(px), int(py), int(vx), int(vy)))

#for robot in robots:
#    print(robot)
#print()

def pos2quadrant(pos, restroom_size):
    if pos[0] < restroom_size[0] // 2 and pos[1] < restroom_size[1] // 2:
        return 0
    elif pos[0] > restroom_size[0] // 2 and pos[1] < restroom_size[1] // 2:
        return 1
    elif pos[0] < restroom_size[0] // 2 and pos[1] > restroom_size[1] // 2:
        return 2
    elif pos[0] > restroom_size[0] // 2 and pos[1] > restroom_size[1] // 2:
        return 3
    return -1

def count_robots_in_quadrant(t, robots, restroom_size):
    quadrants = [0, 0, 0, 0]
    for i, robot in enumerate(robots):
        p = ((robot[0] + t * robot[2]) % restroom_size[0], \
             (robot[1] + t * robot[3]) % restroom_size[1])
        #if i == 10:
        #    print(p)
        q = pos2quadrant(p, restroom_size)
        #print(q)
        if q >= 0:
            quadrants[q] += 1
    return quadrants

# Count robots in quadrants
quadrants = [0, 0, 0, 0]
quadrants = count_robots_in_quadrant(100, robots, restroom_size)
#for t in range(6):
#    q = count_robots_in_quadrant(t, robots, restroom_size)
#    quadrants[0] += q[0]
#    quadrants[1] += q[1]
#    quadrants[2] += q[2]
#    quadrants[3] += q[3]

print(quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3])
