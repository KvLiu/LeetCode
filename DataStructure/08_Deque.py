# -*- coding:utf-8 -*-

class Dequeue(object):
    """list 实现双端队列"""
    def __init__(self):
        self.__list = []
        
    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []

    def add_front(self, val):
        """从头部入队列"""
        self.__list.insert(0, val)

    def add_rear(self, val):
        """从尾部入队列"""
        self.__list.append(val)

    def remove_front(self):
        """头部出队列"""
        if not self.is_empty():
            return self.__list.pop(0)
    
    def remove_rear(self):
        """尾部出队列"""
        if not self.is_empty():
            return self.__list.pop()

    def size(self):
        return len(self.__list)
        
if __name__ == '__main__':
    deque = Dequeue()
    print(deque.is_empty())   
    deque.add_rear(200)
    deque.add_rear(300)
    deque.add_front(100)
    print(deque.is_empty())
    print(deque.size())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_front())
