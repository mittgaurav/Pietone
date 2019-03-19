# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 14:18:09 2019

@author: gaurav

anti-clockwise
"""


def rotation(matrix, rs, re, cs, ce):
    """for matrix dimensions,
    returns shell as array"""
    arr = []
    if rs > re or cs > ce:
        return arr

    for i in range(rs, re+1):
        arr.append((i, cs, matrix[i][cs]))

    for i in range(cs+1, ce+1):
        arr.append((re, i, matrix[re][i]))

    for i in range(re-1, rs-1, -1):
        arr.append((i, ce, matrix[i][ce]))

    for i in range(ce-1, cs, -1):
        arr.append((rs, i, matrix[rs][i]))

    return arr


def matrix_rotation(matrix, rot):
    """rotate matrix layers r times"""
    # form a shell
    rs = 0
    re = len(matrix)-1
    cs = 0
    ce = len(matrix[0])-1

    while True:
        arr = rotation(matrix, rs, re, cs, ce)
        if not arr:
            break
        for i in range(len(arr)):
            # we have matrix shell
            # that needs to rotate
            # we replace location
            # that ith goes into.
            (newr, newc, _) = arr[(i+rot) % (len(arr))]
            matrix[newr][newc] = arr[i][2]
        rs += 1
        re -= 1
        cs += 1
        ce -= 1


matrix = []
matrix.append(list(range(1, 5)))
matrix.append(list(range(5, 9)))
matrix.append(list(range(9, 13)))
matrix.append(list(range(13, 17)))
matrix.append(list(range(17, 21)))
assert [print(_) for _ in matrix]
matrix_rotation(matrix, 1)
print("-----")
assert [print(_) for _ in matrix]
matrix_rotation(matrix, 3)
print("-----")
assert [print(_) for _ in matrix]
matrix_rotation(matrix, 100)
print("-----")
assert [print(_) for _ in matrix]
print("-----")


def matrix_spiral_print(matrix, rs, re, cs, ce):
    """print spiral matrix"""
    if rs > re or cs > ce:
        return
    for i in range(rs, re+1):
        print(matrix[i][cs], end=" ")
    for i in range(cs+1, ce+1):
        print(matrix[re][i], end=" ")
    for i in range(re-1, rs-1, -1):
        print(matrix[i][ce], end=" ")
    for i in range(ce-1, cs, -1):
        print(matrix[rs][i], end=" ")

    matrix_spiral_print(matrix, rs+1, re-1, cs+1, ce-1)


print(matrix_spiral_print.__name__)
matrix_spiral_print(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1)
