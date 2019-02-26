# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 00:23:54 2019

@author: gaurav
"""

SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(string):
    """traverse the string
    and encode as per algo"""
    out = ""
    prev_char = None
    num_prev = 0
    for char in string:
        if not prev_char:  # first element
            num_prev = 1
            prev_char = char
        elif char == prev_char:  # continuing pattern
            num_prev += 1
        else:  # break in pattern
            loc = (ord(prev_char) - ord('A') + num_prev) % len(SET)
            out += SET[loc]
            if num_prev != 1:
                out += str(num_prev)
            prev_char = char
            num_prev_char = 1

    if num_prev_char:
        loc = (ord(prev_char) - ord('A') + num_prev) % len(SET)
        out += SET[loc]
        if num_prev_char != 1:
            out += str(num_prev_char)

    return out


def decode(string):
    """decode given encoded string"""
    out = ""
    prev_char = None
    num_prev = 0
    for char in string:
        if not prev_char:
            prev_char = char
            num_prev = 1
        elif char in SET:
            loc = (ord(prev_char) - ord('A') - num_prev) % len(SET)
            out += SET[loc] * num_prev
            prev_char = char
            num_prev = 1
        else:  # it's a num
            if num_prev > 1:
                num_prev = (10 * num_prev) + int(char)
            else:
                num_prev = int(char)

    if num_prev:
        loc = (ord(prev_char) - ord('A') - num_prev) % len(SET)
        out += SET[loc] * num_prev

    return out


print("encode and decode")
print(encode("WIINNNGGIIFFFFFFFYYYY"))
print(decode("XK2Q3I2K2M7C4"))
print("-----------------")


def remove_chars(string):
    """remove chars that are repeating
    but in the weird way"""
    out = ""

    prev_char = None
    i = 0
    while i < len(string):
        char = string[i]
        if not prev_char:
            out += char
            prev_char = char
            i += 1
        elif ord(char) <= ord(prev_char):
            out += char
            prev_char = char
            i += 1
        else:  # this char is larger than prev
            # hence keep it only if count is 1
            prev_char = char
            count = 0
            while i < len(string) and string[i] == prev_char:
                i += 1
                count += 1
            if count == 1:
                out += char

    return out


print(remove_chars.__name__)
print(remove_chars("WIINGGIIFFFYYY"))
print("-----------------")


BASE = [str(_) for _ in range(10)]

ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE.extend([_ for _ in ALPH.lower()])
BASE.extend([_ for _ in ALPH])
BASE.append('_')
BASE.append('-')


def shift_base(num, base):
    """shift decimal to given base"""
    my_base = BASE[:base]  # elems in my base

    out = ''
    while num > 0:
        num, rem = num // base, num % base
        out = my_base[rem] + out

    return out


print(shift_base.__name__)
print(shift_base(15, 16))    # f
print(shift_base(15, 16))    # f
print(shift_base(16, 16))    # 10
print(shift_base(255, 16))   # ff
print(shift_base(63, 64))    # -
print(shift_base(4095, 64))  # --
print(shift_base(35, 36))    # z
print(shift_base(36, 36))    # 10
print(shift_base(8, 8))      # 10
print(shift_base(63, 8))     # 77
print("-----------------")


def flatten(inp_obj):
    """flatten json"""
    out = {}

    def flatten_internal(inp, parent=''):
        """internal for nested"""
        for k, val in inp.items():
            if parent:  # add parent key
                k = parent + "." + k
            if not isinstance(val, dict):  # easy
                out[k] = val
                continue

            # nested dicts. flatten further
            flatten_internal(val, k)
    flatten_internal(inp_obj)
    return out


print(flatten.__name__)
print(flatten({
    'name': 'jane',
    'last_name': 'doe',
    'profession': 'engineer',
    'characteristics': {
        'intelligent': True,
        'punctual': False,
        'experience': {
            '2012': 'college passout',
            '2014': 'mba passout',
            '2016': 'employed'
        }
    }
}))
print("-----------------")
