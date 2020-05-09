# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 14:51:31 2018

@author: gaurav

subsets and permutations: permutations
are special set of subsets that've all
elements of initial set to choose from
"""
import copy

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


print(create_subsets.__name__)
out = create_subsets([1, 2])
print(len(out), "-", out)
out = create_subsets([1, 2, 3, 4])
print(len(out), "-", out)
print("--------------------")


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


print(create_subsets_bits.__name__)
out = create_subsets_bits([1, 2])
print(len(out), "-", out)
out = create_subsets_bits([1, 2, 3, 4])
print(len(out), "-", out)
print("--------------------")


def permutations(arr):
    """permutations of given
    string. N! different."""
    if not arr:
        return [[]]
    if len(arr) == 1:
        return [arr]
    if len(arr) == 2:
        return [arr, [arr[1], arr[0]]]

    result = []
    for i in range(len(arr)):
        v = arr[i]  # use each element as first elem
        rest = arr[:i] + arr[i+1:]  # permute others
        result.extend([[v] + x for x in permutations(rest)])

    return result


print(permutations.__name__)
print(3, permutations([1, 2, 3]))
print(4, len(permutations([1, 2, 3, 4])))
print(5, len(permutations([1, 2, 3, 4, 5])))
print(7, len(permutations([1, 2, 3, 4, 5, 6, 7])))
print(8, len(permutations([1, 2, 3, 4, 5, 6, 7, 8])))


def permute(arr):
    """permute using backtracking"""
    total = []

    def _solve(arr, res):
        val = copy.deepcopy(res)
        if not arr:
            # goal
            total.append(val)
            return

        for i in arr:
            # choose
            val.append(i)

            # constraint
            #- recurse
            _solve([x for x in arr if x != i], val)

            #- unchoose
            val.pop()

    _solve(arr, [])
    return total

print(permute.__name__)
print(3, permute([1, 2, 3]))
print(4, len(permute([1, 2, 3, 4])))
print(5, len(permute([1, 2, 3, 4, 5])))
print(7, len(permute([1, 2, 3, 4, 5, 6, 7])))
print(8, len(permute([1, 2, 3, 4, 5, 6, 7, 8])))
