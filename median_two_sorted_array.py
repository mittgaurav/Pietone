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
    while True:
        if arr[i] <= brr[j]:
            val = arr[i]
            i += 1
        else:
            val = brr[j]
            j += 1

        if k == first:
            median += val / 2
        if k == second:
            median += val / 2
            break
        k += 1

    return median


print(median_two_sorted_array([1, 3, 5], [2, 4, 6]))
