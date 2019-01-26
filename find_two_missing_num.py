# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 23:04:43 2019

@author: gaurav
"""


def find_two_missing(arr):
    """given array of 1 to n
    with two numbers missing.
    Usually done with XOR"""
    N = len(arr) + 2

    # mean of two numbers
    mean = (((N * (N+1)) // 2) - sum(arr)) // 2

    # we know one num is
    # before mean, other
    # obviously after it
    sum_before = sum([i for i in arr if i <= mean])

    n1 = (mean * (mean + 1)) / 2 - sum_before
    n2 = (((N * (N+1)) // 2) - sum(arr)) - n1
    return int(n1), int(n2)


print(find_two_missing([4, 2, 3]))
A = list(range(1, 100))
A.remove(20)
A.remove(65)
print(find_two_missing(A))
A = list(range(1, 9999999))
A.remove(878778)
A.remove(989898)
print(find_two_missing(A))
A = list(range(1, 9999999))
A.remove(878778)
A.remove(878780)
print(find_two_missing(A))
