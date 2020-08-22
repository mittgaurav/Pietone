# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:48:33 2020

@author: gaurav
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        stack = []
        while head:
            stack.append(head)
            head = head.next

        ret = stack.pop()
        ongoing = ret

        while len(stack):
            ongoing.next = stack[-1]
            ongoing = stack.pop()
            ongoing.next = None

        return ret
