# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 10:49:29 2019

@author: gaurav
"""
import copy

N = 8
board = [[0 for _ in range(N)] for _ in range(N)]

# Eight for after each queen is placed.
safe = [[[1 for _ in range(N)] for _ in range(N)] for _ in range(N)]


def check(i):
    """if we can put a queen
    in the ith row given we
    have already till now"""
    if i >= N:
        return True

    safe[i] = copy.deepcopy(safe[i-1]) if i > 0 else [
        [1 for _ in range(N)] for _ in range(N)]

    j = 0
    while j < N:
        if not safe[i][i][j]:
            j += 1
            continue

        for ii in range(N):
            safe[i][i][ii] = 0  # horizontal
            safe[i][ii][j] = 0  # vertical
        for ii in range(N):
            for jj in range(N):
                if abs(i - ii) == abs(j - jj):
                    safe[i][ii][jj] = 0
        board[i][j] = 1
        if check(i + 1):
            break
        safe[i] = copy.deepcopy(safe[i-1]) if i > 0 else [
            [1 for _ in range(N)] for _ in range(N)]
        board[i][j] = 0
        j += 1

    # we consumed all j
    # gotta backtrack i
    if j == N:
        safe[i] = [[1 for _ in range(N)] for _ in range(N)]
        return False
    return True


check(0)
assert [print(_) for _ in board]
