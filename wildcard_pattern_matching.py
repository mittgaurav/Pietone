# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:24:26 2018

@author: gaurav
"""


def wildcard_matching_no_dp(string, pat):
    """tell whether pattern represents
    string as wildcard. '*' and '?'"""
    if not pat:
        return not string

    if not string:
        for i in pat:
            if i is not '*':
                return False
        return True

    # Either char matched or any char
    if string[0] == pat[0] or pat[0] == '?':
        return wildcard_matching_no_dp(string[1:], pat[1:])

    # Not a wildcard, and no char match
    if pat[0] != '*':
        return False

    # wildcard (*)
    # remove current char or
    # remove current char and * or
    # remove *
    return (wildcard_matching_no_dp(string[1:], pat) or
            wildcard_matching_no_dp(string[1:], pat[1:]) or
            wildcard_matching_no_dp(string, pat[1:]))


def get(matrix, i, j):
    if i >= len(matrix) or i < 0:
        return True
    if j >= len(matrix[0]) or j < 0:
        return True
    return matrix[i][j]


def wildcard_matching_dp(string, pat):
    """memoization"""
    if not pat:
        return not string

    if not string:
        for i in pat:
            if i is not '*':
                return False
        return True

    # fill to prevent out of index
    matrix = list()
    for i in range(0, len(string)):
        matrix.append(list())
        for j in range(0, len(pat)):
            matrix[i].append(False)

    # Fill matrix from end.
    for i in range(len(string)-1, -1, -1):
        for j in range(len(pat)-1, -1, -1):
            if string[i] == pat[j] or pat[j] == '?':
                matrix[i][j] = get(matrix, i+1, j+1)
            elif pat[j] != '*':
                matrix[i][j] = False
            else:
                matrix[i][j] = (get(matrix, i+1, j) or
                                get(matrix, i+1, j+1) or
                                get(matrix, i, j+1))

    return matrix[0][0]


wildcard_matching = wildcard_matching_dp
wildcard_matching = wildcard_matching_no_dp

print(wildcard_matching("", ""))
print(wildcard_matching("", "**"))
print(wildcard_matching("a", ""))  # False
print(wildcard_matching("a", "a"))

string = "baaabab"
print(wildcard_matching(string, "***"))
print(wildcard_matching(string, "a*ab"))  # False
print(wildcard_matching(string, "ba*a?"))
print(wildcard_matching(string, "baaa?ab"))
print(wildcard_matching(string, "*****ba*****ab"))
