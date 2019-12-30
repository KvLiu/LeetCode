



# ListNode defination
class ListNode(object):
    def __init__(self, val):        
        self.val = val
        self.next = None 



def f():
    li= [1,2,3]
    print(id(li[0]))
    print(id(li[1]))
    print(id(li[2]))

f()
