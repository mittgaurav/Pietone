# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 01:21:19 2018

@author: gaurav
"""


def max_ss(arr):
    """max sum of values that
    are not adjacent"""
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1])

    # i + fn(array from next++)
    # or
    # fn(array from next of me)
    # if current index is negative, drop
    return max(max_ss(arr[1:]), max(0, arr[0]) + max_ss(arr[2:]))


def get(matrix, i):
    if i < 0:
        return 0
    return matrix[i]


def maxSubsetSum_dp(arr):
    """similar to non-dp but indices
    reversed. But similar model"""
    m = list()
    for i in range(0, len(arr)):
        m.append(max(get(m, i-1), max(0, arr[i]) + get(m, i-2)))

    return m[-1]


print(maxSubsetSum_dp([1]))
print(maxSubsetSum_dp([1, 2, 4, 1, 2, 3, 5, 3, 1, 2, 3, 4, 5, 2]))

print(max_ss([1]))
print(max_ss([1, 2, 4, 1, 2, 3, 5, 3, 1, 2, 3, 4, 5, 2]))
