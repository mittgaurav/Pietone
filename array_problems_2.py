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


def put_string_in_order(order, string):
    """given order, reaarange
    string in the order. Can
    assume that each char in
    string exists in order"""
    if not string:
        return string
    if not order:
        return string

    # assert no duplicates
    assert len(set(order)) == len(order)

    # map location in order
    order_map = {}
    for i in range(len(order)):
        order_map[order[i]] = i

    # sort string by location in order
    return "".join(sorted(string, key=lambda x: order_map[x]))


print("====", put_string_in_order.__name__)
print(put_string_in_order('abc', 'aaa'))
print(put_string_in_order('abc', 'cabc'))
print(put_string_in_order("bxyzca", "abcabcabc"))


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
for N in range(10):
    array = [0] * 2 * N
    print(N, place_i_spaced_ints(array, N), array)


def add_one(arr, j):
    """add one to an int
    represented by arr"""
    if j < 0:
        arr.insert(0, 1)
        return

    if arr[j] == 9:
        arr[j] = 0
        add_one(arr, j-1)
    else:
        arr[j] += 1


print('====', add_one.__name__)
arrays = [
        [2, 3, 4, 1],
        [9, 9, 9, 9],
        [0]
        ]

for array in arrays:
    print(array, end='->')
    add_one(array, len(array) - 1)
    print(array)


def i_j_maximum_index(arr):
    """Given an array A[] of N positive
    integers. Find max of j-i such that
    A[i] <= A[j]."""
    mines = []
    minim = 9999
    for i in arr:
        minim = min(minim, i)
        mines.append(minim)

    maxes = []
    maxim = -9999
    arr.reverse()
    for i in arr:
        maxim = max(maxim, i)
        maxes.insert(0, maxim)

    print(mines)
    print(maxes)
    i = j = 0
    val = -1
    while i < len(arr) and j < len(arr):
        if mines[i] > maxes[j]:
            i += 1
        else:
            val = max(val, j - i)
            j += 1

    return val


arrays = [
        [9, 2, 3, 4, 5, 6, 7, 8, 18, 0],
        [7, 3, 2, 1, 8, 0, 5, 1, 12, 5],
        [7, 3, 2, 1, 8, 0, 5, 1, 2, 5],
        ]

print('====', i_j_maximum_index.__name__)
for array in arrays:
    print(array)
    print(i_j_maximum_index(array))
