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
print(skyline.__name__)
skyline(A)
print("----------------")


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

    res = []

    start = 9999999
    end = 0
    while times:
        my_times = times.pop(0)
        start = min(start, my_times[0])
        end = max(end, my_times[1])
        if times:  # not the last element
            if end < times[0][0]:  # there is gap between
                # current element end and next start. End
                # right now and collect this into result
                res.append((start, end))
                start = 9999999
                end = 0

    if start != 9999999:
        # there has been no gap
        res.append((start, end))

    print(res)


print("bank_open_times")
main({"JPDL": [(8, 12), (13, 17)], "BARX": [(9, 13), (14, 18)]})
main({"JPDL": [(8, 12), (13, 17)], "BARX": [(9, 13), (19, 20)]})
main({"JPDL": [(8, 12), (13, 17), (19, 19)], "BARX": [(9, 13)]})
main({"JPDL": [(8, 12), (13, 17), (19, 19)], "BARX": []})
main({})
print("----------------")


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
print("----------------")


def first_missing_num_n(arr, start, end):
    """in a sorted array from 0 to n-1
    find the smallest element missing.
    One way, sort the array and then do
    a binary search for index == value
    at index."""
    if end == start:
        return start

    if end - start == 1:
        return start if arr[end] == end else end

    mid = (end - start) // 2
    if mid == arr[mid]:
        return first_missing_num_n(arr, mid + 1, end)

    ret = first_missing_num_n(arr, start, mid - 1)

    # now, ret could be same as the value; in that
    # mid is the first location that things go bad
    return mid if ret == arr[ret] else ret


print(first_missing_num_n.__name__)
print(first_missing_num_n([0, 1, 3, 4, 5, 6, 8], 0, 6))
print(first_missing_num_n([0, 1, 3, 4, 5], 0, 4))
