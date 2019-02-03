# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 00:54:52 2019

@author: gaurav
"""


def longest_palin_seq(arr):
    """longest palindromic
    subsequence"""
    if not arr:
        return 0

    if arr[0] == arr[-1]:
        # The two extremes match,
        # try after removing them
        return 2 + longest_palin_seq(arr[1:-1])
    # see by removing either first or last
    return max(longest_palin_seq(arr[1:]),
               longest_palin_seq(arr[:-1]))


def longest_palin_dp(arr, i, j):
    """memoization: matrix of
    start and end indices"""
    if i < 0 or j >= len(arr) or i > j:
        return 0

    if matrix[i][j] != -1:  # already set
        return matrix[i][j]

    if i == j:
        matrix[i][j] = 1
    elif arr[i] == arr[j]:
        matrix[i][j] = 2 + longest_palin_dp(arr, i+1, j-1)
    else:
        matrix[i][j] = max(longest_palin_dp(arr, i+1, j),
                           longest_palin_dp(arr, i, j-1))

    return matrix[i][j]


for A in ["abdbca", "cddpd"]:
    matrix = [[-1 for _ in A] for _ in A]
    print(longest_palin_seq(A), longest_palin_dp(A, 0, len(A)-1))
