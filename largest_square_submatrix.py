# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 01:26:49 2018

@author: gaurav
"""
"""
[False,         True,        False,        False],
[True,          True,         True,         True],
[False,         True,         True,        False],
for each elem, collect four values:

* Continuous true horizontally

* Continuous true vertically

* Minimum of continuous true
horizontally, vertically, or
diagonally. This tells exact
size of square matrix that's
ending at this very element.

* The overall maximum square
matrix size till this point.

[[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
[[1, 1, 1, 1], [2, 2, 1, 1], [1, 3, 1, 1], [1, 4, 1, 1]]
[[0, 0, 0, 1], [3, 1, 1, 1], [2, 2, 2, 2], [0, 0, 0, 2]]

Though, we can easily remove
4th elems. Instead, maintain
a global max.
"""
matrix = list()


def square_submatrix(input):
    """given a matrix, find the
    largest square matrix with
    all vals equal to true"""
    for i in range(0, len(input) + 1):
        matrix.insert(i, list())
        matrix[i].insert(0, [0, 0, 0, 0])
    for j in range(0, len(input[0]) + 1):
        matrix[0].insert(j, [0, 0, 0, 0])

    m = 0
    for i in range(1, len(input) + 1):
        for j in range(1, len(input[0]) + 1):
            arr = list()
            if input[i-1][j-1]:
                """True"""
                # horizontal
                arr.append(1 + matrix[i-1][j][0])
                # vertical
                arr.append(1 + matrix[i][j-1][1])
                # Size of matrix
                # at this point.
                arr.append(min(arr[0], arr[1],
                               1 + matrix[i-1][j-1][2]))
            else:
                """False"""
                arr.append(0)
                arr.append(0)
                arr.append(0)

            # The overall maximum size
            # of matrix seen till now.
            arr.append(max(arr[2], matrix[i-1][j-1][3],
                           matrix[i-1][j][3], matrix[i][j-1][3]))

            # we can have running max
            m = max(arr[3], m)

            # or keep within memoizer
            matrix[i].insert(j, arr)

    # both should nonetheless be same
    assert(m == matrix[len(input)][len(input[0])][3])

    return m


def square_submatrix_short(input):
    """I don't need to keep so
    many values. What if I get
    only the maximum?
    Quite similar to finding
    longest True series in an
    array. You maintain local
    size and a global max one
    """
    for i in range(0, len(input) + 1):
        matrix.insert(i, list())
        matrix[i].insert(0, 0)
    for j in range(0, len(input[0]) + 1):
        matrix[0].insert(j, 0)

    m = 0
    for i in range(1, len(input) + 1):
        for j in range(1, len(input[0]) + 1):
            if input[i-1][j-1]:
                # if current val is True
                # then we can add on to
                # existing size. Min of
                # left, right, and diag
                val = 1 + min(matrix[i-1][j],
                              matrix[i][j-1],
                              matrix[i-1][j-1])
            else:
                val = 0
            matrix[i].insert(j, val)
            m = max(m, val)
    return m


matrix = []
print(square_submatrix([
        [False, True, False, False],
        [True,  True,  True,  True],
        [False, True,  True, False],
        ]))
matrix = []
print(square_submatrix_short([
        [False, True, False, False],
        [True,  True,  True,  True],
        [False, True,  True, False],
        ]))
print("-----")

matrix = []
print(square_submatrix([
        [True,  True,  True,  True,  True],
        [True,  True,  True,  True, False],
        [True,  True,  True,  True, False],
        [True,  True,  True,  True, False],
        [True, False, False, False, False]
        ]))
matrix = []
print(square_submatrix_short([
        [True,  True,  True,  True,  True],
        [True,  True,  True,  True, False],
        [True,  True,  True,  True, False],
        [True,  True,  True,  True, False],
        [True, False, False, False, False]
        ]))
print("-----")

matrix = []
print(square_submatrix([
        [True,  True,  True,  True,  True],
        [True,  True,  True,  True, False],
        [True, False,  True,  True, False],
        [True,  True,  True,  True, False],
        [True, False, False, False, False]
        ]))
matrix = []
print(square_submatrix_short([
        [True,  True,  True,  True,  True],
        [True,  True,  True,  True, False],
        [True, False,  True,  True, False],
        [True,  True,  True,  True, False],
        [True, False, False, False, False]
        ]))
print("-----")
