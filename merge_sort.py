# -*- coding: utf-8 -*-
"""
merge sort
@author: gaurav
"""
from priority_queue import Heap


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

    # exhaust remaining
    # elements, if any
    while i < len(arr):
        ret.append(arr[i])
        i = i + 1
    while j < len(brr):
        ret.append(brr[j])
        j = j + 1

    return ret


def mergesort(arr):
    """merge sort"""
    if len(arr) == 0 or len(arr) == 1:
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


def kmergesort(arrays):
    """ Given k sorted arrays, merge
    them in a single sorted array"""

    class ThisHeap(Heap):
        """Array with minimum value at root"""
        @classmethod
        def order(cls, arr, parent, child):
            """parent <= child in min heap"""
            return arrays[arr[parent]][0] <= arrays[arr[child]][0]

    heap = ThisHeap()
    result = []

    # consider arrays that are not empty
    [heap.add(i) for i in range(len(arrays)) if arrays[i]]

    while heap.vals:
        val = heap.pop()

        result.append(arrays[val].pop(0))

        # add this guy back
        # at its new location
        if arrays[val]:
            heap.add(val)

    return result


print(kmergesort([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
