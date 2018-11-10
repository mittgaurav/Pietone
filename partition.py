# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:29:45 2018

@author: gaurav
"""


def partition(arr, low, high):
    """ partitions array into three
    sections: numbers less than low,
    from low to high, and remaining
    numbers above high."""
    i = 0
    L = 0
    H = len(arr) - 1

    while i <= H:
        if arr[i] < low:
            tempor = arr[i]
            arr[i] = arr[L]
            arr[L] = tempor
            i += 1
            L += 1
        elif arr[i] >= low and arr[i] <= high:
            i += 1
        else:   # arr[i] > high
            tempor = arr[i]
            arr[i] = arr[H]
            arr[H] = tempor
            H -= 1

    # L-1 is problematic if L
    # equals 0. None is <low
    return arr[: max(0, L-1)], arr[L:H+1], arr[H+1:]


arr = [3, 4, 6, 1, 7, 8, -1, 43, 9, 2, 4, 4, 5, 2, 7, 0]
print(partition(arr, 4, 6))
arr = [3, 4, 6, 1, 7, 8, -1, 43, 9, 2, 4, 4, 5, 2, 7, 0]
print(partition(arr, -10, -3))
arr = [3, 4, 6, 1, 7, 8, -1, 43, 9, 2, 4, 4, 5, 2, 7, 0]
print(partition(arr, 0, 0))
arr = [3, 4, 6, 1, 7, 8, -1, 43, 9, 2, 4, 4, 5, 2, 7, 0]
print(partition(arr, 100, 100))
