# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:46:12 2024

@author: gaurav
"""
def potholes(s, b):
    """Given a string of smooth road and
    potholes, and b as the money that is
    available to fix those, find the max
    number of potholes that can be fixed

    To fix successive group of potholes,
    the number of b required is n+1

    so to fix 1 pothole, 2 b are used
    to fix 5 potholes, 5+1 = 6 and so on
    """
    if not s or not b: return 0

    # find sizes of all potholes groups
    # and order them by reverse of size
    groups = []
    start = -1
    for i in range(len(s)):
        if s[i] == 'x': # pothole
            if start == -1:
                # first time in a group
                start = i
        else: # smooth
            if start != -1:
                groups.append(i - start)
                start = -1

    if start != -1:
        groups.append(len(s) - start)

    # reverse so that we go from largest
    # to smallest group. Solving big one
    # is better than many small ones.
    groups.sort(reverse=True)

    result = 0
    for g in groups:
        if b - 1 <= 0: break
        if b - 1 >= g:
            result += g
            b -= g + 1
        else:
            result += b - 1
            break

    return result


print("====", potholes.__name__)
print("..xxx..xxx..xx", 7, potholes("..xxx..xxx..xx", 7))
print("..xx..x..x.xx.x", 5, potholes("..xx..x..x.xx.x", 5))
print("xxxxxxxxx", 1, potholes("xxxxxxxxx", 1))
