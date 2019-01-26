# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 19:32:39 2018

@author: gaurav
"""
matrix = list()


def levenshtein_dist(arr, brr):
    """figure out the solution"""
    # fill zero column and row
    for i in range(0, len(arr) + 1):
        matrix.insert(i, list())
        matrix[i].insert(0, 0)
    for j in range(0, len(brr) + 1):
        matrix[0].insert(j, 0)

    for i in range(1, len(arr) + 1):
        for j in range(1, len(brr) + 1):
            if arr[i-1] == brr[j-1]:
                matrix[i].insert(j, matrix[i-1][j-1])
            else:
                matrix[i].insert(j, 1 + min(matrix[i-1][j-1],
                                            matrix[i][j-1],
                                            matrix[i-1][j]))
    return matrix[len(arr)][len(brr)]


def levenshtein_dist_no_dp(arr, brr, a, b):
    """find levenshtein distance of given
    strings. We have these possibilities:
    either char are same, arr is removed,
    or brr is removed, or both chars are
    removed."""
    if a == 0:
        return b
    elif b == 0:
        return a

    # if the two chars are same,
    # we check for smaller words
    if arr[a-1] == brr[b-1]:
        return levenshtein_dist_no_dp(arr, brr, a-1, b-1)
    else:
        # We have lost one count. However, we
        # still not sure that the match is in
        # fact better as we may win if remove
        # this char from one or the other arr
        return(1 + min(
            levenshtein_dist_no_dp(arr, brr, a-1, b),  # remove a
            levenshtein_dist_no_dp(arr, brr, a, b-1),  # remove b
            levenshtein_dist_no_dp(arr, brr, a-1, b-1)
            ))


A = "kitten"
B = "sitten"
print(levenshtein_dist_no_dp(A, B, len(A), len(B)))
print(levenshtein_dist(A, B))
A = "booking"
B = "backsin"
print(levenshtein_dist_no_dp(A, B, len(A), len(B)))
print(levenshtein_dist(A, B))
