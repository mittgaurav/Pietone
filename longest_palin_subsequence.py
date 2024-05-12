# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 00:54:52 2019

@author: gaurav
"""


def longest_palin_seq(arr) -> 'int':
    """longest palindromic
    subsequence"""
    if not arr:
        return 0

    if len(arr) == 1:
        return 1

    if arr[0] == arr[-1]:
        # The two extremes match,
        # try after removing them
        return 2 + longest_palin_seq(arr[1:-1])
    # see by removing either first or last
    return max(longest_palin_seq(arr[1:]),
               longest_palin_seq(arr[:-1]))


def longest_palin_dp(arr, i, j) -> 'int':
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


print(longest_palin_seq.__name__)
for A in ["abdbca", "cddpd"]:
    matrix = []
    for i in range(len(A)):
        matrix.append([])
        for j in range(len(A)):
            matrix[i].append(-1)
    print(A, longest_palin_seq(A), longest_palin_dp(A, 0, len(A)-1))
print("--------------------")


def l_p_string(arr):
    """contiguous string
    that's a palindrome"""
    ### NOT CORRECT
    ### Need MANACHER
    if not arr:
        return (0, True)
    if len(arr) == 1:
        return (1, True)
    if len(arr) == 2:
        return (2, True) if arr[0] == arr[1] else (0, False)

    # chars don't match,
    # so check internal.
    # Is not continuous
    if arr[0] != arr[-1]:
        return((max(l_p_string(arr[:-1])[0],
                    l_p_string(arr[1:])[0]), False))

    val, club = l_p_string(arr[1:-1])
    if club:  # inside is continuous
        #  Club with the outer match
        val += 2

    # now, it may happen that sub-str
    # has longer match than continuos
    without = max(l_p_string(arr[1:]), l_p_string(arr[:-1]))
    if without[0] > val:
        return without

    return (val, club)


print(l_p_string.__name__)
print("abab", l_p_string("abab"))
print("babad", l_p_string("babad"))
print("abbccbba", l_p_string("abbccbba"))
print("abbccbballabbccbbal", l_p_string("abbccbballabbccbbal"))
print("abbccbballxabbccbbal", l_p_string("abbccbballxabbccbbal"))
print("rrar", l_p_string("rrar"))
print("--------------------")


def longest_paren(arr):
    """parenthesis match longest"""
    # not working
    if not arr:
        return 0

    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return 2 if arr[0] == '(' and arr[1] == ')' else 0

    if arr[0] == '(' and arr[1] == ')':
        return 2 + longest_paren(arr[1:-1])
    elif arr[0] != '(':
        return longest_paren(arr[1:])
    elif arr[-1] != ')':
        return longest_paren(arr[:-1])


print(longest_paren.__name__)
print(longest_paren("()("))
print(longest_paren("("))
print(longest_paren(")()())"))
print(longest_paren(")())())"))


def count_sub_palindromes(s):
    if not s: return 0
    if len(s) == 1: return 1

    matrix = []
    for i in range(len(s)):
        matrix.append([])
        for j in range(len(s)):
            matrix[i].append(-1)

    def is_palin(s, i, j):
        if j <= i: return True
        if matrix[i][j] == -1:
            matrix[i][j] = s[i] == s[j] and is_palin(s, i+1, j-1)
        return matrix[i][j]

    result = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palin(s, i, j):
                result += 1

    return result


print(count_sub_palindromes.__name__)
print(count_sub_palindromes("abc"))
print(count_sub_palindromes("aaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(count_sub_palindromes("thishannahsir"))
