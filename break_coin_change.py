# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 23:11:31 2018

@author: gaurav
"""
"""
if current coin is too
high val, go to lesser
denomination for final

else, pick current one
and then check in same
row if we can pick the
same again. Still need
to compare lesser coin
as it may minimize num
"""
matrix = []


def make_change_no_dp(arr, a, final):
    """given arr of denominations
    of coins at hand, get minimum
    total number to break sum."""
    if final == 0:
        # we have already won
        return 0
    if arr[a-1] == 1:
        # always have pennies
        return final

    vals = list()
    for n in range(0, final+1, arr[a-1]):
        # for each time I can remove
        # this coin, I have to check
        # whether remaining a-1 coin
        # can fill up remaining gap.
        # I've choosen this coin too
        vals.append(int(n/arr[a-1]) +
                    make_change_no_dp(arr, a-1, final-n))
    return min(vals)


def make_change(arr, final):
    # fill zero column and row
    for i in range(0, len(arr) + 1):
        matrix.insert(i, list())
        matrix[i].insert(0, 0)
    for j in range(1, final + 1):
        matrix[0].insert(j, 100000)

    i = 1
    for a in arr:
        for j in range(1, final + 1):
            vals = list()
            for n in range(0, j+1, a):
                vals.append(int(n/a) + matrix[i-1][j-n])
            matrix[i].insert(j, min(vals))
        i += 1
    return matrix[len(arr)][final]


def make_change_no_dp_short(arr, a, final):
    """given arr of denominations
    of coins at hand, get minimum
    total number to break sum."""
    if final == 0:
        # we have already won
        return 0
    if arr[a-1] == 1:
        # always have pennies
        return final

    if final < arr[a-1]:
        # can't pick this num
        return make_change_no_dp_short(arr, a-1, final)

    # either we pick this element and
    # still allow to pick it again or
    # we don't pick it but the others
    return min(1 + make_change_no_dp_short(arr, a, final-arr[a-1]),
               make_change_no_dp_short(arr, a-1, final))


def make_change_short(arr, final):
    # fill zero column and row
    for i in range(0, len(arr) + 1):
        matrix.insert(i, list())
        matrix[i].insert(0, 0)
    for j in range(1, final + 1):
        matrix[0].insert(j, 100000)

    i = 1
    for a in arr:
        for j in range(1, final + 1):
            if j >= a:
                # Pick or no pick.
                # If pick, then we
                # may we pick this
                # val again. if no
                # pick, then next.
                v = 1 + matrix[i][j-a]
            else:
                v = 100000
            matrix[i].insert(j, min(v, matrix[i-1][j]))
        i += 1

    return matrix[len(arr)][final]


def find_paths(arr, a, matrix, final):
    """
    [2, 3, 7, 8] -> 10

    follow ^ and * for two
    paths in below example

    0 => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    2 => [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
          ^     ^
    3 => [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
          *     ^  *
    7 => [0, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2]
                ^  *                    *
    8 => [0, 1, 1, 1, 2, 2, 2, 1, 1, 2, 2]
                ^                       ^*
    """
    if a == 0 or final <= 0:
        return [[]]

    vals = []
    rem = final-arr[a-1]
    if rem >= 0 and matrix[a][final] - matrix[a][rem] == 1:
        # going horizontally
        # take current elem.
        vals = [x+[arr[a-1]] for x in
                find_paths(arr, a, matrix, rem)]

    if matrix[a-1][final] == matrix[a][final]:
        # going vertically up
        # ignore current elem
        vals.extend(find_paths(arr, a-1, matrix, final))

    return vals


arr = [1, 5, 10, 25]
final = 49
print(make_change_no_dp(arr, len(arr), final))
matrix = []
print(make_change_no_dp_short(arr, len(arr), final))
matrix = []
print(make_change(arr, final))
matrix = []
print(make_change_short(arr, final))
print(find_paths(arr, len(arr), matrix, final))
print("------")
final = 6
print(make_change_no_dp(arr, len(arr), final))
matrix = []
print(make_change_no_dp_short(arr, len(arr), final))
matrix = []
print(make_change(arr, final))
matrix = []
print(make_change_short(arr, final))
print(find_paths(arr, len(arr), matrix, final))
print("------")
matrix = []
final = 16
print(make_change_no_dp(arr, len(arr), final))
matrix = []
print(make_change_no_dp_short(arr, len(arr), final))
matrix = []
print(make_change(arr, final))
matrix = []
print(make_change_short(arr, final))
print(find_paths(arr, len(arr), matrix, final))
print("------")
arr = [1, 5, 8]
final = 14
matrix = []
print(make_change_no_dp(arr, len(arr), final))
matrix = []
print(make_change_no_dp_short(arr, len(arr), final))
matrix = []
print(make_change(arr, final))
matrix = []
print(make_change_short(arr, final))
print(find_paths(arr, len(arr), matrix, final))
print("------")
arr = [1, 2, 3, 7, 8]
final = 10
matrix = []
print(make_change_no_dp(arr, len(arr), final))
matrix = []
print(make_change_no_dp_short(arr, len(arr), final))
matrix = []
print(make_change(arr, final))
matrix = []
print(make_change_short(arr, final))
print(find_paths(arr, len(arr), matrix, final))
