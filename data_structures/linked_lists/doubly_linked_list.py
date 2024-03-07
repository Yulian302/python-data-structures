from data_structures.node import Node
from .linked_list import LinkedList


class DoublyLinkedNode(Node):
    def __init__(self, value: any):
        super().__init__(value)
        self.prev = None


class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    def insert_at_beginning(self, value: any) -> None:
        """
        Inserts a value at the beginning of the doubly linked list.

        :param value: The value to be inserted.
        :return: None
        """
        node = DoublyLinkedNode(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert(self, value: any, index: int) -> None:
        """
        Inserts a value into before the given index in a doubly linked list.

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

        node = DoublyLinkedNode(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            # closer to left side
            if abs(index) < abs(index - self.size):
                curr = self.tail
                curr_idx = self.size - 1
                while curr_idx != index:
                    curr = curr.prev
                    curr_idx -= 1
            # closer to right side
            else:
                curr = self.head
                curr_idx = 0
                while curr_idx != index:
                    curr = curr.next
                    curr_idx += 1
            curr.prev.next = node
            node.prev = curr.prev
            node.next = curr
            curr.prev = node
        self.size += 1

    def insert_at_end(self, value: any) -> None:
        """
        Inserts a value at the end of the doubly linked list.

        :param value:any
        :return: None
        """
        node = DoublyLinkedNode(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def delete_at_beginning(self) -> None:
        """
        Deletes the element at the beginning of a doubly linked list.

        :return: None
        """
        if not self.is_empty():
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None
            self.size -= 1

    def delete(self, index: int) -> None:
        """
        Deletes the element at the end of the forward linked list.

        :return: None
        """
        if index == 0:
            self.delete_at_beginning()
            return
        elif index >= self.size - 1:
            self.delete_at_end()
            return

        if not self.is_empty():
            # closer to left side
            if abs(index) < abs(index - self.size):
                curr = self.tail
                curr_idx = self.size - 1
                while curr_idx != index:
                    curr = curr.prev
                    curr_idx -= 1
            # closer to right side
            else:
                curr = self.head
                curr_idx = 0
                while curr_idx != index:
                    curr = curr.next
                    curr_idx += 1
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        self.size -= 1

    def delete_at_end(self) -> None:
        """
        Deletes the element at the end of the doubly linked list.

        :return: None
        """
        if not self.is_empty():
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None
            self.size -= 1
