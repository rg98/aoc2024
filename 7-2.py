#!/usr/bin/env python3
#############################################################################
# Advent of Code 2024 - Day 7 - Part 1
# --------------------------------------------------------------------------
# © Ralph Ganszky
#############################################################################


def check_equation(result, arguments):
    operator = ['+', '*', '|']
    operators = operator
    for n in range(len(arguments) - 2):
        nops = []
        for ops in operators:
            for op in operator:
                nops.append(ops + op)
        operators = nops

    for i, ops in enumerate(operators):
        res = arguments[0]
        for j, op in enumerate(ops):
            if op == '+':
                res += arguments[j+1]
            elif op == '|':
                res = int(str(res) + str(arguments[j+1]))
            else:
                res *= arguments[j+1]
        if res == result:
            return True
    return False

# Read orderes and pages
valid = 0
with open('7.in', 'r') as fd:
    for line in fd:
        test, values = line[:-1].split(': ')
        if check_equation(int(test), [int(c) for c in values.split(' ')]):
            valid += int(test)

print(valid)
