# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 15:01:38 2019

@author: gaurav
"""

area = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

visited = [[0 for _ in range(len(area[0]))] for _ in range(len(area))]


def count(i, j):
    """count num of
    continuous 1"""
    if i < 0 or i >= len(area) or j < 0 or j >= len(area[i]):
        return 0

    if visited[i][j]:  # already
        return 0

    visited[i][j] = True
    if not area[i][j]:  # zero
        return 0

    return (1 + count(i, j+1) + count(i, j-1) +
            count(i+1, j) + count(i-1, j))  # 4 direction


res = 0
for i in range(len(area)):
    for j in range(len(area[i])):
        res = max(res, count(i, j))

print(res)


area = [[0, 0, 1, 2, 2, 0, 3],
        [0, 1, 1, 2, 3, 3, 3],
        [2, 2, 2, 2, 4, 4, 3],
        [0, 2, 1, 2, 4, 2, 1],
        [4, 0, 1, 1, 3, 3, 3],
        [2, 0, 0, 2, 3, 0, 3],
        [1, 0, 1, 1, 3, 0, 3],
        [1, 1, 0, 2, 3, 3, 3]]

visited = [[0 for _ in range(len(area[0]))] for _ in range(len(area))]


def count_nation(i, j, val):
    """for multiple options,
    give the largest nation"""
    if i < 0 or i >= len(area) or j < 0 or j >= len(area[i]):
        return 0

    if visited[i][j]:  # already
        return 0

    # can add to current nation?
    if area[i][j] != val:
        return 0

    visited[i][j] = True
    return (1 + count_nation(i, j+1, val) + count_nation(i, j-1, val) +
            count_nation(i+1, j, val) + count_nation(i-1, j, val))


res = 0
for i in range(len(area)):
    for j in range(len(area[i])):
        res = max(res, count_nation(i, j, area[i][j]))

print(res)
