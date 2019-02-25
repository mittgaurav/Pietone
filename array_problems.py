# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 00:04:30 2019

@author: gaurav
"""


def overlapping_area_of_rects(rect1, rect2):
    """given left bottom and right top of
    two points, find overlapping area"""
    l1x, l1y = rect1[0]
    l2x, l2y = rect2[0]
    r1x, r1y = rect1[1]
    r2x, r2y = rect2[1]

    # calculate left bottom and right
    # top of the overlapping rectangle
    lx, ly, rx, ry = 0, 0, 0, 0

    if l1x <= l2x <= r1x:
        lx = l2x
    elif l2x <= l1x <= r2x:
        lx = l1x
    else:
        return 0

    if l1y <= l2y <= r1y:
        ly = l2y
    elif l2y <= l1y <= r2y:
        ly = l1y
    else:
        return 0

    if r1x >= r2x >= l1x:
        rx = r2x
    elif r2x >= r1x >= l2x:
        rx = r1x
    else:
        return 0

    if r1y >= r2y >= l1y:
        ry = r2y
    elif r2y >= r1y >= l2y:
        ry = r1y
    else:
        return 0

    return (rx - lx) * (ry - ly)


print(overlapping_area_of_rects(((2, 1), (5, 5)), ((3, 2), (5, 7))))
print(overlapping_area_of_rects(((2, 1), (6, 8)), ((3, 2), (5, 5))))
print(overlapping_area_of_rects(((2, 1), (4, 8)), ((3, 2), (5, 6))))
