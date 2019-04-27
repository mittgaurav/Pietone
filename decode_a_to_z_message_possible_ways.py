# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 00:44:07 2018

@author: gaurav
"""

struct = {}
i = 1
for char in "abcdefghijklmnopqrstuvwxyz":
    struct[i] = char
    i += 1


def decode_message(n):
    if n == 0:
        return [""]

    if n <= 10:
        return [struct[n]]

    if 11 <= n < 20:
        return [struct[n], "a" + struct[n % 10]]

    if n == 20:
        return [struct[n]]

    if 21 <= n <= 26:
        return [struct[n], "b" + struct[n % 20]]

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
                return [struct[b] + v for v in decode_message(d)]
            if 21 <= a <= 26:
                return [struct[a] + v for v in decode_message(c)] \
                     + [struct[b] + v for v in decode_message(d)]
            if a == 20:
                return [struct[a] + v for v in decode_message(c)]
            if 11 <= a < 20:
                return [struct[a] + v for v in decode_message(c)] \
                     + [struct[b] + v for v in decode_message(d)]
            if a <= 10:
                return [struct[b] + v for v in decode_message(d)]
        else:
            return [struct[b] + v for v in decode_message(d)]


print(decode_message(39885))
print(decode_message(12345))


def decode_msg(n):
    """decode all possible ways"""
    val = []
    if not n or n <= 0:
        return [""]

    x = n % 10
    if x in struct:
        val.extend([v + struct[x] for v in decode_msg(n // 10)])

    if n >= 10:
        x = n % 100
        if x in struct:
            val.extend([v + struct[x] for v in decode_msg(n // 100)])

    return val


print(decode_msg(3))
print(decode_msg(32))
print(decode_msg(2213))
print(decode_msg(9))
print(decode_msg(10))
print(decode_msg(11))
print(decode_msg(2213))
