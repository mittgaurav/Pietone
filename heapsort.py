# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:30:22 2018

@author: gaurav
"""


def swap(arr, i, j):
    """swap"""
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def swim_up(arr, i):
    """swim ith elem to
    its right place"""
    if i <= 0:
        return
    par = int((i - 1)/2)
    if arr[par] >= arr[i]:
        return
    swap(arr, i, par)
    swim_up(arr, par)


def heapify(arr, start, end):
    """heapify; i.e. put
    small elem at top to
    its right place"""
    if start > int(end/2):
        return

    L = (2 * start) + 1
    r = (2 * start) + 2

    largest = start
    if L <= end and arr[L] > arr[start]:
        largest = L
    if r <= end and arr[r] > arr[largest]:
        largest = r
    if start == largest:
        return
    swap(arr, largest, start)
    heapify(arr, largest, end)


def heapsort(arr):
    """first, construct max heap
    as we go from left to right.
    Then, take root element again
    and again and put it at end"""
    if len(arr) <= 1:
        return arr

    # heap (n * log n)
    for i in range(len(arr)):
        swim_up(arr, i)

    # heapify (n * log n)
    for i in range(len(arr) - 1, -1, -1):
        # put root to end
        swap(arr, i, 0)
        # heapify remaining
        heapify(arr, 0, i-1)

    return arr


print(heapsort([4, 11, 33, 3]))
print(heapsort([3, 2, 1, 4, 2, -6]))
print(heapsort([0, 10, 2, 23, 5, -8, 1, 12]))
print(heapsort([0]))
print(heapsort([0, 0, 0, 0]))
print(heapsort([-8, 0, 1, 2, 5, 10, 12, 23]))
print(heapsort([23, 12, 10, 5, 2, 1, 0, -8]))
