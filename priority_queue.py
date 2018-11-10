# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:00:54 2018

@author: gaurav
"""


class priority_queue:
    """heap based data stuct
    that stores values as by
    a certain 'priority'"""
    index = -1
    vals = []

    def add(this, num):
        """add to end and
        propogate up"""
        this.index += 1
        this.vals.append(num)

        this._propogati()
        return this

    def _swap(this, i, j):
        temp = this.vals[i]
        this.vals[i] = this.vals[j]
        this.vals[j] = temp

    def __str__(this):
        return str(this.vals)

    def _propogati(this):
        """move number added
        at end higher"""
        i = this.index
        while(i > 0):
            if i % 2 == 0:
                j = int((i - 2)/2)
            else:
                j = int((i - 1)/2)

            if this.vals[j] < this.vals[i]:
                this._swap(i, j)
                i = j
            else:
                return

    def _heapify(this, i):
        """lowest number on
        top is brought down
        to its right loc"""
        L = int((2 * i) + 1)
        r = int((2 * i) + 2)
        largest = i
        if L <= this.index and this.vals[L] > this.vals[i]:
            largest = L
        if r <= this.index and this.vals[r] > this.vals[largest]:
            largest = r
        if largest != i:
            this._swap(largest, i)
            this._heapify(largest)

    def pop(this):
        """take highest num,
        replace with least,
        and heapify; i.e.
        move it down"""
        ret = this.vals[0]

        # replace with very small
        this.vals[0] = this.vals[this.index]

        # bring that very small to end
        this._heapify(0)
        this.vals.pop(this.index)
        this.index -= 1
        return ret


a = priority_queue()
print(a)
print("add 4,", a.add(4))
print("add 5,", a.add(5))
print("add 3,", a.add(3))
a.pop()
print("pop 5,", a)
print("add 31,", a.add(31))
print("add -3,", a.add(-3))
a.pop()
print("pop 31,", a)
a.pop()
print("pop 4,", a)
print("add 23,", a.add(23))
print("add 16,", a.add(16))
a.pop()
print("pop 23,", a)
