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


def apply_input(input):
    solver = getSolver()
    for i in range(9):
        for j in range(9):
            value = input[i][j]
            if (value > 0):
                set_cell(solver, i, j, value)
                clear_col(solver, i, j, value)
                clear_row(solver, i, j, value)
                clear_sector(solver, i, j, value)
    return solver


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


def check_invalid(solver):
    for i in range(9):
        for j in range(9):
            for k in range(9):
                fine = False
                if (solver[i][j][k] > 0):
                    fine = True
                    break
            if (not fine):
                return True
    return False


def solver_2(solver, result, choice):
    # print("solver_2: " + str(choice))
    for max_choices in range(2, 10):
        for i in range(9):
            for j in range(9):
                count = 0
                choices = []
                for k in range(9):
                    if (solver[i][j][k] != 0):
                        count += 1
                        choices.append(solver[i][j][k])

                if (count == max_choices):
                    result[i][j] = choices[choice]
                    for row in result:
                        print(row)
                    print("Position: " + str(i) + " - " +
                          str(j) + " = " + str(choices[choice]) + " #" + str(choice) + " of " + str(len(choices)))

                    return max_choices


def extract_field(solver):
    result = getField()
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
    return result


def getSolver():
    solver = []
    size = 9

    for _i in range(size):
        row = []
        for _j in range(size):
            choices = []
            for k in range(9):
                choices.append(k+1)
            row.append(choices)
        solver.append(row)
    return solver


def getField():
    field = []
    size = 9

    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        field.append(row)
    return field


def print_solver(solver):
    for row in solver:
        print()
        for possibilities in row:
            for num in possibilities:
                if (num > 0):
                    print(num, end='')
            print(",", end='')
    print()


def revisit_choice(choices, tries, minimum):
    last = len(choices) - 1
    if (last >= 0 and tries[last] + 1 < minimum[last]):
        tries[last] += 1
        solver = apply_input(copy.deepcopy(choices[last]))
        result = extract_field(solver)
        print_solver(solver)
        solver_2(solver, result, tries[last])
        print(str(len(choices)))
    else:
        choices.pop()
        tries.pop()
        minimum.pop()
        result = revisit_choice(choices, tries, minimum)
    return result


input = [
    [0, 6, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 5, 3, 0, 8, 0, 6, 0],
    [0, 0, 0, 0, 6, 0, 0, 7, 4],
    [0, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 0, 1, 8],
    [0, 8, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 6, 4, 0],
    [0, 0, 0, 9, 0, 0, 0, 0, 0]
]

# input = [
#     [9, 0, 4, 0, 5, 0, 0, 2, 0],
#     [0, 0, 7, 0, 0, 0, 0, 1, 0],
#     [0, 0, 3, 2, 8, 0, 0, 0, 0],
#     [0, 0, 0, 0, 9, 0, 0, 0, 0],
#     [0, 0, 0, 8, 0, 0, 0, 3, 6],
#     [5, 0, 0, 7, 0, 0, 0, 0, 2],
#     [1, 0, 0, 0, 0, 3, 0, 4, 0],
#     [0, 0, 0, 0, 0, 6, 0, 0, 5],
#     [0, 4, 0, 0, 0, 0, 0, 0, 9]
# ]

# input = [
#     [0, 6, 0, 0, 0, 0, 1, 8, 5],
#     [0, 0, 5, 3, 0, 8, 2, 6, 9],
#     [0, 0, 0, 0, 6, 0, 0, 7, 4],
#     [0, 0, 7, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 4, 5, 0, 1, 8],
#     [0, 8, 0, 0, 0, 0, 0, 0, 3],
#     [5, 0, 0, 0, 0, 3, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 6, 4, 0],
#     [0, 0, 0, 9, 0, 0, 0, 0, 0]
# ]

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

# input = [
#     [1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 2, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 3, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 4, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 5, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 6, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 7, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 8, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 9]
# ]

choices = []
tries = []
minimum = []

for row in input:
    print(row)


while(not check_solved(result)):
    solver = apply_input(input)
    result = extract_field(solver)

    # Made wrong choice
    if(check_invalid(solver)):
        result = revisit_choice(choices, tries, minimum)
    else:
        # Need for choice
        if (compare(input, result)):
            choices.append(copy.deepcopy(result))
            tries.append(0)
            print_solver(solver)
            minimum.append(solver_2(solver, result, 0))
            print(str(len(choices)))

    input = copy.deepcopy(result)

print()

for row in result:
    print(row)
