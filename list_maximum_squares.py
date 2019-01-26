# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 03:25:59 2018

@author: gaurav
"""
import math


def list_squares(n):
    """given n, find the list
    of maximum squares"""
    if n < 1:
        return []
    if n < 4:
        return [1] * n

    x = math.sqrt(n)
    f = math.floor(x)
    if f == x:
        # x is square
        return [n]
    else:
        rem = n - (f ** 2)
        return [f ** 2] + list_squares(rem)


print(list_squares(12))
print(list_squares(15324))
print(list_squares(10000000))
print(list_squares(9998243))
