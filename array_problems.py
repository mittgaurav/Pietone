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


def find_ints_with_sum(arr, v):
    """find two ints with sum v"""
    seen = {}
    for a in arr:
        if v - a in seen:
            return True

        seen[a] = None

    return False


print("====find_int_with_sum====")
print(find_ints_with_sum([1, 2, 3, 4, 5, 6, 1, 4, 6, 9], 12))
print(find_ints_with_sum([1, 2, 3, 4, 5, 6, 1, 4, 6, 9], 1))
print(find_ints_with_sum([1, 2, 3, 4, 5, 6, 1, 4, 6, 9], 2))


def two_sum(arr, k):
    """find two elements that
    are closest to a num k"""
    if not arr:
        return -1

    arr = sorted(arr)
    i = 0
    j = len(arr)-1

    curr_diff = 999999
    while i < j:
        my_sum = arr[i] + arr[j]
        if my_sum > k:
            j -= 1
        else:
            i += 1

        curr_diff = min(curr_diff, abs(my_sum - k))
    return curr_diff


print("====two_sum====")
print(two_sum([-1, 2, 1, -4], 4))


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


def duplicate_nums_n(arr):
    """in an unsorted array from
    1 to n-1, find duplicates"""
    res = set()

    # flip the sign to -ve for
    # value at ith index. Then
    # if we got negative value
    # then i is duplicated.
    for i in range(len(arr)):
        if arr[abs(arr[i])] < 0:
            res.add(i)
        else:
            arr[i] = -arr[i]

    return res


print(duplicate_nums_n.__name__, duplicate_nums_n([2, 3, 3, 1]))


def first_missing_num_n(arr, start, end):
    """Given sorted arr from 0 to n-1
    find the smallest element missing.
    One way, do binary search for the
    index i == val at index arr[i]"""
    if end == start:
        return start

    if end - start == 1:  # two elems: 0 or 1
        return start if arr[end] == end else end

    mid = (end - start) // 2
    if mid == arr[mid]:  # all fine upto mid
        return first_missing_num_n(arr, mid + 1, end)

    ret = first_missing_num_n(arr, start, mid - 1)

    # now, ret could be same as the value; in that
    # mid is the first location that things go bad
    return mid if ret == arr[ret] else ret


print("====", first_missing_num_n.__name__)
print(first_missing_num_n([0, 1, 3, 4, 5, 6, 8], 0, 6))
print(first_missing_num_n([0, 1, 3, 4, 5], 0, 4))


def get_products_of_all_except_index(int_list):
    """don't use divide"""
    product = [1] * len(int_list)

    product_so_far = 1
    for i in range(len(int_list)):
        product[i] = product_so_far
        product_so_far *= int_list[i]

    product_so_far = 1
    for i in range(len(int_list) - 1, -1, -1):
        product[i] *= product_so_far
        product_so_far *= int_list[i]

    return product


print("====", get_products_of_all_except_index.__name__)
print(get_products_of_all_except_index([8, 2, 4, 3, 1, 5]))
print(get_products_of_all_except_index([-7, -1, -4, -2]))


def pair_sum_equal_k(arr, k, i=0, j=9999):
    """in sorted list find whether
    any pair wise sum equal k"""
#    j = min(j, len(arr)-1)
#    if j <= i or i < 0:
#        return 'No'
#
#    if arr[i] + arr[j] == k:
#        return 'Yes'
#    if arr[i] + arr[j] > k:
#        return pair_sum_equal_k(arr, k, i, j-1)
#    if arr[i] + arr[j] < k:
#        return pair_sum_equal_k(arr, k, i+1, j)
#
#    if not arr:
#        return 'No'

    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == k:
            return 'Yes'
        if arr[i] + arr[j] > k:
            j -= 1
        if arr[i] + arr[j] < k:
            i += 1
    return 'No'


print(pair_sum_equal_k([1, 2, 3, 9], 8))
print(pair_sum_equal_k([1, 2, 3, 5], 8))
print(pair_sum_equal_k([1, 2, 3, 5, 9], 8))
print(pair_sum_equal_k([1, 2, 5, 9], 8))


def longest_non_repeating(s):
    """get longest non repeating string
    length.

    track the window of unique substring
    1) for each char, see when does its window starts.
        a) either it is existing window, or
        b) last time we saw this character.
        max of two
    """
    if not s:
        return 0

    window_start = 0
    max_len = 0

    # last location we saw this character
    arr = [-1] * 128
    for i in range(len(s)):
        # start of window including this character
        # it is either existing window
        # or if this char repeated, then it is from that location
        window_start = max(window_start, arr[ord(s[i])] + 1)
        max_len = max(max_len, i - window_start + 1)

        arr[ord(s[i])] = i

    return max_len


print("====", longest_non_repeating.__name__)
print(longest_non_repeating('abcabcbb'))
print(longest_non_repeating('pwwkew'))
print(longest_non_repeating('bbbbbb'))
print(longest_non_repeating('abcdefgbbag'))
print(longest_non_repeating(''))
print(longest_non_repeating('abcbcbb'))
