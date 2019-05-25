# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 14:18:09 2019

@author: gaurav

anti-clockwise
"""


def rotation(A, rs, re, cs, ce):
    """for matrix dimensions,
    returns shell as array"""
    arr = []
    if rs > re or cs > ce:
        return arr

    for i in range(rs, re+1):
        arr.append((i, cs, A[i][cs]))

    for i in range(cs+1, ce+1):
        arr.append((re, i, A[re][i]))

    for i in range(re-1, rs-1, -1):
        arr.append((i, ce, A[i][ce]))

    for i in range(ce-1, cs, -1):
        arr.append((rs, i, A[rs][i]))

    return arr


def matrix_rotation(A, rot):
    """rotate matrix layers r times"""
    # form a shell
    rs = 0
    re = len(A)-1
    cs = 0
    ce = len(A[0])-1

    while True:
        arr = rotation(A, rs, re, cs, ce)
        if not arr:
            break
        for i in range(len(arr)):
            # we have matrix shell
            # that needs to rotate
            # we replace location
            # that ith goes into.
            (newr, newc, _) = arr[(i+rot) % (len(arr))]
            A[newr][newc] = arr[i][2]
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


def matrix_spiral_print(A, rs, re, cs, ce):
    """print spiral matrix"""
    if rs > re or cs > ce:
        return
    for i in range(rs, re+1):
        print(A[i][cs], end=" ")
    for i in range(cs+1, ce+1):
        print(A[re][i], end=" ")
    for i in range(re-1, rs-1, -1):
        print(A[i][ce], end=" ")
    for i in range(ce-1, cs, -1):
        print(A[rs][i], end=" ")

    matrix_spiral_print(A, rs+1, re-1, cs+1, ce-1)


print(matrix_spiral_print.__name__)
matrix_spiral_print(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1)
print('\n-----')


def clockwise_rotation(A):
    """rotate 90 degrees clockwise

    n,0   -> 0,0
    n-1,0 -> 0,1
    n-k,i -> i,i+k....

    n,n   -> n,0
    n,n-1 -> n-1,0
    n,n-k -> n-k,i....

    0,n   -> n,n
    1,n   -> n,n-1
    i+k,n -> n,n-k....

    0,0   -> 0,n
    0,1   -> 1,n
    i,i+k -> i+k,n....
    """
    if not A:
        return A

    i = 0
    n = len(A) - 1
    while i < n:
        k = 0
        while k < n - i:
            temp = A[i][i+k]
            A[i][i+k] = A[n-k][i]
            A[n-k][i] = A[n][n-k]
            A[n][n-k] = A[i+k][n]
            A[i+k][n] = temp
            k += 1
        i += 1
        n -= 1

    return A


print(clockwise_rotation.__name__)
print(clockwise_rotation([[1, 2], [3, 4]]))
