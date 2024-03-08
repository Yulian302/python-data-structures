from .node import Node


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def peek(self) -> any:
        """
        Returns the last element pushed into the stack.

        :return: The last element added to the stack.
        """
        return self.head.next.value

    def push(self, value) -> None:
        """
        Pushes a given value into the stack in a traditional LIFO order.

        :param value: The value to push into the stack.
        :return: None
        """
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self) -> any:
        """
        Pops (deletes) the last element in the stack and returns it.

        :return: The first element to unstack.
        """
        self.head.next = self.head.next.next
        self.size -= 1
        return self.head.next

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        :return: True if stack is empty, False otherwise.
        """
        return self.size == 0

    def clear(self):
        """
        Removes all items from the stack.

        :return: None
        """
        self.size = 0
        del self.head

    def traverse(self) -> None:
        """
        Prints the elements of the stack in LIFO traditional order.

        :return: None
        """
        if self.is_empty():
            print("Stack is empty")
            return
        curr = self.head.next
        while curr:
            symbol = "->" * bool(curr.next) or "\n"
            print(f"{curr.value}{symbol}", end="")
            curr = curr.next
