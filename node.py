# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:51:33 2019

@author: gaurav
"""


class Node:
    """linked nodes"""
    def __init__(self, _val, _next=None):
        self.val = _val
        self.next = _next
        self.now = None

    def __str__(self):
        val = str(self.val)
        return (val + " -> " + str(self.next)) if self.next else val

    __repr__ = __str__

    def __iter__(self):
        self.now = self
        return self

    def __next__(self):
        if self.now:
            now = self.now
            self.now = self.next
            return now
        else:
            raise StopIteration

    def __len__(self):
        n = 0
        node = self
        while True:
            if node is None:
                break
            node = node.next
            n += 1
        return n


def reverse():
    """reverse a linked list"""
    A = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print(A)

    current = A
    prev = None
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    print(prev)


if __name__ is "__main__":
    reverse()
