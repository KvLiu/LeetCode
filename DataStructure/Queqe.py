# using deque
from collections import deque

class Queue:
    def __int__(self):
        self = []

    def append(self, val):
        return self.append(val)

    def pop(self):
        del(self[0])

    def is_empty(self):
        return len(self) == 0


que = Queue()
que.append(1)
que.append(2)
que.append(3)
print(que.pop())
print(que.pop())



