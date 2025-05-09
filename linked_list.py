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

    def __repr__(self):
        return f"{self.val} {('-> ' + str(self.next)) if self.next else ''}"


class Solution:
    def reverseList(head: ListNode) -> ListNode:
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

    def reverseList2(l):
        # 1 -> 10 -> 20 -> 30 -> 40 -> 0
        if not l or not l.next:
            return l

        # take the first element
        # and reverse the rest of it
        remaining = Solution.reverseList2(l.next)

        l.next.next = l
        l.next = None
        return remaining

    def reverseList3(head):
        if not head or not head.next:
            return head

        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

    def removeNthFromEnd(head: ListNode, m: int) -> ListNode:
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


def insert_list(list, n):
    node = list
    prev = None

    while node is not None and node.val < n:
        prev = node
        node = node.next

    this = ListNode(n, node)
    if prev is None:
        return this

    prev.next = this

    return list


def delete_node(list, n):
    node = list
    prev = None

    # edge condition: first value matched
    if node.val == n:
        return node.next

    while node is not None and node.val != n:
        prev = node
        node = node.next

    if node is not None:
        prev.next = node.next

    return list


if __name__ == "__main__":
    print("====", Solution().reverseList.__name__)
    L = ListNode(1, ListNode(2, ListNode(5, None)))  # 1 -> 2 -> 5
    print("original", L)
    print("first", Solution.reverseList2(L))
    L = ListNode(1, ListNode(2, ListNode(5, None)))  # 1 -> 2 -> 5
    print("second", Solution.reverseList3(L))
    L = ListNode(1, ListNode(10, ListNode(12, None
                                          )))
    L = ListNode(1, ListNode(52, ListNode(57, L)))
    print(L)
    print(Solution.reverseList2(L))
    L = None
    L = ListNode(1, ListNode(2, ListNode(10, ListNode(15, None))))

    print("====", delete_node.__name__)
    n = 10
    print(L, "remove", n)
    result = delete_node(L, n)
    print(result)
