"""
Tyler Perkins
15-11-23

Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

"""

class Stack:
    def __init__(self):
        self._data = []

    def push(self, val):
        self._data.append(val)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def empty(self) -> bool:
        return len(self._data) == 0


class Queue:
    """
    Standard FILO Container
    """
    def __init__(self):
        self._lhs = Stack()
        self._rhs = Stack()
        print("Made a new Queue")

    def push(self, val):
        """
        Push a value into the back of the queue
        """
        print(f"Pushed value {val}")
        self._lhs.push(val)

    def pop(self):
        """
        Get the oldest value
        """
        if not self._rhs.empty():
            ret = self._rhs.pop()
            print(f"Pop value {ret}")
            return ret

        while not self._lhs.empty():
            self._rhs.push(self._lhs.pop())

        ret = self._rhs.pop()
        print(f"Pop value {ret}")
        return ret

    def print(self):
        print("Queue State")
        print(f"self._lhs {self._lhs._data}")
        print(f"self._rhs {self._rhs._data}")


print("Testing Queue")
q = Queue()

q.push(1)
q.push(2)
q.push(3)

q.print()

assert q.pop() == 1
assert q.pop() == 2
assert q.pop() == 3

q.print()

q.push(4)
q.push(5)

q.print()

assert q.pop() == 4

q.print()

q.push(6)

q.print()

assert q.pop() == 5

q.print()

