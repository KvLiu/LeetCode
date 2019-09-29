# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_id_set = set()
        pos = 1 
        while head:
            if id(head) not in node_id_set:
                pos += 1
                node_id_set.add(id(head))
            else:
                return True
            head = head.next
            
        return False
        