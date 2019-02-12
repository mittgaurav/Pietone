# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:48:59 2019

@author: gaurav
"""
import math
import random
import itertools


def password_generator():
    """generate random password
    from given possible cases"""
    caps = "ABCDEF"
    lows = "abcdef"
    nums = "123456"

    given = set()
    while True:
        cap = caps[math.floor(len(caps) * random.random())]
        low = lows[math.floor(len(lows) * random.random())]
        num = nums[math.floor(len(nums) * random.random())]

        wili = random.random()
        if wili * 3 < 1:
            wili = caps[math.floor(len(caps) * random.random())]
        elif wili * 3 < 2:
            wili = lows[math.floor(len(lows) * random.random())]
        else:
            wili = nums[math.floor(len(nums) * random.random())]

        # cap, low, num, wili
        words = [cap, low, num, wili]
        random.shuffle(words)
        password = "".join(words)

        if password not in given:
            given.add(password)
            yield password


def password_combinations():
    """all permutations
    for password"""
    caps = "ABCDEF"
    lows = "abcdef"
    nums = "123456"

    x = set()
    for c in caps:
        for l in lows:
            for n in nums:
                for w in caps + lows + nums:
                    for p in itertools.permutations([c, l, n, w]):
                        x.add(p)

    return len(x)


N = 1
total = password_combinations()
for i in password_generator():
    print(N, i, "out of", total)
    if N == total:
        break
    N += 1
