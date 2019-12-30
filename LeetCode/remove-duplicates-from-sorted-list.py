# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = head
        if not head:
            return None
        while head.next != None:
            temp = head.next
            if head.val == temp.val:
                head.next = temp.next
            else:
                head = temp
        return start
