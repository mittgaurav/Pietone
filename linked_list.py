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

    def reverseList2(self, l):
        # 1 -> 10 -> 20 -> 30 -> 40 -> 0
        if not l or not l.next:
            return l

        # take the first element
        # and reverse the rest of it
        remaining = self.reverseList2(l.next)

        l.next.next = l
        l.next = None
        return remaining

    def reverseList3(self, head):
        if not head or not head.next:
            return head

        prev = None
        temp = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

    def removeNthFromEnd(self, head: ListNode, m: int) -> ListNode:
        """Two pointers - first pointer takes
        till mth, so we can start the second,
        which actually takes us to location"""
        first = head
        for i in range(m):
            if not first:
                raise Exception('list is smaller than m {}'.format(m))
            first = first.next

        second = head
        prev_to_second = None
        while first:
            first = first.next
            prev_to_second = second
            second = second.next

        # delete element
        if prev_to_second:
            prev_to_second.next = second.next
        else:
            # there is no prev - we
            # are removing the head
            head = head.next

        return head
