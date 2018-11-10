# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 20:17:09 2018

@author: gaurav
"""

"""
we got to find the first value that is
equal to or greater than given value.

we first do binary search for that val
and if the elem is same, we return it.
(though there can be duplicate elem on
left side, we assume unique hopefully)

Then, if the elem is small, search for
that in right and if larger, search in
left.

Keep looking right is just recursion.
left, that's interesting. It seems to
be recursion, but if we don't find a
val, we have to say that there is no
smaller larger value in left, so the
current elem is the first larger val
"""
def _bs(arr, begin, end, num):
    if begin == end:
        if arr[begin] >= num:
            return begin
        else:
            return -1

    mid = int((begin + end) / 2)
    if arr[mid] == num:
        return mid
    if arr[mid] < num:
        return _bs(arr, mid + 1, end, num)
    if arr[mid] > num:
        loc = _bs(arr, begin, mid - 1, num)

        # if we can't find lesser
        # larger. I'm the largest
        if -1 == loc:
            return mid
        else:
            return loc
    return -1


def binary_search_ge(arr, num):
    """find number equal to or
    least larger than given"""
    loc = _bs(arr, 0, len(arr) - 1, num)
    return loc, arr[loc]


print(binary_search_ge([1, 2, 3, 4, 5, 7, 8], 0))
print(binary_search_ge([1, 2, 3, 4, 5, 7, 8], 10))
print(binary_search_ge([1, 2, 3, 4, 5, 7, 8], 1))
print(binary_search_ge([1, 2, 3, 4, 5, 7, 8], 6))
print(binary_search_ge([1, 2, 3, 4, 5, 7, 8], -1))
