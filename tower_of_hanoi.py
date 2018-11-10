# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 12:48:22 2018

@author: gaurav
"""


def step(n, fr, to):
    print("move {} from {} to {}".format(n, fr, to))


def tower_of_hanoi(n, fr, to, park):
    # prints steps to solve the
    # tower of hanoi for given
    # number of disks.
    if n <= 0:
        return

    # move top n-1 disks to
    # the parking platform.
    tower_of_hanoi(n-1, fr, park, to)
    # move nth to final one
    step(n, fr, to)
    # move top n-1 disks to
    # final from parking.
    tower_of_hanoi(n-1, park, to, fr)


tower_of_hanoi(1, "X", "Z", "Y")
tower_of_hanoi(2, "A", "C", "B")
tower_of_hanoi(4, "A", "C", "B")
tower_of_hanoi(10, "X", "Z", "Y")
