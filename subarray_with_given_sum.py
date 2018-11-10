# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 01:33:25 2018

@author: gaurav
"""


def subarray_with_given_sum(arr, gsum):
    """returns the subarray with
    sum equal to given sum."""
    i = 0
    h = len(arr) - 1

    # unsorted array of positive
    # numbers mean that once we
    # go over the gsum, we skip
    # 1st elem
    lsum = 0
    begin = 0
    while i < h:
        lsum += arr[i]
        while lsum > gsum:
            # might as well be
            # an if. It's just
            # an optimization.
            lsum -= arr[begin]
            begin += 1

        if lsum == gsum:
            endin = i
            return arr[begin:endin + 1]
        i += 1
    return []


print(subarray_with_given_sum([1, 2, 3, 4, 5, 6, 7, 8], 13))
print(subarray_with_given_sum([1, 2, 3, 4, 5, 6, 7, 8], 10))
print(subarray_with_given_sum([1, 2, 3, 4, 5, 6, 7, 8], 99))
