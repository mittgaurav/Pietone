# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 07:28:25 2020

@author: gaurav
"""


def fn(string, words):
    """
    Given a long string, break
    it into minimum num groups
    from given list of strings

    www.youtube.com/watch?v=tOD6g7rF7NA
    """
    if not string:
        return 0  # win in 0 spaces

    if not words:
        return None  # can't win

    minn = 1000

    # for first char of string, pick
    # options that match the string.
    # Then for each of those options
    # do the same for remaining part
    # of string and other options. A
    # Chain of options which returns
    # the lowest count wins.

    # options matching
    # first character.
    char = string[0]
    options = [x for x in words if x[0] == char and x == string[0:len(x)]]

    for option in options:
        # for each option check
        # remaining options for
        # remaining part of str
        rem_string = string[len(option):]

        rem = fn(rem_string, [x for x in words if x != option])
        if rem is not None:
            minn = min(minn, 1 + rem)

    return minn


print(fn('314159265358979323846264',
         ['3', '14', '314', '15926535897', '159', '26535897',
          '9001', '9323', '8', '84', '6264', '46264']
         ))
print(fn('314159265358979323846264',
         ['3', '14', '15926535897', '159', '26535897',
          '9001', '9323', '8', '84', '6264', '46264']
         ))
print(fn('314159265358979323846264',
         ['3', '14', '15926535897', '159', '26535897',
          '9001', '9323', '8', '4', '6264', '62648']
         ))
