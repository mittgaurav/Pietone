# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 04:59:29 2018

@author: gaurav
"""


def max_subarray_sum(arr):
    """largest possible
    sum of subarray."""
    max_sum = 0
    loc_sum = 0
    for i in arr:
        loc_sum += i

        # we can always
        # beat negative
        loc_sum = max(loc_sum, 0)

        # one line to do that
        # and fix for all -ve
        # to have length >= 1
        # loc_sum = max(i, loc_sum + i)

        max_sum = max(max_sum, loc_sum)

    print(max_sum)


def max_subarray_avg(arr):
    """largest possible
    avg in subarray. ie
    see incrementing"""
    max_sum = 0
    max_len = 0
    loc_sum = 0
    loc_len = 0
    for i in arr:
        loc_sum += i
        loc_len += 1

        # we can always
        # beat negative
        if i < 0:
            loc_sum = 0
            loc_len = 0

        max_avg = -1 if max_len == 0 else max_sum / max_len
        loc_avg = -1 if loc_len == 0 else loc_sum / loc_len
        if max_avg <= loc_avg:
            max_sum = loc_sum
        if loc_sum == max_sum:
            max_len = loc_len

    print(max_sum, max_len)


max_subarray_sum([-1, 2, 4, -3, 5, 2, -5, 2])
max_subarray_sum([-1, 2, 4, -13, 5, 2, -5, 2])
max_subarray_sum([-1, 2, 4, -3, 1, 5, 7, 2, -5, 2])
max_subarray_sum([-1, 2, 4, -13, 1, 5, 7, 2, -5, 2])
max_subarray_avg([-1, 2, 4, -3, 1, 5, 7, 2, -5, 2])
max_subarray_avg([-1, 2, 4, -13, 1, 15, 7, 2, -5, 2])
max_subarray_avg([-1, 2, 4, -13, 1, 15, 9, 2, -5, 2])
