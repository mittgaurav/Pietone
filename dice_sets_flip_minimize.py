# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:44:59 2020

leetcode.com/discuss/interview-question/877070

@author: gaurav
"""
import math


def solution(A, B):
    """given two sets of dice results,
    minimize results to be changed to
    match sum of both sets"""
    # if sum match - success
    # if not, let a smaller.
    diff = sum(B) - sum(A)
    if diff == 0:
        return 0
    elif diff < 0:
        A, B = B, A
        diff = abs(diff)

    # find freq of each val
    # make 1 -> 0, diff stays same
    # but it helps with arr access
    N = 6
    a_freq = [0 for _ in range(N)]
    b_freq = [0 for _ in range(N)]

    for i in A:
        a_freq[i - 1] += 1

    for i in B:
        b_freq[i - 1] += 1

    # Now we see for each num, how to minimize diff
    # max possible available in each flip is N-i-1.
    flips_done = 0
    for i in range(N-1):
        # considering the max per flip, how
        # flips will overtake current diff.
        per_flip_count_possible = N-i-1
        flips_required = math.ceil(diff / per_flip_count_possible)

        max_possible_flips = a_freq[i] + b_freq[-i - 1]

        if flips_required > max_possible_flips:
            # diff remains even after all are flipped -
            # remove flipped sum from diff and continue
            flips_done += max_possible_flips
            diff -= max_possible_flips * per_flip_count_possible
        else:
            flips_done += flips_required
            return flips_done

    return -1


print(solution([1, 2, 3, 4, 3, 2, 1], [6]) == -1)  # not possible
print(solution([5, 4, 1, 2, 6, 5], [2]) == 6)  # all should be 1
print(solution([2, 3, 1, 1, 2], [5, 4, 6]) == 2)
print(solution([2, 3, 1, 1, 2], [5, 3, 1]) == 0)  # perfect
