# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:35:48 2018

@author: gaurav
"""


def binary_search_rotated_array(arr, i, j):
    """given ascending order arr,
    find the smallest element"""
    # we have to find the half in
    # which transition from large
    # series to smaller happens.
    if i > j:
        return -1
    if i == j:
        return arr[i]

    mid = i + (j - i - 1) // 2

    if arr[mid] < arr[0]:
        return binary_search_rotated_array(arr, i, mid)
    else:
        return binary_search_rotated_array(arr, mid+1, len(arr))


A = [3, 4, 5, 6, 7, -9, 2]
print(binary_search_rotated_array(A, 0, len(A)))
A = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
print(binary_search_rotated_array(A, 0, len(A)))
