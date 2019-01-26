# -*- coding: utf-8 -*-
"""
quick sort:
    two way partition
"""


def two_partition(arr):
    """two partition"""
    i = 1
    H = len(arr) - 1

    pivot = arr[0]

    # traverse i fwd and H backward.
    # We find how many ith elements
    # are less than pivot. H is the
    # rightful place of pivot as we
    # traverse through the array.
    # if pivot is less than the ith
    # elem, we move that elem to H
    # and decrement H. When i is
    # more than or equal to H, we
    # replace Hth elem with pivot
    while i <= H:
        if arr[i] <= pivot:
            i += 1
        else:
            # replace i with Hth
            tempor = arr[i]
            arr[i] = arr[H]
            arr[H] = tempor
            H -= 1
    # put pivot in its place (H)
    arr[0] = arr[H]
    arr[H] = pivot
    return H


def quicksort(arr):
    """sort given array"""
    if len(arr) == 0 or len(arr) == 1:
        return arr

    p = two_partition(arr)
    return quicksort(arr[:p]) + [arr[p]] + quicksort(arr[p+1:])


print(quicksort([]))
print(quicksort([3, 2, 1, 4, 2, -6]))
print(quicksort([0, 10, 2, 23, 5, -8, 1, 12]))
print(quicksort([0]))
print(quicksort([0, 0, 0, 0]))
print(quicksort([-8, 0, 1, 2, 5, 10, 12, 23]))
print(quicksort([23, 12, 10, 5, 2, 1, 0, -8]))
