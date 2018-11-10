# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:30:22 2018

@author: gaurav
"""
# NOT CORRECT
# NOT CORRECT
# NOT CORRECT
# NOT CORRECT


def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t


def heapsort(arr):
    """we maintain a max heap.
    Then send the maximum elem
    to the end, and repeat"""
    # start from first element
    # and see if it's in right
    # place. Then, second elem
    # and sift down.
    for i in range(len(arr) - 1, -1, -1):
        j = i
        while j < len(arr):
            x = int((2 * i) + 1)
            y = int((2 * i) + 2)
            if x > len(arr):
                j += 1
                continue
            if y < len(arr) and arr[y] > arr[x]:
                temp = y
                y = temp
                x = y
            if arr[x] > arr[j]:
                swap(arr, x, j)
                j = x + i
            else:
                j += 1

    return(arr)


print(heapsort([4, 11, 33, 3]))
