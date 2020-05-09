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
    in the ith row, given we
    have already till now"""
    if i >= N:
        return True

    # for each iteration, make copy
    # of previous safe setting. Can
    # be applied to horizontal and
    # vertical only.
    safe[i] = copy.deepcopy(safe[i-1]) if i > 0 else [
        [1 for _ in range(N)] for _ in range(N)]

    j = 0
    while j < N:
        if not safe[i][i][j]:
            # if we have consumed this
            # loc so far in this check
            j += 1
            continue

        for ii in range(N):
            # we are going to choose this,
            # so this row and column can't
            # be used furthermore.
            safe[i][i][ii] = 0  # horizontal
            safe[i][ii][j] = 0  # vertical
        # diagonals are also not safe now.
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


def _inner_check(board, full=False):
    """check if current board
    is legal and safe"""
    if not board:
        return False
    n = len(board)

    # overall n queens be placed
    if sum(sum(x) for x in board) > n:
        return False

    if full and sum(sum(x) for x in board) != n:
        return False

    for i in range(n):
        # each row should have 1
        if sum(board[i]) > 1:
            return False
        # each col should have 1
        if sum(x[i] for x in board) > 1:
            return False

    for p in range(2*n-1):
        if sum([board[p-q][q] for q in
                range(max(0, p - n + 1), min(p, n - 1) + 1)]) > 1:
            return False
        if sum([board[n-p+q-1][q] for q in
                range(max(0, p - n + 1), min(p, n - 1) + 1)]) > 1:
            return False

    return True


print(_inner_check(board, True))


def nqueen_solve(n):
    """solve nqueen"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    backtrack_j = [0 for _ in range(n)]

    i = 0
    while 0 <= i < n:
        board[i] = [0 for _ in range(n)]

        for j in range(backtrack_j[i], n):
            # put queen and check if
            # we are still okay
            board[i][j] = 1

            if not _inner_check(board):
                # not okay. So, we have to
                # undo this and try next j
                board[i][j] = 0
            else:
                # we are okay, woohoo.
                # lets move to next i
                backtrack_j[i] = j+1
                i += 1
                break

            # if we exhaused everything
            # without setting even last
            # then we chose bad i, back
            # track to previous i
            if j == n-1 and board[i][j] == 0:
                backtrack_j[i] = 0
                i -= 1

        # quirk when previous row
        # is also exhaused - then
        # empty that row and move
        # one more row back
        if i < n and backtrack_j[i] >= n:
            backtrack_j[i] = 0
            board[i] = [0 for _ in range(n)]
            i -= 1

    return board


board = nqueen_solve(8)
assert [print(_) for _ in board]
print(_inner_check(board, True))


def solve_nqueen(n):
    """www.youtube.com/watch?v=u6viVC1fJ9g"""
    col = [True for _ in range(n)]
    d1 = [True for _ in range((2*n) - 1)]
    d2 = [True for _ in range((2*n) - 1)]

    def solve(r, res=0):
        if r == n:
            return res+1

        for c in range(n):
            if col[c] and d1[r-c+n-1] and d2[r+c]:
                col[c] = d1[r-c+n-1] = d2[r+c] = False
                res = solve(r+1, res)
                col[c] = d1[r-c+n-1] = d2[r+c] = True
        return res

    return solve(0)


print(solve_nqueen(4))
print(solve_nqueen(5))
print(solve_nqueen(8))
print(solve_nqueen(12))


def solve_nqueen_2(n):
    """choice - constraint - goal
    * Choice for each cell - 1/0
    * Constraint _inner_check
    * Goal - if reached end - _inner_check
    """
    board = [[0 for _ in range(n)] for _ in range(n)]

    def solve(cell, res=0):
        # goal
        if cell >= (n*n):
            return res+1 if _inner_check(board, True) else res

        r, c = cell // n, cell % n

        for val in (1, 0):
            # choice
            board[r][c] = val

            # constraint
            if _inner_check(board):
                res = solve(cell+1, res)

        board[r][c] = 0
        return res

    return solve(0)


print(solve_nqueen_2(4))
print(solve_nqueen_2(5))
# print(solve_nqueen_2(8))


def solve_nqueen_2(n):
    """choice - constraint - goal
    * Choice for each row - where to put 1
    * Constraint _inner_check
    * Goal - if reached end - _inner_check
    """
    board = [[0 for _ in range(n)] for _ in range(n)]

    def solve(r, res=0):
        # goal
        if r >= n:
            return res+1 if _inner_check(board, True) else res

        for c in range(n):
            # choice
            board[r][c] = 1

            # constraint
            if _inner_check(board):
                res = solve(r+1, res)

            board[r][c] = 0

        return res

    return solve(0)


print(solve_nqueen_2(4))
print(solve_nqueen_2(5))
print(solve_nqueen_2(8))
