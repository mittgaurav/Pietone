# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:46:12 2024

@author: gaurav
"""
def potholes(s, b):
    """Given a string of smooth road and
    potholes, and b as the money that is
    available to fix those, find the max
    number of potholes that can be fixed

    To fix successive group of potholes,
    the number of b required is n+1

    so to fix 1 pothole, 2 b are used
    to fix 5 potholes, 5+1 = 6 and so on
    """
    if not s or not b: return 0

    # find sizes of all potholes groups
    # and order them by reverse of size
    groups = []
    start = -1
    for i in range(len(s)):
        if s[i] == 'x': # pothole
            if start == -1:
                # first time in a group
                start = i
        else: # smooth
            if start != -1:
                groups.append(i - start)
                start = -1

    if start != -1:
        groups.append(len(s) - start)

    # reverse so that we go from largest
    # to smallest group. Solving big one
    # is better than many small ones.
    groups.sort(reverse=True)

    result = 0
    for g in groups:
        if b - 1 <= 0: break
        if b - 1 >= g:
            result += g
            b -= g + 1
        else:
            result += b - 1
            break

    return result


print("====", potholes.__name__)
print("..xxx..xxx..xx", 7, potholes("..xxx..xxx..xx", 7))
print("..xx..x..x.xx.x", 5, potholes("..xx..x..x.xx.x", 5))
print("xxxxxxxxx", 1, potholes("xxxxxxxxx", 1))


def min_window_with_all_chars(s, t):
    """give the minimum length of window
    in s that covers all chars in t"""
    if not s or not t: return ""

    # find freq of each char in t
    from collections import Counter
    orig_freq = dict(Counter(t))
    print(orig_freq)

    # let's first get the first
    # solution that starts at 0
    # also record gathered freq
    # which is for optimization
    first_freq = dict(Counter(t))
    gathered = {}
    start = 0
    for end in range(len(s)):
        # Check if we found a char
        # from the required string
        if s[end] in first_freq:
            if first_freq[s[end]] == 1:
                first_freq.pop(s[end])
            else: first_freq[s[end]] -= 1
        # To keep count of char freq
        # we will use these later on
        if s[end] in orig_freq:
            gathered[s[end]] = gathered.get(s[end], 0) + 1
        if not first_freq:
            break

    # we were not able to exhaust
    if first_freq: return ""

    # first solution
    res_start, res_end = start, end

    while start < end:
        if s[start] in gathered:
            # the start char is relevant
            gathered[s[start]] -= 1
            if gathered[s[start]] >= orig_freq[s[start]]:
                # even after removing it
                # things are ok, so just
                # remove and check min
                start += 1
            else:
                # move end one step till
                # and hope to fill orig
                if end + 1 == len(s): break
                end += 1
                while end + 1 < len(s) and s[end] != s[start]:
                    end += 1
                    if s[end] in gathered:
                        gathered[s[end]] += 1
                start += 1
        else:
            # start char is not relevant
            # so we can skip it to check
            # if new minimum is obtained
            start += 1
        if end - start < res_end - res_start:
            res_start, res_end = start, end
            print(s[res_start: res_end + 1], gathered)

    return s[res_start: res_end + 1]


print("====", min_window_with_all_chars.__name__)
test_cases = [
    # Basic test case
    ("ADOBECODEBANC", "ABC", "BANC"),
    # t is a single character in s
    ("a", "a", "a"),
    # t is a single character not in s
    ("a", "b", ""),
    # s is empty
    ("", "ABC", ""),
    # t is empty
    ("ADOBECODEBANC", "", ""),
    # s and t are the same
    ("ABC", "ABC", "ABC"),
    # Multiple possible windows, one smallest
    ("aaflslflsldkabcdef", "fsl", "fls"),
    # Characters in s are in t, but not all required characters are present
    ("AA", "AAB", ""),
    # All characters in s are the same
    ("aaaaaaa", "aa", "aa"),
    # Larger s, non-repeating pattern
    ("this is a test string", "tist", "t stri"),
]
for s, t, exp in test_cases:
    res = min_window_with_all_chars(s, t)
    assert res == exp, f"{s}, {t}, {exp}, {res}"


def car_fleets(position, speed, target):
    """Given cars at given positions and speed going towards a target.
    Find out how many cars groups will form reaching the target if the
    faster cars can't overtake a slower car and they become a fleet"""
    prev_time = 0
    count = 0
    for i in range(len(position) - 1, -1, -1):
        time = speed[i] * (target - position[i])
        if time > prev_time:
            # this car takes more time than the ones closer
            # to target, so will not get stuck behind them
            count += 1
            prev_time = time

    return count


print("====", car_fleets.__name__)
print(car_fleets([0, 3, 5, 8, 10], [1, 3, 1, 4, 2], 12))
