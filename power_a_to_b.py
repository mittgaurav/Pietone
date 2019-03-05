# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:57:40 2019

@author: gaurav

cache half power results. O(log n)
"""


def power(a, b):
    """power without pow() under O(b)"""
    if a == 0:
        return 0

    if b == 1:
        return a
    elif b == 0:
        return 1
    elif b < 0:
        return 1 / power(a, -b)
    else:  # positive >1 integer
        half_res = power(a, b // 2)
        ret = half_res * half_res
        if b % 2:  # odd power
            ret *= a

    return ret


for A, B in [(4, 5), (2, 3), (2, -6), (12, 4)]:
    CACHE = {}
    print(A, B, ":", pow(A, B), power(A, B))
