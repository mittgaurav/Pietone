# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 00:04:30 2019

@author: gaurav
"""


def overlapping_area_of_rects(rect1, rect2):
    """given left bottom and right top of
    two points, find overlapping area"""
    l1x, l1y = rect1[0]
    l2x, l2y = rect2[0]
    r1x, r1y = rect1[1]
    r2x, r2y = rect2[1]

    # calculate left bottom and right
    # top of the overlapping rectangle
    lx, ly, rx, ry = 0, 0, 0, 0

    if l1x <= l2x <= r1x:
        lx = l2x
    elif l2x <= l1x <= r2x:
        lx = l1x
    else:
        return 0

    if l1y <= l2y <= r1y:
        ly = l2y
    elif l2y <= l1y <= r2y:
        ly = l1y
    else:
        return 0

    if r1x >= r2x >= l1x:
        rx = r2x
    elif r2x >= r1x >= l2x:
        rx = r1x
    else:
        return 0

    if r1y >= r2y >= l1y:
        ry = r2y
    elif r2y >= r1y >= l2y:
        ry = r1y
    else:
        return 0

    return (rx - lx) * (ry - ly)


print("==", overlapping_area_of_rects.__name__, "==")
print(overlapping_area_of_rects(((2, 1), (5, 5)), ((3, 2), (5, 7))))
print(overlapping_area_of_rects(((2, 1), (6, 8)), ((3, 2), (5, 5))))
print(overlapping_area_of_rects(((2, 1), (4, 8)), ((3, 2), (5, 6))))


def duplicate_ints(arr):
    """does array contain
    duplicate nums"""
    seen = {}
    for v in arr:
        if v in seen:
            return True
        seen[v] = None
    return False


print("====duplicate_ints====")
print(duplicate_ints([1, 2, 3, 4, 5, 6]))
print(duplicate_ints([1, 2, 3, 4, 5, 6, 1]))


def find_int_with_sum(arr, v):
    """find two ints with sum v"""
    seen = {}
    for a in arr:
        if v - a in seen:
            return True

        seen[a] = None

    return False


print("====find_int_with_sum====")
print(find_int_with_sum([1, 2, 3, 4, 5, 6, 1, 4, 6, 9], 12))
print(find_int_with_sum([1, 2, 3, 4, 5, 6, 1, 4, 6, 9], 1))
print(find_int_with_sum([1, 2, 3, 4, 5, 6, 1, 4, 6, 9], 2))


def print_sorted_in_range(arr, a, b):
    """get sorted elements
    between a and b"""
    if a > b:  # make sure a <= b
        a, b = b, a

    # quick sort 3 way
    i = 0
    L = 0
    H = len(arr) - 1
    while i <= H:
        if arr[i] < a:  # first bucket
            # we copy the first element in
            # second bucket to ith and ith
            # to Lth as L'll be increased
            arr[i], arr[L] = arr[L], arr[i]
            i += 1  # next element
            L += 1  # first bucket increased
        elif arr[i] > b:  # third bucket
            arr[i], arr[H] = arr[H], arr[i]
            H -= 1  # third bucket increased
        else:  # second bucket
            i += 1

    new = arr[L:H+1]
    new.sort()  # sort only limited size
    return new


print("====print_sorted_in_range====")
print(print_sorted_in_range([1, 2, 4, 5, 3, 6, 1, 4, 6, 9], 3, 5))


def longest_increasing_subarray(arr):
    """longest_increasing subarray"""
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

    return max(max_ret, ret)


print("====longest_increasing_subarray====")
print(longest_increasing_subarray([1, 2, 3, 4, 5, 6, 1, 4, 6, 9]))
print(longest_increasing_subarray([1, 2, 3, 4, 5]))


def meandering_array(arr):
    """return meandering sort
    rearrange an array in minimum-maximum form.

    Prints max at first position, min at second position
    second max at third position, second min at fourth...
    """
    ret = []

    arr.sort()

    # Indices of smallest and largest elements from
    # remaining array. Small goes up, large comes down
    small, large = 0, len(arr) - 1

    # To indicate whether we need to copy remaining
    # largest or remaining smallest at next position
    flag = True

    for _ in range(len(arr)):
        if flag:
            ret.append(arr[large])
            large -= 1
        else:
            ret.append(arr[small])
            small += 1

        flag = not flag

    return ret


print("==", meandering_array.__name__, "==")
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(A, meandering_array(A))


def nth_compartment_rev(size, N):
    """reverse every nth
    compartment in train"""
    if size < N:  # wrap-around
        N %= size

    if N == 1:  # elems stay in place
        return list(range(1, size + 1))
    if size == N:  # reverse every elem
        return list(range(size, 0, -1))

    ret = list(range(1, size+1))
    i = 0
    while i < size - N + 1:
        ii = i
        j = i + N - 1
        while i < j:
            ret[i], ret[j] = ret[j], ret[i]
            i += 1
            j -= 1
        i = ii + N  # move i to next batch

    return ret


print("===", nth_compartment_rev.__name__, "===")
print(nth_compartment_rev(9, 3))
print(nth_compartment_rev(9, 8))
print(nth_compartment_rev(9, 10))
print(nth_compartment_rev(9, 1))
print(nth_compartment_rev(9, 5))
