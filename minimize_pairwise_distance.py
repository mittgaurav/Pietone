# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 23:06:41 2018

@author: gaurav
"""


def pairs(aI):
    """ generate the
    needed pairs."""
    if len(aI) <= 0:
        yield []
        return

    a = aI[0]
    for i in range(1, len(aI)):
        b = aI[i]
        p = pairs(aI[1:i] + aI[i+1:])
        for e in p:
            yield [(a, b)] + e


def minimize_pair_dist(aI):
    """given distances
    reduce the overall
    sum of lengths."""

    mindist = 100000
    for x in pairs(aI):
        dist = 0
        for i in x:
            dist += abs(i[0] - i[1])
        mindist = min(dist, mindist)
    return mindist


print(minimize_pair_dist([1, 0, 3, 4]))
