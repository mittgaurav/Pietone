# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 22:56:07 2019

@author: gaurav
"""
# NOT CORRECT
# NOT CORRECT
# NOT CORRECT
# NOT CORRECT


def skyline(arr):
    """A skyline for given
    building dimensions"""

    now = 0
    while now < len(arr):
        start, height, end = arr[now]
        print(start, height)

        nxt = now + 1
        while nxt < len(arr):  # ignore short and small
            n_start, n_height, n_end = arr[nxt]

            # next building is far away, so read
            if n_start >= end:
                break

            # next building is big, so we take it
            if n_height > height:
                now = nxt
                if end > n_end:  # Add my remains
                    arr.insert(nxt, (n_end, height, end))
                now -= 1
                break

            # next building is small but longer
            # so keep what'll remain after this
            if n_end > end:
                arr[nxt] = (end, n_height, n_end)
                break

            nxt += 1
            now += 1

        now += 1


A = [(1, 10, 4),
     (2, 5, 3),
     (2.5, 5, 8),
     (3, 15, 8),
     (6, 9, 11),
     (10, 12, 15),
     (18, 12, 22),
     (20, 8, 25)]
print("====", skyline.__name__)
skyline(A)


def rain_water(arr):
    """collect rain water in
    different size building"""
    if not arr:
        return 0

    # for i, max on right and left
    left, right = [], []

    # collect max on the left side
    curr_max = 0
    for i in arr:
        left.append(curr_max)
        curr_max = max(curr_max, i)

    # collect max on the right side
    curr_max = 0
    for i in reversed(arr):
        right.insert(0, curr_max)
        curr_max = max(curr_max, i)

    # for each i, get its difference to min of l/r
    res = [max(0, min(_l, _r)-i) for _l, _r, i in
           zip(left, right, arr)]

    return sum(res)


def rain_water_2(arr):
    """One iteration but two pointers"""
    n = len(arr)
    res = [99999] * n

    pre = 0
    post = 0
    for i in range(len(arr)):  # same logic as array problems all ]product but i
        res[i] = min(res[i], max(0, pre - arr[i]))
        pre = max(pre, arr[i])
        res[n - i - 1] = min(res[n - i - 1], max(0, post - arr[n - i - 1]))
        post = max(post, arr[n - i - 1])

    return sum(res)


def rain_water_3(arr):
    """left or right mein kam wala decide karta hai kitna
    paani hoga. toh dekho kaun sa hoga and then usko ek step
    aage bhadhado"""
    left = 0
    right = len(arr) - 1
    res = 0

    max_l = 0
    max_r = 0
    while left < right:
        max_l = max(max_l, arr[left])
        max_r = max(max_r, arr[right])
        if max_l < max_r:
            # left is smaller. so it will decide how much water
            res += max_l - arr[left]
            # agli left position par check karo
            left += 1
        else:
            res += max_r - arr[right]
            right -= 1
    return res


print("====", rain_water.__name__)
print(rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(rain_water_2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(rain_water_3([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


def merge_intervals(intervals):
    """merge overlap-
    ping intervals"""
    out = []
    if not intervals:
        return out

    start, end = intervals[0]

    for new_start, new_end in intervals[1:]:
        if new_start <= end:  # overlapping elements
            end = max(end, new_end)
        else:  # New is after end. There's gap between
            # current element end and next start; end
            # right now and collect this into result
            out.append((start, end))
            start, end = new_start, new_end

    out.append((start, end))

    return out


print("====", merge_intervals.__name__)
print(merge_intervals([[1, 3], [2, 6], [4, 5], [8, 10], [15, 18]]))
print(merge_intervals([[1, 4], [4, 5]]))


def overlapping_intervals(intervals):
    """more than one running"""
    out = []
    if not intervals:
        return out

    prev_start, prev_end = 0, 0
    for start, end in intervals:
        # we have taken care of this later
        # by considering all four cases.
        start = max(start, prev_start)
        if end < start:
            # for shorter interval after
            continue
        if start < prev_end:
            if end < prev_end:
                out.append((start, end))
                prev_start = end
            else:
                out.append((start, prev_end))
                prev_start = prev_end
                prev_end = end
        else:
            prev_start, prev_end = start, end

    # we may have some overlapping intervals.
    out = merge_intervals(out)
    return out


print("====", overlapping_intervals.__name__)
print(overlapping_intervals([[1, 3], [2, 6], [4, 5], [8, 10]]))
print(overlapping_intervals([[1, 7], [2, 6], [4, 5], [8, 10]]))
print(overlapping_intervals([[1, 7], [2, 6], [6, 7], [8, 10]]))
print(overlapping_intervals([[1, 7], [2, 6], [5, 6], [6, 8]]))
print(overlapping_intervals([[1, 6], [2, 8], [3, 10], [5, 8]]))
print(overlapping_intervals([[1, 4], [4, 5]]))


def intersection_intervals(intervals):
    """simple: intersection of all"""
    out = []
    max_start = min([_[0] for _ in intervals])
    min_end = max([_[1] for _ in intervals])

    for start, end in intervals:
        max_start = max(max_start, start)
        min_end = min(min_end, end)

    if min_end > max_start:
        out.append((max_start, min_end))

    return out


print("====", intersection_intervals.__name__)
print(intersection_intervals([[1, 3], [2, 6], [4, 5], [8, 10]]))
print(intersection_intervals([[1, 6], [2, 8], [3, 10], [5, 8]]))


def main(dict_bank_list_of_times):
    """
    Bank hours problem
    Given a list of banks opening hours, determine
    the hours when there is at least one open bank

    This is useful to determine when it's possible
    to submit an order into a trading system.

    Example
    JPDL: 8-12 13-17
    BARX: 9-13 14-18

    Result: 8-18
    """
    times = []

    for bank_times in dict_bank_list_of_times.values():
        times.extend(bank_times)

    times.sort(key=lambda x: x[0])

    print(merge_intervals(times))


print("==== bank_open_times")
main({"JPDL": [(8, 12), (13, 17)], "BARX": [(9, 13), (14, 18)]})
main({"JPDL": [(8, 12), (13, 17)], "BARX": [(9, 13), (19, 20)]})
main({"JPDL": [(8, 12), (13, 17), (19, 19)], "BARX": [(9, 13)]})
main({"JPDL": [(8, 12), (13, 17), (19, 19)], "BARX": []})
main({})


def total_time(arr):
    """tell total time that user
    watched tv, given blocks"""
    if not arr:
        return 0

    arr.sort(key=lambda x: x[0])

    max_end = 0
    time = 0
    for start, end in arr:
        assert start <= end
        start = max(start, max_end)  # start within max_end?
        time += max(0, end - start)  # end > start but is it > max_end
        max_end = max(max_end, end)  # for the next

    return time


print("====", total_time.__name__)
print(total_time([[10, 20], [15, 25]]))
print(total_time([[10, 20], [22, 25]]))
print(total_time([[10, 20], [1, 25]]))


def largest_rectangle_histogram(arr):
    """find rectangle with largest size in histogram using stack"""
    # ek heights and length tuple ka stack banao such that
    # it tells me how far back can i go with this height
    # Phir apun log isko use karenge rectangle ke size mein
    stack = []
    max_rect = 0
    for i in arr:
        print(i, stack, end=" ")
        length = 1
        while stack and i <= stack[-1][0]:
            prev_h, prev_l = stack.pop()
            length += prev_l
        if stack:
            max_rect = max(max_rect, stack[-1][0] * (stack[-1][1] + length))
        stack.append((i, length))
        max_rect = max(max_rect, i * length)
        print(length, i * length, max_rect)

    return max_rect


print("====", largest_rectangle_histogram.__name__)
print(largest_rectangle_histogram([2, 1, 5, 6, 2, 3]))
print(largest_rectangle_histogram([2, 1, 5, 6, 2, 3, 2, 3]))
