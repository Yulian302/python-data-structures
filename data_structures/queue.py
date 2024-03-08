from .node import Node


class Queue(object):
    def __init__(self):
        """
        Head of queue (front) and tail of queue (back). These pointers are needed for
        easier understanding and implementation.

        :return: Front element of the queue.
        """
        self.head: Node = Node("head")
        self.tail: Node = Node("tail")
        self.size: int = 0

    def is_empty(self) -> bool:
        """
        Checks whether the queue is empty.

        :return: True if the queue is empty, False otherwise.
        """
        return self.size == 0

    def size(self) -> int:
        """
        Returns the size of the queue.

        :return: The size of the queue.
        """
        return self.size

    def front(self) -> any:
        """
        Returns the front element of the queue (head).
        :return:
        any
        """
        return self.head.next

    def enqueue(self, value: any) -> None:
        """
        Adds a new element into the queue using a traditional FIFO approach.

        :param value: A new element to be added to the queue.
        :return: None
        """
        node = Node(value)
        if self.is_empty():
            self.head.next = node
            self.tail.next = node
        else:
            self.tail.next.next = node
            self.tail.next = node
        self.size += 1

    def dequeue(self) -> any:
        """
        Removes the first element added into the queue.

        :return: The first element in the queue.
        """
        first = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return first.value

    def clear(self):
        del self.head
        del self.tail
        self.size = 0

    def traverse(self) -> None:
        """
        Shows all the values in the queue in its order.

        :return: None
        """
        if self.is_empty():
            print("Queue is empty")
            return
        curr = self.head.next
        while curr:
            symb = "->" * bool(curr.next) or "\n"
            print(f"{curr.value}{symb}", end="")
            curr = curr.next
