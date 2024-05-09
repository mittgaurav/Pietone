# -*- coding: utf-8 -*-
"""
Created on Sun May 26 03:49:02 2019

@author: gaurav
"""

import unittest
from linked_list import ListNode as L


def contains_cycle(first_node):
    """Check if the linked
    list contains a cycle"""
    if not first_node:
        return False

    slow = first_node
    fast = first_node
    while True:
        slow = slow.next
        fast = fast.next
        if fast: fast = fast.next
        if not fast: return False
        if fast == slow: return True
    return False


class Test(unittest.TestCase):
    """Unit test"""

    class LinkedListNode():
        """linked list data structure"""
        def __init__(self, value, nxt=None):
            self.value = value
            self.next = nxt

    def test_linked_list_with_no_cycle(self):
        """test"""
        fourth = Test.LinkedListNode(4)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        result = contains_cycle(first)
        self.assertFalse(result)

    def test_cycle_loops_to_beginning(self):
        """test"""
        fourth = Test.LinkedListNode(4)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fourth.next = first
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_cycle_loops_to_middle(self):
        """test"""
        fifth = Test.LinkedListNode(5)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fifth.next = third
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_two_node_cycle_at_end(self):
        """test"""
        fifth = Test.LinkedListNode(5)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fifth.next = fourth
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_empty_list(self):
        """test"""
        result = contains_cycle(None)
        self.assertFalse(result)

    def test_one_element_linked_list_no_cycle(self):
        """test"""
        first = Test.LinkedListNode(1)
        result = contains_cycle(first)
        self.assertFalse(result)

    def test_one_element_linked_list_cycle(self):
        """test"""
        first = Test.LinkedListNode(1)
        first.next = first
        result = contains_cycle(first)
        self.assertTrue(result)


unittest.main(verbosity=2)


def merge_sorted_list(i, j):
    if not i: return j
    if not j: return i

    # ensure that i is the smaller one
    result = i = i if i.val <= j.val else j

    prev = None
    while i and j:
        if i.val <= j.val:
            # i is still smaller
            # hence, keep moving
            prev = i
            i = i.next
        else:
            # j is smaller - in this case
            # we have to swap i and j.
            # Cut connection between prev
            # and i, and point prev to j.
            # Now j.next is i and i is j.
            # It's delicate manipulation.
            prev.next = j
            prev = prev.next
            j = i
            i = prev.next

    if i: prev.next = i
    if j: prev.next = j
    return result


i = L(1, L(3, L(7, L(15, L(18)))))
j = L(2, L(8, L(9, L(10))))
print(i, j)
print(merge_sorted_list(i, j))
