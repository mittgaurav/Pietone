# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 18:16:12 2018

@author: gaurav

current + prev less weight
vs.
no curr + prev same weight

W (v)[0](1, 2, 3, 4, 5, 6, 7)
     [0, 0, 0, 0, 0, 0, 0, 0]
1 (1)[0, 1, 1, 1, 1, 1, 1, 1]
3 (4)[0, 1, 1, 4, 5, 5, 5, 5]
4 (5)[0, 1, 1, 4, 5, 6, 6, 9]
5 (7)[0, 1, 1, 4, 5, 7, 8, 9]

first loop fills the 0 sizes.
then iterate over each weight
for the total weight and fill
the matrix with max possible.

Can be used to solve meetings
problem; values equal weights
"""
matrix = []


def knapsack(arrW, arrV, total):
    """arrays of weight and vals
    and total weight allowed. we
    assume arrays are sorted by
    weights"""
    if len(arrW) == 0:
        return 0
    if arrW[0] > total:
        return 0

    # set 0 index
    matrix = [[0 for _ in range(total+1)] for _ in
              range(len(arrW)+1)]

    for i in range(1, len(arrW) + 1):
        for j in range(1, total+1):
            rem_weight = j - arrW[i-1]
            if rem_weight >= 0:
                # we can add current weight
                val1 = arrV[i-1] + matrix[i-1][rem_weight]
            else:
                # can't take current weight
                val1 = 0
            # now check if we maximize
            # with or without this one
            matrix[i].insert(j, max(val1, matrix[i-1][j]))

    return matrix[len(arrW) - 1][total]


def knapsack_no_dp(arrW, arrV, a, total):
    """No dp"""
    if a == 0:  # 0-length array
        return 0
    rem_wt = total - arrW[a-1]
    if rem_wt >= 0:
        v1 = arrV[a-1] + knapsack_no_dp(arrW, arrV, a-1, rem_wt)
    else:
        v1 = 0
    return max(v1, knapsack_no_dp(arrW, arrV, a-1, total))


print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))
print(knapsack_no_dp([1, 3, 4, 5], [1, 4, 5, 7], 4, 7))
print(knapsack([1, 3, 4, 5], [1, 3, 4, 5], 7))
print(knapsack_no_dp([1, 3, 4, 5], [1, 3, 4, 5], 4, 7))


def knapsack_basic(items, maxWght):
    """how i thought out of blue"""
    if not items:
        return 0

    i = items[0]
    without = knapsack_basic(items[1:], maxWght)

    if i.get('w') > maxWght:
        return without

    with_i = knapsack_basic(items[1:], maxWght-i.get('w')) + i.get('v')

    return max(without, with_i)


items = [{'w': 1, 'v': 6}, {'w': 2, 'v': 10}, {'w': 3, 'v': 12}]
print(knapsack_basic(items, 5))
