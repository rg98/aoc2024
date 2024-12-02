#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 2 - Part 2
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

def check_save(l):
    if l[0] > 0:
        for n in l:
            if n < 1 or n > 3:
                return 0
        return 1
    elif l[0] < 0:
        for n in l:
            if n < -3 or n > -1:
                return 0
        return 1
    else:
        return 0

lists = []

# Read lists
with open('2.in', 'r') as fd:
    for line in fd:
        lists.append(line[:-1].split(' '))


save_reports = 0
for l in lists:
    d = [(int(b) - int(a)) for a, b in zip(l[1:], l[:-1])]
    save = check_save(d)
    if save != 1:
        l_len = len(l)
        for i in range(l_len):
            if i == 0:
                ll = l[1:]
            elif i == l_len - 1:
                ll = l[:-1]
            else:
                ll = l[:i] + l[i+1:]
            dd = [(int(b) - int(a)) for a, b in zip(ll[1:], ll[:-1])]
            save = check_save(dd)
            if save == 1:
                break
    if save == 0:
        print(l, 'not save')
    save_reports += save

print(save_reports)
