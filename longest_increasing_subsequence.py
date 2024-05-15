# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:22:40 2018

@author: gaurav
"""


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


print("===", longest_increasing_subarray.__name__, "===")
print(longest_increasing_subarray([1, 2, 3, 4, 5, 6, 1, 4, 6, 9]))
print(longest_increasing_subarray([1, 2, 3, 4, 5]))


def longest_incr_subseq(arr):
    """longest subsequence (can be
    non-consecutive) such that all
    elems are in increasing order"""
    # For seq ending at loc i
    max_till = [1 for _ in arr]

    for i in range(len(arr)):
        # for all values before
        # me, if i am more than
        # them, i can use their
        # longest_subseq plus 1
        for j in range(i):
            if arr[i] >= arr[j]:
                max_till[i] = max(1 + max_till[j], max_till[i])

    # we have so far gotten the
    # longest subseq ending at
    # given i. Now, get maxim
    # which may end anywhere
    return max(max_till)


print("===", longest_incr_subseq.__name__, "===")
print(longest_incr_subseq([1, 2, 4, 1, 3]))
print(longest_incr_subseq([1, 2, 4, 1, 2, 3, 4, 5, 6, 1, 2, 4]))
print(longest_incr_subseq([2, 3, 1, 6, 9, 5]))
print(longest_incr_subseq([2, 3, 1, 6]))
print(longest_incr_subseq([10, 22, 9, 33, 21, 50, 41, 60, 80]))


def max_profit(prices):
    """buy and sell atmost twice.
    we are going to find the best
    possible place to break array
    such that buying and selling
    before and after it gives us
    the most total profit."""
    if not prices:
        return 0

    # first traverse the left to right
    # and get the best in first array
    best_first = []
    min_till_now = 9999999999
    for i in range(len(prices)):
        min_till_now = min(prices[i], min_till_now)
        best_first.append(max(prices[i] - min_till_now,
                              best_first[i-1] if i else -999999999))

    # traverse from behind and get
    # maximum in the second array
    best_last = []
    max_till_now = -999999999
    for j in range(len(prices)-1, -1, -1):
        max_till_now = max(prices[j], max_till_now)
        best_last.insert(0, max(max_till_now - prices[j],
                                best_last[0] if j < len(prices)-1
                                else -9999999999))

    return max([_1 + _2 for _1, _2 in zip(best_first, best_last)])


print("===", max_profit.__name__, "===")
print(max_profit([3, 3, 5, 0, 0, 3, 1, 4]))


def longest_non_repeating_str(string):
    """find the longest non-repeating substring"""
    if not string:
        return ""
    if len(string) == 1:
        return string

    last_loc = {}  # track last location of char
    begin = []  # beginning of non-repeating str

    for i in range(len(string)):
        if string[i] not in last_loc:
            # not seen this char so update last
            # loc and take begin from previous
            begin.append(0 if i == 0 else begin[i-1])
        else:
            # update last_loc. begin is
            # max of next from last_loc
            # or begin for previous one
            last = last_loc[string[i]]
            begin.append(max(last + 1, begin[i-1]))
        last_loc[string[i]] = i

    maxlen = 0
    endloc = 0
    for i in range(len(begin)):
        if (i - begin[i] + 1) > maxlen:
            maxlen = i - begin[i] + 1
            endloc = i

    # now pick maxlen behind start len
    return string[endloc - maxlen + 1:endloc + 1]


print("===", longest_non_repeating_str.__name__, "===")
print(longest_non_repeating_str("abcded"))
print(longest_non_repeating_str("abcdedefgnhxzabc"))
print(longest_non_repeating_str("abcdedefgnhabc"))


def remove_negative_values(array):
    """remove the min negative values such
    that running sum is never negative."""
    if not array: return 0

    def fn(agg, i):
        if i == len(array): return 0
        if agg + array[i] < 0:
            # the value makes the sum negative
            # so must remove it no matter what
            return 1 + fn(agg, i+1)
        elif array[i] < 0:
            # the value is negative but doesn't
            # make sum negative. So check if we
            # reduce removals by either keeping
            # or removing it.
            return min(1 + fn(agg, i+1), fn(agg + array[i], i+1))
        else: return fn(agg + array[i], i+1)

    return fn(0, 0)


print('====', remove_negative_values.__name__)
print(remove_negative_values([10, -10, -1, -1, -1, 10]))
print(remove_negative_values([10, -1, -1, -1, 10]))
print(remove_negative_values([10, -5, -5, -5, 20]))
print(remove_negative_values([10, -11, 10]))
print(remove_negative_values([10, -10, -10, -10, 100]))
print(remove_negative_values([10, -5, -5, 20]))
