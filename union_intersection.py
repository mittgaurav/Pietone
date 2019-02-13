# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:56:39 2019

@author: gaurav
"""
from quick_sort import quicksort


def intersection(arr, brr):
    """intersection"""
    arr = quicksort(arr)
    brr = quicksort(brr)

    out = []
    a = 0
    b = 0

    while a < len(arr) and b < len(brr):
        # if either is consumed
        # we don't care. Not at
        # all as those vals are
        # not intersection
        if arr[a] == brr[b]:
            out.append(arr[a])
            a += 1
            b += 1
        elif arr[a] < brr[b]:
            a += 1
        else:
            b += 1

    return out


print(intersection([1, 3, 1, 2, 4, 6, 3, 2, 4, 6, 7], [10, 1, 7]))


def union(arr, brr):
    """union"""
    arr = quicksort(arr)
    brr = quicksort(brr)

    out = []
    a = 0
    b = 0

    prev = None
    while a < len(arr) and b < len(brr):
        if arr[a] == brr[b]:
            if prev is not arr[a]:
                out.append(arr[a])
                prev = arr[a]
            a += 1
            b += 1
        elif arr[a] < brr[b]:
            if prev is not arr[a]:
                out.append(arr[a])
                prev = arr[a]
            a += 1
        else:
            if prev is not brr[b]:
                out.append(brr[b])
                prev = brr[b]
            b += 1

    # don't forget the
    # remaining ones.
    while a < len(arr):
        if prev is not arr[a]:
            out.append(arr[a])
            prev = arr[a]
        a += 1

    while b < len(brr):
        if prev is not brr[b]:
            out.append(brr[b])
            prev = brr[b]
        b += 1

    return out


print(union([1, 3, 1, 2, 4, 6, 3, 2, 4, 6, 7], [10, 11, 7]))
