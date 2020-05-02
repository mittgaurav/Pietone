# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:00:54 2018

Priority Queue
Maxheap: max num at root.

@author: gaurav
"""


class Heap:
    """heap based data stuct
    that stores values as by
    a certain 'priority'"""
    @classmethod
    def order(cls, arr, parent, child):
        """parent >= child in max heap
        parent <= child in min heap"""
        pass

    def __init__(self):
        self.vals = []

    def add(self, num):
        """add to end and
        propogate up"""
        self.vals.append(num)

        self.swim_up(len(self) - 1)
        return self

    insert = add

    def _swap(self, i, j):
        """swap"""
        self.vals[i], self.vals[j] = self.vals[j], self.vals[i]

    def __str__(self):
        return str(self.vals)

    __repr__ = __str__

    def __len__(self):
        return len(self.vals)

    def swim_up(self, i):
        """move number added
        at end higher to its
        rightful place"""
        if i <= 0:
            return

        # if it and its parent doesn't
        # follow the order, swap them.
        par = int((i - 1)/2)  # parent
        if self.order(self.vals, par, i):
            return  # has heap property

        # Swap as parent less than elem
        self._swap(i, par)
        # Repeat same activity with par
        self.swim_up(par)

    def _heapify(self, i=0):
        """bring the num at the
        top to its right loc"""
        if i >= int(len(self)/2):
            return

        L = (2 * i) + 1
        r = (2 * i) + 2

        # 3 way comparison to
        # get the m**imum. We
        # swap i with m**imum
        topper = i
        if L < len(self) and not self.order(self.vals, i, L):
            topper = L
        if r < len(self) and not self.order(self.vals, topper, r):
            topper = r
        if topper == i:
            return  # has heap property

        self._swap(topper, i)
        self._heapify(topper)

    def pop(self):
        """take top elem,
        replace with end,
        and heapify; i.e.
        move it down, to
        its right place.
        """
        # take top element
        ret = self.peek()

        if len(self.vals) == 1:  # only one element
            self.vals.pop()
        if len(self.vals) > 1:  # more than 1 elements
            # replace top most
            # pos with last.
            self.vals[0] = self.vals.pop()
            self._heapify()

        return ret

    def peek(self):
        """view root"""
        return self.vals[0] if self.vals else None

    @classmethod
    def check(cls, arr, start=0):
        """is arr an intended heap?"""
        if len(arr) <= 1:
            return True

        if start >= int(len(arr)/2):
            return True

        L = (2 * start) + 1
        r = (2 * start) + 2

        if L < len(arr) and not cls.order(arr, start, L):
            return False
        if r < len(arr) and not cls.order(arr, start, r):
            return False

        return cls.check(arr, L) and cls.check(arr, r)


class MaxHeap(Heap):
    """heap based data stuct
    that stores values as by
    a maximum 'priority'"""
    @classmethod
    def order(cls, arr, parent, child):
        """parent >= child in max heap"""
        return arr[parent] >= arr[child]


class MinHeap(Heap):
    """Minimum at root"""
    @classmethod
    def order(cls, arr, parent, child):
        """parent <= child in min heap"""
        return arr[parent] <= arr[child]


if __name__ == "__main__":
    print(MaxHeap.check([8, 6, 6, 0, 2, 3, 1, 1]))
    print(MaxHeap.check([8, 6, 6, 0, 2, 3, 1, 0]))
    a = MaxHeap()
    print(a)
    print("add 4,", a.add(4))
    print("add 5,", a.add(5))
    print("add 3,", a.add(3))
    print("maxheap check:", MaxHeap.check(a.vals))
    a.pop()
    print("pop 5,", a)
    print("add 7,", a.add(7))
    print("add 0,", a.add(0))
    print("maxheap check:", MaxHeap.check(a.vals))
    a.pop()
    print("pop 7,", a)
    a.pop()
    print("pop 4,", a)
    print("add 8,", a.add(8))
    print("add 6,", a.add(6))
    print("add 2,", a.add(2))
    print("add 6,", a.add(6))
    print("add 1,", a.add(1))
    print("add 1,", a.add(1))
    print(a.peek())
    print(a)
    print("maxheap check:", MaxHeap.check(a.vals))
    a.pop()
    print("pop 8,", a)
    a.pop()
    print("pop 6,", a)
    print("maxheap check:", MaxHeap.check(a.vals))
    b = MinHeap()
    print("add 4,", b.add(4))
    print("add 5,", b.add(5))
    print("add 3,", b.add(3))
    print(b.peek())
    print(b)
    b.pop()
    print("pop 3,", b)
    print("minheap check:", MinHeap.check(b.vals))
    print("minheap check:", MinHeap.check(a.vals))
    b.pop()
    b.pop()
    print(b.pop())
