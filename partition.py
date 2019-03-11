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


print("====", partition.__name__, "====")
arr = [3, 4, 6, 1, 7, 8, -1, 43, 9, 2, 4, 4, 5, 2, 7, 0]
print(partition(arr, 4, 6))
arr = [3, 4, 6, 1, 7, 8, -1, 43, 9, 2, 4, 4, 5, 2, 7, 0]
print(partition(arr, -10, -3))
arr = [3, 4, 6, 1, 7, 8, -1, 43, 9, 2, 4, 4, 5, 2, 7, 0]
print(partition(arr, 0, 0))
arr = [3, 4, 6, 1, 7, 8, -1, 43, 9, 2, 4, 4, 5, 2, 7, 0]
print(partition(arr, 100, 100))


def partition_labels(arr):
    """partition string into as many parts
    so that each letter appears in at most
    one part, and return a list of integers
    representing the size of these parts.

    For example:
    Input: S = "ababfeefhijkh"
    Output: [4,4,5]

    Explanation:
    The partition is "abab", "feef", "hijkh"
    Each letter appears in most one part."""
    if not arr:
        return []

    if len(arr) == 1:
        return [arr]

    # find first and last
    # occurence of each char
    first = {}
    last = {}
    for i in range(len(arr)):
        if arr[i] not in first:
            first[arr[i]] = i

    for i in range(len(arr)-1, -1, -1):
        if arr[i] not in last:
            last[arr[i]] = i

    res = []
    start = 0
    end = 0
    for i in range(len(arr)):
        if i > end:  # begin a new group
            if end:
                res.append(arr[start:end+1])
            start = i
            end = last[arr[i]]
        else:  # i is engulfed check end
            end = max(end, last[arr[i]])

    if end:  # add the last one
        res.append(arr[start:end+1])
    return res


print("====", partition_labels.__name__, "====")
print(partition_labels("ababfeefhijkh"))
print(partition_labels("ababfeefhijkha"))
print(partition_labels("ababfeefahijkh"))
print(partition_labels("ababfeefhijkah"))
