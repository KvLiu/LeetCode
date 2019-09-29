# -*- coding:utf-8 -*-
class Queue(object):
    """list 实现队列"""
    def __init__(self):
        self.__list = []
        
    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []

    def enqueue(self, val):
        """入队列"""
        self.__list.append(val)

    def dequeue(self):
        """出队列"""
        if not self.is_empty():
            return self.__list.pop(0)
    
    
    def size(self):
        return len(self.__list)
        
if __name__ == '__main__':
    que = Queue()
    print(que.is_empty())   
    que.enqueue(2)
    que.enqueue(4)
    print(que.is_empty())
    que.dequeue()
    print(que.size())
