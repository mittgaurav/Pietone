# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:03:59 2019

@author: gaurav
"""

N = 4
board = [[0 for _ in range(N)] for _ in range(N)]

steps = 0


def step(i, j):
    """given the current step
    go to the next location"""
    if i < 0 or i >= N or j < 0 or j >= N:
        return False

    if board[i][j]:
        return False

    global steps
    steps += 1
    board[i][j] = steps

    if steps == N ** 2:
        return True

    for x in [i-2, i+2]:
        for y in [j-1, j+1]:
            if step(x, y):
                return True

    for x in [i-1, i+1]:
        for y in [j-2, j+2]:
            if step(x, y):
                return True

    board[i][j] = 0
    steps -= 1
    return False


step(0, 0)
assert [print(_) for _ in board]
