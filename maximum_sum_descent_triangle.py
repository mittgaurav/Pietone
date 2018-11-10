# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:35:52 2018

@author: gaurav
"""


def get(mat, i, j):
    if i < 0:
        return 0
    if j < 0 or j >= len(mat[i]):
        return 0
    return mat[i][j]


def maximum_sum_descent(arr):
    """
    2
    54
    347
    1696
    """
    matrix = []
    for i in range(0, len(arr)):
        matrix.insert(i, list())
        for j in range(0, i+1):
            matrix[i].insert(j, arr[i][j] + max(get(matrix, i-1, j),
                                                get(matrix, i-1, j-1)))
    return max(matrix[i])


print(maximum_sum_descent([[2], [5, 4], [3, 4, 7], [1, 6, 9, 6]]))
