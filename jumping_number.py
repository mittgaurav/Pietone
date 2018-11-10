# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 22:33:58 2018

@author: gaurav
"""


def jumping_number(n):
    nums = []
    for i in range(0, min(9, n) + 1):
        nums.append(i)

    for i in nums:
        if i == 0:
            continue

        if i >= n:
            break

        j = i * 10 + i % 10 - 1
        if j <= n and i % 10 != 0:
            # should not add
            # 9 if num is 10
            nums.append(j)

        j += 2
        if j <= n and i % 10 != 9:
            # should not add
            # 10 if num is 9
            nums.append(j)

    return nums


print(jumping_number(5))
print(jumping_number(12))
print(jumping_number(23))
print(jumping_number(50))
print(jumping_number(100))
print(jumping_number(1000))
