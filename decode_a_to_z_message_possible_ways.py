# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 00:44:07 2018

@author: gaurav
"""

map = {}
i = 1
for c in "abcdefghijklmnopqrstuvwxyz":
    map[i] = c
    i += 1


def decode_message(n):
    if n == 0:
        return [""]

    if n <= 10:
        return [map[n]]

    if n >= 11 and n < 20:
        return [map[n], "a" + map[n % 10]]

    if n == 20:
        return [map[n]]

    if n >= 21 and n <= 26:
        return [map[n], "b" + map[n % 20]]

    if n > 26:
        x = n
        power_of_ten = 0
        while True:
            x = int(x/10)
            if x > 0:
                power_of_ten += 1
            else:
                break

        b = int(n / (10 ** (power_of_ten)))
        d = n - (b * (10 ** (power_of_ten)))

        if power_of_ten > 1:  # power of hundred
            a = int(n / (10 ** (power_of_ten - 1)))
            c = n - (a * (10 ** (power_of_ten - 1)))

            if a > 26:
                return [map[b] + v for v in decode_message(d)]
            if a >= 21 and a <= 26:
                return [map[a] + v for v in decode_message(c)] \
                     + [map[b] + v for v in decode_message(d)]
            if a == 20:
                return [map[a] + v for v in decode_message(c)]
            if a >= 11 and a < 20:
                return [map[a] + v for v in decode_message(c)] \
                     + [map[b] + v for v in decode_message(d)]
            if a <= 10:
                return [map[b] + v for v in decode_message(d)]
        else:
            return [map[b] + v for v in decode_message(d)]


# print(decode_message(39885))
print(decode_message(123))
