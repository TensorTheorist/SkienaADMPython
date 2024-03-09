#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Linked list implementation.

"""

__author__ = "ayan_chattopadhyay"


class ListNode:

    def __init__(self, value: int, next_node: 'ListNode' = None):
        self.value = value
        self.next = next_node

    def __str__(self):
        ret = []
        x = self

        while x is not None:
            ret.append(x.value)
            x = x.next

        return ' -> '.join(map(str, ret))


def toLinkedList(arr: list, suppressPrint: bool = True) -> ListNode:
    dummy = ListNode(0)
    top = dummy

    for el in arr:
        top.next = ListNode(el)
        top = top.next

    if not suppressPrint:
        print(dummy.next)

    return dummy.next


if __name__ == "__main__":
    head = toLinkedList([1, 2, 3, 4, 5])
