# -*- coding: utf-8 -*-
"""
merge sort
@author: gaurav
"""
from priority_queue import Heap


def merge(arr, brr):
    """merge two sorted arrays"""
    ret = []  # extra memory
    i = 0
    j = 0
    while i < len(arr) and j < len(brr):
        if arr[i] <= brr[j]:
            ret.append(arr[i])
            i += 1
        else:
            ret.append(brr[j])
            j += 1

    # exhaust any remaining elements
    if i < len(arr): ret.extend(arr[i:])
    if j < len(brr): ret.extend(brr[j:])

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


print(kmergesort([[1, 4, 7], [2, 5, 8, 10, 10], [3, 6, 9], [], [1, 5, 67]]))


def kmergesort2(arrays):
    class ThisHeap(Heap):
        """Index of array with minimum value at root"""
        @classmethod
        def order(cls, arr, parent, child):
            """parent <= child in min heap"""
            return arr[parent][0] <= arr[child][0]

    heap = ThisHeap()
    result = []

    current_index = [0] * len(arrays)

    # push first element from
    # every array on the heap
    for i in range(len(arrays)):
        if arrays[i]:
            heap.add((arrays[i][0], i))

    while heap.vals:
        val, i = heap.pop()
        result.append(val)

        # check if the array
        # has more elements.
        current_index[i] += 1
        if current_index[i] < len(arrays[i]):
            heap.add((arrays[i][current_index[i]], i))

    return result


print(kmergesort2([[1, 4, 7], [2, 5, 8, 10, 10], [3, 6, 9], [], [1, 5, 67]]))
