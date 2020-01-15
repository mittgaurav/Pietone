# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 22:26:57 2020

@author: gaurav
"""

matrix = []
matrix.append(list(range(1, 5)))
matrix.append(list(range(5, 9)))
matrix.append(list(range(9, 13)))
matrix.append(list(range(13, 17)))
matrix.append(list(range(17, 21)))

result = []
for i in range(len(matrix)):
    result.append([0 for i in range(len(matrix[0]))])


def preprocess(matrix):
    """preprocess"""
    if not len(matrix) or not len(matrix[0]):
        return

    result[0][0] = matrix[0][0]  # first element sum
    for i in range(1, len(matrix)):  # first column
        result[i][0] = result[i-1][0] + matrix[i][0]

    for i in range(1, len(matrix[0])):  # first row
        result[0][i] = result[0][i-1] + matrix[0][i]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            # sum the two rectangular matrices
            # left and up. Subtract the square
            # as it is doubly counted. Add num
            result[i][j] = result[i-1][j] + result[i][j-1] \
                           + matrix[i][j] - result[i-1][j-1]


print("matrix:")
[print(_) for _ in matrix]
preprocess(matrix)
print("\npreprocess result:")
[print(_) for _ in result]


def matrix_sub_sum(matrix, i, j, I, J):
    """return sum of submatrix for
    given size by looking up a pre
    processed dataset"""
    if i > I or j > J:
        return 0

    print('\nsubmatrix:')
    [print(_[j:J+1]) for _ in matrix[i:I+1]]

    left_sum = result[I][j-1] if j > 0 else 0
    up_sum = result[i-1][J] if i > 0 else 0
    diag_sum = result[i-1][j-1] if i > 0 and j > 0 else 0

    return result[I][J] - left_sum - up_sum + diag_sum


print('sum:', matrix_sub_sum(matrix, 1, 1, 2, 3))
print('sum:', matrix_sub_sum(matrix, 0, 0, 4, 3))
print('sum:', matrix_sub_sum(matrix, 0, 0, 0, 0))
print('sum:', matrix_sub_sum(matrix, 0, 3, 3, 3))
