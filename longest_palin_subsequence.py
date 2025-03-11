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
    # Push index of ( on stack and
    # as and when we pop it, update
    # the maximum valid length.
    stack = []
    maxl = 0

    # sometimes there may be a continuation
    # of a valid parenthesis e.g. (()) ()
    # pehle 4 is valid. then next two mein
    # add the previous 4 ka starting point
    prev = -1

    for i, c in enumerate(arr):
        if c == '(':
            if not stack and prev >= 0:
                stack.append(prev)
            else:
                stack.append(i)
        else:
            if stack:
                prev = stack.pop()
                maxl = max(maxl, i - prev + 1)
            else:
                # pichla invalid hai. so don't
                # consider for the next valid
                prev = -1

    return maxl


print("====", longest_paren.__name__)
print("()(", longest_paren("()("))
print("((()())", longest_paren("((()())"))
print(")()())", longest_paren(")()())"))
print(")())())", longest_paren(")())())"))
print(")((())))())", longest_paren(")((())))())"))


def remove_one_get_palin(s):
    """Does the string become a valid palindrome
    by removing one and only one character?"""
    l, r = 0, len(s) - 1
    removed = 0

    while l < r and s[l] == s[r]:
        l += 1
        r -= 1

    if l >= r:
        return "already palindrome"

    def is_palin(L, R):
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True

    return is_palin(l+1, r) or is_palin(l, r-1)


print("====", remove_one_get_palin.__name__)
print("racecar", remove_one_get_palin("racecar"))
print("raecar", remove_one_get_palin("raecar"))
print("racecxyar", remove_one_get_palin("racecxyar"))
print("raceca", remove_one_get_palin("raceca"))
print("raccar", remove_one_get_palin("raccar"))
print("racearr", remove_one_get_palin("racearr"))


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


print("====", count_sub_palindromes.__name__)
print(count_sub_palindromes("abc"))
print(count_sub_palindromes("aaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(count_sub_palindromes("thishannahsir"))


def max_valid_parenthesis(string):
    """remove minimum number to get a valid parenthesis"""
    opens = 0
    to_remove = set()

    # do two passes
    # forward pass - remove the extra closing brackets
    for i, c in enumerate(string):
        if c == '(':
            opens += 1
        elif c == ')':
            if opens > 0:
                opens -= 1
            else:
                to_remove.add(i)

    closes = 0
    for i, c in enumerate(reversed(string)):
        if c == ')':
            closes += 1
        elif c == '(':
            if closes > 0:
                closes -= 1
            else:
                to_remove.add(len(string) - i - 1)

    result = ""
    for i, c in enumerate(string):
        if i not in to_remove:
            result += c

    return result


print(max_valid_parenthesis("(()(())(("))
print(max_valid_parenthesis("(()(a()b)(c("))
