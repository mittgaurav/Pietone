# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 14:51:31 2018

@author: gaurav
"""
"""========Combinations========="""


def create_subsets(arr):
    """create subsets
    of input array"""
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    if len(arr) == 2:
        return [[arr[0]], [arr[1]], arr]

    vals = []
    i = 0
    while i < len(arr):
        # choose one elem,
        # that's singleton
        # and pick subsets
        # of all remaining
        vals += [[arr[i]]]
        vals += create_subsets([v for v in arr if v != arr[i]])
        i += 1

    # we will end up with
    # an awful lot num of
    # duplicate elements.
    res = [arr]
    for v in vals:
        if v not in res:
            res.append(v)
    return res


out = create_subsets([1, 2])
print(len(out), "-", out)
out = create_subsets([1, 2, 3, 4])
print(len(out), "-", out)


def create_subsets_bits(arr):
    """use n bit num. If
    ith bit is set, take
    that num, else no"""
    n = 1 << len(arr)  # one extra bit

    vals = []
    i = 1  # set i=0 to have empty set
    while i < n:
        # pick those elements that are
        # set in i. so, "&" won't be 0
        vals += [[arr[j] for j in range(n) if 0 != i & (1 << j)]]
        i += 1

    return vals


out = create_subsets_bits([1, 2])
print(len(out), "-", out)
out = create_subsets_bits([1, 2, 3, 4])
print(len(out), "-", out)

"""========Permutations========="""
