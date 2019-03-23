# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 03:35:17 2019

@author: gaurav
"""
import numpy as np
import pandas as pd


print("------------")
print("===np tuples")

# numpy arrays are homogeneous multi-dimensional arrays
# these homogeneous datatype can, in fact, be tuple too
res = np.array([("TEXT", 1, 1), ("XXX", 2, 2)], dtype='|S4, i4, i4')
print(res)
print("===np matrix")

# Few matrix type operations on numpy multi-dimensional
# arrays. As matrix is just a view on the array. '@' is
# another way to achieve matrix multiplication.
a = np.array([[1, 2, 3], [1, 4, 5]])
b = np.array([[5, 4], [7, 8], [2, 3]])
print(a*a)
print(np.asmatrix(a) * np.asmatrix(b))
print(a @ b)  # dot product

print("===vectorize")
c = np.array([[2, 1, 3], [3, 5, 2]])
print(a, c)


def out(x, y):
    """vectorize just makes the function
    take a[] and b[] instead of a / b"""
    return x + y if x > y else x - y


print(np.vectorize(out)(a, c))
print(c, c.reshape(3, -1))

print("====mask/indexing")
print(a > 2, a[a > 2])
print(a[1, 2])


def nearest_neighbours():
    """nearest neighbours with numpy"""
    N = 4
    # 1000 points with x, y, z coordinates
    points = np.random.random((N, 3))

    # same points as 1-D array of x, y, z.
    # this is insane. we have brought each
    # point to same cardinality as points.
    pps = points.reshape(N, 1, 3)

    # now broadcasting
    # to generate diff
    # coordinate wise.
    pps = pps - points  # x-x, y-y, z-z
    pps **= 2  # (x-x)^2
    pps = pps.sum(2)  # dx^2 + dy^2 + dz^2

    # ignore diagonals i.e. diff from itself
    pps[np.arange(N), np.arange(N)] = np.inf
    pps.argmin(1)  # which point is min to i
    return (points, pps.argmin(1))


print("===neighbours")
print(nearest_neighbours())

print("------------")
print("====series")
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)

print("------------")
print("===dataframe")
df = pd.DataFrame({"a": [1, 2], "b": [45, 'x'], "c": [2, 1]})
print(df.to_csv(index=False))
