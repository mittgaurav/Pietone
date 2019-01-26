# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 03:17:54 2018

Selection without sorting

'''find_kth_smallest_elem''':
    Max heap of k size. Add elems
and if len goes above k, pop max.
This is optimal for small k as it
allocates k-length array. To find
median or quarter median, this is
bad as too large space is needed.
    We can modify this to get kth
maximum elem as well.

'''find_median''':
    Use partition of 2 way quick
sort algorithm repeatedly to get
to median location.
    We can modify this to get qt
or 3/4 qt median and such.

@author: gaurav
"""
import random
from priority_queue import MaxHeap

A = [i for i in range(100)]
random.shuffle(A)


def find_k_smallest_elems(arr, k):
    """given a large array, find k
    smallest elems, where k << len"""
    heap = MaxHeap()

    # N log k
    for i in arr:
        heap.add(i)
        if len(heap) > k:
            heap.pop()
    heap.vals.sort()
    return heap.vals


print(find_k_smallest_elems(A, 1))
print(find_k_smallest_elems(A, 10))
print(find_k_smallest_elems(A, 100))


def find_kth_smallest_elem(arr, k):
    """given a large array, find kth
    smallest elem, where k << len"""
    vals = find_k_smallest_elems(arr, k)
    return vals[-1]


print(find_kth_smallest_elem(A, 1))
print(find_kth_smallest_elem(A, 10))
print(find_kth_smallest_elem(A, 100))
print("===========================")
# ==================================
# ==================================


def partition(arr, start, end):
    """partition arr into two parts
    with all elements less and more
    than pivot on respective ends"""
    if start >= end:
        return start

    pivot = arr[start]
    H = end
    i = start + 1
    while i <= H:
        if arr[i] <= pivot:
            i += 1
        else:
            temp = arr[i]
            arr[i] = arr[H]
            arr[H] = temp
            H -= 1
    arr[start] = arr[H]
    arr[H] = pivot
    return H


def find_vals_between_locations(arr, i, j):
    """values between locs i, j ~ len"""
    assert i <= j

    def keep_partitioning(arr, start, loc, end):
        """keep partitioning as long
        as partition is not at loc"""
        p = -1
        while p != loc:
            p = partition(arr, start, end)
            if p > loc:
                end = p - 1
            elif p < loc:
                start = p + 1

    # lower partition is from 0 to len
    keep_partitioning(arr, 0, i, len(arr) - 1)

    if i == j:
        return arr[i:i+1]

    # higher partition is from lower to len
    keep_partitioning(arr, i + 1, j, len(arr) - 1)

    return arr[i:j+1]


print(find_vals_between_locations(list(A), 14, 18))
print(find_vals_between_locations(list(A), 10, 18))
print(find_vals_between_locations(list(A), 23, 23))


def find_median(arr):
    """median of large array
    without extra space"""
    if not arr:
        return None
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return (arr[0] + arr[1]) / 2

    # expected location of medians
    m_low = int((len(arr) - 1) / 2)
    m_hig = int(len(arr) / 2)

    return sum(find_vals_between_locations(arr, m_low, m_hig)) / 2


print(find_median(list(A)))  # duplicate list A
print("===========================")
# ==================================
# ==================================
