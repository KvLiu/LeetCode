class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.min == None or self.min > x:
            self.min = x

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) == 0:
            return None
        else:
            pop_int = self.stack.pop()

        if len(self.stack) == 0:
            self.min = None
        elif self.min == pop_int:
            self.min = self.stack[0]
            for i in self.stack:
                if self.min > i:
                    self.min = i

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min



