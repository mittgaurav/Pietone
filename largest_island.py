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

done = [[0 for _ in range(len(area[0]))] for _ in range(len(area))]


def count(i, j):
    """count num of
    continuous 1"""
    if i < 0 or i >= len(area) or j < 0 or j >= len(area[i]):
        return 0

    if done[i][j]:  # already
        return 0

    done[i][j] = True
    if not area[i][j]:  # zero
        return 0

    return (1 + count(i, j+1) + count(i, j-1) +
            count(i+1, j) + count(i-1, j))  # 4 direction


res = 0
for i in range(len(area)):
    for j in range(len(area[i])):
        res = max(res, count(i, j))

print(res)
