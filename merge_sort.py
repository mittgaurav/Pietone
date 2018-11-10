# -*- coding: utf-8 -*-
"""
merge sort
@author: gaurav
"""


def merge(arr, brr):
    """merge two sorted arrays"""
    ret = []
    i = 0
    j = 0
    while i < len(arr) and j < len(brr):
        if arr[i] <= brr[j]:
            ret.append(arr[i])
            i = i + 1
        else:
            ret.append(brr[j])
            j = j + 1

    while i < len(arr):
        ret.append(arr[i])
        i = i + 1
    while j < len(brr):
        ret.append(brr[j])
        j = j + 1

    return ret


def mergesort(arr):
    """merge sort"""
    if 0 == len(arr) or 1 == len(arr):
        return arr

    # divide array in two and recursively sort
    # them both. Then, merge the sorted arrays.
    return merge(mergesort(arr[:int(len(arr)/2)]),
                 mergesort(arr[int(len(arr)/2):]))

print(mergesort([]))
print(mergesort([0, 10, 2, 23, 5, -8, 1, 12]))
print(mergesort([0]))
print(mergesort([0, 0, 0, 0, 0]))
print(mergesort([-8, 0, 1, 2, 5, 10, 12, 23]))
