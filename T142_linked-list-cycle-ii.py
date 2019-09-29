# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node_set = set()
        while head:
            if head not in node_set:
                node_set.add(head)
                head = head.next
            else:
                return head 
        return None
        
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = b
s = Solution()
print((s.detectCycle(a)).val)