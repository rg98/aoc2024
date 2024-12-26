#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 11 - Part 2
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################


# Read input
stones = []
with open('11.in', 'r') as fd:
    for line in fd:
        stones = [int(n) for n in line[:-1].split(' ')]

cache = {}

def in_cache(level, key):
    if level in cache.keys():
        if key in cache[level].keys():
            return cache[level][key]
    return None

def set_cache(level, key, value):
    if level not in cache.keys():
        cache[level] = {}
    cache[level][key] = value

def nBlink(level, stones):
    if level == 0:
        return 1 # len(stones)
    n = 0
    for stone in stones:
        if stone == 0:
            cache_value = in_cache(level - 1, 1)
            if cache_value:
                n += cache_value
            else:
                i = nBlink(level - 1, [1])
                set_cache(level - 1, 1, i)
                n += i
        elif (len(str(stone)) & 1) == 0:
            m = str(stone)
            l = len(m) // 2
            front = int(m[:l])
            back = int(m[l:])
            front_cache = in_cache(level - 1, front)
            if front_cache:
                n += front_cache
            else:
                i = nBlink(level - 1, [front])
                set_cache(level - 1, front, i)
                n += i
            back_cache = in_cache(level - 1, back)
            if back_cache:
                n += back_cache
            else:
                i = nBlink(level - 1, [back])
                set_cache(level - 1, back, i)
                n += i
        else:
            cache_value = in_cache(level - 1, stone * 2024)
            if cache_value:
                n += cache_value
            else:
                i = nBlink(level - 1, [stone * 2024])
                set_cache(level - 1, stone * 2024, i)
                n += i

    return n

print(nBlink(75, stones))
