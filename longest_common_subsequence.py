# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 14:46:09 2018

@author: gaurav

match - delete both chars
and go to smaller matrix.

no match - better between
to remove char from A and match with B
or remove char from B and match with A

Different from Levenshtein
distances; that has option
to substitute current char
i.e. lose on val but check
after delete both char for
the case of no match also.

      c  b  a  b  a  c
  [0, 0, 0, 0, 0, 0, 0]
a [0, 0, 0, 1, 1, 1, 1]
b [0, 0, 1, 1, 2, 2, 2]
c [0, 1, 1, 1, 2, 2, 3]
a [0, 1, 1, 2, 2, 3, 3]
b [0, 1, 2, 2, 3, 3, 3]
b [0, 1, 2, 2, 3, 3, 3]
a [0, 1, 2, 3, 3, 4, 4]
"""
matrix = list()


def longest_common_subsequence(arr, brr):
    """subsequence is something that can
    remove elements but keeps remaining
    in the original order"""

    # fill zero column and row
    for i in range(0, len(arr) + 1):
        matrix.append(list())
        for j in range(0, len(brr) + 1):
            matrix[i].append(0)

    for i in range(0, len(arr)):
        for j in range(0, len(brr)):
            if arr[i] == brr[j]:
                # both elements are same, so
                # we take this and add to so
                # far accumulated max in n-1
                # matrix, matrix[i-1][j-1]
                matrix[i+1][j+1] = 1 + matrix[i][j]
            else:
                # no match so no improvement
                # hence we take max of value
                # from smaller matrices till
                # this column and row.
                matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j])

    return matrix[i+1][j+1]


def find_paths(arr, brr, matrix, i, j):
    """paths are only possible in a certain
    way: matching element: matrix[i-1][j-1]
    unless we go back in same column or row
    or both till we have no match"""
    if i == 0 or j == 0:
        return [""]

    if arr[i-1] == brr[j-1]:
        # elements match: matrix[i-1][j-1]
        more = find_paths(arr, brr, matrix, i-1, j-1)
        return [x+arr[i-1] for x in more]

    result = list()
    if matrix[i][j] == matrix[i-1][j]:
        # we look back in same row and
        # no difference. Hence follow.
        more = find_paths(arr, brr, matrix, i-1, j)
        result.extend(more)
    if matrix[i][j] == matrix[i][j-1]:
        # we look back in same col and
        # no difference. Hence follow.
        more = find_paths(arr, brr, matrix, i, j-1)
        result.extend(more)

    return list(set(result))


def lcs_no_dp(arr, brr, a, b):
    """no DP. Only algorithm"""
    if a == 0 or b == 0:
        return 0
    if arr[a-1] == brr[b-1]:
        # i match, step in both
        return 1 + lcs_no_dp(arr, brr, a-1, b-1)
    # remove a or b
    # BUT NOT BOTH!
    return max(lcs_no_dp(arr, brr, a-1, b),
               lcs_no_dp(arr, brr, a, b-1))


arr = "abcabba"
brr = "cbabac"
print(longest_common_subsequence(arr, brr))
print(find_paths(arr, brr, matrix, len(arr), len(brr)))
print(lcs_no_dp(arr, brr, len(arr), len(brr)))


def lcs(arr, brr):
    """another way of doing
    from starting index."""
    if len(arr) == 0 or len(brr) == 0:
        return 0

    if arr[0] == brr[0]:
        return 1 + lcs(arr[1:], brr[1:])

    return max(lcs(arr, brr[1:]), lcs(arr[1:], brr))


print(lcs(arr, brr))
print("==================")


def is_subsequence(arr, brr):
    """is brr subsequence of arr"""
    if not brr:
        return True

    if not arr:
        return False

    if len(arr) < len(brr):
        return False

    if arr[0] == brr[0]:
        brr = brr[1:]
    return is_subsequence(arr[1:], brr)


print("abcde", "abc", is_subsequence("abcde", "abc"))
print("abcde", "acb", is_subsequence("abcde", "acb"))
