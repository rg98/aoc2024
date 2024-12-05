#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 5 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################

orders = []
pages = []

# Read orderes and pages
with open('5.in', 'r') as fd:
    for line in fd:
        if len(line) == 1:
            break
        orders.append([int(c) for c in line[:-1].split('|')])
    
    for line in fd:
        pages.append({int(c): i for i, c in enumerate(line[:-1].split(','))})

def order_valid(orders, page_order):
    for order in orders:
        if order[0] in page_order.keys() and \
           order[1] in page_order.keys() and \
           page_order[order[0]] > page_order[order[1]]:
            return False
    return True

# Check pages for orders
valid = []
for page_order in pages:
    if order_valid(orders, page_order):
        valid.append(list(page_order.keys()))

results = sum([c[len(c)//2] for c in valid])

print(results)
