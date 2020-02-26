#!/usr/bin/env python3

import copy


def set_cell(solver, i, j, value):
    for k in range(9):
        solver[i][j][k] = 0
    solver[i][j][value - 1] = value


def clear_row(solver, i, j, value):
    for row in range(9):
        if (row != i):
            solver[row][j][value - 1] = 0


def clear_col(solver, i, j, value):
    for col in range(9):
        if (col != j):
            solver[i][col][value - 1] = 0


def clear_sector(solver, i, j, value):
    sector_i_pos = i // 3
    sector_j_pos = j // 3

    for row in range(0 + sector_i_pos * 3, 3 + sector_i_pos * 3):
        for col in range(0 + sector_j_pos * 3, 3 + sector_j_pos * 3):
            if (not (col == j and row == i)):
                solver[row][col][value - 1] = 0


def apply_input(solver, input):
    for i in range(9):
        for j in range(9):
            value = input[i][j]
            if (value > 0):
                set_cell(solver, i, j, value)
                clear_col(solver, i, j, value)
                clear_row(solver, i, j, value)
                clear_sector(solver, i, j, value)


def compare(input, result):
    for i in range(9):
        for j in range(9):
            if(input[i][j] != result[i][j]):
                return False
    return True


def check_solved(result):
    for i in range(9):
        for j in range(9):
            if (result[i][j] == 0):
                return False
    return True

# FIXME: solver_2 is broken!


def solver_2(solver, result):
    for i in range(9):
        for j in range(9):
            count = 0
            counted = 0
            for k in range(9):
                if (solver[i][j][k] != 0):
                    count += 1
                    counted = solver[i][j][k]
            if (count == 2):
                result[i][j] = counted
                return


def extract_field(solver, result):
    for i in range(9):
        for j in range(9):
            count = 0
            counted = 0
            for k in range(9):
                if (solver[i][j][k] != 0):
                    count += 1
                    counted = solver[i][j][k]
            if (count == 1):
                result[i][j] = counted


def getSolver():
    solver = []
    size = 9

    for i in range(size):
        row = []
        for j in range(size):
            choices = []
            for k in range(9):
                choices.append(k+1)
            row.append(choices)
        solver.append(row)
    return solver


def print_solver(solver):
    for row in solver:
        print()
        for possibilities in row:
            for num in possibilities:
                if (num > 0):
                    print(num, end='')
            print(",", end='')


input = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 4, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

result = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


for row in input:
    print(row)


for i in range(100):
    solver = getSolver()
    apply_input(solver, input)
    print_solver(solver)
    extract_field(solver, result)

    if(check_solved(result)):
        break

    if (compare(input, result)):
        solver_2(solver, result)
    print()
    if (not compare(input, result)):
        for row in result:
            print(row)
    input = copy.deepcopy(result)

print()

for row in result:
    print(row)
