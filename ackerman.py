# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:28:12 2024

@author: gaurav
"""
import sys

sys.setrecursionlimit(150000)
sys.set_int_max_str_digits(100000)


def ack(m, n):
    if m <= 0: return n + 1
    if n <= 0: return ack(m-1, 1)
    return ack(m-1, ack(m, n-1))


print("==== basic")
for i in range(5):
    for j in range(1):
        print(i, j, ack(i, j))


def tetration(base, height):
    res = base
    while height > 1:
        res = base ** res
        height -= 1
    return res


print("==== tetration")
print(tetration(2, 1))  # Output: 2 (2)
print(tetration(2, 2))  # Output: 4 (2^2)
print(tetration(2, 3))  # Output: 16 (2^(2^2))
print(tetration(2, 4))  # Output: 65536 (2^(2^(2^2)))
print(tetration(2, 5))  # Output: 2**65536 (2^(2^(2^(2^2))))


def ack2(m, n):
    if m <= 0: return n + 1
    if n <= 0: return ack2(m-1, 1)

    if m == 1: return n + 2
    if m == 2: return 2*n + 3
    if m == 3: return 2**(n+3) - 3
    if m == 4: return tetration(2, n+3) - 3

    return ack2(m-1, ack2(m, n-1))


print("==== base recursion")
for i in range(5):
    for j in range(3):
        print(i, j, ack2(i, j))
