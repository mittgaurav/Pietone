# -*- coding: utf-8 -*-
"""
quick sort

@author: gaurav
"""


def partition(arr):
    """three way partition"""
    i = 1           # iterator
    L = 0           # second begins
    H = len(arr)-1  # second ends

    pivot = arr[0]

    # we start from first element.
    # Checking whether ith elem is
    # less than, equal to, or more
    # than pivot. Based on this we
    # bucketize i.
    #
    # L is the starting location of
    # equal elements and H+1 is the
    # starting location of greater
    # numbers. I is the iterator.
    # L must always have itself. At
    # the end, H must also do same.
    #
    # If i elem is lesser, it means
    # L should come fwd and i elem
    # be before L, i.e. swap L and
    # ith elems.
    # If ith elem is more, it means
    # H should come back and i elem
    # before H, i.e. swap H and ith
    # elem. We don't move i fwd as
    # we are not sure of new ith.
    # L always has pivot. When all
    # is done, L to H are pivots.
    while i <= H:
        if arr[i] < pivot:
            # swap L with i
            tempor = arr[i]
            arr[i] = arr[L]
            arr[L] = tempor
            i += 1
            L += 1
        elif arr[i] > pivot:
            # swap H with i
            tempor = arr[i]
            arr[i] = arr[H]
            arr[H] = tempor
            H -= 1
        else:  # arr[i] == pivot:
            i += 1

    return L, H+1


def quicksort(arr):
    """sort given array"""
    if len(arr) == 0 or len(arr) == 1:
        return arr

    l, h = partition(arr)

    return quicksort(arr[:l]) + arr[l:h] + quicksort(arr[h:])


print(quicksort([]))
print(quicksort([3, 2, 1, 4, 2, -6]))
print(quicksort([0, 10, 2, 23, 5, -8, 1, 12]))
print(quicksort([0]))
print(quicksort([0, 0, 0, 0]))
print(quicksort([-8, 0, 1, 2, 5, 10, 12, 23]))
print(quicksort([23, 12, 10, 5, 2, 1, 0, -8]))
