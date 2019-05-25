# -*- coding: utf-8 -*-
"""
Created on Sat May 25 23:25:16 2019

@author: gaurav
"""


def unique_path_through_obstacles(A):
    """path through a matrix of
    obstacles to reach the end"""
    if not A or not A[0]:
        return 0
    m = len(A)
    n = len(A[0])

    if A[m-1][n-1] == 1:
        return 0

    def paths_from(x, y):
        if x == m or y == n:
            return 0
        if A[x][y] == 1:
            return 0
        if x == m-1 and y == n-1:
            return 1
        return paths_from(x+1, y) + paths_from(x, y+1)

    return paths_from(0, 0)


print(unique_path_through_obstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
]))

print(unique_path_through_obstacles([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
]))
