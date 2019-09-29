#https://leetcode-cn.com/problems/implement-queue-using-stacks/


class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.s1.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.s2.empty():
            return self.s2.pop()
        while not self.s1.empty():
            temp_val = self.s1.pop()
            self.s2.push(temp_val)
        return self.s2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.s2.empty():
            return self.s2.top()
        while not self.s1.empty():
            temp_val = self.s1.pop()
            self.s2.push(temp_val)
        return self.s2.top()


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.s1.empty() and self.s2.empty()