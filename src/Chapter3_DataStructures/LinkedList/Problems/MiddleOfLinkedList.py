#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Leetcode 876 -> EASY.

"""

__author__ = "ayan_chattopadhyay"


from src.Chapter3_DataStructures.LinkedList.LinkedList import *


class MiddleOfLinkedList:
    @staticmethod
    def Solution(head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        slow = fast = dummy

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow.next


if __name__ == "__main__":
    import numpy as np

    myList = np.arange(1, 11)
    np.random.shuffle(myList)
    top = toLinkedList(list(myList))

    soln = MiddleOfLinkedList()

    print(f'Original Linked List given: {top}')
    print(f'Middle of the Linked List: {soln.Solution(top)}')
