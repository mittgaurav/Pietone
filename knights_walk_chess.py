# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:03:59 2019

@author: gaurav

knight's tour across the board.
Start from (0, 0) and see if we
can make the next step. Keep it
going till we can't. Then back-
track and try next value.
"""

N = 5
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

    if steps == N ** 2:  # consumed all board
        return True

    for x in [i-2, i+2]:
        for y in [j-1, j+1]:
            if step(x, y):
                return True

    for x in [i-1, i+1]:
        for y in [j-2, j+2]:
            if step(x, y):
                return True

    # we have no way
    # to see through
    # this location.
    board[i][j] = 0
    steps -= 1
    return False


step(0, 0)
assert [print(_) for _ in board]
