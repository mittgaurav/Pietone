# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 02:08:44 2018

If we have to keep track of
median of a stream of nums.

Not good when the stream is
already provided as we have
to allocate two heaps with
combined length of numbers.
Better to use kth_elem algo

@author: gaurav
"""
from priority_queue import MinHeap, MaxHeap
import numpy as np


class TrackMedian():
    """tracks median via
    min and max heaps"""
    def __init__(self):
        self.min = MinHeap()  # upper half
        self.max = MaxHeap()  # lower half

    def __str__(self):
        return str(self.min) + str(self.max)

    __repr__ = __str__

    def add(self, elem):
        """add new elem, always
        making sure min and max
        heaps have maximum diff
        in length equal to 1"""
        if not self.min.vals or elem >= self.min.peek():
            self.min.add(elem)
        else:
            self.max.add(elem)

        if abs(len(self.min) - len(self.max)) <= 1:
            return
        if len(self.min) > len(self.max):
            self.max.add(self.min.pop())
        else:
            self.min.add(self.max.pop())

    def get_median(self):
        """return median"""
        if len(self.min) > len(self.max):
            return self.min.peek()
        if len(self.max) > len(self.min):
            return self.max.peek()
        if not self.min:  # both are empty
            return None
        return (self.min.peek() + self.max.peek()) / 2


A = TrackMedian()
B = list()
print("======= Track Median =======")
for i in [6, 1, 3, 5, 7, 4, 8, 2, 9]:
    A.add(i)
    B.append(i)
    B.sort()
    print(B, "=>", A.get_median())
    assert A.get_median() == np.median(B)


class KthLargest():
    """Keep track of kth largest
    number, don't care about the
    rest. If yes, then store num
    array and use it to add vals
    when a new number is put."""
    def __init__(self, array, K):
        self.min = MinHeap()  # smallest of larger
        self.K = K

        for i in array:
            self.add(i)

    def __str__(self):
        return str(self.min)

    __repr__ = __str__

    def add(self, elem):
        """add new elem"""
        self.min.add(elem)
        if len(self.min.vals) > self.K:
            # Heap has now more than k
            self.min.pop()

        return self.min.peek()


print("======= Kth Largest ========")
A = KthLargest([3, 1, 5, 12, 2, 11], 4)
print(A)
for i in [6, 6, 10, 1, 3, 7, 8, 20, 30]:
    print(A, A.add(i))
