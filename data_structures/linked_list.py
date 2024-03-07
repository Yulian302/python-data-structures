#!/usr/bin/env python3
from .node import Node


class LinkedList(object):
    def __init__(self):
        self.head: Node = Node("head")
        self.size: int = 0

    def is_empty(self) -> bool:
        """
        Checks whether the linked list is empty.

        :return: True if empty, False otherwise
        """
        return self.size == 0

    def insert_at_end(self, value: any) -> None:
        """
        Inserts a value at the end of the linked list.

        :param value:any
        :return: None
        """
        node = Node(value)
        if self.is_empty():
            self.head.next = node
        else:
            curr = self.head.next
            while curr.next:
                curr = curr.next
            curr.next = node
        self.size += 1

    def insert_at_beginning(self, value: any) -> None:
        """
        Inserts a value at the beginning of the linked list.

        :param value: The value to be inserted.
        :return: None
        """
        node = Node(value)
        if self.is_empty():
            self.head.next = node
        else:
            node.next = self.head.next
            self.head.next = node
        self.size += 1

    def insert(self, value: any, index: int) -> None:
        """
        Inserts a value into before the given index in a linked list.

        If the given index is 0, the value is inserted at the beginning.
        If the given index is greater than the list's size, the value is inserted at the end.

        :param value: The value to be inserted.
        :param index: The index before which the value should be inserted.
        :return: None
        """
        if index == 0:
            self.insert_at_beginning(value)
            return
        elif index >= self.size:
            self.insert_at_end(value)
            return

        node = Node(value)
        if self.is_empty():
            self.head.next = node
        else:
            curr = self.head.next
            for i in range(index - 1):
                curr = curr.next
            node.next = curr.next
            curr.next = node
        self.size += 1

    def traverse(self) -> None:
        """
        Traverses a linked list and prints the values in its preserved order.

        :return: None
        """
        curr = self.head.next
        while curr:
            symb = "->" * bool(curr.next) or "\n"
            print(f"{curr.value}{symb}", end="")
            curr = curr.next
