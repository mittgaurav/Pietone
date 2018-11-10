# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:35:48 2018

@author: gaurav
"""


def binary_search_rotated_array(arr):
    """given ascending order arr,
    find the smallest element"""
    # we have to find the half in
    # which transition from large
    # series to smaller happens.
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return min(arr)

    mid = int((len(arr) - 1) / 2)

    if arr[mid] <= arr[0]:
        return binary_search_rotated_array(arr[:mid+1])
    else:
        return binary_search_rotated_array(arr[mid:])


print(binary_search_rotated_array([3, 4, 5, 6, 7, -9, 2]))
