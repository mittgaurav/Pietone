# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 01:13:14 2018

@author: gaurav
"""


def staircase(n):
    """Can hop 1, 2, or 3 steps in one go, how
    many possible ways to go up a staircase"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return staircase(n-1) + staircase(n-2) + staircase(n-3)


def staircase_dp(n):
    """DP keeping track of number
    of ways possible to reach the
    given step"""
    out = [0] * (n+1)
    out[0:4] = [0, 1, 2, 4]

    for i in range(4, n+1):
        out[i] = out[i-1] + out[i-2] + out[i-3]

    return out[n]


def staircase_dp_short(n):
    """short one that uses DP by
    keping track of last four as
    those are the ones we really
    care about"""
    a = 0
    b = 1
    c = 2
    d = 4

    if n == 0:
        return a
    if n == 1:
        return b
    if n == 2:
        return c
    if n == 3:
        return d

    for _ in range(4, n+1):
        a = b + c + d
        b = c
        c = d
        d = a

    return a


print(staircase.__name__)
print(staircase(4))
print(staircase(10))
print(staircase(20))
print("=================")

print(staircase_dp.__name__)
print(staircase_dp(4))
print(staircase_dp(10))
print(staircase_dp(20))
print(staircase_dp(200))
print("=================")

print(staircase_dp_short.__name__)
print(staircase_dp_short(4))
print(staircase_dp_short(10))
print(staircase_dp_short(20))
print(staircase_dp_short(200))
print("=================")


def staircase_given_steps(n, allow):
    """if you can take allowed steps at
    a time, how many steps are possible"""
    if n < 0:
        return 0
    if n == 0:
        return 0

    out = sum(staircase_given_steps(n-x, allow) for x in allow)
    if n in allow:
        out += 1
    return out


print(staircase_given_steps.__name__)
print(staircase_given_steps(4, [1]))
print(staircase_given_steps(10, [1, 2, 3]))
print(staircase_given_steps(20, [1, 2, 3]))
print("=================")
