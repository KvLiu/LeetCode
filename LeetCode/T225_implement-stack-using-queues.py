class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__list1 = []
        self.__list2 = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        if self.__list1 ==[] and self.__list2 == []:
            self.__list1.append(x)
            return
        
        if self.__list1 !=[]:
            self.__list1.append(x)
            return

        if self.__list2 != []:
            self.__list2.append(x)

            
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """        
        if self.__list1 != []:
            while len(self.__list1) > 1:
                self.__list2.append(self.__list1.pop(0))
            return self.__list1.pop(0)
        
        if self.__list2 != []:
            while len(self.__list2) > 1:
                self.__list1.append(self.__list2.pop(0))
            return self.__list2.pop(0)       


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.__list1 != []:
            temp = 0
            while len(self.__list1) > 0:
                temp = self.__list1.pop(0)
                self.__list2.append(temp)
                
            return temp
        
        if self.__list2 != []:
            temp = 0
            while len(self.__list2) > 0:
                temp = self.__list2.pop(0)
                self.__list1.append(temp)
            return temp 


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.__list1 == [] and self.__list2 == []  
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()