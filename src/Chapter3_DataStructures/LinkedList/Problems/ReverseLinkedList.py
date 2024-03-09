#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Leetcode 206 -> EASY.

"""

__author__ = "ayan_chattopadhyay"


from src.Chapter3_DataStructures.LinkedList.LinkedList import *


class ReverseLinkedList:
    @staticmethod
    def iterativeSolution(head: ListNode) -> ListNode:
        rev = None
        curr = head

        while curr is not None:
            tmp = curr.next
            curr.next = rev
            rev = curr
            curr = tmp

        return rev

    def recursiveSolution(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head

        curr = head
        currNext = head.next
        head = self.recursiveSolution(currNext)
        currNext.next = curr
        curr.next = None

        return head


if __name__ == "__main__":
    import numpy as np

    myList = np.arange(1, 11)
    np.random.shuffle(myList)
    top = toLinkedList(list(myList))

    rll = ReverseLinkedList()

    print(f'Original Linked List given: {top}')
    print(f'Iteratively reversed Linked List: {rll.iterativeSolution(top)}')

    top = toLinkedList(list(myList))
    print(f'Recursively reversed Linked List: {rll.recursiveSolution(top)}')