from data_structures.node import Node
from abc import ABC, abstractmethod


class LinkedList(ABC):
    def __init__(self):
        self.head = None
        self.size: int = 0

    def is_empty(self) -> bool:
        """
        Checks whether the linked list is empty.

        :return: True if empty, False otherwise
        """
        return self.size == 0

    def traverse(self) -> None:
        """
        Traverses a linked list and prints the values in its preserved order.

        :return: None
        """
        curr = self.head
        while curr:
            symb = "->" * bool(curr.next) or "\n"
            print(f"{curr.value}{symb}", end="")
            curr = curr.next

    @abstractmethod
    def insert_at_beginning(self, value: any) -> None:
        ...

    @abstractmethod
    def insert(self, value: any, index: int) -> None:
        ...

    @abstractmethod
    def insert_at_end(self, value: any) -> None:
        ...

    @abstractmethod
    def delete_at_beginning(self) -> None:
        ...

    @abstractmethod
    def delete(self, index: int) -> None:
        ...

    @abstractmethod
    def delete_at_end(self) -> None:
        ...
