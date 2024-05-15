# -*- coding: utf-8 -*-
"""
Created on Fri May 22 03:23:23 2020

@author: gaurav
"""


def greatest_product(matrix, i, j):
    """
    www.byte-by-byte.com/matrixproduct/
    Given a matrix, find the path from
    top left to bottom right, with the
    greatest product by moving in only
    down and right direction.
    Works with only positive values...
    """
    if i < 0 or j < 0:
        return 1

    return max(matrix[i][j] * greatest_product(matrix, i-1, j),
               matrix[i][j] * greatest_product(matrix, i, j-1))


matrix = [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
]
print(greatest_product(matrix, 2, 2))

matrix = [
         [-1, 2, 3],
         [4, 5, -6],
         [7, 8, 9],
         ]
print(greatest_product(matrix, 2, 2))  # incorrect


def greatest_product(matrix, i, j):
    """
    www.byte-by-byte.com/matrixproduct/
    Given a matrix, find the path from
    top left to bottom right, with the
    greatest product by moving in only
    down and right direction.
    """
    if i == 0 and j == 0:
        return (matrix[i][j], matrix[i][j])

    # return two element - first max and
    # second lowest. Since, negative val
    # can change lowest to max - so we'd
    # keep track of both and use the one
    # that fits our usecase here.
    if i > 0:
        prev_i_max, prev_i_min = greatest_product(matrix, i-1, j)
    else:
        prev_i_max, prev_i_min = -999999, 999999
    if j > 0:
        prev_j_max, prev_j_min = greatest_product(matrix, i, j-1)
    else:
        prev_j_max, prev_j_min = -999999, 999999
    i_j_max = matrix[i][j] * max(prev_i_max, prev_j_max)
    i_j_min = matrix[i][j] * min(prev_i_min, prev_j_min)

    return max(i_j_max, i_j_min), min(i_j_max, i_j_min)


matrix = [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
]
print(greatest_product(matrix, 2, 2))

matrix = [
         [-1, 2, 3],
         [4, 5, -6],
         [7, 8, 9],
         ]
print(greatest_product(matrix, 2, 2))


def ordered_points(points):
    import math

    def angle(x, p):
        # return angle in radian
        at = math.atan2(x[1]-p[1], x[0]-p[0])
        # if negative atan, then
        # 2*pi to make it to +ve
        return at if at >= 0 else math.tau + at

    if len(points) < 3: return 0
    for i in range(len(points)):
        p = points[i]
        rem = sorted(points[i+1:], key=lambda x: angle(x, p))
        print(p, rem)


print(ordered_points.__name__)
points = [(0, 0), (0, 1), (1, 0), (-4, 4), (-3, -2)]
ordered_points(points)


def num_triangles_no_point_inside(points):
    """for given list of points in 2-D plane
    return number of triangles possible with
    three points such that no other point is
    inside or on the edge of the triangle"""
    pass
