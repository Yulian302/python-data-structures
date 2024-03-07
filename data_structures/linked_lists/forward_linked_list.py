#!/usr/bin/env python3
from data_structures.node import Node
from .linked_list import LinkedList


class ForwardLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def insert_at_beginning(self, value: any) -> None:
        """
        Inserts a value at the beginning of the forward linked list.

        :param value: The value to be inserted.
        :return: None
        """
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def insert(self, value: any, index: int) -> None:
        """
        Inserts a value into before the given index in a forward linked list.

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
            self.head = node
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            node.next = curr.next
            curr.next = node
        self.size += 1

    def insert_at_end(self, value: any) -> None:
        """
        Inserts a value at the end of the forward linked list.

        :param value:any
        :return: None
        """
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        self.size += 1

    def delete_at_beginning(self) -> None:
        """
        Deletes the element at the beginning of a forward linked list.

        :return: None
        """
        if not self.is_empty():
            self.head = self.head.next
            self.size -= 1

    def delete(self, index: int) -> None:
        """
        Deletes the element at the given index in a forward linked list.

        :return: None
        """
        if index == 0:
            self.delete_at_beginning()
            return
        elif index >= self.size - 1:
            self.delete_at_end()
            return

        if not self.is_empty():
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            curr.next = None
            self.size -= 1

    def delete_at_end(self) -> None:
        """
        Deletes the element at the end of the forward linked list.

        :return: None
        """
        if not self.is_empty():
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None
            self.size -= 1
