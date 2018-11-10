# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 01:43:24 2018

@author: gaurav
"""


def max_index_diff(arr):
    """return maximum diff
    between i & j, so that
    arr[i] <= arr[j]."""
    i = 0
    j = len(arr) - 1

    lows = []
    hihs = []
    least = 100000
    maxim = -least
    while i <= j:
        if arr[i] < least:
            least = arr[i]
        lows.append(least)
        i += 1
    while j >= 0:
        if arr[j] > maxim:
            maxim = arr[j]
        hihs.append(maxim)
        j -= 1
    hihs.reverse()  # why?

    # so we got two arrays
    # with one having nums
    # in increasing and in
    # decreasing order. We
    # work simultaneously.
    i = 0
    j = 0
    d = -1
    print(lows, hihs)
    while i < len(arr) and j < len(arr):
        if lows[i] < hihs[j]:
            d = max(d, j - i)
            j += 1
        else:
            i += 1
    return d


print(max_index_diff([14, 52, 23, 100, 5, 6, 7, 8]))
print(max_index_diff([9, 2, 3, 4, 5, 6, 7, 8, 18, 0]))
