# -*- coding: utf-8 -*-
"""
Created on Sun May 10 02:12:35 2020

@author: gaurav
"""
import math
from functools import reduce
from operator import add

board = [
        [4, 3, 0, 0],
        [1, 2, 3, 0],
        [0, 0, 2, 0],
        [2, 1, 0, 0]
        ]


def _check(board, full=False):
    N = len(board)

    def _inner(r):
        vals = [x for x in r if x != 0]  # non-zero elements
        if full:
            # contain all elements up to N
            if sorted(vals) != list(range(1, N + 1)):
                return False
        else:
            # no value below 1 and no value above N
            if [x for x in vals if x <= 0 or x > N]:
                return False
            # all unique
            if len(vals) != len(set(vals)):
                return False
        return True

    for i in range(N):
        # row and column
        for r in (board[i], [x[i] for x in board]):
            if not _inner(r):
                return False

    # each sub-matrix is sqrt(N)
    sqrt = int(math.sqrt(N))
    for i in range(0, N, sqrt):
        for j in range(0, N, sqrt):
            cells = reduce(add,
                           [r[j:j+sqrt] for r in board[i:i+sqrt]], [])
            if not _inner(cells):
                return False

    return True


def solve_sudoku(board):
    N = len(board)

    def _solve(cell):
        """choose - constraint - goal"""
        if cell >= N * N:  # goal
            print('solution')
            [print(_) for _ in board]
            return True if _check(board, True) else False

        r, c = cell // N, cell % N

        if board[r][c] != 0:
            # cell is already filled. go to next
            return _solve(cell + 1)

        for i in range(1, len(board) + 1):
            # choose
            board[r][c] = i
            # constraint
            if _check(board):
                # recurse
                _solve(cell + 1)
            # undo
            board[r][c] = 0

    _solve(0)


[print(_) for _ in board]
solve_sudoku(board)

board = [
         [5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
solve_sudoku(board)

grid = []
grid.append([3, 0, 6, 5, 0, 8, 4, 0, 0])
grid.append([5, 2, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 8, 7, 0, 0, 0, 0, 3, 1])
grid.append([0, 0, 3, 0, 1, 0, 0, 8, 0])
grid.append([9, 0, 0, 8, 6, 3, 0, 0, 5])
grid.append([0, 5, 0, 0, 9, 0, 6, 0, 0])
grid.append([1, 3, 0, 0, 0, 0, 2, 5, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 7, 4])
grid.append([0, 0, 5, 2, 0, 6, 3, 0, 0])

solve_sudoku(grid)