# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 20:17:09 2018

@author: gaurav

we got to find the first value that is
equal to or greater than given value.

we first do binary search for that val
and if the elem is same, we return it.
(though there can be duplicate elem on
left side, we assume unique hopefully)

Then, if the elem is small, search for
that in right and if larger, search in
left.

Keep looking right is just recursion.
left, that's interesting. It seems to
be recursion, but if we don't find a
val, we have to say that there is no
smaller larger value in left, so the
current elem is the first larger val
"""


def _bs(arr, num, begin, end):
    if end < begin:
        return -1
    if begin == end:  # one element, is it >=?
        return begin if arr[begin] >= num else -1

    mid = (begin + end) // 2  # integer div
    if arr[mid] < num:  # less num, go more
        return _bs(arr, num, mid + 1, end)

    # mid is equal or greater.
    # if we can't find lesser
    # larger, I'm the largest.
    loc = _bs(arr, num, begin, mid - 1)
    return mid if loc == -1 else loc


def binary_search_ge(arr, num):
    """find number equal to or
    least larger than given"""
    loc = _bs(arr, num, 0, len(arr) - 1)
    return loc, arr[loc] if loc >= 0 else None


if __name__ == "__main__":
    print("====", binary_search_ge.__name__)
    print(0, binary_search_ge([1, 2, 3, 4, 5, 7, 8], 0))
    print(10, binary_search_ge([1, 2, 3, 4, 5, 7, 8], 10))
    print(1, binary_search_ge([1, 1, 1, 1, 1, 2, 3, 4, 5, 7, 8], 1))
    print(8, binary_search_ge([1, 2, 3, 4, 5, 7, 8], 8))
    print(6, binary_search_ge([1, 2, 3, 4, 5, 7, 8], 6))
    print(-1, binary_search_ge([1, 2, 3, 4, 5, 7, 8], -1))


def _bss(arr, num, begin, end):
    """internal"""
    if begin > end:
        return -1
    if begin == end:
        return begin if arr[begin] > num else -1

    mid = (begin + end) // 2
    if arr[mid] <= num:
        return _bss(arr, num, mid + 1, end)

    # mid is larger. So are
    # there smaller larger?
    loc = _bss(arr, num, begin, mid - 1)
    return mid if loc == -1 else loc


def binary_search_greater(arr, num):
    """find num greater than given"""
    loc = _bss(arr, num, 0, len(arr) - 1)
    return loc, arr[loc] if loc >= 0 else None


if __name__ == "__main__":
    print("====", binary_search_greater.__name__)
    print(0, binary_search_greater([1, 2, 3, 4, 5, 7, 8], 0))
    print(10, binary_search_greater([1, 2, 3, 4, 5, 7, 8], 10))
    print(1, binary_search_greater([1, 2, 3, 4, 5, 7, 8], 1))
    print(8, binary_search_greater([1, 2, 3, 4, 5, 7, 8], 8))
    print(6, binary_search_greater([1, 2, 3, 4, 5, 7, 8], 6))
    print(-1, binary_search_greater([1, 2, 3, 4, 5, 7, 8], -1))


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

    return binary_search_rotated_array(arr, mid+1, len(arr))


if __name__ == "__main__":
    print("====", binary_search_rotated_array.__name__)
    A = [3, 4, 5, 6, 7, -9, 2]
    print(binary_search_rotated_array(A, 0, len(A)))
    A = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
    print(binary_search_rotated_array(A, 0, len(A)))
