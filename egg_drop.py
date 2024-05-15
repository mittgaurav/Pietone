# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 13:18:16 2019

@author: gaurav

ef 0 1 2 3 4 5 6 7 8 9 10
0  0 0 0 0 0 0 0 0 0 0 0
1  0 1 2 3 4 5 6 7 8 9 10
2  0 1 2 2
"""


def egg_floor(floor, egg):
    """minimum number of tries
    to find max floor that egg
    won't break from"""
    if egg == 1:
        return floor
    if 0 <= floor <= 1:
        return floor

    steps = 99999
    for i in range(1, floor + 1):
        # -if the egg breaks at i
        # floor, check i-1 floors
        # with one less egg.
        # -egg doesn't break at i
        # so check with the above
        # floors with same eggs.
        # Max of these cases will
        # be upperlimit on num of
        # trials for floor i. For
        # every floor, minimizing
        # this limit is min steps
        res = max(egg_floor(i - 1, egg - 1),  # breaks
                  egg_floor(floor - i, egg))  # check floors above
        steps = min(1 + res, steps)
    return steps


def egg_floor_dp(floor, egg):
    """dynamic programming"""
    matrix = [[0 for _ in range(floor+1)] for _ in range(egg+1)]

    # one egg is tried linearly for each floor
    for j in range(1, floor+1): matrix[1][j] = j
    # one floor is tried only once for any #egg
    for i in range(1, egg+1): matrix[i][1] = 1

    for i in range(2, egg+1):
        for j in range(2, floor+1):
            steps = 999999
            for x in range(1, j+1):
                steps = min(steps, 1 + max(matrix[i-1][x-1],
                                           matrix[i][j-x]))
            matrix[i][j] = steps
    return matrix[egg][floor]


print(egg_floor(12, 2))
print(egg_floor_dp(12, 2))
print(egg_floor_dp(36, 4))
print(egg_floor_dp(36, 2))
print(egg_floor_dp(100, 2))
print(egg_floor_dp(100, 100))
