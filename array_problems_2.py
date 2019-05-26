# -*- coding: utf-8 -*-
"""
Created on Sun May 26 21:13:01 2019

@author: gaurav
"""


def string_in_order(order, string):
    """given order, check if chars
    in string follow that order"""
    if not string:
        return True
    if not order:
        return True

    ordered_set = set(order)
    j = 0
    for char in string:
        if char in ordered_set:
            while j < len(order) and order[j] != char:
                j += 1

            if j == len(order):
                return False

    return True


print("====", string_in_order.__name__)
print(string_in_order('abc', 'aaa'))
print(string_in_order('abc', 'cabc'))
print(string_in_order('abc', 'xadb'))


def place_i_spaced_ints(arr, n):
    """place pair of n ints spaced
    at ith distance from each other"""
    if n == 0:
        return True

    for i in range(0, len(arr) - n - 1):
        if arr[i] == 0 and arr[i+n+1] == 0:
            arr[i], arr[i+n+1] = n, n
            if not place_i_spaced_ints(arr, n-1):
                # failure, backtrack
                arr[i], arr[i+n+1] = 0, 0

    # check that n exists
    # twice in the array
    count = len([x for x in arr if x == n])
    return count == 2


print("====", place_i_spaced_ints.__name__)
array = [0] * 2 * 3
print(place_i_spaced_ints(array, 3), array)
array = [0] * 2 * 4
print(place_i_spaced_ints(array, 4), array)
