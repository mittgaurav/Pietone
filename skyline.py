# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 22:56:07 2019

@author: gaurav
"""
# NOT CORRECT
# NOT CORRECT
# NOT CORRECT
# NOT CORRECT

def skyline(arr):
    """A skyline for given
    building dimensions"""
    stack = list()
    result = list()

    now = 0
    while now < len(arr):
        start, height, end = arr[now]
        print(start, height)

        nxt = now + 1
        while nxt < len(arr):
            n_start, n_height, n_end = arr[nxt]

            # next building is far away
            if n_start >= end:
                break

            # next building is big, so we take it.
            if n_height > height:
                now = nxt
                if end > n_end:  # Add to stack
                    stack.append((n_end, height, end))
                now -= 1
                break

            if n_end > end:
                stack.append((end, n_height, n_end))
            nxt += 1
            now += 1
        now += 1


A = [
     (1, 10, 4),
     (3, 15, 8),
     (6, 9, 11),
     (10, 12, 15),
     (18, 12, 22),
     (20, 8, 25),
     ]
skyline(A)
