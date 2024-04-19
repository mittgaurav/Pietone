# -*- coding: utf-8 -*-
"""
Created on Sun May 26 21:13:01 2019

@author: gaurav
"""


def string_in_order(order, string):
    """given order, check if chars
    in string follow that order"""
    if not string: return True
    if not order:  return True

    ordered_set = set(order)
    j = 0
    for char in string:
        if char not in ordered_set: continue

        # increment till we reach
        # char in the given order
        while j < len(order) and order[j] != char:
            j += 1

        if j == len(order):
            return False

    return True


print("====", string_in_order.__name__)
print('order', 'abc', 'str', 'aaa', string_in_order('abc', 'aaa'))
print('order', 'abc', 'str', 'abc', string_in_order('abc', 'abc'))
print('order', 'abc', 'str', 'cabc', string_in_order('abc', 'cabc'))
print('order', 'abc', 'str', 'xadb', string_in_order('abc', 'xadb'))


def put_string_in_order(order, string):
    """given order, reaarange
    string in the order. Can
    assume that each char in
    string exists in order"""
    if not string:
        return string
    if not order:
        return string

    # assert no duplicates
    assert len(set(order)) == len(order)

    # map location in order
    order_map = {}
    for i in range(len(order)):
        order_map[order[i]] = i

    # sort string by location in order
    return "".join(sorted(string, key=lambda x: order_map[x]))


print("====", put_string_in_order.__name__)
print(put_string_in_order('abc', 'aaa'))
print(put_string_in_order('abc', 'cabc'))
print(put_string_in_order("bxyzca", "abcabcabc"))


def place_i_spaced_ints(arr, n):
    """place pair of n ints spaced
    at ith distance from each other"""
    if n == 0:
        return True

    # for each i, check whether any
    # location and (location+i) loc
    # are empty to put i value
    for i in range(0, len(arr) - n - 1):
        if arr[i] == 0 and arr[i+n+1] == 0:
            arr[i], arr[i+n+1] = n, n
            if not place_i_spaced_ints(arr, n-1):
                # failure, backtrack
                arr[i], arr[i+n+1] = 0, 0

    # check that n exists
    # twice in the array
    count = len([x for x in arr if x == n])
    return count == 2


print("====", place_i_spaced_ints.__name__)
for N in range(13):
    array = [0] * 2 * N
    print(N, place_i_spaced_ints(array, N), array)


def add_one(arr, j):
    """add one to an int
    represented by arr"""
    if j < 0:
        arr.insert(0, 1)
        return

    if arr[j] == 9:
        arr[j] = 0
        add_one(arr, j-1)
    else:
        arr[j] += 1


print('====', add_one.__name__)
arrays = [
        [2, 3, 4, 1],
        [9, 9, 9, 9],
        [0]
        ]

for array in arrays:
    print(array, end='->')
    add_one(array, len(array) - 1)
    print(array)


def i_j_maximum_index(arr):
    """Given an array A[] of N positive
    integers. Find max of j-i such that
    A[i] <= A[j]."""
    mines = []
    minim = 9999
    for i in arr:
        minim = min(minim, i)
        mines.append(minim)

    maxes = []
    maxim = -9999
    arr.reverse()
    for i in arr:
        maxim = max(maxim, i)
        maxes.insert(0, maxim)

    print(mines)
    print(maxes)
    i = j = 0
    val = -1
    while i < len(arr) and j < len(arr):
        if mines[i] > maxes[j]:
            i += 1
        else:
            val = max(val, j - i)
            j += 1

    return val


arrays = [
        [9, 2, 3, 4, 5, 6, 7, 8, 18, 0],
        [7, 3, 2, 1, 8, 0, 5, 1, 12, 5],
        [7, 3, 2, 1, 8, 0, 5, 1, 2, 5],
        ]

print('====', i_j_maximum_index.__name__)
for array in arrays:
    print(array)
    print(i_j_maximum_index(array))


def parallel_platforms(arr, dep):
    """given arrival and departure times
    of trains; how many platforms should
    be there to process them all"""
    arr.sort()
    dep.sort()

    i = 0
    j = 0
    maxi = 0
    val = 0
    while i < len(arr):
        if arr[i] < dep[j]:
            # another arrival before departure
            val += 1
            i += 1
        elif arr[i] == dep[j]:
            # departure along with arrival. We
            # don't need an extra platform.
            i += 1
            j += 1
        elif arr[i] > dep[j]:
            # departure happened. see how many
            # platforms were needed for this.
            maxi = max(maxi, val)
            j += 1
            val -= 1

    # to capture departure right after last arrival
    # which potentially has the maximum platforms
    maxi = max(maxi, val)

    return maxi


def parallel_platforms_times(arr, dep):
    """given arrival and departure times
    of trains; how many of the platforms
    are going to be used by time slot"""
    arr.sort()
    dep.sort()

    i = 0
    j = 0
    prev_time = -1
    val = 0
    result = []
    while i < len(arr):
        if arr[i] < dep[j]:
            if prev_time > 0: result.append((prev_time, arr[i], val))
            prev_time = arr[i]
            val += 1
            i += 1
        elif arr[i] == dep[j]:
            i += 1
            j += 1
        elif arr[i] > dep[j]:
            result.append((prev_time, dep[j], val))
            prev_time = dep[j]
            j += 1
            val -= 1

    # departures after arrivals
    while j < len(arr):
        result.append((prev_time, dep[j], val))
        prev_time = dep[j]
        val -= 1
        j += 1

    assert val == 0, "All platform are free at end"
    return result


print("====", parallel_platforms.__name__)
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(parallel_platforms(arr, dep))
print(parallel_platforms_times(arr, dep))
dep = [910, 1200, 1120, 1100, 1900, 2000]
print(parallel_platforms(arr, dep))
print(parallel_platforms_times(arr, dep))


def minesweeper(arr):
    """given mines in a field,
    draw minesweeper map; i.e.
    count the number of bombs
    surrounding each index"""
    def _g(i, j):
        try:
            return 1 if arr[i][j] == '*' else 0
        except IndexError:
            return 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != '*':
                arr[i][j] = str(_g(i-1, j) + _g(i, j-1) + _g(i+1, j)
                                + _g(i, j+1) + _g(i-1, j-1) + _g(i+1, j+1)
                                + _g(i-1, j+1) + _g(i+1, j-1))
    return arr


print('====', minesweeper.__name__)
arr = [
       ['*', '.', '.', '.'],
       ['.', '.', '.', '.'],
       ['.', '*', '.', '.'],
       ['.', '.', '.', '.'],
]
assert [print(_) for _ in arr]
arr = minesweeper(arr)
assert [print(_) for _ in arr]


def share_buy_sell_once(arr):
    """given share prices, buy and
    sell once to maximize profits.
    No short selling allowed."""
    min_price = 99999
    max_profit = 0

    for x in arr:
        max_profit = max(x-min_price, max_profit)
        min_price = min(x, min_price)

    return max_profit


print('====', share_buy_sell_once.__name__)
print(share_buy_sell_once([5, 10, 2, 8, 12, 5]))
print(share_buy_sell_once([5, 10, 15, 8, 12, 5]))
print(share_buy_sell_once([5, 10, 15, 8, 16, 5]))
print(share_buy_sell_once([5, 10, 15, 20, 25, 30]))
print(share_buy_sell_once(reversed([5, 10, 15, 20, 25, 30])))


def max_meetings(s, e):
    """given start and end times
    find max num of meetings."""
    result = []
    for i in range(len(s)):
        if i == len(s) - 1:
            result.append([s[i], e[i]])
            return result
        if e[i] <= s[i+1]:
            # if this meeting ends before
            # start of next, must pick it
            result.append([s[i], e[i]])
        elif e[i] > e[i+1]:
            # if this meetings extends
            # beyond next, do not pick
            continue
        else:
            # second meeting is useless.
            # remove it, first may still
            # keep it for next iteration
            s[i+1], e[i+1] = s[i], e[i]

    return []


print('====', max_meetings.__name__)
print(max_meetings([0, 1, 3, 5, 5, 8], [6, 2, 4, 7, 9, 9]))
print(max_meetings(
        [8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924],
        [93424, 54316, 35533, 81825, 114515, 73383, 112960, 160252]))
print(max_meetings([1, 5, 6, 8, 8], [10, 20, 8, 9, 10]))
