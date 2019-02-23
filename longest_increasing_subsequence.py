# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:22:40 2018

@author: gaurav
"""


def longest_incr_subseq(arr):
    """longest subsequence (can be
    non-consecutive) such that all
    elems are in increasing order"""
    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return 1

    val = 0
    for i in range(len(arr)):
        # for all values before
        # me, if i am more than
        # them, i can use their
        # longest_subseq plus 1
        for j in range(i):
            if arr[i] >= arr[j]:
                val = max(1+longest_incr_subseq(arr[:j+1]), val)

    return val


print(longest_incr_subseq([2, 3, 1, 6, 9, 5]))
print(longest_incr_subseq([2, 3, 1, 6]))
print(longest_incr_subseq([10, 22, 9, 33, 21, 50, 41, 60, 80]))


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
            begin.append(0 if i is 0 else begin[i-1])
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


print(longest_non_repeating_str("abcded"))
print(longest_non_repeating_str("abcdedefgnhxzabc"))
print(longest_non_repeating_str("abcdedefgnhabc"))
