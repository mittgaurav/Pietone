# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 23:29:19 2018

@author: gaurav
"""


def duplicate_ints(arr):
    """does array contain
    duplicate nums"""
    list = {}
    for v in arr:
        if v in list:
            return True
        list[v] = None
    return False


print("====duplicate_ints====")
print(duplicate_ints([1, 2, 3, 4, 5, 6]))
print(duplicate_ints([1, 2, 3, 4, 5, 6, 1]))


def find_int_with_sum(arr, v):
    list = {}
    for a in arr:
        if v - a in list:
            return True

        list[a] = None

    return False


print("====find_int_with_sum====")
print(find_int_with_sum([1, 2, 3, 4, 5, 6, 1, 4, 6, 9], 12))


def print_sorted_in_range(arr, a, b):
    if a > b:  # a <= b
        a = a + b
        b = a - b
        a = a - b

    i = 0
    L = 0
    H = len(arr) - 1
    while i <= H:
        if arr[i] < a:
            tempor = arr[i]
            arr[i] = arr[L]
            arr[L] = tempor
            i += 1
            L += 1
        elif arr[i] > b:
            tempor = arr[i]
            arr[i] = arr[H]
            arr[H] = tempor
            H -= 1
        else:
            i += 1

    new = arr[L:H+1]
    new.sort()
    return new


print("====print_sorted_in_range====")
print(print_sorted_in_range([1, 2, 3, 4, 5, 6, 1, 4, 6, 9], 3, 5))


def longest_increasing_subarray(arr):
    if len(arr) <= 1:
        return len(arr)

    last = arr[0]
    ret = 1
    max_ret = 1
    for i in arr[1:]:
        if i >= last:
            ret += 1
        else:
            max_ret = max(max_ret, ret)
            ret = 1
        last = i

    return max_ret


print("====longest_increasing_subarray====")
print(longest_increasing_subarray([1, 2, 3, 4, 5, 6, 1, 4, 6, 9]))
