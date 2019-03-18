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


print("====", rain_water.__name__)
print(rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


def merge_intervals(intervals):
    """merge overlap-
    ping intervals"""
    out = []
    if not intervals:
        return out

    start = intervals[0][0]
    end = intervals[0][1]

    for i in intervals[1:]:
        new_start = i[0]
        new_end = i[1]
        if new_start <= end:  # overlapping elements
            end = max(end, new_end)
        else:  # New is after end. There's gap between
            # current element end and next start; end
            # right now and collect this into result
            out.append((start, end))
            start = new_start
            end = new_end

    out.append((start, end))

    return out


print("====", merge_intervals.__name__)
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge_intervals([[1, 4], [4, 5]]))


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
