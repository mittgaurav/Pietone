# -*- coding: utf-8 -*-
"""
Created on Sun May 26 21:13:01 2019

@author: gaurav
"""


def string_in_order(order, string):
    """given order, check if chars
    in string follow that order"""
    if not string:
        return True
    if not order:
        return True

    ordered_set = set(order)
    j = 0
    for char in string:
        if char in ordered_set:
            while j < len(order) and order[j] != char:
                j += 1

            if j == len(order):
                return False

    return True


print(string_in_order('abc', 'aaa'))
print(string_in_order('abc', 'cabc'))
print(string_in_order('abc', 'xadb'))
