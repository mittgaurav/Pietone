# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 04:59:29 2018

@author: gaurav
"""


def max_subarray_sum(arr):
    """largest possible
    sum of subarray."""

    i = 0
    max_sum = 0
    loc_sum = 0
    while i < len(arr):
        loc_sum += arr[i]

        # we can always
        # beat negative
        loc_sum = max(loc_sum, 0)

        # one line to do this
        # and fix for all -ve
        # loc_sum = max(arr[i], loc_sum + arr[i])

        max_sum = max(max_sum, loc_sum)
        i += 1

    print(max_sum)


def max_subarray_avg(arr):
    """largest possible
    avg in subarray."""

    i = 0
    max_sum = 0
    max_len = 0
    loc_sum = 0
    loc_len = 0
    while i < len(arr):
        loc_sum += arr[i]
        loc_len += 1

        # we can always
        # beat negative
        if arr[i] < 0:
            loc_sum = 0
            loc_len = 0
        max_avg = -1 if 0 == max_len else max_sum / max_len
        loc_avg = -1 if 0 == loc_len else loc_sum / loc_len
        if max_avg <= loc_avg:
            max_sum = loc_sum
        if loc_sum == max_sum:
            max_len = loc_len

        i += 1

    print(max_sum, max_len)


max_subarray_sum([-1, 2, 4, -3, 5, 2, -5, 2])
max_subarray_avg([-1, 2, 4, -3, 1, 5, 7, 2, -5, 2])
