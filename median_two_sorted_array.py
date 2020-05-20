# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:51:53 2018

@author: gaurav
"""


def median_two_sorted_array(arr, brr):
    total_len = len(arr) + len(brr)

    if total_len == 0:
        return 0

    half = total_len // 2
    if total_len % 2 == 0:
        first, second = half - 1, half
    else:
        first, second = half, half

    i = 0
    j = 0
    k = 0
    median = 0
    for k in range(0, second+1):
        # second is the larger of two
        # indices, so we go till that
        if j == len(brr) or arr[i] <= brr[j]:
            val = arr[i]
            i += 1
        elif i == len(arr) or arr[i] > brr[j]:
            val = brr[j]
            j += 1

        # we need this twice since first
        # can be equal to second - thus,
        # we have to capture both so we
        # don't miss having them twice.
        if k == first:
            median += val / 2
        if k == second:
            median += val / 2

    return median


print(median_two_sorted_array([1, 3, 5], [2, 4, 6]))
print(median_two_sorted_array([1, 1, 5], [2, 4, 6]))
print(median_two_sorted_array([1, 3, 5, 12, 33, 122, 56], [2, 4, 6]))
print(median_two_sorted_array([], []))
print(median_two_sorted_array([1], []))
