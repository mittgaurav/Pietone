# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:22:40 2018

@author: gaurav
"""
# NOT CORRECT


def longest_incr_subsequence(arr):
    """longest subsequence (can be
    non-consecutive) such that all
    elems are in increasing order"""

    # should not go sequentially
    # backward as we end up with
    # terms that larger than me.
    # Instead, jump back to vals
    # that are smaller than me.
    if len(arr) == 0:
        return 0

    for i in range(len(arr)):



# print(longest_increasing_subsequence([2, 3, 1], 1))
print(longest_incr_subsequence([2, 3, 1, 6, 9, 5]))
print(longest_incr_subsequence([2, 3, 1, 6]))
print(longest_incr_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]))
