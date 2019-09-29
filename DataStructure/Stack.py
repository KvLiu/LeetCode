# -*- coding:utf-8 -*-
class Stack(object):
    """list 实现栈"""
    def __init__(self):
        self.__list = []
        
    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []

    def push(self, val):
        """压栈"""
        self.__list.append(val)


    def pop(self):
        if not self.is_empty():
            return self.__list.pop()
    
    def peek(self):
        """返回栈顶元素"""
        return self.__list[-1]
    
    def size(self):
        return len(self.__list)
        
if __name__ == '__main__':
    a = Stack()
    print(a.is_empty())
    a.push(1)
    a.push(3)
    a.push(5)
    print(a.is_empty())
    print(a.peek())
    print(a.size())
    print(a.pop())