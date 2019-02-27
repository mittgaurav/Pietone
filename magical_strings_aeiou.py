# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 21:33:28 2019

@author: gaurav
"""


def next_chars(char):
    """possible next chars for this char"""
    ret = []
    if char == 'a':
        ret = ['e']
    if char == 'e':
        ret = ['a', 'i']
    if char == 'i':
        ret = ['a', 'u', 'o', 'e']
    if char == 'o':
        ret = ['u', 'i']
    if char == 'u':
        ret = ['a']
    if char == '':
        ret = ['a', 'u', 'o', 'e', 'i']

    return ret


CACHE = {}  # memoization


def remaining_strings(char, n):
    """how many are possible"""
    if (char, n) not in CACHE:
        if n == 1:
            CACHE[(char, n)] = len(next_chars(char))
        else:
            CACHE[(char, n)] = sum([remaining_strings(c, n-1)
                                    for c in next_chars(char)])

    return CACHE[(char, n)]


def magical_strings(n):
    """get number of magical
    strings are possible"""

    # build memoization (dp) table
    for i in range(1, n+1):
        remaining_strings('', i)
    return CACHE[('', n)]


if __name__ == '__main__':
    print(magical_strings(3))
    print(magical_strings(30))
